# Skill Framework — Planning Document

**Created:** March 3, 2026
**Status:** Design Phase — Syntax specs TBD
**Linear (Rev-Ops):** REV-158 (Meta-Skill), REV-159 (Audit)
**Location:** `projects/skill-framework/`

---

## Overview

A universal framework for creating Claude Code skills — from discovery through deployment. The framework includes a meta-skill (the skill that builds skills), syntax standards for every file type, and a scaffolding engine that generates compliant skill directories.

**First deployment:** Extendly Rev-Ops team (Chris + Zach), where skills power revenue operations workflows — webinar builds, offer design, copy frameworks, etc.

**Broader vision:** This framework is designed to be portable. It's not bound to Rev-Ops or Extendly. The syntax standards, skill types, and meta-skill are generic enough to share with the Skool community, use in courses (Claude Code Masterclass), and distribute as a standalone tool for anyone building Claude Code skills. The Rev-Ops implementation is the proving ground — once validated there, the framework gets extracted and packaged for distribution.

---

## Problem Statement

Skills today are built ad hoc. Each one has its own structure, naming conventions, and internal patterns. When a team is building many skills:

- New skills take too long because there's no starting template
- Quality is inconsistent because there's no shared standard
- Onboarding is painful because every skill works differently
- Collaboration breaks down because team members can't predict where things are or how they're structured

The framework solves this by standardizing the **what** (file types and their syntax) and automating the **how** (discovery + scaffolding).

---

## Architecture

### Skill Types (Three Tiers)

| Type | Description | When to Use | Example |
|------|------------|-------------|---------|
| **Suite** | Meta-orchestrator + sub-skills | Large frameworks with multiple specialized areas | Expert Secrets (7 sub-skills) |
| **Standalone** | Single skill with auxiliary folders | Most skills | RevOps Expert |
| **Task-only** | Lightweight single-purpose guide | Invoked by parent skill, not standalone | Full Webinar Build |

### Standard Skill Structure

```
skills/{skill-name}/
  {skill-name}.md              # Entry point (thin: persona + activation + routing)
  README.md                    # What it does, how to use, what it loads

  # Auxiliary folders (include only what's needed):
  tasks/                       # Step-by-step guided workflows
  templates/                   # Reusable output structures (fill-in-the-blank)
  frameworks/                  # Reference knowledge the skill loads
  context/                     # Business/user context files
  checklists/                  # Validation/QA checklists
  data/                        # Static data the skill references
  rules/                       # Authoring rules per folder type (meta layer)

  # Suite-only:
  {sub-skill}.md               # Sub-skill entry points
```

### Deployment Model

- **`skills/`** — Git-tracked shared library. Source of truth. Team pushes here.
- **`.claude/commands/`** — Local deploy target. Not committed. Copy from `skills/` to use.

---

## Syntax Standards (Per Folder Type)

The core IP of this framework. Every file of the same type, across ALL skills, follows the same syntax. This is what makes skills feel consistent and predictable.

### Entry Point (`{skill-name}.md`)

- YAML frontmatter: name, type, version, category, description
- XML sections: `<activation>`, `<persona>`, `<commands>`, `<greeting>`
- Thin — routes to `tasks/` for heavy work, loads `frameworks/` for knowledge

### Tasks (`tasks/*.md`)

- XML-structured execution files
- Sections: `<purpose>`, `<user-story>`, `<steps>` with `<step name="">`, `<output>`, `<acceptance-criteria>`
- User story format: "As a [role], I want [action], so that [outcome]"
- Acceptance criteria as plain checklists: `- [ ] Output includes X`
- Steps are numbered, imperative, specific

### Templates (`templates/*.md`)

- Fenced markdown block containing the actual template
- Placeholder conventions: `[square brackets]` for human-fillable prose, `{curly braces}` for variable interpolation
- Section specs below the fenced block explaining what goes where

### Frameworks (`frameworks/*.md`)

- Reference knowledge loaded by the skill
- Plain markdown with standard headers
- Can use optional XML container for parseable sections
- Read-only — never modified during skill execution

### Context (`context/*.md`)

- Business/user context files
- Plain markdown with standard sections (profile, preferences, history)
- May include onboarding templates for new users

### Checklists (`checklists/*.md`)

- Structured `- [ ]` lists grouped by category
- Each item has a clear pass/fail criterion
- Used for QA validation of skill outputs

### Rules (`rules/*.md`)

- Authoring rules for each folder type in the skill
- Defines what every file of that type must contain
- Lives in the meta-skill only — individual skills don't carry their own rules

**STATUS: Syntax specs for each type are drafted above but not finalized. Need to build concrete examples and iterate before locking in.**

---

## Meta-Skill Workflow (2 Phases)

### Phase 1: Discovery

Interview the user to determine skill type, structure, and persona.

1. What's the skill's goal? What problem does it solve?
2. How will users interact? (conversational, sequential build, task runner, ideation-first)
3. What knowledge sources does it need? (books, frameworks, data, context)
4. Does it need onboarding? Sub-skills? Templates?
5. **Output:** Skill spec — type, auxiliary folders needed, persona definition, command list

### Phase 2: Scaffolding

Generate the complete skill directory based on the spec.

1. Generate directory structure based on skill spec
2. Create entry point with YAML frontmatter + XML sections
3. Create README.md
4. Scaffold auxiliary files using correct syntax standard per folder type
5. Populate frameworks/ with references if source material exists
6. **Output:** Complete skill directory ready for implementation and testing

---

## Build Order

| Step | What | Depends On |
|------|------|-----------|
| 1 | Draft syntax spec files (one per folder type) with concrete examples | — |
| 2 | Review and iterate syntax specs | Step 1 |
| 3 | Build meta-skill entry point + discovery workflow | Step 2 |
| 4 | Build scaffolding phase | Step 2 |
| 5 | Test: create one new skill end-to-end using the meta-skill | Steps 3+4 |
| 6 | Run audit of existing skills against standards (REV-159) | Step 5 |

---

## Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Acceptance criteria format | User Stories + checklists (not BDD) | Skills serve revenue/content work, not software. User stories are natural. |
| Cross-file syntax consistency | Same type = same syntax across all skills | Predictability. A `tasks/*.md` file should look the same whether it's in Expert Secrets or a brand new skill. |
| Skill location | `skills/` (tracked) → copy to `.claude/commands/` (local) | Team needs shared library; `.claude/` isn't committed. |
| Rules folder scope | Meta-skill only (not every skill) | Individual skills follow the standards; they don't need to carry the rulebook. |
| Inspired by | PAUL framework `src/` patterns | XML sections, step-based workflows, folder-specific rules, placeholder conventions. Adapted for non-dev context. |

---

## Open Questions

- [ ] Exact syntax for each folder type — need to build concrete example files and iterate
- [ ] Meta-skill name: `/skill-builder`? `/forge`? `/create-skill`?
- [ ] Naming convention enforcement: kebab-case for all skill directories?
- [ ] How to handle skill versioning (cu block has version field — is it meaningful?)
- [ ] Distribution packaging: when extracting for Skool/courses, what gets included vs excluded?

---

## Distribution Strategy (Post-Validation)

Once the framework is proven in Rev-Ops:

1. **Extract** the meta-skill + syntax specs from the Rev-Ops repo
2. **Package** as a standalone skill framework (no Extendly-specific content)
3. **Channels:**
   - Skool community (free resource for VIP members)
   - Claude Code Masterclass (course module)
   - YouTube (tutorial content — "How to Build Claude Code Skills That Scale")
   - GitHub (open template repo)

This is Chris AI Systems IP, not Extendly IP. The Rev-Ops deployment is the first customer.
