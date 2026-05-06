+++
title = "Checklist Automator"
date = 2026-05-06
draft = false
weight = 2
summary = "Pick a reporting standard, upload a manuscript and supplements, and get back a fully cited compliance checklist with verbatim quotes and downloadable reports."
project_code = "CHECKLIST AUTOMATOR"
subtitle = "Evidence-grounded reporting audits"
status = "Live tool"
lead = "COSSEE"
audience = "Authors, reviewers, and editors of systematic reviews and meta-analyses"
location = "Web app"
timing = "On demand"
commitment = "Upload a PDF, get a checklist back"
external_url = "https://prismatic.cossee.org/"
hero_image = "checklist-automator-logo.svg"
hero_image_fit = "contain"
highlights = [
  { label = "What it does", value = "Fills reporting checklists with verbatim, page-cited evidence from a manuscript" },
  { label = "Standards supported", value = "PRISMA 2020 today; MATES 2026 and others coming next" },
  { label = "How it works", value = "Hybrid retrieval (BM25 + dense embeddings) with grounded-quote extraction and rubric verification" },
  { label = "Inputs", value = "Main PDF, optional supplements, and an optional analysis code repository" },
  { label = "Outputs", value = "JSON, Markdown report, CSV, XLSX, and DOCX exports" },
]
+++

Checklist Automator is COSSEE's evidence-grounded reporting audit tool for research manuscripts. Pick a reporting standard, upload a manuscript and any supplements, and get back a fully cited compliance checklist with verbatim quotes, page-level citations, and downloadable reports.

It supports PRISMA 2020 today (the 27-item systematic-review reporting standard) and is built to be pluggable: MATES 2026 is coming next, and new standards can be added as siblings under the checklists module without changing the pipeline.

Visit [prismatic.cossee.org](https://prismatic.cossee.org/) to upload a paper and run the pipeline.
