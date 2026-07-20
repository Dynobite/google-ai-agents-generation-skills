Write a Python script that processes a directory of IT course PDFs into agent skills using a two-step pipeline: local Markdown extraction followed by Google GenAI schema generation.

Technical Requirements:

Step 1: Local PDF to Markdown Conversion: Scan a local ./course_pdfs/ directory. For each PDF, use the docling library (DocumentConverter) to parse the file locally and save a raw markdown copy to an intermediate directory ./course_markdowns/<filename>.md. Ensure code blocks and tables are preserved.

Step 2: Dependency Injection: For the LLM phase, use the modern Google GenAI SDK (from google import genai) and Pydantic (from pydantic import BaseModel). Do NOT use the legacy google-generativeai library.

Structured Output Schema: Define a Pydantic model called Skill with three string fields: name (hyphenated), description (trigger instructions), and body (the actual technical instruction markdown). Define a parent model called SkillExtraction containing a list of Skill objects.

LLM Analysis: Read the newly generated .md files from ./course_markdowns/. Pass the text content of these markdown files to gemini-2.5-flash using client.models.generate_content().

Configuration: Pass the SkillExtraction Pydantic model into the config using response_schema with a temperature of 0.1. Instuct the model to extract every distinct procedural process into the schema.

File Tree Generation: Iterate over the returned Pydantic object. For each skill, create a directory at ./extracted_skills/<skill.name>/ and write a SKILL.md file containing the YAML frontmatter and the markdown body.