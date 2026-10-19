# Lessons learned: SQL injection found during penetration testing

## What happened
During the pre-handoff penetration test, a team member suspected the client's public website was vulnerable to SQL injection. The website was outside the original scope, which covered the network and infrastructure only.

## Why it mattered
The engagement existed because of data breaches that exposed customer PII. A SQL injection flaw can exfiltrate exactly that data, so the finding was treated as critical.

## Response
1. Notified the client immediately and got approval to modify the site.
2. Fixed it with **input validation** and **parameterized queries**.
3. Re-tested, and checked the rest of the site for other critical flaws. None were found.

## Impact on the project
- Added a 2-day task (Aug 17-18, 2025).
- Absorbed by finishing technical infrastructure updates 2 days early (Aug 6 instead of Aug 8).
- Final handoff still happened on schedule on Aug 19, 2025.

## Takeaways
- A first-phase audit and pentest narrows scope, but late discoveries still happen, so build slack into a waterfall plan.
- Raise out-of-scope critical findings with the client right away and get written approval before changing anything.
- Validate the fix, then widen the check to the surrounding attack surface.
- A severe web application flaw set could have required a separate project, so scope boundaries should name what is excluded.
