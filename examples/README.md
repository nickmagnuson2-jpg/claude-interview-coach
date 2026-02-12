# Example Data — Alex Chen (Fictional)

This directory contains a complete, fictional freelancer profile so you can try the framework's features before importing your own data.

**Alex Chen** is a fictional freelance DevOps/Cloud consultant based in Berlin, with 8 years of experience across AWS and Azure, specialising in Kubernetes and infrastructure automation.

## How to use

Copy the example data into the repo's working directories:

```bash
cp -r examples/data/* data/
cp -r examples/output/* output/
```

Then try the features:

- **Review the sample CV:** `/review-cv output/sample-cv-cloud-engineer.md`
- **Deep review:** `/review-cv-deep output/sample-cv-cloud-engineer.md`
- **Practice a screening:** `I want to practice a recruiter screening for a Senior Cloud Engineer role`
- **Generate a voice simulation:** `/voice-export output/sample-cv-cloud-engineer.md https://example.com/job-ad`

## How to remove

When you're ready to use your own data, delete the example files:

```bash
rm -rf data/projects/*
rm -f data/profile.md data/skills.md data/certifications.md data/education.md data/companies.md data/project-index.md data/professional-identity.md
rm -rf output/*
```

Then run `/import-cv path/to/your-cv.pdf` — one command turns your CV into the same structured data files.
