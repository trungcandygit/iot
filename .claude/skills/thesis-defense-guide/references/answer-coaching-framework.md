# Answer Coaching Framework

The **defense voice** — a separate pass from the weakness audit. Turns each generated question into a bounded, speakable answer the student can actually say under pressure. This is where defense happens; the audit (weakness-audit-framework.md) was attack-only.

> Generator/evaluator separation: answers are written here, *after* the Weakness Ledger is committed. An answer may not pretend a logged weakness doesn't exist. If an answer needs the weakness to be smaller than the ledger says, the ledger wins.

---

## IRON RULES (anti-overclaiming — migrated and hardened)

- **IRON RULE A1 — No overclaim beyond thesis evidence.** Never present:
  - simulation as real-world deployment evidence;
  - correlation / trend / single case as causality;
  - a small or local result as universal effectiveness;
  - planned/future work as an already-completed contribution.
- **IRON RULE A2 — No hiding.** Do not bury missing baselines, missing ablations, limited datasets, unverified assumptions, or negative results. A controlled concession beats a forced justification.
- **IRON RULE A3 — Honor the ledger.** An answer must not claim a CRITICAL/MAJOR weakness is resolved when it isn't. Severity is read from the entry's latest `W#-A#` amendment ruling, if any — an answer may rely on a downgrade only after the auditor voice ruled it (never argue the ledger down from inside an answer). Acknowledge → bound → defend what the evidence *does* support → name the next step.
- **IRON RULE A4 — Bounded verbs.** Prefer "indicates / supports / under this setting / within this dataset / preliminary evidence". Avoid "proves / guarantees / always / fully solves / optimal / real-world validated" unless the thesis truly earns it.
- **IRON RULE A5 — Speakable.** Each answer is something the student can say aloud in the stated time. No thesis prose, no paragraph the size of an abstract.
- **IRON RULE A6 — Integrity questions get honest answers.** For AI-use, originality/查重, and authorship questions, coach a truthful, policy-compliant answer. Never coach concealment or minimization — a defensible process stated plainly beats a discovered evasion.

---

## The 4-move answer skeleton

Every substantive answer moves through, in order:

1. **Directly answer** the question (don't dodge; give the chair a clean first sentence).
2. **State the boundary** — the scope/assumption under which the claim holds.
3. **Defend what's still valid** — why, within that boundary, the work stands.
4. **Name the next step** — the validation/extension you'd do next (only *after* answering, never as a substitute for answering).

Skeleton:
> "Yes, within [boundary]. In this thesis I [assume/limit] … because the goal was first to [verify X]. Under that scope, the result shows [bounded claim]. For a real system, the next thing I'd verify is [step]."

---

## Stance by severity (derived, not chosen ad hoc)

Read the weakness `severity` from the ledger; it sets the posture:

| Severity | Stance | Behavior |
|---|---|---|
| **CRITICAL** | **Concede + redirect** | Acknowledge the limit plainly, draw the tight boundary the claim survives in, redirect to scope/next-step. **Do not hard-defend** — that's how you get cornered. |
| **MAJOR** | **Qualify** | Defend a *narrowed* version of the claim; admit what's not covered. |
| **MINOR** | **Defend** | Answer cleanly and move on; don't over-apologize. |

Concession discipline: a concession is a *bounded* admission ("this holds only in simulation"), immediately paired with what remains valid and the next step. It is never a collapse ("yes, my work is invalid").

---

## Layered answers (10 / 30 / 60 seconds)

Provide layers so the student can match the chair's tempo. Required for every Top-10 question; optional for MINOR.

- **10秒 / 10-second** — one controlled sentence. The safe core.
- **30秒 / 30-second** — the default spoken answer (the one to rehearse first). Full 4-move, compressed.
- **60秒 / 60-second** — for complex/high-risk items; adds the boundary detail and the next step.
- **若被追问 / If pressed** — one fallback line that preserves the boundary when interrupted.

Add **▶ 加分点 / Bonus point** only when a single extra sentence genuinely raises the answer (a smart limitation, a neat comparison). Published/accepted papers from the thesis are the best bonus material — peer review is a credibility anchor ("this model passed review at [venue]"). Never pad.

---

## Personalized red-line phrases (thesis-specific, not generic)

For this thesis, list the exact sentences the student must NOT say, with safer replacements. Derive them from the Weakness Ledger, not from a stock list.

| Do not say | Safer wording | Why |
|---|---|---|
| "This is validated in real scenarios." | "This is validated in simulation; field validation is the next step." | only simulation exists |
| "The method is optimal." | "The method gives the best result among the settings I tested." | only a heuristic / local best |
| "Future work will solve this." | "[answer the actual limitation first], and a concrete next step is …" | future work ≠ an answer |
| "This limitation doesn't affect the conclusion." | "This limitation bounds the conclusion to [scope]; within it the result holds." | honesty buys credibility |

---

## Claim calibration table (keep from the original skill)

For every risky claim, rewrite into defensible oral wording before the defense:

| Thesis wording / implied claim | Evidence level (strong/moderate/weak/missing) | Overclaim risk (low/med/high) | Safer defense wording |
|---|---|---|---|

Preserve the student's real contribution — narrow it, don't erase it.

---

## Self-check (run after drafting answers)

1. Does every CRITICAL answer **concede + redirect** rather than hard-defend?
2. Does any answer contradict the Weakness Ledger (claim a flaw is gone)? If yes, fix the answer, not the ledger.
3. Could the student actually say the 30-second version aloud without notes?
4. Did I avoid every banned verb in A4 unless the thesis truly earns it?
5. For the scariest question, is there an "if pressed" line so the student isn't left silent?

> Hand-off: answered questions feed the per-evaluator battle cards and the day-of one-pager; the scariest chains feed `mock-defense-protocol.md` (P1) for live pressure-testing.
