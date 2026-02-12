# Example Data — Alex Chen (Fictional)

This directory contains a complete, fictional freelancer profile so you can try the framework's features before importing your own data.

**Alex Chen** is a fictional freelance DevOps/Cloud consultant based in Berlin, with 8 years of experience across AWS and Azure, specialising in Kubernetes and infrastructure automation.

## How to use

Copy the example data into the repo's working directories:

```bash
cp -r examples/data/* data/
cp -r examples/output/* output/
```

Then try any of the features below.

## Example Invocations

### Resume / CV Generation

**From a job ad URL:**

```
Generate a CV targeting this role: https://example.com/jobs/senior-devops-engineer
```

**From a pasted job description:**

```
Generate a CV for this role:

Senior Cloud Engineer - FinServ Corp
Requirements: 5+ years AWS, Kubernetes, Terraform, CI/CD pipelines.
Strong experience with microservices architecture and observability.
```

**With a fictional job profile (no job ad needed):**

```
Generate a CV targeting a Senior Platform Engineer role at a mid-size SaaS company.
Focus on Kubernetes, GitOps, and developer experience. Remote, contract, 6 months.
```

```
Create a resume for a Lead DevOps Architect position. Come up with a realistic
job profile for a large German automotive company moving to cloud-native.
```

### CV Review

**Quick review:**

```
/review-cv output/sample-cv-cloud-engineer.md
```

**Multi-perspective deep review:**

```
/review-cv-deep output/sample-cv-cloud-engineer.md
```

### Interview Coaching

**Recruiter screening with a specific job ad:**

```
I want to practice a recruiter screening for this role: https://example.com/jobs/cloud-engineer
```

**Recruiter screening with a pasted job description:**

```
Let's do a recruiter screening practice. Here's the job:

DevOps Engineer at TechCorp Berlin
Must have: AWS, Docker, Kubernetes, Terraform
Nice to have: Go or Python, monitoring (Datadog/Prometheus)
```

**Recruiter screening with a fictional job profile:**

```
Start a recruiter screening for a Senior Cloud Architect position.
Come up with a fictional job profile for it.
```

```
Practice recruiter call for a Kubernetes Platform Engineer at a fintech startup.
Make up a realistic job description.
```

**Mock interview (hiring manager, more technical):**

```
Start a mock interview for a Java developer position.
Come up with a fictional job profile for it.
```

The model creates a complete job profile on the fly and then drops straight into character as the hiring manager:

> **Senior Java Backend Developer**
> Company: Riviera Digital GmbH -- Berlin, Germany
> Industry: Travel Tech / Marketplace | Team: ~8 backend engineers
> Contract: Permanent (or long-term freelance considered)
>
> Riviera Digital operates a B2B travel marketplace connecting tour operators
> with resellers across 14 European markets. The platform handles 500k+
> booking transactions/month. The team is rebuilding core booking and pricing
> services from a legacy monolith into event-driven Java microservices.
>
> **Must have:** Java 17+, Spring Boot 3.x, RESTful APIs, event-driven
> microservices, Kafka, PostgreSQL, Kubernetes, CI/CD, observability
> (Prometheus/Grafana)
>
> **Nice to have:** DDD, AWS/Azure, travel/marketplace/high-transaction experience

After presenting the profile, the interviewer begins the session immediately. You just answer as yourself.

```
I want to do a mock interview with a hiring manager for an AWS Solutions Architect role.
Create a fictional job profile for a healthcare SaaS company.
```

```
Start a hiring manager mock interview. The role is Lead DevOps Engineer
at a Series B startup building a developer tools platform. Make up the details.
```

**Full simulation (uninterrupted conversation, debrief after):**

```
Run a full simulation for a Senior Infrastructure Engineer screening.
Invent a realistic job profile at a large e-commerce company.
```

### Voice Simulation (for Claude App)

**Generate a voice-mode prompt:**

```
/voice-export output/sample-cv-cloud-engineer.md https://example.com/jobs/cloud-engineer
```

After practising in the Claude App, paste the transcript back and debrief:

```
/debrief output/sample-cv-cloud-engineer.md
```

### Other Features

**Import your own CV (can run multiple times, data merges):**

```
/import-cv path/to/your-cv.pdf
```

**Discover your professional identity:**

```
/extract-identity
```

**Scan a job portal for matching roles:**

```
/scan-jobs upwork.com kubernetes devops
```

## Tips

- **No job ad? No problem.** You can always ask the model to invent a fictional job profile. Just describe the role, seniority, industry, and any specifics you want to practise against.
- **Mix and match.** Combine a real CV with a fictional job, or a fictional job with specific constraints ("make the recruiter skeptical about freelancer gaps").
- **Plugins change the vibe.** Drop a plugin into `plugins/` to modify interview tone, add industry-specific questions, or adjust coaching style. See `examples/plugins/` for a working example.

## How to remove

When you're ready to use your own data, delete the example files:

```bash
rm -rf data/projects/*
rm -f data/profile.md data/skills.md data/certifications.md data/education.md data/companies.md data/project-index.md data/professional-identity.md
rm -rf output/*
```

Then run `/import-cv path/to/your-cv.pdf` -- one command turns your CV into the same structured data files.
