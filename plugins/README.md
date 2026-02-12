# Plugins

Drop-in extensions for interview coaching and CV generation. Each plugin is a self-contained directory with a `plugin.md` manifest.

## Quick Start

1. Create a directory here (e.g. `plugins/fintech/`)
2. Add a `plugin.md` manifest (copy `framework/templates/plugin.md` as a starting point)
3. That's it -- the framework discovers and loads active plugins automatically

## Activation

By default, all plugins in this directory are active. To disable specific plugins or switch to an allowlist, edit `data/plugins.md`.

## What Plugins Can Do

- Add industry-specific interview questions
- Add custom answering strategies (same format as `framework/answering-strategies/`)
- Add domain-specific anti-patterns to track
- Modify interviewer persona and coaching style (tone, pacing, pressure level)
- Add CV sections or formatting rules
- Add new coaching modes

## Plugin Structure

Minimal (everything inline):
```
plugins/my-plugin/
└── plugin.md
```

Expanded (separate files):
```
plugins/my-plugin/
├── plugin.md              # Required: manifest + integration rules
├── questions.md           # Optional: interview question bank
├── anti-patterns.md       # Optional: domain-specific anti-patterns
├── cv-rules.md            # Optional: CV formatting/section rules
└── strategies/            # Optional: answering strategy files
    └── my-strategy.md
```

## Git

This directory is version-controlled (not gitignored). Plugins you add here will be committed with the rest of the repo. If a specific plugin contains sensitive content, add it to `.gitignore` individually.

## Session Behavior in Action

A plugin with `## Session Behavior` can change how the interviewer acts. For example, a mean-mode plugin that sets the interviewer to hostile and impatient produces exchanges like this:

> **Recruiter** *(impatient)*: Right. I see you've been freelancing since 2019. Now you're applying for a permanent position. Why the switch?
>
> **Candidate:** I want more regular working hours and the chance to go deep on one topic, instead of seeing something new every two to three months.
>
> *(Short pause)*
>
> **Recruiter:** Regular working hours. For an L3 position with on-call rotation. You did read the job posting, right?

Without the plugin, the default recruiter is professional and direct but not hostile. The plugin overrides the tone section of the recruiter persona, and the framework skips the normal/tough mode selection since the plugin already defines the session intensity.

## Example

See `examples/plugins/fintech/` for a complete example plugin demonstrating all extension points.
