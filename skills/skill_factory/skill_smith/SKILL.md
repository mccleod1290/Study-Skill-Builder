---
name: skill_smith
description: >-
  skill factory. turns the skill candidates from the depth, range and altitude
  agents into runnable, private skills: a step-by-step guide, scripts, a
  checklist, a lab and a verification test. then reads the execution feedback
  from labs, CTFs, bounty and work back into the backlog. use when the user
  says build the skill, skill factory, make this runnable, turn this into a
  skill, skill_smith, or /skill_smith.
model: inherit
effort: high
---

# skill_smith

The factory is the last stage of the loop: study -> wiki -> depth, range, altitude agents -> factory -> real use -> feedback -> backlog. Everything it builds is private. It stays under `skill_factory/built/` and is never exported.

## Inputs

1. Candidates in `skill_factory/inbox/<slug>/*.md`, written by the three agents in `.agents/`. If the inbox is empty, stop.
2. The wiki pages the candidate cites (`llm_wiki/wiki/`).
3. The house rules: `.rules/skill-authoring.md`. Use `skills/misc/skill_creator` to write each skill.

## Steps

1. **Pick.** One candidate per run. Skip a candidate that an existing skill already covers. Say which skill covers it.
2. **Build the five parts** in `skill_factory/built/<skill_name>/`:

| part | file | what |
|---|---|---|
| guide | `SKILL.md` | the step-by-step skill, front matter per `.rules/skill-authoring.md` |
| tools | `scripts/` | any step that must give the same result each time |
| checklist | `references/checklist.md` | the workflow to run in practice |
| lab | `references/lab.md` | one hands-on exercise on an authorized target (lab, CTF, own machine) |
| test | `references/verify.md` | the quiz or exercise that proves the skill, with the pass mark |

3. **Validate.** `python skills/scripts/validate_skill.py skill_factory/built/<skill_name>/SKILL.md` must print OK.
4. **Outside check.** Run the test in `verify.md` with a fresh subagent that did not build the skill. Record the result.
5. **Move the candidate** from `inbox/` to `inbox/done/`.

## Feedback loop

After he uses a skill in a lab, a CTF, a bounty or work, append one line to `skill_factory/feedback.md`:

```text
## [YYYY-MM-DD] <skill_name> | <where used> | worked: ... | did not: ... | gap: ...
```

A gap goes to the learning backlog: phase 4 `diagnostician` reads `feedback.md`, and `altitude_agent` re-ranks the roadmap from it.

## Do not

- Do not write a built skill into `skills/`, `.claude/skills/` or the public export. Built skills are private.
- Do not build a skill that acts on a target he has not named as authorized.
- Do not mark a skill proven without the outside check.
