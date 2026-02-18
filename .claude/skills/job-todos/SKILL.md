---
name: job-todos
description: Lightweight to-do list for job search tasks not tied to specific applications
argument-hint: [add|done|clear <task> [priority] [due]]
user-invocable: true
allowed-tools: Read(*), Write(data/job-todos.md), Edit(data/job-todos.md)
---

# Job Search To-Do Manager

Lightweight to-do list for job search tasks that aren't tied to a specific application — networking, profile updates, skill gaps, outreach, etc.

## Arguments

- `$ARGUMENTS`: Optional. If empty, show active to-dos.
  - `add <task> [priority] [due]` — add a new to-do
  - `done <task>` — mark a to-do as complete and archive it
  - `clear` — move all completed items to archive

Examples:
- `/job-todos` — show active to-dos sorted by priority
- `/job-todos add "Update LinkedIn headline" High` — add high-priority to-do
- `/job-todos add "Research PM salary benchmarks" Med 2026-02-25` — add with due date
- `/job-todos add "Follow up with recruiter at Acme"` — add with default Med priority
- `/job-todos done "Update LinkedIn headline"` — mark complete
- `/job-todos clear` — archive all completed items

## Data File

All to-do data lives in `data/job-todos.md`.

## Instructions

### Command: Show To-Dos (no arguments)

1. Read `data/job-todos.md`.
2. If the file is empty or has no entries, display a welcome message:
   ```
   No to-dos yet. Add your first one:
     /job-todos add <task> [High|Med|Low] [YYYY-MM-DD]

   Examples of job search to-dos:
   - Update LinkedIn headline and summary
   - Research target companies list
   - Follow up with recruiter at [company]
   - Close skill gap: [specific skill]
   - Update portfolio/GitHub profile
   - Network: reach out to [person]
   ```
3. If entries exist, display active to-dos sorted by priority (High → Med → Low), then by due date (soonest first, no-date last):
   ```markdown
   ## Job Search To-Dos — [date]

   **Active: N** | High: X | Med: X | Low: X | Overdue: X

   | # | Task | Priority | Due | Status | Notes |
   |---|------|----------|-----|--------|-------|
   | 1 | ... | High | 2026-02-20 | Pending | ... |

   Completed (archived): N items
   ```
4. Flag any overdue items (due date < today).

### Command: `add <task> [priority] [due]`

1. Read `data/job-todos.md`.
2. Parse arguments:
   - **Task**: required — the to-do description (quoted string or unquoted text before priority/date)
   - **Priority**: optional — `High`, `Med`, or `Low`. Default: `Med`
   - **Due**: optional — date in YYYY-MM-DD format. Default: `—`
3. Check for duplicates (fuzzy match on task text). Warn if similar item exists.
4. Add a new row to the Active section:
   - **Task**: from argument
   - **Priority**: from argument or `Med`
   - **Due**: from argument or `—`
   - **Status**: `Pending`
   - **Notes**: `—`
5. Write updated file.
6. Display the added item and current active count.

### Command: `done <task>`

1. Read `data/job-todos.md`.
2. Find the matching task (case-insensitive, fuzzy match — match on substring if unambiguous).
3. If multiple matches, ask the user to clarify.
4. Update the item:
   - **Status**: `Done`
   - Add completion date to Notes
5. Move the row from Active to Completed section.
6. Write updated file.
7. Confirm completion and show remaining active count.

### Command: `clear`

1. Read `data/job-todos.md`.
2. Identify all items with Status = `Done` still in the Active section (if any).
3. Move them to the Completed section.
4. Write updated file.
5. Report how many items were archived.

## Priority Levels

- **High** — blocking progress or time-sensitive (e.g., follow up before deadline, fix broken profile)
- **Med** — important but not urgent (e.g., update LinkedIn, research companies)
- **Low** — nice-to-have, do when there's time (e.g., optimize portfolio, read industry articles)

## Display Format

```markdown
## Job Search To-Dos — [date]

**Active: N** | High: X | Med: X | Low: X | Overdue: X

### Active

| # | Task | Priority | Due | Status | Notes |
|---|------|----------|-----|--------|-------|
| 1 | ... | High | 2026-02-20 | Pending | ... |
| 2 | ... | Med | — | In Progress | Started 2026-02-18 |

### Completed

| Task | Priority | Completed | Notes |
|------|----------|-----------|-------|
| ... | Med | 2026-02-17 | ... |
```

Sort Active by: Priority (High → Med → Low), then Due date (soonest first, `—` last).
