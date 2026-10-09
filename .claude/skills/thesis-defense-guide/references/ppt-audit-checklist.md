# Defense Slides (PPT) Audit Checklist

The defense slides are a **separate attack surface** from the thesis. Committees stop you *on a slide*, ask about *that figure*, and notice when slide 7 says something the conclusion contradicts. This audit runs as part of Stage 1 (weakness audit), feeds rows into the Weakness Ledger, and scores **D5 (Presentation/PPT)** in `readiness-rubric.md`.

> Why separate: a thesis can hedge in a paragraph; a slide states a bald claim with a number. "98%", "optimal", "secure" on a slide is a freeze-frame target — the examiner reads it and asks "prove this." The slides often overclaim more than the thesis because they compress.

---

## IRON RULES

- **IRON RULE P1 — Cite slide numbers.** Every PPT weakness names the slide. No "the slides generally…".
- **IRON RULE P2 — Spoken = written = thesis.** Flag any place where the slide claim, what the student plans to say, and the thesis evidence don't line up. Mismatch is the easiest place to get caught.
- **IRON RULE P3 — Slides feed the ledger.** A slide-level overclaim is a real weakness; add it to the Weakness Ledger with severity, don't keep it in a side list.
- **IRON RULE P4 — No silent fixing.** Flag and recommend; do not rewrite the student's slides for them unless asked.

---

## 1. Pacing & structure

- **Slide budget:** roughly 1–1.5 min/slide for the talk. Count slides vs. allotted talk time; flag if the deck can't finish (e.g., 26 slides in a 12-min talk = rushed → the student will skip the limitation slides exactly when they matter).
- **Contribution up front:** is there a slide that states the one-sentence contribution *and* its boundary, early? If the novelty only appears in the summary, the committee forms its own (worse) interpretation first.
- **Time-sink slides:** identify slides dense enough to eat 3+ minutes; they steal time from Q&A prep and from the results that need caveats.

## 2. Per-slide overclaim scan (the freeze-frame test)

For every slide, scan for a stated claim that exceeds the evidence. Typical triggers: a bare performance number, an absolute word, a security/again claim.

| On the slide | Why it's a freeze-frame target | Safer slide wording |
|---|---|---|
| A bare result number ("效果提升 98%") with no condition | Examiner: "under what conditions / sample / scope?" | put the condition *on the slide* ("…在[设定/样本/范围]下") |
| "物理层安全 / 安全性" | Invites the interceptor question | "未同步无法解调" — state the precise mechanism |
| "抗干扰能力" (generic) | "against what jammer? processing gain?" | "对所测 OFDM/LFM 干扰具一定容忍" |
| "optimal / 最优 / 完全" | A single counter-case sinks it | "在所测设定下最佳" |

**Each overclaiming slide becomes a Weakness Ledger row** and almost certainly a Top-10 question.

## 3. "Which slide will they stop you on?"

Rank the 2–3 slides most likely to trigger a dangerous question (map each to a Weakness Ledger ID). These are usually the headline results slides and any slide with a security/again/optimal claim. For each:
- name the question it invites,
- confirm the student has the bounded answer ready,
- decide whether a **backup slide** is needed (see §6).

## 4. Figures & readability

- Axis labels, units, legends present and legible from the back of a room (font ≥ ~18pt for body, ≥ ~24pt for the key result).
- Each results figure has a one-line takeaway the student can say; no "here is a busy plot, moving on".
- No screenshot-of-a-table dumps; no 6-line bullet paragraphs (the audit found this thesis's slides are text-dense in places).
- Color/contrast readable; key curve distinguishable.

## 5. Missing-limitations check

- Does **any** slide acknowledge a boundary, or is the deck all wins? A deck with zero limitations reads as naïve to a committee and removes the student's chance to frame the concession on their own terms.
- Recommend one honest "局限与展望 / Limitations & next steps" slide that pre-empts the Top-3 exposures (better the student raises them than the committee).

## 6. Backup slides (defense-specific, high value)

For each Top-3 exposure, recommend a **backup slide** held after the "thank you" slide, ready to pull up when pressed:
- the conditions/realism caveat + the next-step validation plan (for a headline-number question);
- the precise security threat model / "未同步不可解调" diagram (for the LPI question);
- the autocorrelation/PSL or ambiguity discussion (for the waveform question);
- a comparison table vs. prior work (for the novelty question).
Backup slides turn the scariest questions into "I'm glad you asked — slide B3."

## 7. Spoken-vs-written consistency

- Cross-check each results slide claim against the thesis number and against the student's intended verbal claim. Flag drift (e.g., slide says "secure", thesis says "physical-layer, sync-based").
- Flag any slide that says more than the thesis proves — the examiner has read the thesis.

---

## Output

1. **PPT weakness rows** appended to the Weakness Ledger (`slide #`, claim, severity, safer wording).
2. **Stop-risk ranking:** the 2–3 slides most likely to trigger danger, each tied to a Top-10 question.
3. **Recommended edits:** condition-on-the-number fixes, one limitations slide, and a backup-slide list for the Top-3 exposures.
4. **D5 score** input for `readiness-rubric.md`.

> Hand-off: PPT weaknesses merge into the Weakness Ledger (so they flow into questions and the mock defense); the backup-slide list goes onto the day-of one-pager.
