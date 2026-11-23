<!--
Template for second_order_thinking. Copy it to Artifacts/artifacts/<group>/<slug>/phase2_so.md. Fill the copy. Delete these comments. Do not edit the template. SKILL.md points here for the column names, the header fields and the cell formats.
- Pair sentence: use it as written for a page run. A chat-only decision, or a group or slug that is missing, uses the form in SKILL.md, section Output.
- node id: bare, as in phase2_fp.md, for example d1a. A decision typed in chat: chat1. Braces ({d1a}) are the page-tag form only.
- decision or mechanism: start a default with "default:".
- first order: from what phase2_fp.md says is true, with its base grade. A chat-only decision: graded here. End the cell with its grade: (g5).
- second order, third order: end each filled cell with its grade: (g4). A guess ends (g2, not verified).
- horizon: the first horizon where the second order shows: 10 min, 10 mo or 10 yr.
- who responds: use only the listed parties. Business decision: employees, competitors, suppliers, regulators. System: users, operators, attackers, vendors. Add a party only when the decision names it, and cite a source for its effect. Write "party: effect" for each listed party that responds. Leave out a party that does not respond. Write the single word none only when no listed party responds.
- lesson: "yes: <what the reader gets wrong if the section ends at the first effect>" or "no: <reader | kind | source | cap | base>, <why>". Name a Merton factor in a yes reason when it explains the miss.
- grade: 1 to 5 for the second-order claim, the one a next-event sentence would carry. A "no: base" row shows the grade of its base.
- grade tally: count the rows of the Chain table by their grade cell. One count for each row.
- Chat-only decision: one decision is one row, chat1. Put side effects inside the order cells. Add chat2 only when he asks for a second decision. The No chain list says "none". Kept rows says "none, no page". The cap field says "n/a, the topic is a decision".
- A number, a percentage or a probability for an effect needs a source id. Without one, leave it out.
- Every node id of the map appears once: in the Chain table or in the No chain list.
-->

# Consequence chain: <slug>

Pair: first_principles wrote phase2_fp.md (what is true). second_order_thinking wrote phase2_so.md (what follows).

| field | value |
|---|---|
| group / slug | <group> / <slug> |
| date | <YYYY-MM-DD> |
| review on | <YYYY-MM-DD> |
| reviewer | <who compares the kept rows with what happened, and how he keeps the date. Nothing in this repo opens this file on the review date> |
| domain sections on the map | <n> |
| cap | <n divided by 3, rounded down, at least 1> |
| sections with a next-event sentence | <k> |
| exception | none, or: the topic is a decision, or: control with a known side effect: <side effect>, <source id>, g<n> |
| grade tally | g5 = <_>, g4 = <_>, g3 = <_>, g2 = <_>, g1 = <_> |

## Chain

| node id | decision or mechanism | first order | second order | third order | horizon | who responds | lesson (yes or no, with the reason) | grade |
|---|---|---|---|---|---|---|---|---|
| d1a | <decision, mechanism, or default: ...> | <effect (g5)> | <effect (g4)> | <effect (g2, not verified), or empty> | <10 min / 10 mo / 10 yr> | <party: effect; or none> | <yes: ... / no: ...> | <1-5> |

## No chain

<ids with no later effect worth a chain, for example d1, d1b. Each is `no: reader` unless noted.>

## Kept rows

<One row for each kept yes row. At most one per section. The number of rows is at most the cap, unless the exception names a section.>

| node id | section |
|---|---|
| d1a | d1 |

## Stops

| node id | stopped after | because |
|---|---|---|
| d1a | order <n> | <the next order would not change the decision / it is below the noise / three orders are done> |

## Review log

<Nothing in this repo opens this file on the review date. The reviewer keeps the date. On that date, compare each kept row with what happened. One row each. Change the grade if the check changes it.>

| date | node id | what happened | hit, miss or unseen | new grade |
|---|---|---|---|---|
| | | | | |
