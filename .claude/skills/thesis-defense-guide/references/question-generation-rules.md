# Question Generation Rules

Turns the committed **Weakness Ledger** into the questions a committee will actually ask, ranks them by danger, and only *then* re-weights by evaluator. This is the "压题 / question-prediction" engine.

> Core principle: **questions are derived from weaknesses first, evaluators second.** Even when you cannot research a professor, you still know a methodology-minded examiner will hit a "simulation-only" weakness. Weakness-derived questions are the reliable backbone; evaluator research only re-weights and personalizes.

---

## IRON RULES

- **IRON RULE Q1 — Weakness-first.** Every generated question must trace to a Weakness Ledger `id` (or to the universal backbone / Concept Drill below). No free-floating "generic" questions presented as predictions.
- **IRON RULE Q2 — Never drop a CRITICAL.** A CRITICAL weakness always becomes at least one question, even if no committee member obviously "owns" it. The same guarantee applies to `[REVIEWER]`-seeded weaknesses — official reviewers re-ask their own comments.
- **IRON RULE Q3 — Backbone is evaluator-independent.** Produce the full weakness-derived question set assuming an unknown panel. Evaluator info adjusts ordering and adds a thin personalized layer; it never gates the backbone.
- **IRON RULE Q4 — No fabricated personalization.** "Prof. X will ask about Y" requires an evidence-graded basis from evaluator research. Otherwise tag the question by evaluator *type*, not a named person.

---

## Step 1 — Weakness → question

For each ledger entry, write the question an examiner derives from `why_attackable`. Phrase it the way a committee member speaks, not as thesis prose.

- Keep the question pointed at the *gap*, not the strength.
- One weakness can spawn 1–3 questions across escalation levels (Step 2).
- Carry the weakness `severity` onto the question (drives ranking in Step 4).

## Step 2 — The 3-level escalation ladder

Every dangerous weakness gets a chain that gets harder. This replaces ad-hoc "chain follow-ups" with chains that have a *source*.

1. **Concept check** — "How do you define X? Why this metric/assumption?" (warm-up; confirms understanding)
2. **Assumption challenge** — "On what basis do you assume [the key premise]? What if it doesn't hold?"
3. **Evidence / limitation pressure** — "You only have simulation. How do you know it holds in a real system? Your Table N shows [tension] — explain."

For CRITICAL weaknesses, also draft a **4th "cornered" turn** (the worst follow-up) so the student rehearses the bottom of the chain, not just the top.

## Step 3 — Tag by evaluator *type* (paradigm-aware)

Load the **evaluator archetypes for the detected paradigm** from `discipline-profiles.md` and tag each question with the archetype most likely to raise it. Archetypes are stable even when names aren't. As a cross-paradigm default, most panels contain four roles:

| Generic role | Cares most about | In a humanities / law panel this is… |
|---|---|---|
| **Rigor examiner** | soundness by the field's standard (stats, proofs, source criticism, doctrine) | the source/archive or doctrinal specialist |
| **Domain / literature examiner** | prior work, novelty, positioning in the field | the historiography / scholarship examiner |
| **Significance / "so what" examiner** | contribution, originality, why it matters | the originality challenger |
| **Adversarial / logic examiner** | internal consistency, overclaiming, counterarguments | the strongest-counterargument challenger |

For empirical-quant work the rigor examiner splits into methodology/stats + application/feasibility; for interpretive/normative work it splits into source-criticism + theory/framework. Use the paradigm profile's specific archetypes.

When real evaluator research exists (evidence-graded High/Med/Low), bind specific people to archetypes and **re-weight** their questions up. Low-confidence guesses stay tagged by *archetype*, not asserted as a person's certain question.

## Step 4 — Rank danger → Top-10

Score each question for the triage list:

`danger = severity_weight + evaluator_likelihood + answer_fragility + exposure_surface + reviewer_flag`

- `severity_weight`: CRITICAL=3, MAJOR=2, MINOR=1.
- `evaluator_likelihood`: +1 if a High/Med-confidence evaluator maps to it; backbone questions still count via their type's near-certainty (e.g., an application examiner on a deploy-feasibility gap).
- `answer_fragility`: +1 if the student currently has no clean bounded answer (often true for CRITICAL).
- `exposure_surface`: +1 if the attacked claim sits in the **title / abstract / conclusion / a headline slide** — committees fixate on what is most visible.
- `reviewer_flag`: +1 if the weakness came from an official reviewer report (`[REVIEWER]`) — near-certain to be re-asked.

Output the **Top-10 Most Dangerous Questions** (the spine of the day-of one-pager). These get the deepest answers and the most mock-defense reps.

---

## Stage awareness (carry over the original skill's strength)

Re-skew the question emphasis to the defense stage. If the stage is unknown, default to final/viva and state the assumption.

| Stage | Question emphasis |
|---|---|
| **Proposal** | research value, gap, feasibility, route choice, expected validation, scope control — *do not ask as if results exist* |
| **Midterm** | progress vs plan, completed evidence, unfinished work, schedule risk, method changes, can it be finished |
| **Pre-defense** | structure, missing comparisons/evidence, contribution wording, completeness of the case, revision priorities |
| **Final / viva** | evidence credibility, contribution boundary, rigor, limitations, reproducibility, generalization |
| **Written review** | source traceability, argument structure, compliance, objections needing written replies |

The same weakness yields a stage-shaped question: a proposal examiner asks "why is this route feasible?"; a final-defense examiner asks "what evidence proves this under your stated assumptions?"

---

## Universal backbone (research-independent safety net)

Even with zero evaluator info and a thin thesis, always include these high-probability questions, mapped to whichever weaknesses they touch:
- "In one sentence, what is your contribution / original argument?" (Lens 3)
- "What is your single biggest limitation, or the weakest part of your case, and how does it affect your conclusion?"
- "Why this method / source base / framework instead of the obvious alternative?" (dim 6)
- "What would you do differently / next if you had more time?" (redirect target)
- "Which of your claims is most contestable, and how do you defend it?"

**Academic-norms set (near-universal since ~2025; coach honest, policy-compliant answers — never concealment):**
- "Did you use AI tools in producing this thesis — where, and how is that consistent with the school's policy?"
- "What is the relationship between your published papers and this thesis?" (大小论文关系 / overlap / authorship)
- Originality / 查重 / citation-practice questions, if the school's process flags them.

---

## Concept Drill (必然题层 — fundamentals derived from the thesis itself)

Dangerous questions are weakness-derived, but real panels also test **fundamentals**: they pick core terms off the title/abstract/methods and ask "define it / why this one". Fumbling a definition hurts more than conceding a limitation.

1. Extract **15–20 core terms / quantities / methods** from the title, abstract, keywords, and chapter heads (the bound, the estimator, the named framework, the doctrine, the corpus — per paradigm).
2. For each: a 1–2 sentence **spoken** definition + one sentence of "why this (over the obvious alternative)".
3. By design this layer is exempt from Q1's trace rule (it is not a weakness prediction — it is insurance). Drill items that overlap a ledger weakness inherit its `W#` tag.
4. Ships as the **appendix of the day-of one-pager**; it is generated from *this thesis's own vocabulary*, never from a static per-major question bank.

---

## Output shape (per question)

Use the labels the docx converter highlights (keep the Chinese labels for Chinese manuals):

```
### Q{n}: {question}   [{severity}] [{evaluator type / named evaluator}] [→ W{ids}]
▶ 问题意图 / Question intent
▶ 10秒回答 / 30秒回答 / 60秒回答   (layered; see answer-coaching-framework.md)
▶ 加分点 / Bonus point   (optional)
▶ 若被追问 / If pressed   (the next rung of the ladder)
```

> Hand-off: questions + severity + evaluator tags go to `answer-coaching-framework.md` (draft bounded answers) and the Top-10 goes to the day-of one-pager and `mock-defense-protocol.md` (P1).
