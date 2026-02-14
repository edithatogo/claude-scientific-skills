---
adapter_metadata:
  skill_name: claude-scientific-skills
  skill_version: 1.0.0
  last_synced: 2026-02-14
  source_path: README.md
  adapter_id: codex-cli
  adapter_format: AGENTS.md
---

# Claude Scientific Skills (agents manifest)

This repository contains a comprehensive collection of **140 ready-to-use scientific skills** for AI agents. These skills transform general-purpose agents into specialized research assistants capable of executing complex workflows in biology, chemistry, medicine, and more.

## Capability

The collection provides specialized domain knowledge and tool-use instructions for:
- 🧬 **Bioinformatics & Genomics**: Sequence analysis, single-cell RNA-seq, etc.
- 🧪 **Cheminformatics & Drug Discovery**: Molecular manipulation, docking, ADMET.
- 🏥 **Clinical Research**: Clinical trial data, pharmacogenomics, variant annotation.
- 📊 **Data Analysis**: Statistical modeling, network analysis, visualization.
- 📚 **Scientific Communication**: Literature review, peer review, scientific writing.

Primary instructions for each skill are located in `scientific-skills/<skill-name>/SKILL.md`.

## Context

This file serves as the **Agents.md** standard manifest for discovery and indexing.

### Repository structure

- `scientific-skills/`
  - Each subdirectory contains a `SKILL.md` (the core logic), plus optional `assets/`, `scripts/`, and `references/`.
- `scripts/`
  - `sync_scientific_skills.py`: Automation to distribute these skills to local tool environments.

### Core instructions

When asked to perform a scientific task:
1. Identify the most relevant skill in `scientific-skills/`.
2. Follow the `Core Workflow` and `Best Practices` defined in its `SKILL.md`.
3. Use the provided Python scripts or tool integration examples where appropriate.

## Maintenance

To sync all 140+ skills to your local agentic tool directories (Cline, Kilo, Amp, etc.), run:

```bash
python scripts/sync_scientific_skills.py
```

## Interoperability

These skills are optimized for Claude Code but compatible with any agent following the `SKILL.md` standard, including Antigravity, Cline, Kilo Code, Amp, and OpenCode.
