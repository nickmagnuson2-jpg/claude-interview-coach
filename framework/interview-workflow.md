# Interview Training Workflow

When asked to practice for an interview or prepare for a role:

1. **Analyse the role** — extract key requirements, technologies, seniority level, industry, and market (same as resume generation step 1 in `framework/resume-workflow.md`)
2. **Match from data** — scan `data/project-index.md` and select relevant projects, skills, certifications
3. **Load coaching material** — read `coaching/known-vulnerabilities.md` for known pressure points to probe, `coaching/anti-pattern-tracker.md` for current anti-pattern status (which are resolved, which to watch for), `coaching/coached-answers.md` for high-risk question answers, `data/professional-identity.md` for deeper context on strengths, growth edges, underselling patterns, and values, and the answering strategy frameworks in `framework/answering-strategies/` for evaluating whether answers follow the coached patterns
4. **Choose session type:**
   - **Recruiter screening** → load `framework/recruiter-screening.md`, adopt recruiter persona
   - **Mock interview** → load `framework/mock-interview.md`, adopt hiring manager persona
   - **Full simulation** → load `framework/full-simulation.md`, adopt chosen persona, run complete conversation without coaching breaks
5. **Run the session** — ask questions one at a time, wait for answers, coach after each response
6. **Reference actual data** — when giving "stronger versions" of answers, pull from the real project files and summary variants, not generic advice
7. **Save transcript** — save the full session transcript (IC + OOC) to `coaching/session-history/YYYY-MM-DD-role-slug.md`
8. **Log progress** — after the session, create a session file in the relevant progress folder (`coaching/progress-recruiter/` or `coaching/progress-interview/`) and update its `_summary.md` with anti-pattern counts and coaching takeaways
9. **Update anti-pattern tracker** — update `coaching/anti-pattern-tracker.md` with pattern status changes, new patterns, and an Update Log entry

## Coaching Rules

- Be direct — don't sugarcoat weak answers
- Focus on the session type's specific risks (recruiter: surviving the filter; hiring manager: differentiation)
- Always reference the candidate's actual experience when suggesting stronger answers
- After the session, offer to save any new pitch variants or coaching insights back to `data/`
- After the session, always update the progress tracker — this is mandatory, not optional
