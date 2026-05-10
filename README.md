# Job Scraper & Aggregator

A scalable Python-based job scraping and aggregation system built using Playwright, FastAPI, PostgreSQL, and async Python.

The goal of this project is to automate job discovery across multiple job portals and company career pages so that users no longer need to manually search for jobs every day.

This project is being built as both:

- a real-world engineering project
- a hands-on Python learning project

---

# Project Goals

The system should allow users to:

- Search jobs based on:

  - years of experience
  - location
  - skills/keywords
  - remote/hybrid/on-site preference
  - company preferences
  - salary range (future)

- Scrape jobs from multiple sources

- Normalize job data into a common structure

- Remove duplicate jobs

- Store jobs in PostgreSQL

- Expose APIs to query/filter jobs

- Rank jobs based on relevance

- Eventually send alerts and notifications

---

# Why This Project Exists

Searching for jobs manually across multiple portals is:

- repetitive
- time-consuming
- inefficient

Most job portals:

- contain duplicate listings
- have poor filtering
- hide relevant jobs behind noise

This project aims to solve that by building a centralized job aggregation system.

---

# Important Engineering Philosophy

This is NOT intended to be:

- a quick script
- a one-file scraper
- a tutorial-level toy project

The architecture is intentionally designed to be:

- modular
- extensible
- scalable
- maintainable

The project will start small but should support future expansion without major rewrites.

---

# Core Features

## Phase 1 Features

- Scrape jobs from:

  - Greenhouse
  - Lever
  - Wellfound

- Store jobs in PostgreSQL

- Basic filtering:

  - location
  - experience
  - keywords

- Deduplication

- FastAPI backend

---

## Phase 2 Features

- Scheduled scraping jobs

- Additional portals:

  - LinkedIn
  - Naukri
  - Indeed

- Search APIs

- Job ranking/scoring

- User saved searches

---

## Phase 3 Features

- Notifications:

  - Email
  - Telegram
  - WhatsApp

- AI-powered ranking

- Resume matching

- Dashboard/UI

---

## Phase 4 Features

- Auto-apply system

- Resume customization

- AI-generated cover letters

- Advanced anti-bot handling

---

# Tech Stack

## Backend Framework

### FastAPI

Used for:

- REST APIs
- async backend support
- request validation
- API documentation

Why FastAPI?

- async-native
- modern typing support
- high performance
- clean architecture

---

## Scraping Framework

### Playwright

Used for:

- browser automation
- handling JavaScript-heavy websites
- interacting with dynamic pages

Why Playwright?

- modern browser automation
- more reliable than Selenium
- better async support
- supports Chromium, Firefox, WebKit

---

## Database

### PostgreSQL

Used for:

- job storage
- deduplication
- filtering
- indexing

Why PostgreSQL?

- reliable
- scalable
- strong querying capabilities

---

## ORM

### SQLAlchemy

Used for:

- database models
- query abstraction
- migrations support

---

## Validation

### Pydantic

Used for:

- request validation
- response validation
- data normalization

---

## Environment Management

### python-dotenv

Used for:

- managing environment variables

---

# High-Level Architecture

```text
                +-------------------+
                |   User/API Client |
                +-------------------+
                          |
                          v
                +-------------------+
                |     FastAPI API   |
                +-------------------+
                          |
                          v
                +-------------------+
                |   Scraper Engine  |
                +-------------------+
                    |     |      |
                    v     v      v
               Greenhouse Lever Wellfound
                    |
                    v
                +-------------------+
                |  Data Normalizer  |
                +-------------------+
                          |
                          v
                +-------------------+
                | Deduplication     |
                +-------------------+
                          |
                          v
                +-------------------+
                | PostgreSQL DB     |
                +-------------------+
```

---

# Folder Structure

```text
job_scraper/
│
├── app/
│   │
│   ├── api/
│   │   ├── routes/
│   │   └── dependencies/
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── constants.py
│   │   └── logger.py
│   │
│   ├── db/
│   │   ├── database.py
│   │   ├── base.py
│   │   └── session.py
│   │
│   ├── models/
│   │   └── job.py
│   │
│   ├── schemas/
│   │   ├── job_schema.py
│   │   └── search_schema.py
│   │
│   ├── scrapers/
│   │   ├── base.py
│   │   ├── greenhouse.py
│   │   ├── lever.py
│   │   └── wellfound.py
│   │
│   ├── services/
│   │   ├── scraper_service.py
│   │   ├── ranking_service.py
│   │   └── dedup_service.py
│   │
│   ├── utils/
│   │   ├── parser.py
│   │   ├── helpers.py
│   │   └── retry.py
│   │
│   └── main.py
│
├── alembic/
│
├── tests/
│
├── requirements.txt
│
├── .env
│
├── .gitignore
│
├── docker-compose.yml
│
└── README.md
```

---

# Scraper Design Philosophy

Every scraper should implement a common interface.

Example:

```python
class BaseScraper:

    async def scrape_jobs(self, query):
        raise NotImplementedError
```

This ensures:

- consistency
- easier maintenance
- easier scaling
- plug-and-play scraper architecture

---

# Data Normalization

Different job portals structure data differently.

Examples:

- "2-4 years"
- "3+ years"
- "Junior Engineer"

The system will normalize all job data into a standard internal format.

Example normalized job object:

```python
{
    "title": "Backend Engineer",
    "company": "Acme",
    "location": "Bangalore",
    "experience": "2-4 years",
    "source": "greenhouse",
    "url": "https://...",
}
```

---

# Deduplication Strategy

Duplicate jobs are extremely common.

The system will deduplicate jobs using:

- company name
- job title
- location
- hash matching

Future improvements may include:

- fuzzy matching
- semantic similarity

---

# Anti-Bot Considerations

Some job portals aggressively block scraping.

Strategies that may be used:

- rotating user agents
- randomized delays
- browser fingerprint masking
- session reuse
- proxy rotation (future)

Important:
This project will NOT initially focus on bypassing advanced anti-bot systems.

The early goal is:

- stable architecture
- reliable scraping
- clean data pipeline

---

# Database Design (Initial)

## jobs table

Fields:

- id
- title
- company
- location
- experience
- source
- url
- description
- salary
- created_at
- updated_at

Indexes will later be added for:

- title
- company
- location
- source

---

# Milestones Breakdown

# Milestone 1 — Environment Setup

Goal:

- Install Python
- Setup virtual environment
- Install dependencies
- Setup Playwright

Deliverables:

- working Playwright browser launch

---

# Milestone 2 — Basic Scraper

Goal:

- Create first scraper
- Scrape basic job listings

Deliverables:

- scrape jobs from one source

---

# Milestone 3 — Database Integration

Goal:

- Store jobs in PostgreSQL

Deliverables:

- jobs persisted in database

---

# Milestone 4 — Multi-Scraper Architecture

Goal:

- Support multiple sources

Deliverables:

- standardized scraper interface

---

# Milestone 5 — FastAPI Backend

Goal:

- Expose APIs

Deliverables:

- search/filter endpoints

---

# Milestone 6 — Deduplication

Goal:

- remove duplicate jobs

Deliverables:

- unique jobs only

---

# Milestone 7 — Scheduler

Goal:

- automate scraping

Deliverables:

- recurring scraping jobs

---

# Milestone 8 — Ranking System

Goal:

- prioritize relevant jobs

Deliverables:

- scoring engine

---

# Milestone 9 — Notifications

Goal:

- send job alerts

Deliverables:

- email/telegram integration

---

# Milestone 10 — Advanced Features

Goal:

- AI-powered enhancements

Potential Features:

- resume matching
- auto-apply
- AI ranking
- cover letter generation

---

# Future Improvements

Possible future additions:

- Dockerization
- Kubernetes deployment
- distributed scraping workers
- Redis queues
- Celery task queues
- monitoring/logging
- analytics dashboard

---

# Important Lessons Expected From This Project

This project is intentionally designed to teach:

- Python
- async programming
- browser automation
- scraping architecture
- API development
- database modeling
- clean backend architecture
- production thinking

---

# Warning About Scope Creep

This project can grow endlessly.

The initial focus should remain:

1. reliable scraping
2. clean architecture
3. useful job aggregation

Do NOT prematurely optimize:

- distributed systems
- microservices
- AI integrations
- infrastructure complexity

before the core product works reliably.

---

# Initial Development Priority

Priority order:

1. Playwright setup
2. First scraper
3. Database integration
4. Multi-source support
5. API layer
6. Scheduling
7. Ranking
8. Notifications

Everything else is secondary.

---

# Author

Personal learning + productivity project focused on:

- reducing job search friction
- learning Python deeply
- building production-grade scraping systems
