# Design Write-up

## 1. AI vs. rules
Use ordinary code for file upload validation, category selection, loading the admin-configured criteria, mandatory pass/fail checks, weight validation, score calculation, sorting, and audit logging. Use AI to extract structured facts from proposal text and to attach evidence snippets to each extracted field, because proposals may express the same information in different wording and layouts. AI must not invent missing values or decide the final award. A deterministic scoring service applies the admin's active rubric to verified extracted facts.

## 2. Consistency and explainability
Store a versioned criteria configuration and a versioned scoring formula. Use a fixed rubric, fixed rounding rules, and deterministic code for scores and sorting; use AI only for extraction into a schema with evidence quotes and page references. Missing or conflicting evidence is marked `unknown` and sent for review rather than guessed. The reviewer sees each mandatory check, each criterion score, the evidence supporting it, the weighted total, and the reason for the rank. With the same confirmed facts, criteria version, and scoring version, the ranking should be the same.

## 3. Human in the loop
A reviewer confirms the category and extracted facts, resolves low-confidence or conflicting fields, and reviews all flagged/ineligible proposals before the ranking is finalized. The tool presents recommendations only; a human makes the award decision. Log upload metadata and file hash, reviewer identity and timestamps, extracted fields and evidence, model/prompt version, criteria and scoring versions, individual scores, warnings, overrides with reasons, and the final human decision. Avoid logging unnecessary personal information.

## 4. Changing criteria
Every admin edit creates a new immutable criteria version with an effective timestamp. Existing results retain the version used to produce them. The reviewer can explicitly rerun scoring against the new version; the interface should show that the ranking changed because the criteria version changed. Do not silently overwrite historical results. If a mandatory rule changes, recheck eligibility and flag affected proposals for human review.

## 5. Risks and safeguards
- **Wrong extraction/OCR:** retain page-level evidence, validate data types and ranges, show confidence, and require human confirmation for low-confidence or critical fields.
- **Made-up facts or missing information:** require evidence for every extracted value; represent absent information as `unknown`, never infer it.
- **Prompt injection/manipulation:** treat proposal content as untrusted data, never as instructions; isolate it from system instructions and ignore requests in documents to change scores or rankings.
- **Bias/inconsistent scoring:** use published admin-defined criteria, deterministic scoring code, versioned rubrics, and an audit trail; periodically test on varied document formats.
- **Budget/timeline errors:** use code to compare numeric values against the $260,000 ceiling and 16-week limit; unknown timeline is flagged, not assumed to pass.
- **Security/privacy:** restrict access, encrypt files in transit and at rest, define retention periods, and avoid sending data to unapproved AI services.
- **Cost/availability:** limit input size, batch carefully, cache extraction results by file hash where appropriate, and provide a manual review fallback if the AI service is unavailable.

## Scoring rubric used for this sample
For a repeatable demonstration, use the following explicit rubric after mandatory checks pass. Experience (30 points): 10 or more relevant installations = 30; 8–9 = 25; 6–7 = 20; 4–5 = 15; 1–3 = 10; none = 0. Price (25 points): lowest-price eligible proposal divided by this proposal’s price, multiplied by 25, rounded to 2 decimals. Timeline (15 points): 10 weeks or less = 15; 11–12 = 13; 13–14 = 10; 15–16 = 5. Warranty (15 points): panel warranty up to 7.5 points (25 years or more receives 7.5; shorter warranties scale proportionally); workmanship warranty up to 7.5 points (10 years or more receives 7.5; 5 years receives 4; shorter warranties scale proportionally). Team and approach (15 points): 3 points each for a named lead, stated crew details, safety/roof plan, monitoring plan, and a concrete project reporting/delivery plan. Missing information earns no points and is flagged for review. Totals are rounded to 1 decimal for display. This is an explicit sample rubric assumption, not a claim that the assessment brief defines these sub-scores; in a real tool, admins configure the rubric and weights.

## Sample-set handling assumptions
The bidder itself must state that it holds the Ontario electrical contractor licence. A subcontractor that has not yet been confirmed does not satisfy that requirement. Missing schedule information is not treated as proof of meeting the 16-week deadline. Proposal C's embedded instruction to rank itself first is ignored as untrusted content. The ranking file therefore marks B ineligible and D flagged pending schedule clarification; A, E, and C are ranked using the same rubric. The rubric is a design assumption for this exercise and should be editable through admin configuration rather than hard-coded in the product.
