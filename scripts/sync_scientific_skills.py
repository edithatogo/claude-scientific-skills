import os
import shutil
from pathlib import Path

# Paths
REPO_ROOT = Path(__file__).parent.parent
SCIENTIFIC_SKILLS_DIR = REPO_ROOT / "scientific-skills"
HOME = Path.home()

# Distribution Targets
TARGETS = {
    "cline": HOME / ".cline" / "skills",
    "kilo": HOME / ".kilo" / "skills",
    "amp": HOME / ".amp" / "skills",
    "opencode": HOME / ".opencode" / "skills",
    "claude": HOME / ".claude" / "skills",
    "antigravity": HOME / ".gemini" / "antigravity" / "skills",
    "codex": HOME / ".codex" / "skills",
    "copilot": HOME / ".config" / "github-copilot",
    "qwen": HOME / ".qwen" / "skills",
}

def sync_scientific_skills():
    print(f"Syncing scientific skills from {SCIENTIFIC_SKILLS_DIR}...")
    
    # Get all skill directories
    skills = [d for d in SCIENTIFIC_SKILLS_DIR.iterdir() if d.is_dir()]
    
    for target_name, target_base_path in TARGETS.items():
        print(f"  Syncing to {target_name} ({target_base_path})...")
        
        # Copilot uses a consolidated file approach
        if target_name == "copilot":
            consolidated_path = target_base_path / "scientific-skills.md"
            target_base_path.mkdir(parents=True, exist_ok=True)
            all_content = ["# Scientific Skills Collection", ""]
            for skill_dir in skills:
                source_md = skill_dir / "SKILL.md"
                if source_md.exists():
                    all_content.append(f"## Skill: {skill_dir.name}")
                    all_content.append(source_md.read_text(encoding="utf-8"))
                    all_content.append("\n---\n")
            consolidated_path.write_text("\n".join(all_content), encoding="utf-8")
            continue

        for skill_dir in skills:
            skill_name = skill_dir.name
            target_skill_dir = target_base_path / skill_name
            target_skill_dir.mkdir(parents=True, exist_ok=True)
            
            # Source SKILL.md
            source_skill_md = skill_dir / "SKILL.md"
            if not source_skill_md.exists():
                continue
                
            # Target SKILL.md
            target_skill_md = target_skill_dir / "SKILL.md"
            
            # Read content and inject metadata
            content = source_skill_md.read_text(encoding="utf-8")
            
            # Basic metadata injection
            today = "2026-02-14"
            metadata = (
                f"adapter_metadata:\n"
                f"  skill_name: {skill_name}\n"
                f"  skill_version: 1.0.0\n"
                f"  last_synced: {today}\n"
                f"  source_path: scientific-skills/{skill_name}/SKILL.md\n"
                f"  adapter_id: {target_name}\n"
                f"  adapter_format: {target_name.capitalize()} skill"
            )

            # Handle YAML frontmatter
            if content.startswith("---"):
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    new_content = f"---{parts[1]}{metadata}\n---{parts[2]}"
                else:
                    new_content = f"---\n{metadata}\n---" + content
            else:
                new_content = f"---\n{metadata}\n---\n\n" + content
                
            target_skill_md.write_text(new_content, encoding="utf-8")
            
    print("\nSync Complete.")

if __name__ == "__main__":
    sync_scientific_skills()
