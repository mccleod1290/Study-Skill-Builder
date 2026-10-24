---
name: trajectory_distill
description: >-
  self-improvement loop. reads a DeepSeek Harness trajectory export (every
  assistant reasoning step and tool call) and turns it into two HTML files:
  one with all assistant reasoning, one with the reasoning and tool use the
  model and harness did that our skill did not cover. then emails both. the
  gaps feed the skill factory and phase 4. use when the user says distill the
  trajectory, self improve, what did the model do beyond the skill, review the
  run, trajectory distill, or /trajectory_distill.
model: inherit
effort: high
---

# trajectory_distill

The harness already records the whole run: every assistant reasoning step, every tool call, every result (`deepseek-ai/deepseek-harness`, the "Trajectory" tab, "Download session log"). The old hooks never saw the reasoning. This skill reads that export and finds what the run did that the skill did not teach, so the skill improves.

## Inputs

1. The trajectory export: a session-log JSON from the harness. Save it to `Artifacts/sessions/<...>/trajectory.json` and give the path. If none is named, stop and ask.
2. The skill the run was meant to follow, by name (for a hunt, `Research-Skill`; for a study run, the phase skills). Read its `SKILL.md` and references so you know what it covers.

## Steps

1. Parse the export: `python skills/self_improve/trajectory_distill/scripts/distill.py <trajectory.json> <out_dir>`. It writes:
   - `reasoning_all.html` — every assistant reasoning step, in order, each with its turn and step number and the tool calls that followed it.
   - `reasoning_steps.json` — the same, machine-readable, for your gap pass.
2. **Document all reasoning first.** Open `reasoning_all.html`. Confirm it has every assistant step from the export, none dropped. This is the record, not yet the judgement.
3. **Then document the gaps.** Read `reasoning_steps.json` against the named skill. For each reasoning step or tool call the model or harness did that the skill does not describe, write one entry: what it did, why it mattered, and the skill step it should become. Write these to `reasoning_gaps.html`. Ground each gap in the trajectory (cite the turn and step). Do not invent a gap the trajectory does not show.
4. **Email both.** `python skills/scripts/send_notes_email.py --subject "trajectory distill <slug>" --body "all reasoning, then the gaps" <out_dir>/reasoning_all.html <out_dir>/reasoning_gaps.html`. Email needs the SMTP env file: see `references/email-setup.md`. Send only when he asks.
5. **Close the loop.** Append each real gap to `skill_factory/feedback.md`. A gap that recurs is a skill change: `skill_smith` builds it, `diagnostician` routes it.

## Output

`reasoning_all.html` and `reasoning_gaps.html` under the run's topic folder in `Artifacts/`, HTML per `.rules/html-deliverables.md`. Lines in `skill_factory/feedback.md`.

## Do not

- Do not grade the run from memory. Read the export.
- Do not put any password, key or token in a file or in the email body. The SMTP credential lives only in the env file (`references/email-setup.md`).
- Do not claim a gap the trajectory does not show.
