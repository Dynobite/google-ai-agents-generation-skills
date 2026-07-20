import os

def fetch_skill_blueprint(skill_id: str, context_reason: str) -> str:
    """
    Retrieves the full Level 2 and Level 3 documentation, code specifications, 
    and canonical standards for a specific agentic skill.
    
    This acts as the JIT (Just-In-Time) context retrieval tool for custom agent orchestrators.
    
    Args:
        skill_id: The exact directory name of the skill to fetch (e.g., 'configure-mcp-server-connection').
        context_reason: A brief explanation of why the agent requested this skill.
        
    Returns:
        The full Markdown body of the requested skill, or an error message.
    """
    # Resolve the directory of this script to locate the skills folders
    base_dir = os.path.dirname(os.path.abspath(__file__))
    skill_dir = os.path.join(base_dir, skill_id)
    skill_file = os.path.join(skill_dir, "SKILL.md")
    
    if not os.path.exists(skill_file):
        return (f"Error: Skill '{skill_id}' not found. "
                f"Please ensure the skill_id exactly matches the folder name.")
        
    try:
        with open(skill_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Strip the YAML frontmatter since the agent already knows the Level 1 metadata
        parts = content.split("---")
        if len(parts) >= 3:
            body = "---".join(parts[2:]).strip()
        else:
            body = content.strip()
            
        return f"Successfully retrieved blueprint for {skill_id} (Reason: {context_reason}):\n\n{body}"
    except Exception as e:
        return f"Error reading skill blueprint: {str(e)}"

# Example usage for testing:
if __name__ == "__main__":
    print(fetch_skill_blueprint("configure-mcp-server-connection", "Need to connect to a Postgres DB"))
