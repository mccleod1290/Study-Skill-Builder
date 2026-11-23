---
name: second_order_thinking
description: >-
  phase 2 skill. traces what happens after the first effect of a decision, mechanism
  or default, and says which later effect is the lesson. gives the phase 2 writer one
  consequence chain per node (phase2_so.md) and a gate that keeps next-event sentences
  to the places where the next event is the lesson. runs after first_principles, only on nodes
  reduce_ambiguity marked, for a decision, mechanism or default.
  skip it when the map has none. does not write the page and does not run
  first_principles. use when the user says and then what, second order effects, what
  happens next, consequences of this decision, unintended consequences, think it
  through, or /second_order_thinking.
model: inherit
effort: high
---

# second_order_thinking

Order of runs: `first_principles` first (what is true), then this skill (what follows). Files: `phase2_fp.md`, then `phase2_so.md`.

Trace what happens after the first effect of a decision, a mechanism or a default. Say which later effect is the lesson. Most are not. A next-event sentence (`CRITERIA.md` calls it a next-event line) is the point of its section, or it stays off the page.

This is inline guidance. It does not fork: it needs the chat and the two files of the run. It writes one working file and no page.

Tags. `[n] g5:` source n says it (the grade is for what it says, not for whether it is true). `[n] g5 (says), g3 (true):` the source says it, and only a blog backs the claim about the world. `reading g2:` this skill's own reading, not verified. `rule:` a rule or definition of this skill. No source gives it (g2). It is not a claim about the world. Scale: `.rules/grounding-and-confidence.md`. Source numbers: `references/sources.md`.

## Where it sits

| skill | owns |
|---|---|
| `skills/phase_2/PAGE_ORDER.md` | the page order, the lens gate, and the one-line rule: second-order only where the next event is the lesson |
| this skill | the method, the tests, the cap and the chain file behind that rule. It runs after `first_principles`, only on nodes `reduce_ambiguity` marked, for a decision, mechanism or default. Skip it when no node is marked |
| `skills/phase_2/skills/writer_skill/SKILL.md` | the sentences |
| `skills/phase_2/skills/frugal_judge/SKILL.md` | the verdict, from `skills/phase_2/CRITERIA.md`, check `second_order` |

Do not edit them. Do not copy their text here.

## Read first

1. `Artifacts/artifacts/<group>/<slug>/phase2_fp.md`. first_principles wrote it. Do not edit it. Take the node ids and the `base grade` from it (the weakest grade among the law and convention parts the rebuild stands on). Why: later links of a chain rest on the first, and the weakest link limits a chain. [11] g5: Urban says the weakest link limits a chain of reasons. `reading g2`: the first link of a chain of effects matters most.
2. `phase1_mindmap.json` in the same folder. Older runs keep it in `skills/phase_1/output/<slug>/`. A map pasted in the request counts as the file. It gives the node ids and the number of domain sections.
3. `phase2_sources.md` in the same folder. Cite each later effect by an id from it. A new source goes into that file. Do not start a second list.

| case | do |
|---|---|
| page run, `phase2_fp.md` missing | stop. Say: run first_principles first. Rows pasted in the request count as the file |
| chat-only decision (one decision asked in chat, no map) | continue. One decision is one row, id `chat1`. Put side effects inside the order cells. The No chain list says `none`. Use `chat2` only when he asks for a second decision. Grade the first order here. The base floor in step 2 and the cap do not apply: no `phase2_fp.md` row exists, and the topic is a decision. With group and slug given, write `phase2_so.md`. Cap the reply at 150 words plus the file path |
| group or slug missing | give the table in the reply. Write no file. Name the path it would take. Ask for the group and the slug |

## When to run

Run on a decision (a choice among options), a mechanism (it runs and feeds something else) or a default (the value in force when nobody sets one). Do not run on a definition, a list, a flag or a syntax. There the first effect is the whole point.

Trace in full when the first option fits what you already want. [1] g5 (says), g3 (Dalio said it): the page credits Dalio with the warning that ignoring later effects hurts most when the first poor option fits your bias. The quote names no work.

## Steps

1. Sort each node: decision, mechanism, default or none. A node of kind none gets no chain: list its id in the No chain list. Why: a chain on a definition is filler.
2. Write the first order from what `phase2_fp.md` says is true, with its `base grade`. A node whose base grade is below g3 gets no chain: write `no: base`. Why: a guess on a guess is not a chain.
3. Ask "and then what?". The answer is the second order. Ask again for the third. Back each later effect with a source from `phase2_sources.md`, or open one and add it there. With no source, the effect is a guess. `references/concepts.md` has what the sources say about orders.
4. Probe the horizons: 10 minutes, 10 months, 10 years. Write none where nothing changes. Why: people miss delayed harm. [6] g5 (says): harm is easy to tie to an intervention when it is immediate, visible and direct.
5. Ask how each party responds. Use only the listed parties. Business decision: employees, competitors, suppliers, regulators [1] g5. System: users, operators, attackers, vendors (`reading g2`: no source gives this list). Add a party only when the decision names it, and cite a source for its effect. Write `party: effect` for each listed party that responds. Leave out a party that does not respond. Write the single word `none` only when no listed party responds.
6. Check the chain: words, numbers, effects (Hardin). Harm as well as gain (iatrogenics). Why a later effect was missed (Merton). Read `references/checks_and_warnings.md`.
7. Look for the two shapes in `references/cases.md`: cost now and gain later, gain now and cost later. At the third order, look for a reversal.
8. Apply the stop rule.
9. Apply the gate: three tests, rank, cap, floor. Fill the lesson cell. A `no` row is a result, not a gap.
10. Write the file from `assets/so_chain.md`. Set the review date and the reviewer. Count the rows by grade. Every node id of the map appears once: in the Chain table or in the No chain list.
11. Pass the file to the writer. The writer puts one `**Next event.**` sentence for each kept row in its section, with its source and grade. Place it last, after the how part. Never first: the page order is parts, condition, when it does not apply, then how (`CRITERIA.md`, check `first_principles`). A `no` row with a real limit goes into the condition part or the when-it-does-not-apply part, as plain prose with no label. The table and the three tests stay off the page. They are working notes, and a page has no quiz (`CRITERIA.md`, check `not_a_test`).

## Gate (binding)

`CRITERIA.md`, check `second_order`, is the authority. The judge reads it and no other rubric. This section is how this skill meets it.

A next-event sentence goes in a section only when the next event is the lesson. A section is a domain section of the page (`d1`, `d2`), the unit `CRITERIA.md` uses for pages and words. A topic or an anchor sits inside a section: the id `d2g` belongs to `d2`.

Test each traced row. All three answers must be yes.

| # | test | ask | a no means |
|---|---|---|---|
| 1 | reader | If the section ended at the first effect, would the reader hold a wrong picture or take a wrong action? | the first effect is the whole point. Write `no: reader` |
| 2 | kind | Does the later effect differ from the first in sign, in who is hit, or in kind? | it is more of the same. Write `no: kind` |
| 3 | source | Does an opened source back the later effect at g3 or higher? | it is a guess. The row stays at g2, not verified. Write `no: source` |

Cap. At most one section in three carries a sentence. Cap = domain sections divided by 3, rounded down, and at least 1. A section carries at most one sentence. A run over part of the map (one domain at a time) counts the sections on the page so far, this run's included, and the sentences already there. Over the cap, keep the strongest rows. A reversal of sign ranks first. A new party hit ranks second. A delay alone ranks third. Ties go to the higher grade. The rest become `no: cap`.

Floor. When the page has more than one section, at least one section carries no sentence, even under the exception. A page with one section carries a sentence only if all three tests pass and the lesson cell says why the first effect alone misleads.

Exception. The cap does not apply to a section whose topic is itself a decision, or a control with a known side effect. Known means documented in an opened source at g3 or higher. Name the side effect and its source in the lesson cell and in the header. The three tests and the floor still apply.

`rule:` The tests, the cap, the floor and the 1-in-3 ratio are this skill's design, set 2026-11-21. No source gives them. The ratio is a default. Tune it after real runs.

## Stop rule

Stop at the first order where either is true:

1. Decision. The next order would not change what the reader does or decides.
2. Noise. The next order is below the noise: you cannot size it against the first effect, or it is smaller than the spread of the first. [7] g5: Merton says a repeated act gives a range of results, and chance effects come from too many forces to predict. He adds that there are limits to waiting for certainty.

Three orders is the default stop. Go to a fourth only when the third still changes the decision. Write the reason in the Stops block. A guess does not stop the chain. It gets a mark: end its cell with `(g2, not verified)`. A guess never carries a next-event sentence (gate test 3).

`rule:` The stop is a rule of this skill, not of the sources. Why: `references/concepts.md`, section "Why the stop is a rule".

## Output

Where: `Artifacts/artifacts/<group>/<slug>/phase2_so.md`. Only there. The path follows the phase2_writer agent, not `skills/phase_2/PATHS.md`. The two differ. Proposal: update PATHS.md. Copy `assets/so_chain.md`, fill the copy, leave the template alone. The template holds the nine column names, the header fields and the cell formats. The file is a markdown working file. The page is HTML and stays with the writer.

Pair sentence. It opens the file and the reply, word for word. Page run: `Pair: first_principles wrote phase2_fp.md (what is true). second_order_thinking wrote phase2_so.md (what follows).` Chat-only decision: `Pair: first_principles not run (chat-only decision). second_order_thinking wrote phase2_so.md (what follows).` Group or slug missing: `Pair: first_principles not run (chat-only decision). second_order_thinking wrote no file (group or slug missing).`

Node ids are bare, as in `phase2_fp.md`: `d1a`, and `chat1` for a decision typed in chat. Braces (`{d1a}`) are the page-tag form only. The writer joins the two files by node id.

Reply in chat with the path, the Pair sentence, the kept rows, the grade tally and what is not verified. Name the later effect that matters most, even when its row is `no: source`, and say it is a guess. At most 150 words of prose plus the path. The table stays in the file.

## Do not

- Do not write the page, an HTML file, or any file outside `Artifacts/artifacts/<group>/<slug>/`.
- Do not edit `phase2_fp.md`, the template or any other skill. Name a missing feature in the reply.
- Do not write a number, a percentage or a probability for an effect without a source. That is false precision.
- Do not state a guess as a fact. Mark it g2, not verified.
- Do not borrow Hardin's policy positions. Take the method only [4].
- Do not read Merton or [6] as a rule to do nothing. Limits: `references/checks_and_warnings.md`.

## model

model: inherit. no pinned model id.
effort: high. the failure is a next-event sentence on every section. Three more: false precision (a third order written as fact, with no source and no size), an endless chain (and then what, until nothing can change), and a chain with no reviewer (a forecast nobody checks).

## Files in this folder

- `assets/so_chain.md`: the template. Copy it for every run.
- `references/concepts.md`: read at step 3, or when you need what the sources say about orders, Marks's levels, the four practices or why the stop is a rule.
- `references/checks_and_warnings.md`: read at step 6, when you use the word iatrogenic, or when a later effect looks too clean. Hardin's three checks, the iatrogenics warning, Merton's factors.
- `references/cases.md`: read when you need an example of a kept row, a dropped row, or one of the two shapes.
- `references/sources.md`: read when you cite or reuse a claim and need its source, its grade and its limits. It holds the source list [1] to [15].
- `evals/evals.json`: two test prompts. Both write into the scratch group `second_order_thinking-workspace`. Each assertion has a [format] or a [substance] tag. Score the two tags apart and report both counts for the skill run and the baseline run. A fair baseline may receive `assets/so_chain.md` as plain text.
