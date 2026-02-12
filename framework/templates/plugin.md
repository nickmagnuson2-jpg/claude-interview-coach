---
name: Plugin Name
description: One-line description of what this plugin adds
scope: coaching, cv
---

<!-- scope options: coaching, cv, or both (comma-separated) -->

# Plugin Name

## When to Activate

<!-- Natural language description of when this plugin should be loaded.
     Claude evaluates this contextually against the target role, job ad, and industry. -->

Activate when the target role or job ad involves: [keywords, industries, or role types].

## Interview Questions

<!-- Additional questions for recruiter screenings and mock interviews.
     These are added to the question pool alongside core questions. -->

- "[Question 1]"
- "[Question 2]"

## Anti-Patterns

<!-- Domain-specific anti-patterns to track during coaching sessions.
     Use a plugin-specific prefix (e.g. X1, X2) to avoid collision with core patterns (1-16). -->

| # | Pattern | Description |
|---|---------|-------------|
| X1 | [Pattern name] | [What it looks like and why it's problematic] |

## Answering Strategies

<!-- Either inline strategies here, or reference separate files:
     See `strategies/my-strategy.md` for the full strategy guide.

     Strategy files should follow the same format as framework/answering-strategies/*.md:
     - Quick Overview section
     - Full strategy with examples
     - When to Use / When NOT to Use -->

## Session Behavior

<!-- Optional: modify interviewer persona or coaching style when this plugin is active.
     These layer on top of the core persona — they adjust tone and behavior, not replace the role.

     What you can modify:
     - Interviewer tone (skeptical, impatient, aggressive, friendly, formal)
     - Coaching style (brutally direct, no encouragement, Socratic, etc.)
     - Pacing (rapid-fire, interrupts long answers, never lets silences sit)
     - Pressure calibration (always push back twice, never accept first response)

     Example:
     - **Interviewer:** Cold and transactional. Cuts off answers longer than
       two sentences. Never says "great" or "interesting." Follows every
       answer with "And what evidence do you have for that?"
     - **Coach:** No positive feedback. Lead with what was wrong and why it
       would lose the role. Deliver the strongest version without softening. -->

## CV Rules

<!-- Rules for CV generation when this plugin is active.
     Examples: additional sections, formatting rules, keyword requirements. -->
