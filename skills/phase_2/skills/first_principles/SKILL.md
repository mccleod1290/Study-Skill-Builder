---
name: first_principles
description: >-
  phase 2 skill. takes one claim, belief, design choice or problem (a node of a phase 1 map),
  splits it into law, convention and assumption, grades each part, and rebuilds from what stays
  true in this context. gives the phase 2 writer a worksheet (phase2_fp.md). does not write the
  page, adds no quiz, and does not order a page: page order goes to `PAGE_ORDER.md`. use when the user
  says first principles on this claim, first principles on this node, what is actually true here,
  break this down, why do we do it this way, challenge this assumption, reason from the ground up,
  or /first_principles.
model: inherit
effort: high
---

# first_principles

Pair: run this first. `second_order_thinking` then says what follows.

One node in. One worksheet out. This skill writes no page. `PAGE_ORDER.md` owns page order. `writer_skill` owns the sentences.

## When the writer calls it

- Trigger (house, 2026-11-23): only on a node `reduce_ambiguity` marked in `phase2_ambiguity.md` as an unclear claim. No mark, no run. Output on the page: one why line at most.
- The phase 2 writer should read `phase2_fp.md` when it exists. A missing file does not stop the writer. A forked writer cannot ask him, so it answers each move from opened sources.
- Wiring: no phase 2 agent or skill names `phase2_fp.md` unless the spawn brief does. `second_order_thinking` reads `base grade` from this file for its `no: base` test.

## Marks

| mark | means |
|---|---|
| `[2 R5 g4]` | Source 2 in `references/sources.md`, claim R5 in its notes file, grade 4. Grades run 1 to 5, higher is better. They are the notes' grades. `references/sources.md` says which were rechecked. |
| `(derived, g4)` | A claim this skill derived from two or more cited passages. A cite names the main sources. The notes file lists them all. |
| `(house)` | Guidance from this skill that no note supports. Treat it as g2. |

The FS page (Farnam Street) is source 1. Urban's post is source 2. A filled worksheet grades its own parts from the sources opened for that topic (`.rules/grounding-and-confidence.md`).

## Gate: run it, or write one short row

The skill treats analogy as the right tool when one of four reasons holds (house, g2). The premise behind each reason is sourced as shown. `references/background.md` has the costs of both tools.

| # | reason | premise |
|---|---|---|
| 1 | routine: the team made this choice many times and knows why (house) | a chef runs on autopilot on a normal day [2 L1 g5] |
| 2 | decomposing costs more than it returns (house) | first principles takes a lot more mental energy, as Musk says [1 C27 g5 as said] |
| 3 | stakes are low: an error is cheap (house) | move 5 asks what an error would cost [1 C10 g5] |
| 4 | the facts move faster than you can use the parts: copy, test, adjust (house) | the parts hold for now [2 U2 g5] |

`references/background.md`, section Gate cases, has five illustrations (house): a login form, a sandbox, a spike agent, a normal day and a bucket name prefix. Each shows the copy and the flip signal. Read it when you write a gate row.

Three lines decide the gate.

1. Routine test, from the node text alone. Count a rule for every new thing, or a step the text says the team repeats, as made 3 or more times. Count it even when the text gives no reason. Read that as a reason the team knows but did not write down, and write it in the row as the carry-over assumption. A reason of only "everyone does it" fails the test. A routine node stops at the gate, unless the text already shows a flip signal.
2. A request to break a node down does not lift the gate. Write the short row.
3. The flip signal names the inputs that would flip the gate. One new input is enough: for example a new data class, a shared tenant or new spend. A change in the facts that the text does not show, such as a vendor feature you found, is not a flip signal. It is reason 4: copy, test, adjust. Note it in the row.

A node that fails line 1 goes on to reasons 2 to 4, and so does a claim that is not a choice. If none of the four reasons holds, run the node in full.

A gate stop is not a dropped node. A topic can be one line. It cannot be missing (`.rules/phase-order-and-coverage.md`, section 2). A gated node gets a short row:

- `parts`: the copied convention with its holder, and the carry-over assumption. An analogy hides a claim: the old case and the new case share the feature that matters (house). Each of the two gets a row in the Parts table, with a grade.
- `condition` and `when it does not apply`: where the copy holds, then the flip signal and any change in the facts that you noted.
- `rebuild (how)`: starts with `gate: analogy`.

A node that is not a claim (a name, a command, a list) gets a one-line row. It says what the node is and how it is used. `rebuild (how)` starts with `gate: not a claim`. `parts` says none, and it has no Parts-table row. Both grade cells say n/a.

## Steps

### 1. Frame the node

Write the claim as stated, in one sentence. Write its context: what, for whom, which version. A part is true in a context, not in general [1 C05 g5]. Then run the gate.

A map node uses its map id (`d1a`). A claim typed in chat has no map: use `chat1`, `chat2`. When no topic folder is named, answer in chat with the header block (Pair line, opened sources, tally) and the same three tables. Write no file. Do not guess a folder.

### 2. Split the claim into parts

A claim has three kinds of part. The split is derived from two FS passages. One splits what you know is true from what you only assume. The other says that what is not a law of nature is a shared belief [1 C02 C07 g5]. The notes do not list three kinds as such (derived, g4). `references/background.md` has an example of each.

| kind | test | record |
|---|---|---|
| law | holds in this context whatever anyone believes. You can point to a measurement, a calculation you ran, or an opened source | context, evidence, grade |
| convention (shared belief) | holds because a named group sets, repeats or agrees it: a price, a default, a standard, a habit, "it was always done this way" | the holder, and what would make the holder change it |
| assumption | nobody tested it in this context, or you opened no source for it | the cheapest test |

- Kind follows the test. Grade follows the evidence. A law with no evidence fails its own test: file it as an assumption, grade 2, "not verified".
- A part that fits two kinds goes under the weaker one: assumption before convention, convention before law. Promote only with evidence. Do not raise a grade without opening a source (`.rules/grounding-and-confidence.md`, section 3).
- Name the holder of every convention. A spec, a vendor default or a team rule that you cannot change is still a convention. Someone holds it (house).
- In software work, file a part as law only when arithmetic or a measurement backs it. A framework behaviour, a header someone chose, a vendor default or a spec is a convention. A measured behaviour of a named version is evidence for a convention. It does not make it a law (house).
- The shared-belief line comes without an argument [1 L07 g5]. Use it as a prompt: law or belief? Do not treat it as settled.

### 3. Question the claim: six moves

Run six moves on the claim: clarify, challenge assumptions, look for evidence, other viewpoints, consequences, question the question. The list is the FS page's six steps [1 C09 g5]. Each move finds one thing and files it in the worksheet. Read `references/questioning.md` before the first run. It has the stems, the filing map (house), the Paul and Elder cross-check and the ask-or-answer rule.

Some stems in `references/questioning.md` carry a +. They are not on the FS page. One is the move 6 stem "which question must be settled first?". It comes from [3 4 15 C27] (derived, g4).

Move 5 asks what an error in this part would cost. The answer sets depth and the gate only. It is a cost, not a chain. If the next event is the lesson, write `so: yes` in the `evidence` cell and leave the chain to `second_order_thinking`.

### 4. Ask why until a stop

Take the claim. Ask why it holds. Answer with a fact you saw, measured or read in an opened source. Ask why about that answer, not about a new topic [5 C30 g5]. Repeat. Write where you stopped and why. Read `references/five_whys.md` before the first run. It has the Toyota example, a chain that ends at "I do not know", and the limits.

Stop at one of three.
1. A law: it holds in this context whatever anyone believes.
2. A measurement: a fact you saw, measured or priced.
3. An honest "I do not know". It is a finding, not a failure. Write it as an open question, grade 1, with the test that would settle it.

The law stop and the "I do not know" stop are derived from the FS page, Urban's model, the notes' working stop rule and the grounding rule (derived, g4) [1 C06 C13; 2 W2; 5 14 9 6 C43]. The measurement stop is this skill's own (house, g2). No opened source gives an objective test of a root cause [5 11 7 14 6 C42 g4]. The stop is a judgement. So record it.

Do not stop at:
- an authority's word. File it as a convention, name the holder, ask the holder's reason, and go on. Urban calls a stop on an authority's word dogma [2 W2 g5];
- the count of five. Five is a rule of thumb [5 C36 g4];
- the first why. The chain feels slow. After one or two whys, people often find they do not know the answer, and they turn defensive [1 C14 g5]. That moment is the finding;
- a symptom or a person. `references/five_whys.md` has both limits.

A chain has known limits, as argued by named sources (g3). When a why has two true answers, run one chain for each. Record the stop reason.

### 5. Rebuild from the parts

Write the goal in one line. Then three outputs, in this order.

1. **What must be true.** A law stays. A convention stays, changes or is routed around: name the holder and the price of change. An assumption must pass a test.
2. **The cheapest set.** The smallest set of changes or confirmations that reaches the goal. Order the tests by cost, cheapest first. Test small before you bet big. Hardin lists history, a pilot test and theory as three ways to cut the cost of error [12 G6 g5].
3. **The gap to the analogy answer.** State the analogy answer, the rebuilt answer, and the difference: none, smaller, larger, or different in kind. The gap shows where the real work sits [2 T1 g4]. A rebuild that lands on the analogy answer is a result. Write it: the analogy was right here (house).

Then treat the rebuild as a hypothesis. Act, collect data, adjust [2 U3 g5]. Ask people who know the field for the catch [2 R1 g5; T1 g4].

Depth. Go one or two levels deeper than people who work from the analogy. The atoms are not required [1 C03 g5]. A part is deep enough when changing it would change the rebuild. Do not decompose below the level where swapping a part changes nothing (house).

`references/rebuild_example.md` holds two worked cases with numbers (a battery pack and a rocket) and a template for software nodes. Read it before the first rebuild, or before a figure goes on a page.

## Output

Fill `assets/fp_worksheet.md`. Save the copy as `Artifacts/artifacts/<group>/<slug>/phase2_fp.md`. Skip `<group>` for an ungrouped topic. It is a working file. The page stays with the phase 2 writer. A rerun overwrites the same file: no date and no `v2` in the name (`.rules/artifacts-and-sessions.md`, rule 3).

The node table has these columns, in this order: `node id`, `claim as stated`, `parts`, `evidence`, `grade`, `base grade`, `condition`, `when it does not apply`, `rebuild (how)`. The order follows the page order that `PAGE_ORDER.md` sets: parts, condition, when it does not apply, then how.

- `parts` lists part ids by kind. A second table holds each part with its kind, holder, evidence and grade. A third table holds the stops.
- `grade` is the weakest grade among all the node's parts.
- `base grade` is the weakest grade among the law and convention parts the rebuild stands on. An assumption is a test to run, so it does not lower `base grade`. A node with no law or convention part takes the grade of its stop. A node that is not a claim: n/a.
- Why `base grade` exists: one untested assumption pulls `grade` to 2 or 1, and `second_order_thinking` would then chain nothing. It takes its `no: base` test (below g3) from `base grade`.
- One row per node, in map order. No node is dropped.
- The tally of parts by grade sits at the top, weak spots first (`.rules/grounding-and-confidence.md`, section 3).
- The partner file `phase2_so.md` uses the same `node id`. The writer matches the two files by node id.
- For a vulnerability node, `when it does not apply` can seed item (c) of the Discovery section. The writer owns that section (`skills/phase_2/RULES.md`, item 4).
- Chat length: at most 700 words for each full-run node and 150 for each gate row. A node's count includes its Parts-table and Stops rows. The header block does not count (house).
- Reply in chat with the path, the verdict per node (run or gate) and what is not verified. One short reply (`.rules/context-isolation.md`, rule 3).

## Do not

- Do not write the page, reorder it, or add a quiz, a workbook or a question block. `writer_skill`, `PAGE_ORDER.md` and `skills/phase_2/RULES.md` own those. The six moves are working tools: do not copy them to the page as a list of questions. The Knowledge Check is the only question section, and it is the writer's.
- Do not file a convention as a law. A spec, a default or a team rule has a holder.
- Do not run it on a routine node. Use the gate.
- Do not present a figure from the notes as current data. The 2 percent and the 80 dollars per kWh are g3 and are examples of the method [1 W1 W2 L04].
- Do not merge Urban's first principles with Aristotle's, and do not link Musk's phrase to Aristotle. `references/background.md` has the sources.
- Do not write the "and then what" chain. `second_order_thinking` owns it. No next-event line per node (`skills/phase_2/CRITERIA.md`, check `second_order`).
- Do not fill a part from memory. No opened source and no calculation: grade 2, "not verified".
- Do not edit another skill, rule or script. Write only under `Artifacts/artifacts/<group>/<slug>/`.

## Files in this folder

- `assets/fp_worksheet.md`: the template. Copy it for every run.
- `references/questioning.md`: read before the first run of step 3.
- `references/five_whys.md`: read before the first run of step 4, when a chain stops too early, and when a problem seems to have more than one cause.
- `references/rebuild_example.md`: read before the first rebuild, or before a figure goes on a page.
- `references/background.md`: read when you explain first principles, give an example of a kind of part, weigh analogy against parts, write a gate row, or meet the Aristotle question.
- `references/sources.md`: read when you cite a claim and need its source, URL, type or grade.
- `evals/evals.json`: four test prompts with assertions. An assertion marked (no skill words) can be passed by a run that never saw the skill.

## model

model: inherit. no pinned model id.
effort: high. the failure is a routine node run in full, a convention filed as a law, a chain that stops at the first why, or a decomposition that goes below the useful level.
