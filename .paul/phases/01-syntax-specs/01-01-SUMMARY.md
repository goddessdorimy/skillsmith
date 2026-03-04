---
phase: 01-syntax-specs
plan: 01
subsystem: specs
tags: [syntax, entry-point, tasks, templates, markdown]

requires:
  - phase: none
    provides: first plan
provides:
  - Entry point syntax spec
  - Tasks syntax spec
  - Templates syntax spec
affects: [01-02 auxiliary specs, 02-01 skillsmith discovery, 03-01 scaffolding]

tech-stack:
  added: []
  patterns: [YAML frontmatter for entry points, semantic XML sections, placeholder conventions]

key-files:
  created: [specs/entry-point.md, specs/tasks.md, specs/templates.md]
  modified: []

key-decisions:
  - "Entry points use 5 XML sections: activation, persona, commands, routing, greeting"
  - "Tasks use user-story + plain checklists (not BDD)"
  - "Templates distinguish content frontmatter from template frontmatter"
  - "Placeholder convention: [square]=human prose, {curly}=variable interpolation"

patterns-established:
  - "Spec file structure: header, section order, specifications, naming, core principle, good/bad examples, anti-patterns"
  - "Semantic XML tags only — no generic section/block/item"
  - "Every spec includes anti-patterns table"

duration: 7min
started: 2026-03-04T13:08:00-06:00
completed: 2026-03-04T13:15:00-06:00
---

# Phase 1 Plan 01: Core Syntax Specs Summary

**Concrete syntax specs for entry points, tasks, and templates — the 3 core skill file types, grounded from PAUL `src/` patterns with good/bad examples.**

## Performance

| Metric | Value |
|--------|-------|
| Duration | ~7 min |
| Started | 2026-03-04 13:08 |
| Completed | 2026-03-04 13:15 |
| Tasks | 3 completed |
| Files created | 3 |

## Acceptance Criteria Results

| Criterion | Status | Notes |
|-----------|--------|-------|
| AC-1: Entry Point Spec Complete | Pass | YAML frontmatter (6 fields), 5 XML sections, versioning convention, good/bad examples, anti-patterns |
| AC-2: Tasks Spec Complete | Pass | 8 XML sections, step attributes, user-story format, plain checklists, conditional logic patterns |
| AC-3: Templates Spec Complete | Pass | Fenced block structure, both placeholder types, field docs, content vs template frontmatter distinction |
| AC-4: Cross-Spec Consistency | Pass | Placeholder conventions, XML tag style, example format, heading hierarchy all consistent |

## Accomplishments

- Established the placeholder convention (`[square]` = human prose, `{curly}` = variable) as a cross-cutting standard
- Adapted PAUL patterns for non-dev context: commands→entry points, workflows→tasks, templates→templates
- Each spec is self-contained — a skill author can read one spec and write compliant files without other docs

## Files Created/Modified

| File | Change | Purpose |
|------|--------|---------|
| `specs/entry-point.md` | Created | Syntax spec for `{skill-name}.md` — YAML frontmatter, 5 XML sections, versioning |
| `specs/tasks.md` | Created | Syntax spec for `tasks/*.md` — step-based workflows with user stories |
| `specs/templates.md` | Created | Syntax spec for `templates/*.md` — fenced blocks with placeholder conventions |

## Decisions Made

| Decision | Rationale | Impact |
|----------|-----------|--------|
| 5 XML sections for entry points (activation, persona, commands, routing, greeting) | Maps cleanly from PAUL commands while adding skill-specific needs (persona, greeting) | Defines the identity layer for all skills |
| Tasks use `<user-story>` not `<objective>` | Skills serve people, not code — user stories are natural | All task files include who benefits and why |
| Templates have NO frontmatter themselves | Prevents confusion with generated content frontmatter inside fenced blocks | Clear rule: frontmatter only inside template content |

## Deviations from Plan

None — plan executed exactly as written.

## Issues Encountered

None.

## Next Phase Readiness

**Ready:**
- 3 of 7 specs complete — the core file types
- Conventions established that Plan 01-02 will follow (placeholder types, spec structure, anti-patterns format)

**Concerns:**
- None

**Blockers:**
- None — Plan 01-02 (auxiliary specs) can proceed immediately

---
*Phase: 01-syntax-specs, Plan: 01*
*Completed: 2026-03-04*
