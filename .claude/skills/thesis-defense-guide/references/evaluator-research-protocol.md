# Evaluator Research Protocol

Disciplines Stage 2 (researching the committee). The goal is an **evidence-graded** profile of each evaluator that re-weights and personalizes the weakness-derived questions — **without inventing anything**. When research is thin, the protocol degrades gracefully to paradigm archetypes rather than fabricating specifics.

> Hard truth from real runs: most committee members have thin public footprints. The skill must be useful anyway. Evaluator research is a *re-weighting* layer on top of the weakness backbone — never the foundation. A profile you can't source is worse than no profile, because a stressed student over-indexes on a wrong guess.

---

## IRON RULES

- **IRON RULE E1 — No fabrication.** Never assert a person's papers, students, awards, or "the question they'll ask" without a citable source. If you can't source it, don't write it. Mark genuine gaps `[MATERIAL GAP]`.
- **IRON RULE E2 — Grade every claim.** Tag each profile statement High / Med / Low (defined below). The grade ships in the output, not just internally — the student must see how solid each inference is.
- **IRON RULE E3 — Thin research → archetype, not invention.** If a person is Low/▢ evidence, tag them by their paradigm **evaluator archetype** (from `discipline-profiles.md`) and stop. Do not manufacture a specific research focus.
- **IRON RULE E4 — Verify the panel itself.** Cross-check the user-provided committee against the thesis's official record (cover page / institutional notice). Flag mismatches. Identify the **supervisor** — they usually don't attack their own student.
- **IRON RULE E5 — Public, professional only.** Use public professional information (faculty pages, publications, talks). No personal, private, or sensitive data.

---

## Evidence grades

| Grade | Means | Source examples |
|---|---|---|
| **High** | Officially confirmed or directly verified | Official faculty page / CV / lab page; a verified publication record; institutional bio |
| **Med** | A repeated pattern across recent work | Recurring themes across several recent papers/talks/projects; a review/survey they authored |
| **Low** | Field-adjacent, plausible but unconfirmed | Inference from team membership, department, or one secondary mention |
| **▢ none** | Not found publicly | → fall back to paradigm archetype (E3) |

---

## Source hierarchy (try in order; paradigm-appropriate)

1. **Official faculty / department page** (title, declared research directions, courses, recent grants) — usually the single best High source.
2. **Scholar / publication profile** — Google Scholar; and the discipline's index:
   - Sciences/engineering: IEEE/ACM/Scopus/Web of Science, lab pages.
   - Economics/finance: RePEc/IDEAS, SSRN, NBER, journal pages.
   - Law: SSRN, HeinOnline, the law-school faculty page.
   - Humanities: the department page, the university press / journal record, books.
   - **Chinese institutions (the common case in practice):** the 学院官网 faculty page / 导师队伍 page (High); CNKI 知网 author page, 万方, 百度学术 for the publication record (many Chinese faculty have **no** Google Scholar profile); 学校新闻 / 学报 pages (Med). Search the Chinese name + 学院 first, not the romanization.
3. **Recent work themes** — last ~3–5 years of titles/abstracts → infer recurring methods, questions, and "what they'd press."
4. **Talks / reviews / editorial roles** — a survey or review they wrote is gold for "what they think rigor means."
5. **Secondary mentions** (news, interviews) — Low grade; corroborate before use.

If a faculty page is JavaScript-rendered and a plain fetch returns a shell, escalate to a rendering fetch (browser tools) before giving up. If still nothing → `[MATERIAL GAP]`.

---

## What to extract per evaluator

- Title, department/team, (public) page link.
- **Confirmed** research directions (High).
- Recent themes / recurring methods, datasets, frameworks (Med).
- Supervised-student themes **only if publicly found** (else say so).
- Their likely **evaluator archetype** for this thesis's paradigm (from `discipline-profiles.md`).
- 1–2 "signature attacks" they are most likely to raise — each tied to a Weakness Ledger ID and graded.

---

## Stage 2.5 — Verification gate (cannot be skipped)

Before any evaluator claim enters the guide:
1. Is it sourced at High/Med? If not → downgrade to Low and reword as a *type* inference, or drop it.
2. Does any "signature attack" assume a fact about the person not in the sources? → remove the personal attribution; keep it as a paradigm-archetype question instead.
3. Did I separate "confirmed" from "inferred" in the wording ("confirmed…", "recent work suggests…", "as a [archetype] examiner, likely…")?

---

## Panel verification (the administrative catch)

- Compare the provided committee list to the thesis cover page / official defense notice. **Flag any mismatch** (it happens — names swapped, an old list, the supervisor included by mistake).
- Identify the **supervisor**: they are normally present but do not cross-examine their own student. If a "committee member" turns out to be the supervisor, note it — don't prep attacks for them.
- Confirm titles/names/honorifics so the student doesn't misaddress the chair.
- **Tag each member's role — roles shape questions:** 主席/chair (controls time; often opens with the contribution-framing question), 评阅人/official reviewers (have read closely and submitted written comments — if reviewer reports exist, bind each report to its reviewer: their comments are near-certain questions), 委员/members, 导师/supervisor (doesn't attack), 秘书/secretary (doesn't question). Typical allocation: chair asks 1–2 framing questions; reviewers go deepest.

---

## Graceful degradation (the thin-research reality)

When a member is Low/▢:
- Tag them by paradigm archetype (e.g., "applied-econ / policy examiner", "source-criticism examiner") and prep the **backbone** questions for that archetype.
- Say so plainly in the output: "Public info thin (Low) — treated by archetype." This is honest and still useful, because the dangerous questions come from the thesis's weaknesses, not from the person.
- Do **not** let a thin profile shrink the prep: every CRITICAL weakness still ships as a question regardless of who "owns" it.

---

## Output (per evaluator → battle card)

```
### {Name} ({title}) — evidence: {High/Med/Low}
【潜在关切点 / Potential concern】 {why this person may press, graded}
- Confirmed: {High facts}
- Recent themes: {Med}
- Archetype: {paradigm archetype}
- Signature attacks: {1–2, each → W#, graded}
- One trap to avoid with them.
Source: {link(s)}  |  ⚠ if supervisor / unverified, say so.
```

> Hand-off: graded battle cards feed Threat Mapping (re-weight the Top-10) and the Mock-Defense personas. The panel-verification flags go on the day-of one-pager ("confirm the committee list").
