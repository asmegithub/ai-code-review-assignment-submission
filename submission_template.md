# AI Code Review Assignment (Python)

## Candidate
- Name: Asmare Zelalem
- Approximate time spent: 30 minutes

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- Divides by total orders including cancelled, so averages are incorrect and too low.
- Divides by zero when the input list is empty.
- Raises KeyError when `status` or `amount` keys are missing.

### Edge cases & risks
- Non-dict inputs or missing keys can throw.
- Non-numeric `amount` values raise TypeError during summation.

### Code quality / design issues
- No validation or defaults; assumes perfect inputs.
- Business rule (exclude cancelled orders) is not enforced in the divisor.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Skip cancelled orders for both sum and divisor; return 0.0 when none qualify.
- Use safe lookups with defaults and count only valid entries.
- Guard against empty inputs to avoid division by zero.

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

- Empty list, all cancelled, and mix of cancelled/active to verify divisor logic.
- Orders missing `amount` or `status`, and non-dict items to ensure safety.
- Non-numeric `amount` values to confirm they are handled or rejected.


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- Claims cancelled orders are excluded, but divisor still counts them.
- Omits the division-by-zero risk on empty input.
- Ignores missing-key and type error risks.

### Rewritten explanation
- Sums amounts of non-cancelled orders, counts only those orders, and returns their average; if none qualify, returns 0.0. Uses safe defaults to avoid missing-key errors.

## 4) Final Judgment
- Decision: Reject
- Justification: Produces incorrect averages when cancellations exist and crashes on empty or malformed input.
- Confidence & unknowns: High; behavior is deterministic and easily reproduced.

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- Counts any string containing `@`, so invalid emails are treated as valid.
- Crashes or miscounts on non-string inputs (None, numbers) if they include `@` representation.

### Edge cases & risks
- Leading/trailing spaces and missing local/domain parts pass incorrectly.
- Domains without dots are accepted.

### Code quality / design issues
- No validation helper or guardrails; logic is a single coarse check.
- Lacks documentation of expected email shape.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Validate only string inputs; reject entries with spaces or multiple `@` symbols.
- Require non-empty local and domain parts, domain containing a dot, and forbid leading/trailing dots and double dots.

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

- Clearly valid examples vs. common invalid forms (missing local, missing domain, no dot in domain, double dots, spaces).
- Non-string inputs (None, ints) to ensure they are skipped.
- Empty list to confirm zero is returned.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- Claims it “safely ignores invalid entries” and “handles empty input,” which it does not.
- Overstates correctness of validation with only an `@` check.

### Rewritten explanation
- Counts entries that resemble emails: string input, exactly one `@`, non-empty local and dotted domain without spaces or leading/trailing dots; skips everything else.

## 4) Final Judgment
- Decision: Reject
- Justification: Accepts many invalid emails and provides no safeguards for non-string entries.
- Confidence & unknowns: High; issues are straightforward to reproduce.

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- Divides by total length, so None values are included in the divisor, skewing or crashing.
- Raises ZeroDivisionError on empty input.
- Raises TypeError/ValueError when encountering non-numeric values or None.

### Edge cases & risks
- All values None yields ZeroDivisionError despite no valid data.
- Numeric strings are not handled explicitly; other string inputs cause failures.

### Code quality / design issues
- No filtering for valid measurements; assumes every entry is usable.
- No documentation of expected types or handling of missing values.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Ignore None and any non-numeric values; coerce numeric-like inputs via float.
- Track count of valid numeric entries only and return 0.0 when none exist.

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

- Empty list, all None, and mixed valid/invalid entries to confirm divisor correctness.
- Numeric strings vs. non-numeric strings to verify coercion behavior.
- Large/small floats and negatives to ensure arithmetic correctness.


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- Claims None values are ignored, but they remain in the divisor and can crash.
- Claims it handles mixed input types, but non-numeric types raise errors.

### Rewritten explanation
- Averages only numeric (coercible) measurements, skipping None and non-numeric entries; returns 0.0 if nothing valid remains.

## 4) Final Judgment
- Decision: Reject
- Justification: Crashes on empty or invalid input and produces incorrect averages when missing values are present.
- Confidence & unknowns: High; failures are deterministic.
