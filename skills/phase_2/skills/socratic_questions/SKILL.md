---
name: socratic_questions
description: >-
  phase 2 lens, opt-in. asks him one short question at a time about one marked,
  ambiguous node, until the hole has a name, then adds at most one line to the
  note or page. never lengthens a short note. runs live in the chat only. not the
  phase 3 spar and not a quiz. use when the user says question me on this,
  socratic questions, challenge my note, test my understanding of this node, ask
  me why, or /socratic_questions.
model: inherit
effort: medium
---

# socratic_questions

Third lens, after `first_principles` and `second_order_thinking`. Opt-in. It runs only when he asks, or when `phase2_ambiguity.md` marks a node "socratic". Rule: `skills/phase_2/PAGE_ORDER.md`.

It is not `socratic_spar` (phase 3 is the formal test, against a whole page). This one takes one node and one hole.

## Steps

1. Read the node and its note. Quote the one line that is ambiguous.
2. Ask one question. Wait. Never two. Choose the move: clarify ("what do you mean by X here?"), probe the assumption, ask for evidence, ask for the case where it fails, ask for the next event.
3. Use his answer for the next question. Stop when the hole has a name: a term he mixed up, a condition he skipped, a case he did not see.
4. Write back at most one line. Form: `why: <the condition or the failing case>`. Put it under the node, or in the note body as one bullet.
5. If the note is already at its short budget, the line replaces a weaker line. The note never grows.

## Do not

- Do not put the questions on the page or in the note. The Knowledge Check is the one place for questions (`skills/phase_2/RULES.md`).
- Do not grade him. No score.
- Do not fork. A subagent cannot ask him the next question.
- Do not run on a node with no ambiguity.

The failure is a question list nobody answered, or a note that grew by a paragraph.
