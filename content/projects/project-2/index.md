+++
title = "Prismatic"
date = 2026-04-27
draft = false
weight = 2
summary = "Prismatic is an evidence-based PRISMA 2020 assistant that ingests papers and code, retrieves per-checklist-item evidence, and fills the 27-item checklist with grounded quotes."
project_code = "PRISMATIC"
subtitle = "Automated PRISMA 2020 checklist filler for researchers"
status = "Live tool"
lead = "COSSEE"
audience = "Authors, reviewers, and editors of systematic reviews"
location = "Web app"
timing = "On demand"
commitment = "Upload a PDF, get a checklist back"
external_url = "https://prismatic.cossee.org/"
hero_image = "prismatic-logo.png"
highlights = [
  { label = "What it does", value = "Fills the 27-item PRISMA 2020 checklist from a paper PDF" },
  { label = "How it works", value = "Hybrid retrieval (BM25 + dense) with grounded-quote extraction and verification" },
  { label = "Inputs", value = "Main PDF, optional supplements, and an optional analysis code repository" },
  { label = "Outputs", value = "Strict JSON, Markdown report, CSV, XLSX, and DOCX exports" },
]
+++

Prismatic is COSSEE's automated PRISMA 2020 checklist assistant. It ingests a systematic review's PDF (plus any supplements and analysis code), retrieves the most relevant passages for each of the 27 PRISMA items, and extracts answers with grounded quotes that are then verified by rules and rubrics.

Visit [prismatic.cossee.org](https://prismatic.cossee.org/) to upload a paper and run the pipeline.
