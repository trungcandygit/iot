# Discipline Profiles (Paradigm-Adaptive Layer)

Makes the skill work for **any** discipline — sciences, engineering, social science, law, economics, history, literature, philosophy, the arts — without hard-coding hundreds of majors. The engine (weakness audit → questions → answers → mock defense → readiness) is the same for everyone; this file supplies the **lens** that engine looks through.

> Core idea: do **not** classify the *major* (e.g., "radar", "tort law", "Ming history"). Classify the **research paradigm** (how the work makes and defends knowledge). A handful of paradigm families cover every field. The same thesis-defense pressures take different shape in each.

---

## IRON RULES

- **IRON RULE D1 — Detect paradigm, then load its lens.** At Stage 0, classify the thesis into a paradigm family (below) and apply that profile's vocabulary, evaluator archetypes, and severity examples throughout. Never apply empirical-quantitative expectations (baselines, ablations, p-values, reproducibility) to interpretive, doctrinal, or creative work.
- **IRON RULE D2 — Evidence is paradigm-relative.** "Evidence" means experimental data *and* archival sources *and* case law *and* close readings *and* proofs *and* the creative artifact, depending on the paradigm. Judge claim-evidence fit by the standards of that paradigm.
- **IRON RULE D3 — Mixed is normal.** Many theses blend paradigms (mixed-methods, law-and-economics, digital humanities, practice-based design with empirical evaluation). Detect a **dominant** and a **secondary** paradigm and blend both lenses; do not force one.
- **IRON RULE D4 — Universal core still applies.** Regardless of paradigm, every defense tests: contribution ("so what / what's new"), the claim-evidence/warrant link, scope/limits honesty, and the candidate's command of the field. These survive translation across all profiles.

---

## How to detect the paradigm (Stage 0)

Read the thesis abstract, contributions, and methods section. Ask:
1. What does the work offer as proof — data/experiments? interviews/fieldwork? proofs/formal argument? texts/archives? statutes/cases/normative argument? a created artifact + exegesis?
2. Is the claim mainly *descriptive/causal* (what is / what causes), *interpretive* (what it means), *normative* (what ought to be), or *generative* (what I made)?
3. What would a hostile examiner attack — the data, the reading, the argument's validity, the sources, the doctrine, or the craft?

Map answers to one (or two) of the six families below. If genuinely unsure between two, treat as **Mixed** and confirm with the user. State the detected paradigm in the guide ("Detected paradigm: …; if this is wrong, tell me").

---

## The six paradigm families

### P1 · Empirical–Quantitative 实证–定量
*Sciences, engineering, quantitative social science, quantitative economics/finance, epidemiology, experimental psychology.*
- **Evidence:** experiments, measurements, datasets, simulations, statistical inference, models.
- **Method rigor (the D3 lens):** design validity, sampling/power, controls, baselines/comparisons, ablations, statistical validity, reproducibility, simulation-vs-real gap.
- **CRITICAL patterns:** sim/lab result sold as real-world; correlation→causation without controls; data table contradicts the stated conclusion; missing baseline makes the gain meaningless; over-generalized from a narrow sample.
- **Evaluator archetypes:** methodology/stats examiner · domain examiner · application/feasibility examiner · adversarial/logic examiner.
- **Signature questions:** "under what conditions? clutter/confounds?"; "where's the baseline?"; "is the effect meaningful, not just significant?"; "does it replicate / deploy?"
- **Slides:** yes, typical.

### P2 · Empirical–Qualitative 实证–定性
*Anthropology, sociology (qual), education, qualitative public health, organization/management studies, communication.*
- **Evidence:** interviews, ethnography, case studies, documents, grounded-theory coding, observations.
- **Method rigor:** positionality/reflexivity, sampling logic, data saturation, triangulation, coding reliability, trustworthiness/credibility, transferability (not statistical generalization).
- **CRITICAL patterns:** claims of generalization the design can't support; researcher bias / unexamined positionality driving the reading; cherry-picked quotes; thin data presented as saturated; alternative interpretations not addressed.
- **Evaluator archetypes:** qualitative-methods examiner · theory/framework examiner · "transferability & rigor" challenger · ethics/positionality examiner.
- **Signature questions:** "how is this generalizable / transferable?"; "what's your positionality and how did it shape findings?"; "did you reach saturation?"; "what rival interpretation did you rule out?"
- **Slides:** usually.

### P3 · Theoretical–Formal 理论–形式/思辨
*Mathematics, theoretical CS, analytic philosophy, theoretical physics/economics, logic.*
- **Evidence:** proofs, derivations, formal models, logical argument, counterexample analysis.
- **Method rigor:** validity/soundness of proofs, stated assumptions, generality vs. special cases, robustness to counterexamples, non-triviality.
- **CRITICAL patterns:** a step in the proof doesn't follow; a hidden/unstated assumption does the real work; the result is trivial or already known; a counterexample breaks the claim; generality overstated.
- **Evaluator archetypes:** rigor/proof examiner · novelty/non-triviality challenger · assumptions/limits examiner · relevance/"why care" examiner.
- **Signature questions:** "justify this step"; "what exactly are your assumptions, and where do they bind?"; "how is this stronger than the known result?"; "give the intuition / a counterexample."
- **Slides:** sometimes (board/talk); viva-style possible.

### P4 · Textual–Interpretive / Humanistic 文本–阐释
*Literature, history, religious studies, area/cultural studies, classics, continental philosophy, musicology.*
- **Evidence:** primary texts, archival sources, close reading, historiography, contextual evidence.
- **Method rigor:** source criticism (authenticity, bias, provenance), contextualization, interpretive coherence, engagement with secondary literature, transparency of the interpretive/hermeneutic framework.
- **CRITICAL patterns:** reading the sources can't bear; ignoring counter-evidence in the archive; weak/絶 source base; anachronism or decontextualization; not engaging the major existing interpretations; thesis is description, not an argument.
- **Evaluator archetypes:** source/archive specialist · theory/method (which interpretive lens) examiner · historiography/literature examiner · "originality & significance" challenger.
- **Signature questions:** "why this interpretive framework over [alternative]?"; "how do you handle the sources that cut against you?"; "what's your original contribution vs. [scholar X]?"; "isn't this anachronistic?"
- **Slides:** often **none** (oral viva); a handout or no visual aid is common.

### P5 · Doctrinal–Normative 法学–教义/规范
*Law (doctrinal), jurisprudence, normative ethics/political theory, some policy analysis.*
- **Evidence:** statutes, case law, doctrine, legislative history, normative argument, comparative material.
- **Method rigor:** doctrinal accuracy, precedent/authority analysis, internal logical consistency of the normative argument, treatment of counterarguments, jurisdictional/comparative scope.
- **CRITICAL patterns:** misreads a controlling authority; argument proves too much / internal contradiction; ignores the strongest counterargument; normative premise unsupported; over-claims beyond the jurisdiction/scope.
- **Evaluator archetypes:** doctrinal specialist · comparative/jurisdiction examiner · normative-foundations challenger · consequences/policy examiner.
- **Signature questions:** "doesn't [case/authority] cut against you?"; "what's the strongest objection, and your answer?"; "where does your normative premise come from?"; "does this hold in another jurisdiction?"
- **Slides:** sometimes; often oral.

### P6 · Design–Creative / Practice-based 设计–创作/实践
*Fine art, design, architecture, creative writing, music composition, some practice-based HCI.*
- **Evidence:** the artifact / portfolio / body of work **plus** a reflective exegesis or commentary.
- **Method rigor:** conceptual coherence, craft/technique, the artifact–exegesis link, situating the work in its field/canon, contribution to practice.
- **CRITICAL patterns:** the exegesis claims something the work doesn't deliver; weak situating in the canon/precedents; concept-craft mismatch; no articulable contribution beyond the personal.
- **Evaluator archetypes:** craft/technique critic · concept/theory critic · canon/contextualization examiner · "contribution to the field" challenger.
- **Signature questions:** "what's the contribution beyond a good piece of work?"; "how does this sit against [precedent/movement]?"; "does your written account match what the work actually does?"; "why these choices?"
- **Slides:** varies — exhibition/portfolio + viva; often artifact-centered, not slide-centered.

### P0 · Mixed / Applied 混合/应用
*Mixed-methods, professional/clinical doctorates, business, interdisciplinary, digital humanities, law-and-economics.*
- Detect a **dominant** + **secondary** family; load both lenses and merge the evaluator archetypes. Flag the seam — interdisciplinary committees often attack the **join** ("your quant is thin for an economist, your theory is thin for a sociologist"). Make sure the candidate can defend the integration, not just each half.

---

## How to apply a profile (every downstream stage reads this)

- **Weakness audit** (`weakness-audit-framework.md`): instantiate the Three Lenses and severity criteria using this paradigm's "evidence" and "CRITICAL patterns". Use the paradigm's examples, not radar examples.
- **Question generation** (`question-generation-rules.md`): replace the generic evaluator-type table with this paradigm's **evaluator archetypes**; bias the universal backbone toward the paradigm's signature questions.
- **Readiness rubric** (`readiness-rubric.md`): define D3 "method/argument rigor" by this paradigm's rigor list; if the defense has no slides (common in P4/P5/P6 vivas), drop D5 and re-weight.
- **Mock defense** (`mock-defense-protocol.md`): the examiner personas are this paradigm's archetypes.

> Hand-off: the detected paradigm (and any secondary) is stated at Stage 0 and threaded through every later stage. When in doubt between families, treat as P0 Mixed and confirm with the user.
