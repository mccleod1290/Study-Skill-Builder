# Five whys, as a stop rule for parts

Read this before the first run of step 4 in `SKILL.md`, when a chain stops too early, and when a problem seems to have more than one cause. Source numbers and marks are in `references/sources.md` and in `SKILL.md`.

## What the sources say

- Toyota's 2006 article credits Taiichi Ohno with the rule: ask why five times about every problem. The aim is to study the problem on the spot, with facts, down to its root causes. A countermeasure then stops it from coming back [5 C28 C29 C31 g5]. Ohno valued data and gave facts the most weight [5 C32 g5].
- The FS page shows only a child's chain of three whys. It ends when the adult says the answer is unknown and offers to look it up [1 C13 g5]. It gives no five-step procedure and no origin for the name [1 L05 g5]. Cite Toyota for the method. Do not cite the FS page.
- Five is a rule of thumb. Toyota prints five as advice and sets the aim as the root causes [5 C36 g4]. Two other pages say the count does not matter, and that a chain can run to seven or eight levels [11 C37 g3; 8 C39 g3].

## Toyota's example

A welding robot stops in the middle of a job. Each question takes the last answer as its subject [5 C30 g5].

| why | answer |
|---|---|
| 1 | a circuit overloaded and blew a fuse |
| 2 | the bearings had too little lubricant and locked |
| 3 | the oil pump did not circulate enough oil |
| 4 | the pump intake was clogged with metal shavings |
| 5 | the pump had no filter |

Use one wording. LEI quotes a second wording from Ohno's 1988 book. It uses a machine and a worn pump shaft, and it ends at a missing strainer. The notes did not open the book. The two versions end at the same point and differ in the middle [11 C44 g3; 5 11 C45 g4].

Graban argues that the chain stops at containment. The next why, why was there no filter, leads to design, standard work or checks. Unpacked, the example has seven links [9 C55 g3]. So five is not a natural boundary.

## The procedure, cut down for a claim

Adapted from the procedure for a failure. The notes derive that procedure from five sources [5 14 8 11 C34 g4].

1. Write the claim as one plain statement.
2. Ask why it holds. Answer with a fact you saw, measured or read in an opened source.
3. Ask why about that answer, not about a new topic.
4. Repeat until a stop.
5. Write the stop and the reason: "stopped at <law, measurement or I do not know> because <reason>".

## The three stops

| stop | test | what you record |
|---|---|---|
| law | holds in this context whatever anyone believes (derived, g4) | a part of kind law, its evidence, its context |
| measurement | a fact you saw, measured or priced (house, g2) | a part with the measurement, graded by its source |
| "I do not know" | no fact is at hand (derived, g4) | an assumption part, grade 1, the words "open question", the test that would settle it |

The law stop and the "I do not know" stop are derived from the FS page, Urban's model, the notes' working stop rule and the grounding rule [1 C06 C13; 2 W2; 5 14 9 6 C43 g4]. The measurement stop is this skill's own (house, g2). Its premise is that Toyota gives facts the most weight [5 C32 g5].

An honest "I do not know" is a finding. The FS page's own chain ends there [1 C13 g5]. The grounding rule calls it a valid answer (`.rules/grounding-and-confidence.md`, section 1, item 5).

An authority's word is not a stop. Urban separates two kinds of stop. A stop on facts about reality or about you, with sound logic above it, means you reason in the lab. A stop on an authority's word means you reason on dogma [2 W2 g5]. Urban's own word for a stop is "floor". File the authority as a convention. Name the holder. Ask the holder's reason. Go on.

No opened source gives an objective test of a root cause. The stop is a judgement by the investigator or the team [5 11 7 14 6 C42 g4]. Where a chain stops is a choice: on a familiar event, on the first event someone can fix, where information runs out, or on what is politically acceptable. Allspaw relays this from Leveson's book, which the notes did not open [6 C52 g3]. So write the reason you stopped.

## Toyota's stop and this stop differ

Toyota stops when it has found the root causes. The purpose is to stop the problem returning [5 C40 g5]. A first-principles chain stops at a part that stays true in this context. Use Toyota's stop when the node is a failure to fix. Use the first-principles stop when the node is a claim to understand (house).

## A chain that ends at "I do not know"

Built from Urban's rocket passage and the FS page [2 R1 R4 g5; 1 C15 g5]. The figure is g3.

| why | answer | kind |
|---|---|---|
| 1 | Why will a rocket stay costly? Because it always was. | convention. Holder: the usual view in the field, as Musk tells it [2 R1 g5]. Not a stop |
| 2 | Why does it cost what it costs? Price the parts alone: about 2 percent of the usual figure. | measurement as said, g3 as fact [1 W1 g3; 2 R3 g3] |
| 3 | So where does the cost sit? In the arrangement of the atoms, not in the atoms [2 R1 g5]. | Musk's reading of the result. The share is a cost floor, not a forecast [2 R5 g4] |
| 4 | Why does the arranging cost that much? The notes hold no figure and no breakdown [2 R4 g5]. | stop: "I do not know". Assumption part, grade 1, open question. Test: ask people who know the field for the catch [2 R1 g5] |

## Limits, as argued by named sources (g3)

- One cause. A chain can lock you into one chain of causes and ignore the complexity of the event [6 C46]. A root cause is built, not found: the questioner picks where to start and where to stop [6 C47]. A problem can have more than one root cause, and two people can find different ones [7 C48]. Several causes may each need their own chain [8 C49]. Card, through a summary, warns that the method can flatten a complex problem [10 C50]. Card's full text was not read.
- Too early. The thing taken for the cause may be another symptom [7 C53]. The chain can stop at containment [9 C55].
- Blame. One page states a no-blame aim [8 C59]. Allspaw argues that the question form still pulls toward who, and proposes how instead [6 C58]. The two do not conflict: one gives the aim, the other the effect [8 6 C60].
- Fit. One page says the method suits simple or moderately difficult problems and may still give insight on complex ones [8 C62].

Guard: when a why has two true answers, run one chain for each. Record the stop reason. When the why drifts to a person, ask how.
