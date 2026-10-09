# Weakness Audit Framework

The adversarial, **evaluator-agnostic** audit of the thesis and slides. This stage runs **before** any answer is drafted and produces a read-only **Weakness Ledger** that all later stages must respect.

> Why this exists: the old skill let one pass find weaknesses *and* write reassuring answers. The same voice doing both systematically under-powers the attack — the weaknesses a real committee exploits get smoothed over because the model "already has an answer." This framework forces the attack to be committed first, in isolation, with no answer in mind.

---

## IRON RULES (do not violate, even late in a long session)

- **IRON RULE W1 — Pre-commitment.** Produce the full Weakness Ledger *before* drafting any question answer. Do not soften, merge, or delete a ledger entry once committed. Later stages may only *reference* ledger IDs, never edit them. New evidence enters only through the append-only **Amendment protocol** below — and only the auditor voice rules on it.
- **IRON RULE W2 — Evaluator-blind.** Audit the thesis on its own terms. Do NOT look at the committee list during this stage. A weakness is a weakness regardless of who is on the panel.
- **IRON RULE W3 — Attack only, no rescue.** This stage finds problems. It must NOT propose how to defend them, reword claims to sound safer, or reassure. (Defense happens later, in answer-coaching-framework.md.)
- **IRON RULE W4 — No invented flaws (anti-leakage).** Every weakness must cite a specific location (section, figure, table, slide) **and quote the attacked claim verbatim (≤30 chars) in the `verbatim` field**. If you cannot produce the quote, the entry is not committable — re-check the materials or mark `[MATERIAL GAP]`, never assert a fabricated defect.
- **IRON RULE W5 — Lead with the single most dangerous flaw.** The ledger is ordered by severity. The first entry must be the one issue most likely to sink the defense.

---

## Output: the Weakness Ledger

A table the rest of the pipeline reads. One row per weakness.

| Field | Meaning |
|---|---|
| `id` | `W1, W2, …` (stable; later stages cite these) |
| `claim_or_target` | The specific thesis claim / method / experiment / slide under attack |
| `location` | Section / figure / table / slide number |
| `verbatim` | ≤30-char exact quote of the attacked claim (anti-hallucination anchor; required — see W4) |
| `lens` | Which lens/dimension surfaced it (see below) |
| `severity` | `CRITICAL / MAJOR / MINOR` (criteria below) |
| `evidence_now` | What evidence the thesis currently offers for the claim |
| `why_attackable` | The gap, in one plain sentence — the thing a committee member would press |
| `default_stance` | Derived from severity (see answer-coaching-framework.md): CRITICAL→concede+redirect, MAJOR→qualify, MINOR→defend |

Append a one-line **calibration footer** after the ledger (see "Self-check" below).

---

## Part 0 — Reviewer-report seeding (run first when 盲审/评阅意见 exist)

Official reviewer reports are pre-validated attacks — the highest-signal input this stage can get:

1. Convert each substantive comment into a ledger row: `lens = REVIEWER`, evidence High, `location` = the report item; severity by the normal criteria below.
2. Cross-check the revision-response sheet (修改说明): a comment marked "revised" that the materials do **not** actually fix is **CRITICAL** (evidence–conclusion mismatch — the committee will check exactly this).
3. Reviewer rows keep a `[REVIEWER]` tag through question generation and get guaranteed Top-10 consideration (reviewers re-ask their own comments).

This does not violate W2: reports attack the *thesis*, not the panel. Stay blind to the committee list itself.

---

## Part A — The Three Lenses (scan every central claim)

First load the thesis's paradigm profile (`discipline-profiles.md`) so "evidence" and "rigor" mean the right thing for this field. Then run all three lenses on each core contribution, in order.

### Lens 1 — Internal validity: "Does the evidence support the claim?"
1. What exactly is the claim?
2. What evidence is offered? (*Evidence* = data/experiment, interview/field data, proof step, primary source/archive, case/statute, or the created artifact — per paradigm.)
3. Is there a clean chain evidence → claim (the *warrant*)? Where is the warrant unstated?
4. What alternative explanation / rival reading did the author not rule out?
5. **Linchpin test:** if you removed one piece of evidence (a result, a source, a case, a proof step), would the argument collapse? If yes → flag the single point of failure.

### Lens 2 — Scope & generalization: "Does the claim overreach what was examined?"
1. What is the intended scope of the claim (population, setting, period, corpus, jurisdiction)?
2. Does the evidence base actually cover that scope, or is it narrower?
3. Per paradigm: empirical-quant → representativeness/reproducibility; qualitative → transferability; interpretive/doctrinal → do the texts/cases support a claim this broad; formal → how general are the assumptions.
4. Would it hold in a different context (dataset, culture, period, corpus, jurisdiction)?
5. What boundary conditions are unstated? (Authors usually overstate generality.)

### Lens 3 — Contribution: "So what?"
1. What did the field know before this thesis?
2. What does it know after?
3. Is the delta meaningful (not merely statistically significant)?
4. Who benefits from knowing this?
5. Can you state the delta in **one sentence**? If not, the contribution is weak *or* poorly communicated — both are defense-relevant.

---

## Part B — Devil's Advocate, 8 attack dimensions

For each, construct the *strongest* version of the attack. Adapted from adversarial peer review; de-coupled from journal/publication concerns.

1. **Core-thesis challenge** — strongest counter-argument to the central claim. Is there a simpler (more parsimonious) explanation than the authors'?
2. **Cherry-picking** — are baselines/citations/results selected to favor the conclusion? What contradicting evidence is omitted?
3. **Confirmation bias** — were conclusions effectively decided before the analysis? Do method choices pre-load the expected result?
4. **Logic-chain validation** — hidden assumptions, logical leaps, correlation sold as causation.
5. **Overgeneralization** — does the stated conclusion exceed what the data supports? Narrow result → universal claim?
6. **Alternative paths** — why method A over B/C/D? Is there a more mature / cheaper / more standard approach the thesis ignored?
7. **Reproducibility & feasibility** — can it be re-run? Cost / compute / real-time / hardware feasibility avoided? (the engineering "so what")
8. **"So what?" test** — is the incremental contribution enough to defend as a thesis?

---

## Severity classification

| Severity | Definition | Consequence for defense |
|---|---|---|
| **CRITICAL** | A core assumption is unsubstantiated/false, the conclusion doesn't follow from the evidence, the data contradicts the stated conclusion, OR a rival explanation fits the data better | A question here can sink the defense. Top priority, most rehearsal. Stance is usually **concede + redirect**, never hard-defend. |
| **MAJOR** | Seriously weakens credibility but can be handled with a qualified, bounded answer | Required prep. Stance: **qualify**. |
| **MINOR** | Does not touch the core argument; worth a clean answer | Light prep. Stance: **defend** plainly. |

**A weakness is CRITICAL only if it meets at least one hard criterion:**
- **Foundation collapse** — a core premise is demonstrably false or unsupported.
- **Logic-chain break** — the main conclusion does not follow even if the evidence is valid (e.g., correlation → causation without ruling out confounds).
- **Evidence–conclusion mismatch** — the thesis's own evidence points the other way: a table/figure shows n.s. results, an archival source says the opposite, a cited case actually holds against the claim, or a quoted passage undercuts the reading.
- **Stronger counter-narrative** — an alternative explanation is more parsimonious *and* fits the presented data better (e.g., the observed gain is more plausibly a dataset/selection artifact than the proposed mechanism).

Do **not** inflate to CRITICAL: a missing non-central reference, imprecise wording in a side claim, formatting, or an already-acknowledged minor limitation.

---

## Worked example signals (load examples for the detected paradigm)

Pull the paradigm's "CRITICAL patterns" from `discipline-profiles.md` and use them as a sanity check that the audit is biting. The patterns differ by field — for example:
- **Empirical-quant (sciences/engineering):** simulation/lab-only with no field data; idealized assumptions; a narrow regime generalized to "effective in general"; missing baseline/ablation; no feasibility/cost analysis for a "deployable" method.
- **Textual-interpretive (history/literature):** a reading the sources can't bear; counter-evidence in the archive ignored; anachronism/decontextualization; not engaging the major existing interpretations; description posing as argument.
- **Doctrinal-normative (law/ethics):** misreads a controlling authority; ignores the strongest counterargument; an unsupported normative premise; over-claims beyond the jurisdiction examined.

(These are *prompts*, not a fixed list. Always cite the actual thesis, and use the detected paradigm's patterns.)

---

## Amendment protocol (append-only — the only way the ledger ever changes)

W1/W3 protect against self-softening, not against new facts. When the student supplies evidence from **outside** the audited materials ("the field data is in my published paper"), do not edit the ledger and do not let the answer voice handle it:

1. Only the **auditor voice** re-examines the entry, in a separate pass — never the answer voice, never mid-answer.
2. Record the ruling as an appended line `W{n}-A{k}: {new evidence, source, ruling}` with ruling ∈ **upheld / downgraded** (e.g., CRITICAL→MAJOR) **/ closed-by-revision**. The original row is never edited or deleted; the audit trail stays visible.
3. Answers and the readiness score read severity from the **latest ruling**.
4. Anti-abuse: an amendment requires *citable* new evidence (a paper, dataset, document). Reassurance ("I'm confident it holds") is not evidence — ruling stays **upheld**.

---

## Self-check (calibration footer — run after drafting the ledger)

Answer briefly, in one line each; adjust the ledger if any answer is "no":
1. Did I lead with the single most dangerous flaw (W1)?
2. Is every CRITICAL backed by one of the four hard criteria (not just "I'd prefer more data")?
3. Am I being at least as hard as a real external examiner would be (not as gentle as on my own work)?
4. Did I cite a concrete location **and a verbatim quote** for every entry, and mark true gaps as `[MATERIAL GAP]` rather than inventing flaws?
5. Did I resist writing any defense/answer in this stage (W3)?

> Hand-off: the committed Weakness Ledger feeds `question-generation-rules.md` (turn weaknesses into questions) and `readiness-rubric.md` (score exposure). It is read-only from here on.
