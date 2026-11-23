# Cases

Read when you need an example of a kept row, a dropped row, or one of the two shapes. A case with no source is an illustration: g2, not verified. No illustration goes on a page as it stands. The illustrations use no vendor name, no limit and no number on purpose. Tags are in `SKILL.md`. Source numbers are in `references/sources.md`.

## The gate on five rows

Each row applies the three tests in `SKILL.md` to one node.

| node | test 1 reader | test 2 kind | test 3 source | lesson cell |
|---|---|---|---|---|
| what a cipher suite name means (a definition) | no: the first effect is the whole point | not run | not run | `no: reader` |
| a second rule for the same bug class | yes | no: more filtering of the same kind | not run | `no: kind` |
| slow password hashing (shape A below) | yes | yes | no: no source opened | `no: source`, g2 |
| a human approves every agent call (shape B below) | yes | yes | no: no source opened | `no: source`, g2 |
| the Aswan High Dam (sourced case below) | yes | yes | yes, if worded as what Hardin says | `yes`, one sentence |

Two rows pass tests 1 and 2 and still stay off the page. That is the point of test 3. A lesson with no opened source is a guess, even when it sounds true. Open a source first.

## The two shapes

[1] g5 (says), g3 (true): many extraordinary results cost something at first order and pay off at second order, and fewer rivals chase them because first-order thinkers stop early. It gives no example. The opposite shape is harm after a good first result. [7] g5: Merton says unforeseen results are not always undesirable. [6] g5 (says): it warns of harm that exceeds the gain.

| shape | first order | second order | illustration (this skill's own, g2, not verified) |
|---|---|---|---|
| A. cost now, gain later | negative | positive | slow, salted password hashing. Every login costs more. A stolen hash file costs the attacker more per guess |
| B. gain now, cost later | positive | negative | a human approves every agent tool call. No risky call runs unseen. Later the reviewer approves without reading |

Both illustrations are this skill's own. No source was opened for them. They are not evidence. As written, both fail gate test 3, so neither goes on a page. At the third order, look for a reversal: the gain of shape A and the cost of shape B can both undo themselves.

## A sourced case: the Aswan High Dam (shape B)

[4] g5: Hardin says it. His figures were not checked. Word the page sentence as what he says. Do not write that the dam caused them.

| order | what Hardin lists |
|---|---|
| first (positive) | more water and power, the aim |
| later (negative) | far fewer sardines, an eroding delta, salted soil, more schistosomiasis |

- Test 1: stopping at the aim hides who pays. Yes.
- Test 2: the sign flips and other people are hit. Yes.
- Test 3: g5 for "Hardin lists these". Not g5 for "the dam caused these". Yes, if the sentence says what he says.
- A Merton factor that may fit: immediate interest, the actor intent on the foreseen near-term result [7]. `reading g2`.
- The case is policy, not security. It stays here as the one case with a primary source.

## Shape A: cost now, gain later (security, illustration, g2, not verified)

Decision: hash stored passwords with a slow, salted function.

| order | effect | horizon |
|---|---|---|
| first (negative) | Every login costs more time and compute. | 10 min |
| second (positive) | A stolen hash file costs the attacker more work for each guess. | 10 mo |
| third (check for reversal) | An attacker can send many login requests to use up the server's compute. (guess, g2, not verified) | 10 yr |

- Who responds: users (slower login), operators (capacity and tuning), attackers (guess the likely passwords first), vendors (library defaults).
- Condition. The cost is tuned so login stays quick. The password is not among the first guesses. A slow function raises the cost of each guess. It does not rescue a password that falls in the first few.
- When it does not apply. The secret has so much randomness that guessing is out of reach. There the cost buys nothing.
- Stop. After order 3. A fourth order cannot be sized (stop test 2).
- Row: `no: source`, g2. To put it on a page, open an official password storage guide first.

## Shape B: gain now, cost later (agent systems, illustration, g2, not verified)

Decision: ask a human to approve every tool call the agent makes.

| order | effect | horizon |
|---|---|---|
| first (positive) | No risky call runs unseen. | 10 min |
| second (negative) | The reviewer meets the same prompt many times and starts to approve without reading. The gate stops filtering. | 10 mo |
| third | The team adds an allow-list to cut the noise. The list now decides what nobody reviews. (guess, g2, not verified) | 10 yr |

- Who responds: users (slower runs), operators (the approvers), attackers (shape a request to look routine), vendors (auto-approve options).
- Condition for the harm. Many low-risk prompts, so the reviewer learns to skip.
- When it does not apply. Prompts only for rare, high-risk calls, so each one gets read.
- Stop. After order 3. A fourth order would not change the decision (stop test 1).
- Row: `no: source`, g2. This is a control with a possible side effect. The exception needs a known side effect: documented in an opened source at g3 or higher. This one has none, so it gets no exception.

## What to copy from these cases

- Write the condition and the case where it does not apply, as the page order asks. A chain with neither is a story.
- Name each listed party that responds. Leave out a party that does not. Write `none` only when no listed party responds.
- Check the third order for a reversal. The gain of shape A and the cost of shape B can both undo themselves.
- Keep the grade on the row that a next-event sentence would carry. An illustration is g2 until a source is opened.
