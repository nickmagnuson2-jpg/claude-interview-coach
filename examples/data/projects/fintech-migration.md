# Cloud Architect — AWS to Azure Migration

- **Period:** 03/2024 – 12/2024
- **Role:** Cloud Architect, Migration Lead
- **Client:** NordPay GmbH
- **Industry:** FinTech / Payments
- **Location:** Germany (DE)
- **Type:** consulting

## Description

Led the cloud migration of a payment processing platform from AWS to Azure, driven by regulatory requirements for EU data residency and the client's strategic shift to Microsoft-centric infrastructure. The platform processed 2M+ transactions daily with strict latency SLAs (<200ms p99).

## Responsibilities

- Designed target Azure architecture (AKS, Azure SQL, Service Bus, Key Vault)
- Created migration runbooks for 12 microservices with zero-downtime cutover strategy
- Built Terraform modules for the entire Azure landing zone
- Established CI/CD pipelines in Azure DevOps (migrated from GitHub Actions)
- Implemented blue-green deployment strategy for the cutover weekend
- Coordinated with payment processor partners on DNS and certificate changes
- Designed observability stack migration (Datadog → Azure Monitor + Grafana)

## Key Achievements

- Zero-downtime migration completed 2 weeks ahead of schedule
- Reduced infrastructure costs by 22% through reserved instances and right-sizing
- Cut deployment time from 35 minutes to 12 minutes with new pipeline architecture
- Passed PCI DSS re-certification on first attempt post-migration

## Technologies

Azure (AKS, SQL Database, Service Bus, Key Vault, Monitor, DevOps), Terraform, Kubernetes, Helm, Docker, Go, PostgreSQL, Grafana, Prometheus

## Tags

azure, aws, migration, fintech, payments, kubernetes, terraform, architecture, pci-dss, zero-downtime
