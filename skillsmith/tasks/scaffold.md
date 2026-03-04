<purpose>
Generate a compliant skill directory from a completed skill spec. Reads the structured output of /skillsmith discover and creates all files — entry point, tasks, frameworks, templates, context, checklists — following syntax specs as authoring rules.
</purpose>

<user-story>
As a skill builder, I want my skill spec automatically turned into a working directory with properly structured files, so that I can start customizing content immediately instead of manually creating boilerplate.
</user-story>

<when-to-use>
- After completing /skillsmith discover and confirming the skill spec
- When you have a skill spec (pasted or in a file) and want to generate the directory
- Entry point routes here via /skillsmith scaffold
</when-to-use>

<context>
@templates/skill-spec.md
</context>

<references>
@../specs/entry-point.md (when generating entry point)
@../specs/tasks.md (when generating task files)
@../specs/templates.md (when generating template files)
@../specs/frameworks.md (when generating framework files)
@../specs/context.md (when generating context files)
@../specs/checklists.md (when generating checklist files)
@rules/entry-point-rules.md (for validation)
@rules/tasks-rules.md (for validation)
@rules/templates-rules.md (for validation)
@rules/frameworks-rules.md (for validation)
@rules/context-rules.md (for validation)
@rules/checklists-rules.md (for validation)
</references>

<steps>

<step name="locate_spec" priority="first">
Get the skill spec to scaffold from.

1. Check if a skill spec was just produced by /skillsmith discover in this session
   - If yes: "I have the spec from your discovery session. Use it?"
   - Wait for confirmation

2. If no recent spec, ask the user:
   - "Paste your skill spec below, or provide a file path to read it from."
   - Wait for input

3. Parse the spec and extract all sections:
   - **Identity**: name, type, version, category, description
   - **Persona**: role, style, expertise
   - **Activation**: what, when to use, not for
   - **Commands**: command table (if not task-only)
   - **Content Architecture**: tasks, frameworks, templates, context, checklists (each with file names, purposes, loading conditions)

4. Validate parsed spec:
   - Name must be kebab-case
   - Type must be suite, standalone, or task-only
   - At least one content architecture section should have entries (unless task-only)

5. Confirm: "Ready to scaffold `{name}` ({type}) with: {N} tasks, {N} frameworks, {N} templates, {N} context files, {N} checklists. Proceed?"

**Wait for confirmation before continuing.**
</step>

<step name="create_directory_structure">
Create the skill directory and subdirectories.

1. Create the root directory: `{skill-name}/`

2. Create subdirectories ONLY for folder types that have entries in the spec:
   - If tasks listed → create `{skill-name}/tasks/`
   - If frameworks listed → create `{skill-name}/frameworks/`
   - If templates listed → create `{skill-name}/templates/`
   - If context listed → create `{skill-name}/context/`
   - If checklists listed → create `{skill-name}/checklists/`

3. Do NOT create empty directories for folder types with no entries

4. Report: "Directory structure created: {skill-name}/ with {list of subdirectories}"
</step>

<step name="generate_entry_point">
Generate the skill entry point file following specs/entry-point.md.

Create `{skill-name}/{skill-name}.md` with:

**YAML Frontmatter:**
```yaml
---
name: {skill-name}
type: {skill-type}
version: 0.1.0
category: {category}
description: {description}
allowed-tools: [Read, Write, Glob, Grep, Edit, AskUserQuestion]
---
```

**XML Sections (all 5, in order):**

1. `<activation>` — Populate from spec's Activation section:
   - ## What → spec's "What" field
   - ## When to Use → spec's "When to Use" list
   - ## Not For → spec's "Not For" list

2. `<persona>` — Populate from spec's Persona section:
   - ## Role → spec's "Role" field
   - ## Style → spec's style bullet points
   - ## Expertise → spec's expertise bullet points

3. `<commands>` — Populate from spec's Commands table:
   - Render as markdown table: Command | Description | Routes To
   - For suites: Sub-Skill | Description | Entry Point
   - Omit entire section for task-only skills

4. `<routing>` — Derive from content architecture:
   - ## Always Load → context files (loading: always)
   - ## Load on Command → task files (loading: on-command)
   - ## Load on Demand → framework files (loading: on-demand)
   - Use @-references: `@context/{file}.md`, `@tasks/{file}.md`, `@frameworks/{file}.md`

5. `<greeting>` — Compose from skill identity:
   - First line: "{Skill Display Name} loaded."
   - Blank line
   - Available actions as bullet list (derived from commands)
   - Blank line
   - Prompt: "What are you working on?" or similar

**Principle: Keep it thin.** Entry point is identity + routing. No process logic.
</step>

<step name="generate_auxiliary_files">
Generate each file listed in the spec's content architecture.

**For each task file** (specs/tasks.md syntax):
```xml
<purpose>
[Derive from task's purpose in spec]
</purpose>

<user-story>
As a [derive from skill's target user], I want [derive from task purpose], so that [derive from expected outcome].
</user-story>

<when-to-use>
- [Derive trigger conditions from task context]
- Entry point routes here via /{skill-name} {command}
</when-to-use>

<steps>

<step name="gather_input" priority="first">
[Scaffolded first step — gather requirements or input from the user.
Include specific questions relevant to the task's domain.]

**Wait for response before proceeding.**
</step>

<step name="execute_core_work">
[Scaffolded main step — the primary work this task performs.
Include domain-relevant instructions based on the task's purpose.]
</step>

<step name="review_and_deliver">
[Scaffolded final step — present results to user for review.]

Present the output to the user.
Ask: "Does this look right? Any adjustments?"

**Wait for approval or revision requests.**
</step>

</steps>

<output>
[Describe expected output artifact and format]
</output>

<acceptance-criteria>
- [ ] [Domain-relevant completion criterion]
- [ ] [Quality criterion based on task purpose]
- [ ] User approved final output
</acceptance-criteria>
```

**For each framework file** (specs/frameworks.md syntax):
- Start with purpose section explaining what this framework teaches
- Add ## Core Concepts with 2-3 skeleton subsections relevant to the domain
- Add ## Examples section with placeholder
- Add ## Anti-Patterns section with placeholder
- No frontmatter (frameworks are read-only knowledge)

**For each template file** (specs/templates.md syntax):
- Start with `# {Name} Template` header
- Add intro line with output file naming pattern
- Add fenced `template` code block with placeholder fields using correct conventions:
  - {curly-braces} for variable interpolation
  - [square-brackets] for human-written prose
- Add ## Field Documentation table explaining each field
- Add ## Section Specifications with guidance for each section

**For each context file** (specs/context.md syntax):
- Start with `# {Name}` header
- Add standard sections based on the context type (user-profile, business-profile, or custom)
- Use placeholder values: `[Not yet captured]` for empty fields
- No frontmatter (context is plain markdown)

**For each checklist file** (specs/checklists.md syntax):
- Start with `# {Name} Checklist` header
- Add **Purpose:** one-line description
- Add 2-3 category groups with `- [ ]` items relevant to the skill's domain
- Each item must be independently pass/fail verifiable

**Important:** Every generated file must have enough scaffolded content to be immediately useful. Do NOT generate empty shells or files that just say "TODO".
</step>

<step name="validate_and_report">
Validate generated files and report results.

1. Load each rules file from `rules/` directory
2. For each generated file, check against its corresponding rule:
   - Entry point: Has frontmatter? Has all 5 XML sections? Thin?
   - Tasks: Has all required XML sections? Step names snake_case?
   - Templates: Has header, intro, template block, field docs?
   - Frameworks: Has purpose, core concepts?
   - Context: Has header, standard sections?
   - Checklists: Has header, purpose, categorized items?

3. Report results:
   ```
   Scaffold Complete: {skill-name}

   Files created:
   - {skill-name}/{skill-name}.md (entry point)
   - {skill-name}/tasks/{file}.md
   - {skill-name}/frameworks/{file}.md
   - ...

   Validation: {N}/{N} files pass rules

   Next steps:
   1. Review each file and customize for your domain
   2. Replace placeholder content with real domain knowledge
   3. Test by running /{skill-name}
   ```

4. If any validation issues found, list them with fix suggestions.
</step>

</steps>

<output>
## Artifact
Complete skill directory with all files scaffolded from the skill spec.

## Structure
```
{skill-name}/
├── {skill-name}.md          (entry point)
├── tasks/                   (if tasks in spec)
│   └── {task-name}.md
├── frameworks/              (if frameworks in spec)
│   └── {framework-name}.md
├── templates/               (if templates in spec)
│   └── {template-name}.md
├── context/                 (if context in spec)
│   └── {context-name}.md
└── checklists/              (if checklists in spec)
    └── {checklist-name}.md
```

## Location
Created in the current working directory or user-specified path.
</output>

<acceptance-criteria>
- [ ] Skill spec successfully parsed with all sections extracted
- [ ] Directory structure created with only populated folder types
- [ ] Entry point has correct YAML frontmatter and all 5 XML sections
- [ ] All auxiliary files follow their respective syntax specs
- [ ] Generated files contain meaningful scaffolded content (not empty placeholders)
- [ ] Validation report shows all files pass rules
- [ ] User informed of results and next steps
</acceptance-criteria>
