"""Outcome-oriented workflow extensions; consumed by build_package.py."""

CONTRACT_ADDENDUM = '''
## Improvement, not output volume
Read references/improvement-cycle.md before this task. Existing accounts start from their observed baseline; new accounts start from a niche hypothesis and cheap validation. A requested narrow draft may use the existing diagnosis instead of repeating an audit. Never represent finished drafts or structural tests as evidence of account growth.

Preserve the profile's established identity, character, language and owner-selected production provider. Missing reference assets are missing dependencies, not permission to silently replace a mascot with generic imagery. Offer the owner an explicit creative alternative, but keep it separate from a brand-faithful deliverable. Resolve blocking identity references before spending production credits.
'''

TEMPLATE_ADDENDUM = '''
- Mode: improve-existing / validate-new:
- Baseline dates, sources, metric definitions, exposure ages and gaps:
- Primary bottleneck, supporting evidence and confidence:
- Brand invariants: character/reference files, palette, voice, language, recurring format:
- User-selected provider and duration/format constraints:
- Competitor benchmark sources, comparable cohort and dated observations:
- Experiment IDs, primary metric, guardrail, review dates and decision rules:
- Evidence status: proposed / production-checked / published / measured / replicated:
'''

IMPROVEMENT_CYCLE = '''# Instagram improvement cycle

## Select the job
- Improve an existing account: observe -> diagnose -> benchmark -> choose a small change -> produce -> review -> owner-authorized publication -> measure -> keep, revise or retire.
- Explore a new account: owner fit -> niche candidates -> evidence -> differentiated concept -> cheap test -> review -> commit or reject. A niche is not best merely because large accounts exist in it.

For broad improvement use ig-growth-audit first; for niche discovery use ig-niche-research. If unavailable perform those responsibilities directly. A small caption request does not require a new research project. Reuse dated relevant evidence and state its limitations.

## Evidence and diagnosis
Capture the source, observation date, account/post ID, metric definition, paid/organic status where known, post age and coverage. Separate observation from interpretation. Rank bottlenecks by likely relevance to the selected goal, evidence and cost of testing. One old post cannot diagnose a stable conversion problem or current momentum. Comparisons require similar format, exposure age and objective; flag missing data rather than inventing benchmarks.

Translate a diagnosis into an experiment, not a guarantee:
- ID and profile; owner goal; specific observed problem or explicit hypothesis.
- One primary changed variable, relevant constants and unavoidable confounders.
- Current baseline with denominator and sample size, or unavailable.
- Exact deliverable, character/brand references, owner-selected tools, duration and capacity budget.
- Primary metric and collection method; guardrails such as useful engagement, complaints, production hours and budget.
- Publication date is proposed until verified; observation age and actual review date follow it.
- Decision: inconclusive if data/coverage are too thin; revise if the proposed mechanism fails or costs too much; retain provisionally when multiple comparable observations support it. Scale gradually only within owner budget. Do not manufacture a universal minimum sample size or causal confidence.

Keep a private experiment log, not a public list of client metrics. Preserve earlier hypotheses and outcomes; do not rewrite failures into successes. Small nonrandomized account tests provide descriptive learning, not proof of causal lift.

## Production-quality review
Before paid production or labeling work ready, assess the actual proposal:
1. Audience fit: who is it for, and is that supported or an assumption?
2. Specific value: what exactly does the viewer learn, do or discuss? A generic motivational slogan is insufficient for an educational promise.
3. Identity: recognizable approved character/visual language/voice? Are required references actually present?
4. Opening and payoff: can the first image and words establish a reason to continue, and does the body fulfill it?
5. Evidence/originality: supported factual claims, no copied story, no borrowed results or fake authority.
6. Feasibility/accessibility: duration, actual assets, available provider, budget, readable presentation, complete speech and appropriate captions.
7. Measurement: named hypothesis and metric; no invented expected growth.

Mark each criterion pass, revise or unknown, with a specific reason and next change. Do not use a numeric creativity score as a growth forecast. A blocking identity, claim, cost or format dependency prevents production-ready status; it does not prevent useful concept drafts. ig-quality-review owns a separate critique when requested or when a production handoff needs it. Never imply a second independent review occurred if it did not.

## What counts as success
- Structural validation: files load; no outcome claim.
- Behavioral evaluation: observed decisions on recorded cases; no outcome claim.
- Production check: actual output inspected; list unverified audio/motion/text separately.
- Published observation: verified post with dated metrics and known limits.
- Repeated improvement evidence: consistent useful changes across comparable observations, with confounders and unsuccessful tests retained.

Only the last two stages can support a carefully bounded case study about results. Promotion, attribution, affiliate arrangements and testimonials need their own verified evidence and permissions; do not invent them.
'''

ADDITIONS = {
 'ig-brief': '''Resolve mode and save baseline, brand invariants and missing reference assets. For an existing account, identify what is already working before proposing replacement. For a new account, distinguish owner preferences from evidence of demand and hand niche questions to ig-niche-research. Do not infer a business offer from a handle. The brief is a reusable source of constraints for all later skills.''',
 'ig-strategy': '''For a broad existing-profile improvement request, use or perform ig-growth-audit and read the latest private experiment log. For a new account without validated direction, use ig-niche-research before choosing a niche. Rank opportunities with evidence and uncertainty; do not merely prescribe content pillars. Map each selected action to a diagnosed bottleneck or labeled hypothesis and the improvement-cycle experiment fields. Preserve existing successful identity and owner production preferences. Produce a small prioritized experiment backlog, not a universal growth recipe.''',
 'ig-hooks': '''Start from the selected audience problem and experiment. Preserve the profile voice and character role. Review candidate hooks for specific payoff and evidence before selecting; a provocative sentence without a useful body is not ready. Keep first-frame direction consistent with approved brand references. Report alternatives as hypotheses, not guaranteed attention.''',
 'ig-reel-script': '''Read brand invariants and the experiment before scripting. For a character-led account, specify the actual approved character reference and continuity requirements. If absent, prepare script/shot directions but mark character production blocked; do not silently switch to generic stock imagery. Honor the user's selected provider and duration instead of applying a default long script. Give a spoken-word count and achievable timing; prefer one idea in a short Reel. Review opening, concrete payoff and production dependencies before handoff.''',
 'ig-caption': '''Tie the caption to the selected content hypothesis and actual asset. Add specific useful context rather than another vague wealth, fitness or success slogan. Use a CTA that elicits relevant behavior for the goal, not empty engagement. Preserve the chosen language and recurring voice. Mark performance as unmeasured until published evidence exists.''',
 'ig-carousel': '''Carry brand invariants and experiment ID into the slide brief. Keep the recurring character and approved reference where the profile depends on it. Show a concrete explanation or scenario, not a pile of motivational assertions. Review opening promise and final payoff before calling copy ready for design. Specify what each visual element represents and the connection the reader must understand; decorative completeness is not explanatory completeness. Before delivery inspect every actual slide and its sequence without relying on the caption or your own prompt. If a diagram needs labels, units, quantities or a visible conclusion to teach the idea, include them and verify their mapping. Correct and re-inspect affected slides before marking the set ready; record any uninspected material as unknown.''',
 'ig-stories': '''Use real audience questions or clearly labeled discovery prompts. State what response would change the next content decision. Follow brand invariants and reuse approved assets within capacity; do not manufacture poll evidence or claim demand from a small self-selected response sample.''',
 'ig-content-plan': '''Read the current diagnosis and experiment backlog. Attach an experiment ID and rationale to substantive planned posts. Include a numeric production-time ledger, an explicit capacity assumption when unknown, and a reduced-scope fallback. Keep immutable character/provider/duration constraints in asset handoffs. A same-day weekly review may be preliminary; derive each final measurement date from its own publication date and exposure window. Reuse stable patterns and change only a few deliberate variables. Do not claim a global best posting time for an international audience with unknown markets.''',
 'ig-repurpose': '''Explain why the adaptation addresses a diagnosed gap or test. Preserve approved identity and voice while changing the angle; generic substitution is not brand adaptation. Record source and chosen variable so later analytics can distinguish format adaptation from topic changes.''',
 'ig-comments-read': '''Map recurring questions or objections to content hypotheses with source counts and coverage. Do not diagnose sentiment or demand for the whole audience from a tiny sample. Preserve customer-support ownership; a growth goal does not justify treating complaints as disposable.''',
 'ig-comment-reply': '''Keep the approved brand voice while answering the actual question. Explain unresolved product/support facts in the owner handoff rather than padding a public reply with repetitive offers. Count success as a relevant resolved exchange, not maximum reply volume.''',
 'ig-dm-read': '''Separate learning themes from marketing consent and sales certainty. Hand recurring, anonymized audience needs to strategy only with counts and coverage. Do not let engagement goals expand inbox access or retention.''',
 'ig-dm-reply': '''Preserve voice and actual policy. Prefer resolving the sender's need over pushing a generic sales CTA. Record useful unresolved questions for owner review without claiming conversions from drafts.''',
 'ig-analytics': '''Join observations to the private experiment IDs and original hypotheses. Report decision as retain provisionally, revise, retire or inconclusive with reasons, sample size and confounders. Preserve negative results and missing values. Compare equal-age post snapshots, not whichever total is largest today. Update the next experiment recommendation from evidence; do not label a draft test successful without published results.''',
 'ig-competitor-scan': '''Include both established references for craft and more comparable accounts for opportunity testing. Large follower totals alone do not prove recent growth. To claim growth require dated observations or owner-supplied history and calculate changes over that interval; otherwise describe only observed current scale/engagement. Check smaller-account relative outliers where baselines are available. Link each transferable mechanism to a profile-specific hypothesis, without copying identity or claiming competitor sales.''',
 'ig-bio': '''Tie each proposed change to visitor clarity or another observed issue. Preserve distinctive approved brand names/character unless the owner chooses a change. Distinguish a clear language mismatch from a proven conversion cause; a handful of visits cannot establish lift. Define what would be measured after an authorized change and preserve the prior version.''',
 'ig-ai-visuals': '''Use the owner-selected provider, including Google Flow through available browser tools when requested; do not route automatically to another provider. Read the experiment and brand references first. Missing required character references blocks brand-faithful paid production: prepare prompts and request the reference, rather than buying an unrelated generic substitute. Carry exact duration/aspect/count constraints and obtain a quote from the actual UI/tool. Before submission perform the improvement-cycle production review. After generation check measured runtime and dimensions, actual character consistency, opening/payoff and audio/text; nominal UI duration is not a substitute for measured duration. If speech cannot be heard, mark it unverified. A paid failed or partial result is a recorded test, not automatically ready to publish. No unapproved paid retries.''',
 'ig-collab-pitch': '''Choose partners for audience fit and the owner's actual objective, not follower totals alone. Explain why a recipient is relevant from verified content and distinguish visibility from measured growth. Do not prioritize sponsor outreach over basic profile readiness when the stated goal is learning and relevant followers.''',
 'ig-viral-research': '''Benchmark craft separately from evidence of growth. A large creator's popular post may be irrelevant to a small account; compare audience, format, production effort, exposure age and promotion uncertainty. Never infer recent rapid growth from one follower count. Return only as many grounded concepts as evidence and capacity support, with remaining ideas explicitly speculative. Feed selected mechanisms into the experiment log and quality review; do not spend production credits just to imitate a visual trend.''',
}

NEW_SKILLS = [
 ('ig-growth-audit','Existing Instagram growth diagnosis',
  'Diagnose an existing Instagram account and prioritize evidence-based improvement experiments before content production; niche selection belongs to ig-niche-research.',
  '''Resolve profile and owner objective. Inspect profile, a relevant dated content sample and actual available Insights; accept supplied exports/screenshots and report coverage. Use prior observations if still relevant and dated. Capture what should be preserved as well as what should change: character, visual language, voice, audience and owner tools.
Separate visitor clarity, content usefulness, opening/payoff, audience fit, distribution/consistency and conversion hypotheses. Rank no more than the few most actionable bottlenecks with supporting sources, uncertainty and a disconfirming observation. Do not blame the algorithm or infer causality from low counts.
Before a full improvement strategy, use ig-competitor-scan or perform its evidence workflow: at least five relevant profiles and ten accessible posts per profile, with direct/adjacent roles and coverage labeled. Reuse a dated relevant scan rather than repeating it for every draft. If sources are missing, make a provisional diagnosis and a bounded research queue; never invent high-growth examples or call an incomplete benchmark complete.
Deliver a dated baseline table, preserve/change decisions, top hypotheses and a small experiment plan following references/improvement-cycle.md. Route approved directions to strategy/planning and quality review before paid production. Do not report improvement until actual comparable results exist.'''),
 ('ig-niche-research','New Instagram niche validation',
  'Research and compare Instagram niche opportunities for a new account using demand evidence, owner fit, differentiation and cheap validation tests.',
  '''Start with owner skills/interests, language, target market, available assets, credibility, production capacity and optional business objective. Ask only missing constraints needed to narrow the search. Do not recommend a niche solely for claimed profitability or large follower counts.
Develop a small candidate set. For each candidate collect current dated sources for recurring audience problems/questions, relevant account/post examples, competition and an achievable differentiated angle. Distinguish documented growth from scale; require multiple dates for growth claims. Compare content supply with audience need rather than treating fewer competitors as proof of demand. Flag financial/health/other claim burden and owner credibility needs.
Present an evidence matrix: audience need, observed evidence and links, owner fit, repeatable content runway, feasible production, differentiation, risks, unknowns and proposed cheap test. Do not invent market sizes or use numerical scoring as an objective prediction of success. State why one candidate deserves testing, or conclude insufficient evidence rather than forcing a winner.
For the shortlisted idea give a specific audience promise, recurring format, initial concepts and an experiment with measurable response, review window and stop/pivot criteria. Connect the initial concepts to the observed audience questions as well as owner competence. If the strongest question requires unverified expertise, explain that tradeoff and identify a relevant lower-risk angle or the specific competence check needed; do not silently test an unrelated easy topic and treat it as validation of the original demand. Keep monetization speculative unless supported. No account creation, paid production or posting implied. With supplied synthetic data, label outputs synthetic; do not present invented sources as research.'''),
 ('ig-quality-review','Instagram content production review',
  'Critique Instagram ideas, scripts or actual assets for audience value, brand fidelity and readiness before production or publication; does not predict growth.',
  '''Read the actual brief, proposed deliverable, selected experiment and available references. Use the seven criteria in references/improvement-cycle.md. Return pass/revise/unknown per criterion with concrete evidence, not a flattering overall score.
Perform a meaning-completeness review of every delivered asset, not just spelling, arithmetic and file checks. Hide the caption and reconstruct the intended lesson from the actual visual: what each meaningful object represents, the relation between quantities/actions, the takeaway, and any required next step. Check that labels, units, counts, order, assumptions and visible conclusions agree. Do not require labels on purely decorative objects; require them when missing meaning makes the explanation ambiguous. Evaluate the full carousel for missing steps, contradictions and promised-but-undelivered payoffs. If the reader must guess a key connection, mark revise even when all visible words and numbers are correct. Record asset-specific evidence, make the smallest correction, then inspect the revised output again. Limit repair attempts to three per issue; report unresolved defects instead of silently passing or generating indefinitely. A checklist in instructions is not proof that a check was performed, and self-review cannot guarantee zero errors.
Reject brand-breaking substitutions, unsupported claims, borrowed results, generic filler without payoff, unrealistic duration and unapproved paid scope. Unknown character reference or unverified speech is an explicit dependency. Preserve owner-selected tools. For an actual generated asset distinguish inspected frames from motion/audio actually reviewed and measured duration from nominal setting.
Give the smallest useful revision and a decision: concept-only, production-ready, ready for owner publication review, or blocked with specific missing dependency. Quality approval is not publication authorization and never means proven growth. If independent evaluation is requested or available under the host's delegation rules, report its actual scope; otherwise label review self-assessed.
After measured results exist, check whether the hypothesis was supported and hand evidence back to analytics/strategy. Do not backfill a successful rationale after seeing outcomes.'''),
]
