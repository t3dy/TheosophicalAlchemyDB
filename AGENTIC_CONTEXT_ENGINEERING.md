# Agentic Context Engineering Best Practices

**Derived from TheosophicalAlchemyDB Project (Phases 0–1)**

This document consolidates patterns and principles discovered while building a 206-entity knowledge portal with LLM agents across 5+ sessions. Apply these to similar multi-phase, multi-session projects.

---

## Problem Statement

**Challenge:** How do you maintain coherence, quality, and direction across multiple LLM agent sessions when:
- No single session has full context (context window limits)
- Agents don't remember prior sessions
- Project scope grows iteratively
- Quality standards must hold across 200+ entries
- User desires emerge gradually (not fully specified upfront)
- Work spans weeks/months with multiple context resets

**Solution:** Comprehensive documentation infrastructure that serves as "external memory" for the agentic environment.

---

## Core Principle: Documentation is Code

**In traditional software:** Code is the source of truth. Comments, READMEs, tickets are secondary.

**In agentic environments:** Documentation IS the source of truth. Code/data are secondary.

**Why?** An LLM agent reading documentation is fundamentally different from an LLM reading existing code:
- Reading code requires parsing syntax, understanding state, inferring intent
- Reading documentation can be declarative: "Here's what we want, here's how to do it"
- Reading code is brittle: changes break understanding
- Reading documentation is robust: it can be kept up-to-date and explicit

**Implication:** Invest heavily in documentation. It's not overhead; it's your primary tool for agent coordination.

---

## The Documentation Stack (5 Layers)

### Layer 1: Master Requirements Document

**Purpose:** Single source of truth for what the user wants.

**File:** `CONVERSATION_REQUIREMENTS_HARVEST.md`

**Content:**
- Every explicit requirement from every session
- Every inferred/implicit requirement
- Indexed by session so agent can see evolution of desires
- Consolidated master list at end
- Success metrics and critical success factors
- Context engineering principles discovered

**Why it matters:** Agent can read this once to understand the entire vision, without re-asking user for clarification.

**Pattern:**
```markdown
## Session N: [Description]

### Explicit Requirements
- [ ] Requirement 1
- [ ] Requirement 2

### Implicit Requirements
- Inferred desire 1
- Inferred desire 2

---

## Consolidation: Master Requirements List
- ✅ Completed item 1
- [ ] Pending item 2
- [ ] Critical success factor 1
```

**Update:** Append to end of conversation, before each session ends.

---

### Layer 2: System Prompt / Project Constitution

**Purpose:** How to work on this project; non-negotiable standards.

**Files:** `CLAUDE.md`, `PROMPTS.md`, `STYLEGUIDE.md`

**Content:**

**CLAUDE.md:**
- Project overview (what is this?)
- Active phases and status
- Critical constraints (e.g., "portal must remain live")
- File structure (where are things?)
- How to get help
- Links to detailed docs

**PROMPTS.md:**
- Canonical vision statement (what should this become?)
- Design principles (what matters to the user?)
- User communication style (how to interact?)
- Examples of good work
- Examples of bad work

**STYLEGUIDE.md:**
- Writing standards (for entries, essays, descriptions)
- Voice and tone
- Common pitfalls
- Quality checklist
- Examples of exemplary work
- Version history (how standards evolved)

**Why it matters:** Agent can read these once and know the operating principles without constant user clarification.

**Pattern:** Update section-by-section as learning accumulates. Keep version history showing how standards evolved.

---

### Layer 3: Data Schema Documentation

**Purpose:** Explicit specification of data structure; enables agent to write data correctly.

**File:** `ONTOLOGY_UPDATED.md` or similar

**Content:**
- Entity types (figures, concepts, texts, emblems, etc.)
- For each entity type:
  - Required fields and types
  - Optional fields
  - Constraints (e.g., "every concept links to ≥2 others")
  - Example (full JSON)
- Relationships (how entities link)
- Validation rules
- Fields to update when learning deepens

**Why it matters:** Agent doesn't have to reverse-engineer JSON structure from examples; it's explicit.

**Pattern:**
```markdown
## Entity Type: Figure

### Required Fields
- id (integer, unique)
- name (string)
- birth_year (integer)
- death_year (integer)
- lat (float, -90 to 90)
- lng (float, -180 to 180)
- summary (string, 100-150 words)
- essay (string, 500-1500 words)
- scholars (array of strings, ≥2)
- concepts (array of concept IDs, ≥2)

### Optional Fields
- nickname (string)
- gender (string)
- image_url (string)

### Constraints
- birth_year < death_year
- summary is concise overview; essay is detailed biography
- scholars must be names of actual scholars (Yates, Godwin, etc.)
- concepts must reference valid concept IDs

### Example
[Full JSON example]
```

**Update:** Refine as you learn more about what data you need. Add new entity types as scope grows.

---

### Layer 4: Phase Roadmap & Status

**Purpose:** What's in progress, what's blocked, what's next.

**Files:** `PHASESTATUS.md`, `PHASE_2_HANDOVER.md`

**Content:**

**PHASESTATUS.md:**
- Current phase (0, 1, 2, etc.)
- Objectives for this phase
- Completion date (target + actual)
- Completed items (with checkmarks)
- Blocked items (with explanations)
- Next steps
- Metrics (how many entries, how much done)
- Session log (who did what, when)

**PHASE_N_HANDOVER.md:**
- Detailed roadmap for phase (7 workstreams, timeline, milestones)
- Success criteria
- Critical notes for next agent
- Common pitfalls
- Escalation points (when to ask user questions)
- Files to reference

**Why it matters:** Agent knows what's in scope for this phase; doesn't get distracted; can prioritize.

**Pattern:** Update PHASESTATUS.md weekly. Create detailed handover docs when transitioning phases.

---

### Layer 5: Quick Reference Guides

**Purpose:** Fast lookup for common questions.

**Files:** `QUICK_START.md`, `RESUMPTION_PROMPT.md`, `README.md`

**Content:**

**QUICK_START.md:**
- What is this project? (1 paragraph)
- The entity types (brief explainer for each)
- The data structure (simple JSON example)
- How to build & deploy (4 step process)
- Key files and their purpose
- Writing standards (TL;DR)
- Current phase status
- Scholarly authorities (table)
- When you get stuck (checklist)

**RESUMPTION_PROMPT.md:**
- Copy-paste prompt for new session
- "Read these files first" (prioritized list)
- Current task and workstreams
- Key constraints
- User communication style
- What success looks like

**Why it matters:** New agent gets oriented in minutes, not hours.

**Pattern:** QUICK_START.md doesn't change much; keep it stable. RESUMPTION_PROMPT.md updates with each phase.

---

## The Documentation Workflow

### At Phase Start

1. **Create PHASE_N_HANDOVER.md**
   - Detailed workstream breakdown
   - Timeline and milestones
   - Success criteria
   - Critical notes for executing agent

2. **Update RESUMPTION_PROMPT.md**
   - New task description
   - New reading list
   - Updated constraints

3. **Update PHASESTATUS.md**
   - Record phase start date
   - List objectives
   - Reset "Next Steps"

### During Phase Execution

1. **Agent updates PHASESTATUS.md** at end of session
   - Add completed items
   - Note any blockers
   - Update next steps
   - Add session log entry

2. **User provides feedback** (corrects approach, confirms what worked)
   - **Agent documents feedback** in a memory file or comment in PHASESTATUS.md
   - Example: "User feedback: Prefer one bundled PR over many small ones (saves churn)"

3. **Agent discovers patterns** (e.g., "all concept essays need etymological grounding")
   - **Agent updates STYLEGUIDE.md** to capture the pattern
   - Example: Add section "Etymological grounding: always explain where term comes from"

### At Phase End

1. **Agent updates CONVERSATION_REQUIREMENTS_HARVEST.md**
   - Add session section
   - Document what was completed vs. deferred
   - Consolidate new learning into master list

2. **Agent creates next-phase handover doc**
   - Detailed roadmap for Phase N+1
   - References learning from Phase N

3. **Agent updates PHASESTATUS.md**
   - Record completion date
   - Update metrics
   - Add comprehensive session log entry

---

## Key Patterns

### Pattern 1: "Write-First, Integrate-Second"

**Problem:** Agent gets overwhelmed trying to write entries AND integrate them into data structure.

**Solution:**
1. Write complete, standalone entries first (essays, descriptions)
2. Then integrate into JSON/database with relationships
3. Allows quality control before database commit

**Implementation:**
- Create entries in staging files first
- Review quality
- Then merge into `prototype_data.json`
- Then rebuild portal and test

**Documentation:** Add to STYLEGUIDE.md and PHASE_N_HANDOVER.md.

---

### Pattern 2: "Scholarly Rigor Over Completeness"

**Problem:** Agent tries to cover everything shallowly rather than some things deeply.

**Solution:** Document explicit quality minimum:
- "Every entry must have 300+ word substantive content"
- "Every entry must cite ≥2 scholarly sources"
- "Every entry must have ≥3 relational links"

**Implementation:** Add quality checklist to STYLEGUIDE.md. Agent self-checks before submitting.

**Documentation:** Put checklist in STYLEGUIDE_UPDATED.md and reference in PHASE_HANDOVER.

---

### Pattern 3: "Entity as Gateway Entry"

**Problem:** Which entity type is highest-leverage to focus on?

**Solution:** For this project, emblems are gateway entries.
- Each emblem reveals 3-5 concepts
- Each emblem connects to 2-3 figures
- Building emblem entries builds out entire relational graph

**Implementation:** Prioritize emblem research. Phase 2 focus is on emblems.

**Documentation:** Put in CONVERSATION_REQUIREMENTS_HARVEST.md "Critical Implementation Patterns" section.

---

### Pattern 4: "Genealogical Thinking"

**Problem:** Agent treats historical figures as isolated, not as transmitters of knowledge.

**Solution:** Emphasize transmission genealogy in STYLEGUIDE.md:
- "For every figure, ask: Who did they learn from? Who learned from them?"
- "Show continental differences (Islamic alchemy ≠ European)"
- "Document women's participation despite marginalization"

**Implementation:** Add "Transmission Tracking" section to STYLEGUIDE.md with examples.

**Documentation:** Reference in every figure biography. Show genealogy in concepts.

---

### Pattern 5: "Embodied Practice Integration"

**Problem:** Agent writes theory without grounding in actual practice.

**Solution:** STYLEGUIDE.md standard:
- "For every concept, ask: What does a practitioner actually DO?"
- "Laboratory alchemy: what operations produce what results?"
- "Spiritual alchemy: what practices transform consciousness?"

**Implementation:** Add examples to STYLEGUIDE.md. Provide templates for concept essays.

**Documentation:** Make it explicit in "Concept Definitions" section of STYLEGUIDE.

---

## Anti-Patterns (What NOT to Do)

### ❌ Anti-Pattern 1: "Scattered Requirements"

**Problem:** User desires spread across chat messages, Slack threads, comments. Agent can't find them.

**Solution:** Consolidate into CONVERSATION_REQUIREMENTS_HARVEST.md. Index by session.

---

### ❌ Anti-Pattern 2: "Implicit Standards"

**Problem:** Agent guesses at writing style, data format, quality minimum by reading examples.

**Solution:** Make standards explicit in STYLEGUIDE.md. Document every example as precedent.

---

### ❌ Anti-Pattern 3: "Silent Failures"

**Problem:** Agent quietly diverges from user vision (wrong style, missed requirements, unclear links).

**Solution:** Explicit testing and sign-off on live site. User reviews portal before next phase.

---

### ❌ Anti-Pattern 4: "Context Collapse"

**Problem:** Agent runs out of context mid-task, loses work or creates inconsistencies.

**Solution:** Commit frequently (daily). Update PHASESTATUS.md. Create detailed handover docs.

---

### ❌ Anti-Pattern 5: "One-Way Communication"

**Problem:** Agent executes blindly without asking clarifying questions when scope ambiguous.

**Solution:** Escalation points in PHASE_HANDOVER.md. Agent asks user BEFORE acting if confused.

---

## Metrics & Tracking

### What to Track

**Quantitative:**
- Entries created (figures, concepts, texts, emblems)
- Geographic coordinates added/verified
- Relational links established
- Scholarly sources cited
- Images sourced
- Pages read/ingested from PDFs

**Qualitative:**
- % entries meeting style guide standards
- % entries with historiographical rigor (multiple perspectives shown)
- % entries with gender awareness
- % entries with transmission genealogy documented
- % entries with embodied knowledge grounding
- % features tested on live site

### Where to Track

**PHASESTATUS.md:**
- Session-by-session log
- Cumulative metrics table
- Blockers and resolutions

**Data Quality Validation Script:**
- Automated checks for required fields
- Relationship integrity (every link goes somewhere)
- Coordinate validation (lat/lng within range)
- Circular dependency checks

---

## Failure Recovery

### If Context Runs Out Mid-Task

1. **Agent commits work immediately**
   - `git add -A`
   - `git commit -m "WIP: [descriptive message about what was in progress]"`

2. **Agent updates PHASESTATUS.md**
   - What was completed
   - What was in progress
   - What blocked (if anything)
   - Exact next step for resumption

3. **Next agent reads RESUMPTION_PROMPT.md**
   - Orients quickly
   - Picks up exactly where previous agent left off

### If Requirements Change Mid-Phase

1. **User communicates new desire**
   - Agent documents in PHASESTATUS.md as "New requirement discovered"
   - Agent adds to CONVERSATION_REQUIREMENTS_HARVEST.md

2. **Agent asks for clarification if scope unclear**
   - Reference: PHASE_HANDOVER.md "Escalation Points"

3. **Agent updates phase roadmap if needed**
   - Adjust timeline/workstreams if necessary
   - Document change and reason

### If Quality Issues Discovered

1. **Agent flags in PHASESTATUS.md**
   - Which entries don't meet style guide
   - Why they fail (e.g., "No historiographical debate shown")

2. **Agent can fix incrementally**
   - Create PR with corrections
   - Document what was fixed and why

3. **User reviews** before next phase start

---

## Adaptation to Other Projects

This framework works for any multi-phase LLM project with:
- 100+ entities (whether documents, code, data, or content)
- 6+ weeks timeline
- 3+ session resets
- Quality/consistency requirements
- User involvement without user being in every session

**Adapt these documents:**
- CONVERSATION_REQUIREMENTS_HARVEST.md → "Project Vision & Evolution"
- STYLEGUIDE.md → "Writing/Code/Design Standards" (whatever applies)
- ONTOLOGY_UPDATED.md → "Data Schema" or "Architecture Documentation"
- PHASESTATUS.md → "Project Status & Phase Log" (same)
- PHASE_N_HANDOVER.md → "Phase Roadmap" (same)
- RESUMPTION_PROMPT.md → "Session Start Prompt" (same)
- QUICK_START.md → "Quick Orientation" (same)

---

## The Mindset: Build for Amnesia

**Key insight:** Assume the agent reading your documentation has zero context from prior sessions.

**Write as if:**
- "I am a new agent. I have no memory of prior work. I have 5 minutes to orient. What do I need to know?"

**Don't assume:**
- "The agent will remember we decided X" (put it in docs)
- "The code comments are clear enough" (add explicit docs)
- "The examples show the standard" (write a style guide)
- "The user will re-explain" (harvest their desires once)

**Every document should be self-contained:** A new agent should be able to read QUICK_START.md → RESUMPTION_PROMPT.md → PHASE_HANDOVER.md and be productive within an hour.

---

## Final Principle: Documentation is a Skill

Writing clear, comprehensive documentation for LLM agents is different from writing for humans.

**Key differences:**

| Aspect | Human Documentation | Agent Documentation |
|--------|-------------------|-------------------|
| **Explicitness** | Can be implicit; context assumed | Must be fully explicit; no context assumed |
| **Structure** | Can be narrative/exploratory | Must be structured/declarative |
| **Examples** | Illustrative | Prescriptive (these are the standards) |
| **Completeness** | Can be partial (fill in gaps with experience) | Must be complete (agent can't guess) |
| **Updating** | Often stale; maintainers give up | Must be kept current; it's the source of truth |
| **Audience Assumption** | Knowledgeable professional | Blank slate with specific reasoning capabilities |

**Best practices for agent-focused docs:**

1. **Declarative, not narrative:** "Figures must include transmission genealogy" not "It would be nice to show how ideas spread"
2. **Prescriptive, not descriptive:** "Follow this template" not "We usually do it like this"
3. **Indexed, not sequential:** Agent skips around; make every section self-contained
4. **Explicit constraints:** "Every concept links to ≥2 others" not "Link concepts when relevant"
5. **Examples as specification:** Show exemplary work as standard to match, not inspiration
6. **Version history:** When standards evolve, show it; agent can understand why old entries differ
7. **Checklists, not prose:** "[ ] Historiographical rigor: multiple perspectives shown" is better than paragraph explanation

---

## Conclusion

**The investment in documentation pays off exponentially:**

- **Session 1:** Document setup (8 hours)
- **Session 2:** Fewer clarifying questions; execute faster (6 hours saved)
- **Session 3:** Zero onboarding; continuation from docs; maximum productivity (4 hours saved)
- **Session 4+:** Each session builds on previous without re-explanation (12+ hours saved over 3 sessions)

**Result:** Instead of 40+ total hours spread over 5+ sessions with constant clarification, you get:
- 30 hours of productive work
- Better quality (standards are explicit, not inferred)
- Less frustration (agent knows what to do)
- Faster context resets (new agent orients in 30 minutes)

**Bottom line:** In agentic environments, documentation is not overhead. It's the primary tool for coordination and quality control. Build it first. Keep it current. Trust it.

---

**Last Updated:** 2026-05-25  
**Applies to:** TheosophicalAlchemyDB and similar multi-phase knowledge portal projects  
**Next Review:** End of Phase 2 (2026-06-21)

