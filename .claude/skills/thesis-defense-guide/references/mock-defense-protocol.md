# Mock-Defense Protocol

Turns Stage 6 from a scripted Q&A into a **live, interactive drill** where a simulated examiner pressure-tests the student and **does not soften when the answer is weak**. This is the single most valuable rehearsal mechanism — it makes the student fail *here*, in practice, instead of at the real defense.

> The defining behavior: a real committee member does not accept a so-so answer and move on. They restate, sharpen, or escalate. The old static manual cannot do this. This protocol makes the examiner hold the line.

---

## IRON RULES

- **IRON RULE M1 — No softening under pushback.** A weakness rated CRITICAL in the Weakness Ledger stays CRITICAL during the drill unless the student's answer genuinely dismantles it (rubric ≥4). Persistence is not a rebuttal.
- **IRON RULE M2 — Score before reacting.** Every student answer is silently scored 1–5 (rubric below) before the examiner responds. The score, not politeness, decides escalate vs. advance.
- **IRON RULE M3 — Stay in persona and in scope.** The examiner attacks only from the assigned persona's angle and only weaknesses that actually exist in the materials (anti-leakage). No inventing flaws to seem tough.
- **IRON RULE M4 — One examiner attacks, the coach debriefs.** During an exchange the examiner does not teach. Coaching/model-answers come only at debrief, so the student experiences real pressure first.
- **IRON RULE M5 — Honest log.** Record the student's actual performance, including fumbles. The drill exists to find weak answers, not to make the student feel ready.

---

## Two modes

- **Exam mode (default).** Hard, realistic. Examiner escalates, interrupts, and only concedes on a genuinely strong answer. Use close to the defense.
- **Coach mode (Socratic).** Gentler: after a weak answer the examiner gives a hint or a leading question instead of escalating, and turns are 200–400 words. Use early, to build the answers. Switch with "coach me" / "exam me".

---

## Session setup

1. Pull the **Top-10 dangerous questions** (from `question-generation-rules.md`) and the **Weakness Ledger**.
2. Pick scope: a single question, one evaluator's battle card, or a full random panel round.
3. Assign the examiner **persona** (methodology / domain / application / adversarial / ESM-or-field-specific), matched to the question's evaluator tag.
4. Set rounds (default: escalate up to 4 rungs per question) and mode (exam/coach).
5. State the rules to the student once, then begin. The student answers out loud / in text as they would at the defense.

---

## The rebuttal-scoring rubric (score every student answer 1–5)

| Score | Meaning | Examiner's next move |
|---|---|---|
| **5** | Directly dismantles the attack with correct evidence/logic, within the thesis's real scope | Concede the point; advance to next question |
| **4** | Substantially answers; bounds the claim correctly; minor gap | Acknowledge; one light follow-up, then advance |
| **3** | Partial — addresses the surface but the core gap remains | **Hold the finding**; restate the core and press again |
| **2** | Tangential, changes the subject, or over-claims | Name the deflection; re-ask the original question harder |
| **1** | Assertion without evidence, or claims a known limitation is gone | **Escalate**; add a second attack dimension |

Mark each answer's score in the log. The student's average across the Top-10 feeds **D6 (Q&A robustness)** in `readiness-rubric.md`.

---

## Escalation ladder (per question)

Walk down the rungs until the student stabilizes at a defensible boundary (or runs out):

1. **Concept check** — definitions, why this metric/assumption.
2. **Assumption challenge** — "on what basis do you assume [the key premise — ideal conditions, a representative sample, an authoritative source, a stated framework]?"
3. **Evidence pressure** — "you only have simulation / no baseline — how do you know it holds?"
4. **Limitation pressure** — push the admitted limit to its consequence for the conclusion.
5. **Cornered turn** — the worst follow-up ("so your headline claim only holds in the ideal / best case?"). The student must land a boundary-preserving survival line, not collapse.

**Stop rule:** stop escalating a question once the student gives a score-4/5 answer **or** stabilizes for two consecutive turns on the "concede + bounded scope" line. Note where they stabilized — that rung is their current floor.

---

## Anti-sycophancy discipline (critical — this is what makes it real)

- **No consecutive concessions.** If the examiner conceded the previous question, the bar for the next concession rises to 5/5. A score-4 answer after a prior concession → hold, don't concede.
- **Persistence ≠ rebuttal.** The student repeating the same answer louder/three times does not raise its score.
- **Track concession rate.** If the examiner has conceded >40% of findings in a session, flag it: "I'm conceding a lot — either the answers are genuinely strong, or I'm going easy. A human should re-test the conceded questions." (Mirrors the real risk that the model role-playing the examiner is too agreeable.)
- **Deflection naming.** On a score-2 answer, explicitly say what was dodged: "You answered [X]; my question was [Y]."

---

## Drill log (capture every question)

```
[MOCK] Q{n} ({weakness W#}, persona) | rungs reached: {1-5} | answer scores: {e.g. 3,2,4} | floor: {the rung where they stabilized} | verdict: SOLID / SHAKY / FUMBLED | note: {what failed}
```

- **FUMBLED / SHAKY** questions are pushed to the top of the next session and re-ranked up in the Top-10 (close the loop).
- Recurrent failure on the same weakness → flag it for the day-of one-pager as a "must-drill" item.

---

## Session debrief (coach voice, only here)

After the round, the coach (not the examiner) reports:
1. **Readiness delta** on D6 and overall (vs. last session).
2. **The 2–3 questions that broke down**, with the model answer (4-move, from `answer-coaching-framework.md`) and the exact rung where the student lost the boundary.
3. **The one habit to fix** (e.g., "you kept defending the 98% as real — your floor must be 'simulation feasibility', reached faster").
4. Updated **Top-10** ordering and any new red-line phrase the student said by accident.

---

## Quality bar

- The examiner felt like the *assigned* committee member, not a generic critic.
- At least one question was escalated to the cornered turn.
- No CRITICAL weakness was silently let go because the student pushed back.
- The log names where each weak answer actually failed, and the debrief gives a concrete fix.
- The student leaves knowing their **floor** for each dangerous question — the boundary they can always retreat to.

> Hand-off: the drill log updates `readiness-rubric.md` (D6) and re-ranks the Top-10; fumbled questions headline the next drill and the day-of one-pager's "must-drill" list.
