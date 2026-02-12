# Resume Coach

A framework that turns [Claude Code](https://docs.anthropic.com/en/docs/claude-code) into a career toolkit — targeted CV generation, interview coaching, voice simulation, and progress tracking — all driven by structured markdown files.

## What it does

- **Generate tailored CVs** from a single experience database — one job ad in, one role-specific CV out
- **Practice recruiter screenings** with AI coaching after every answer (or full uninterrupted simulations)
- **Practice hiring manager interviews** with technical depth probes and tough-mode pressure tests
- **Simulate real calls** via voice — generate a self-contained prompt, practise by speaking, debrief the transcript
- **Track improvement** with structured scorecards, anti-pattern counts, and session logs
- **Scan job boards** for matching roles with fit scoring

## What coaching looks like

All examples below are from a tough-mode recruiter screening with the fictional example profile (Alex Chen). The recruiter questions, pressure points, and coached answers are generated automatically from the job ad and the candidate's project data — nothing is scripted.

**The coaching loop** — you answer, the coach catches anti-patterns and provides the strongest version:

> **Recruiter:** "The role is heavily Go — it's our primary language for platform services. I see three years on your CV. The engineers on this team have been writing Go for seven, eight years. How would you handle that gap in experience?"
>
> **You:** "Probably not as good as them *laughs*. But I'm a quick learner."
>
> **Coach:** That answer just killed your candidacy. Let me be specific about why:
>
> "Probably not as good as them" — she didn't say you're worse than the team. You said that. She asked how you'd handle the difference. You confirmed yourself as the weakest engineer on the team before you've even interviewed. That goes straight into her notes.
>
> "I'm a quick learner" — every single candidate says this. It means nothing. It's the recruiter equivalent of white noise.
>
> Anti-patterns triggered:
> - **Confirming the recruiter's concern** — she floated the gap. You confirmed it and made it worse.
> - **Volunteering negatives** — she said the team has 7-8 years. She didn't say "so you'd be the weakest." You volunteered that.
> - **Generic self-description** — "quick learner" is not a differentiator.
> - **Missing quantitative checkboxes** — you have 3 years of Go. You didn't even state the number or what you built with it.
>
> What she actually needed to hear: what you've built with Go, and why 3 years of production Go from someone who also does infrastructure is different from 3 years of Go from a pure backend dev.
>
> **Strongest version:** "Three years of production Go — I built the microservice layer at NordPay for their payment platform, and I wrote Go tooling at ShopStream for the internal developer platform. My angle isn't competing on pure language years — it's that I write Go AND design the infrastructure it runs on. Most Go engineers don't think about the platform layer. I do both. Is the team looking for a pure Go specialist, or someone who bridges Go development and infrastructure?"

**Session debrief** — after each session, you get structured feedback and a concrete focus for next time:

> **Dominant patterns:** Volunteering negatives (5 of 8 answers) and not answering the actual question (4 of 8).
> No gap reframing applied — despite having frameworks for it, zero questions used the acknowledge-pivot-question back pattern.
>
> **Focus for next session:**
> 1. Write and memorise 15-second recruiter pitch
> 2. Practise gap reframing on 3 common gaps
> 3. Practise direct answer structure — answer first, brief context, stop
> 4. Work on emotional regulation — when a question feels unfair, pause, don't react

**Progress tracking** — anti-pattern counts across sessions so you can see improvement over time:

> | Anti-Pattern | Total | Trend |
> |---|---|---|
> | Volunteered a negative unprompted | 5 | — (baseline) |
> | Not answering the actual question | 4 | — (baseline) |
> | Hedging on rate/availability/logistics | 2 | — (baseline) |
> | Confirming recruiter's concern | 2 | — (baseline) |

## Quick start

### Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed and configured — requires a Claude Pro or Max subscription (Max recommended — coaching sessions and deep reviews are token-intensive)
- Git
- Python 3.8+ (optional — only needed for PDF generation via `tools/md_to_pdf.py`)

### 1. Clone

```bash
git clone https://github.com/raphaotten/claude-resume-coach.git
cd claude-resume-coach
```

### 1b. Try it first (optional)

The repo includes a fictional example profile — **Alex Chen**, a freelance DevOps/Cloud consultant in Berlin with 8 years across AWS and Azure, CKA certified, looking to move into a permanent platform engineering role. You can try all features with this data before importing your own:

```bash
cp -r examples/data/* data/
cp -r examples/output/* output/
```

Then open Claude Code in the repo and try:
- `/review-cv output/sample-cv-cloud-engineer.md` — review the sample CV
- `I want to practice a recruiter screening for a Senior Cloud Engineer role` — try coaching

When you're ready to use your own data, delete the examples and run `/import-cv path/to/your-cv.pdf` — one command turns your CV into the same structured data files.

### 2. Import your data

Import your existing CV:

```
/import-cv path/to/your-cv.pdf
```

This creates your profile, skills, certifications, education, and projects as structured `data/` files — including `data/profile.md` (gitignored, so your personal data stays private even on public forks).

You can also paste CV text directly:

```
/import-cv paste
```

**Import multiple documents** to build a complete picture — an older CV first, then a newer one, a LinkedIn PDF export, a project list. Each import merges with existing data: new projects get added, existing ones get enriched, nothing gets lost.

### 3. Review and fill gaps

After importing, review the generated files and fill in the `TODO` markers. The most impactful ones:

- **Compensation** and **availability** in `data/profile.md` (never on CVs, but essential for targeting)
- **Key achievements** in each project file (makes generated CVs dramatically stronger)

### 3b. Discover your professional identity (optional but valuable)

```
/extract-identity
```

A guided coaching conversation about who you are professionally — your strengths, growth edges, how you frame your work, and what you value. Produces `data/professional-identity.md`, which improves the tone and narrative quality of everything the framework generates.

### 4. Generate your first CV

Paste a job ad:

```
Generate a targeted CV for this role: [paste job ad]
```

Claude reads your data files, matches relevant experience, and produces a tailored CV in `output/`.

### 5. Practice an interview

```
I want to practice a recruiter screening for this role: [paste job ad]
```

Choose normal or tough mode. Claude plays the recruiter, coaches you after each answer, and logs the session.

### 6. Try voice simulation

```
/voice-export output/your-cv.md https://job-ad-url
```

Paste the generated prompt into the Claude mobile app (voice mode). Practise by speaking. Then paste the transcript back and run:

```
/debrief output/your-cv.md
```

## Available commands

| Command | What it does |
|---|---|
| `/import-cv <path>` | Import a CV into structured data files (additive merge) |
| `/extract-identity` | Guided conversation to discover your professional identity |
| `/review-cv` | Fast quality-gate review of a generated CV |
| `/review-cv-deep` | Six-perspective deep-dive CV review |
| `/voice-export <cv> <url>` | Generate voice simulation prompt |
| `/debrief <cv>` | Analyse a voice simulation transcript |
| `/scan-jobs <portal> [query]` | Scan a job portal for matching projects (upwork.com, etc.) |

## How it works

The framework has three layers:

1. **Data layer** (`data/`) — your professional experience in structured markdown
2. **Methodology layer** (`framework/`) — workflows, coaching methodologies, answering strategies
3. **Automation layer** (`CLAUDE.md` + `.claude/skills/`) — tells Claude how to use the first two layers

Claude Code automatically reads `CLAUDE.md` at the start of every session. This file tells Claude where your data lives, what format it uses, and how to generate CVs and run coaching. The `.claude/skills/` folder defines the slash commands — multi-step workflows triggered by `/import-cv`, `/voice-export`, etc. Together, they make the framework work without any code — just structured markdown and instructions.

For the full explanation of how each component works: **[docs/methodology.md](docs/methodology.md)**

## Repository structure

```
CLAUDE.md              ← Orchestration: tells Claude where everything is
framework/             ← Reusable methodology (workflows, coaching, strategies)
data/                  ← Your professional data (templates included, private once filled)
coaching/              ← Coaching outputs and progress tracking (private once used)
examples/              ← Fictional example data to try features before importing
.claude/skills/        ← Claude Code skill definitions
tools/                 ← PDF conversion utilities
output/                ← Generated CVs and reports
docs/                  ← Framework documentation
```

## Adapting to your situation

The coaching methodology works for any market and career type. Regional conventions (CV format, recruiter expectations) are configurable in `framework/style-guidelines.md` — the initial examples and style defaults reflect the DACH/European freelance market, but all frameworks (gap reframing, pin-down defense, direct answer structure, etc.) are universally applicable.

To adapt:

- Edit `data/profile.md` for your professional details
- Edit `framework/style-guidelines.md` for your market's CV conventions (US, UK, DACH, and international formats are included)
- Edit `framework/recruiter-screening.md` to adjust coaching focus to your interview patterns
- Add answering strategies in `framework/answering-strategies/` for pressure points specific to your domain
- `/scan-jobs` works with any job portal — provide the domain and it navigates the site, or pass a full search URL
- The coaching progress structure works as-is for any role

## License

Dual-licensed:
- **Code** (tools/, .claude/skills/, CLAUDE.md): [MIT](LICENSE)
- **Written methodology** (framework/, coaching/ templates): [CC BY 4.0](LICENSE)

Your personal data in `data/` and `coaching/` is yours — the licenses cover only the framework and tooling.

## Credits

Originally created by [Raphael Otten](https://www.linkedin.com/in/raphaelotten/)
