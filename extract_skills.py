import os
import glob
from tenacity import retry, wait_exponential
import re
import logging
from pathlib import Path
from pydantic import BaseModel
from google import genai
from google.genai import types
from docling.document_converter import DocumentConverter
from dotenv import load_dotenv

# Setup progressive console logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load env variables (for GEMINI_API_KEY)
load_dotenv()

# Define Pydantic schemas for Structured Output
class Skill(BaseModel):
    name: str
    description: str
    body: str

class SkillExtraction(BaseModel):
    skills: list[Skill]

# System Instruction
SYSTEM_INSTRUCTION = """You are an expert Systems Architect and Agent Engineer. Your task is to analyze technical IT course materials and decompose them into distinct, atomic "Agent Skills" for a coding assistant.

A "Skill" is NOT a summary of a topic. It is an operational runtime directive that answers "How do I implement or configure X?" rather than "What is X?". 

Follow these strict extraction rules:
1. Trigger Isolation (Description): The `description` field must act as a strict conditional router. Phrase it in the imperative mood, specifying exactly when a coding agent should invoke this file (e.g., "Use this skill when asked to configure a multi-agent state machine in LangFlow.").
2. Actionable Body: The `body` field must contain step-by-step, actionable programming or configuration instructions. Write directly to the AI coding agent using an authoritative tone ("You are an expert at... When tasked with X, follow these steps:").
3. Preserve Code and Architecture: Do not summarize code snippets, terminal commands, or framework configuration parameters. You must extract them verbatim and wrap them in clean Markdown code blocks within the body.
4. Vibecoding Posture: Format the body so that a downstream coding LLM can immediately copy-paste the architecture, boilerplate, or logic trees into a workspace without needing to figure out the implementation details.

Anti-Patterns to Avoid:
- Never start the body or description with introductory filler like "This section covers..." or "In this lesson, you will learn...".
- Do not group unrelated technical procedures into a single skill. If a text covers both "Authentication" and "Rate Limiting", extract them as two separate skills.
"""

def clean_markdown_body(body: str) -> str:
    """Strips Markdown code fences from the extracted body string if the model wrapped it."""
    body = body.strip()
    if body.startswith("```markdown") and body.endswith("```"):
        body = body[len("```markdown"): -len("```")].strip()
    elif body.startswith("```") and body.endswith("```"):
        first_newline = body.find('\n')
        if first_newline != -1 and " " not in body[:first_newline]:
            body = body[first_newline:].strip()
            body = body[:-3].strip()
        else:
            body = body[3:-3].strip()
    return body

def sanitize_folder_name(name: str) -> str:
    """Creates a safe folder name from the skill name."""
    sanitized = re.sub(r'[^a-zA-Z0-9\-]', '-', name.lower())
    sanitized = re.sub(r'-+', '-', sanitized).strip('-')
    return sanitized if sanitized else "unnamed-skill"

@retry(wait=wait_exponential(multiplier=1, min=2, max=10))
def generate_content_with_retry(client, text_content):
    return client.models.generate_content(
        model='gemini-3.1-flash-lite',
        contents=text_content,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            response_mime_type="application/json",
            response_schema=SkillExtraction,
            temperature=0.1
        )
    )

def process_pdfs():
    input_dir = Path("course_pdfs")
    md_dir = Path("course_markdowns")
    out_dir = Path("extracted_skills")
    
    # Create necessary directories
    md_dir.mkdir(exist_ok=True)
    out_dir.mkdir(exist_ok=True)
    
    pdf_files = list(input_dir.glob("*.pdf"))
    if not pdf_files:
        logger.warning(f"No PDFs found in {input_dir}. Please add some PDFs to process.")
        return

    logger.info(f"Step 1: Found {len(pdf_files)} PDFs. Starting local PDF to Markdown conversion...")
    converter = DocumentConverter()
    
    for i, pdf_path in enumerate(pdf_files, 1):
        logger.info(f"Parsing file {i}/{len(pdf_files)}: {pdf_path.name}...")
        try:
            result = converter.convert(str(pdf_path))
            md_text = result.document.export_to_markdown()
            
            md_path = md_dir / f"{pdf_path.stem}.md"
            md_path.write_text(md_text, encoding="utf-8")
        except Exception as e:
            logger.error(f"Error parsing {pdf_path.name}: {e}")

    logger.info("Step 2: Running Gemini extraction loop...")
    
    # Check for API key before initializing
    if not os.environ.get("GEMINI_API_KEY"):
        logger.error("GEMINI_API_KEY environment variable is not set.")
        logger.info("Please create a .env file with GEMINI_API_KEY=your_key or set it in your environment.")
        return
        
    try:
        client = genai.Client()
    except Exception as e:
        logger.error(f"Failed to initialize GenAI client: {e}")
        return

    md_files = list(md_dir.glob("*.md"))
    total_skills_extracted = 0
    
    for i, md_file in enumerate(md_files, 1):
        logger.info(f"Extracting skills from {i}/{len(md_files)}: {md_file.name}...")
        text_content = md_file.read_text(encoding="utf-8")
        
        if not text_content.strip():
            logger.warning(f"File {md_file.name} is empty, skipping.")
            continue
            
        try:
            response = generate_content_with_retry(client, text_content)
            
            if response.parsed:
                extraction = response.parsed
                skills = extraction.skills
                
                logger.info(f"Found {len(skills)} skills in {md_file.name}.")
                for skill in skills:
                    clean_body = clean_markdown_body(skill.body)
                    base_name = sanitize_folder_name(skill.name)
                        
                    # Handle folder naming collisions
                    skill_dir = out_dir / base_name
                    counter = 2
                    while skill_dir.exists():
                        skill_dir = out_dir / f"{base_name}-{counter}"
                        counter += 1
                        
                    skill_dir.mkdir(parents=True, exist_ok=True)
                    
                    # Write SKILL.md with frontmatter
                    skill_file = skill_dir / "SKILL.md"
                    frontmatter = f"---\nname: {skill.name}\ndescription: {skill.description}\n---\n\n"
                    skill_file.write_text(frontmatter + clean_body, encoding="utf-8")
                    total_skills_extracted += 1
            else:
                logger.warning(f"No structured output returned for {md_file.name}.")
                
        except Exception as e:
            logger.error(f"Error during Gemini extraction for {md_file.name}: {e}")

    logger.info(f"Successfully wrote {total_skills_extracted} skills to disk in '{out_dir}'.")

if __name__ == "__main__":
    process_pdfs()
