import time
import os
import glob
from pathlib import Path
from pydantic import BaseModel
from google import genai
from google.genai import types
from dotenv import load_dotenv

class BackgroundLink(BaseModel):
    markdown_content: str

SYSTEM_INSTRUCTION = """You are an expert technical editor. 
Your task is to add a `## Background` section to an existing Agent Skill.
You will be provided with:
1. The content of an Agent Skill.
2. A consolidated REFERENCE INDEX of all available conceptual whitepaper files.

Your job is to identify the 1-3 most relevant reference files from the index that provide the theoretical or conceptual backing for the procedural skill.
Then, output a Markdown string containing exactly:
## Background
- [Title of Reference](relative_path_to_reference/filename.md)
- [Title of Reference](relative_path_to_reference/filename.md)

Important rules:
- Provide ONLY the `## Background` section in your output. Do not rewrite the original skill.
- The links MUST be relative paths. Use the "Base Path" provided in the index and combine it with the filename. For example, if Base Path is `../../references/course/paper` and the item is `- **[Intro](01-intro.md)**`, the relative path is `../../references/course/paper/01-intro.md`.
- Only link to files that are highly relevant to the skill's purpose.
"""

def main():
    load_dotenv()
    client = genai.Client()

    skills_dir = Path("skills_refined")
    ref_dir = Path("references")
    
    # Consolidate all indices
    indices = list(ref_dir.rglob("_index.md"))
    consolidated_index = "--- REFERENCE INDEX ---\n\n"
    for idx in indices:
        rel_base_path = f"../../{idx.parent}"
        consolidated_index += f"Base Path for links below: {rel_base_path}\n"
        consolidated_index += idx.read_text(encoding="utf-8")
        consolidated_index += "\n\n"

    skill_files = list(skills_dir.rglob("SKILL.md"))
    print(f"Processing {len(skill_files)} skills...")
    
    for i, skill_file in enumerate(skill_files, 1):
        content = skill_file.read_text(encoding="utf-8")
        if "## Background" in content:
            print(f"[{i}/{len(skill_files)}] Skipping {skill_file.parent.name}, already has Background.")
            continue
            
        print(f"[{i}/{len(skill_files)}] Adding Background to {skill_file.parent.name}...")
        
        prompt = f"SKILL CONTENT:\n\n{content}\n\n{consolidated_index}"
        
        while True:
            try:
                response = client.models.generate_content(
                    model='gemini-3.1-flash-lite',
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=SYSTEM_INSTRUCTION,
                        response_mime_type="application/json",
                        response_schema=BackgroundLink,
                        temperature=0.1
                    )
                )
                if response.parsed:
                    background_text = response.parsed.markdown_content
                    skill_file.write_text(content.strip() + "\n\n" + background_text + "\n", encoding="utf-8")
                break
            except Exception as e:
                if "429" in str(e):
                    print("Rate limit hit, sleeping for 60s...")
                    time.sleep(60)
                else:
                    print(f"Failed on {skill_file.parent.name}: {e}")
                    break

if __name__ == "__main__":
    main()
