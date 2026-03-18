# Blog Publishing Checklist

Use this checklist when you want to publish a blog post on the COSSEE website.

## 1. Put the post in the right place

Recommended structure:

```text
content/blog/my-post/
  index.md
  cover.jpg
  figure-1.png
```

## 2. Check the front matter

Make sure the top of the Markdown file includes:

```toml
+++
title = "Your Post Title"
date = 2026-03-18
draft = false
author = "Your Name"
summary = "A short summary for the blog page."
cover_image = "cover.jpg"
tags = ["open science"]
+++
```

Notes:

- Use `draft = false` when you want the post to go live.
- Use `author` for one author.
- Use `authors = ["Name One", "Name Two"]` for multiple authors.

## 3. Add the cover image

If you are using a page bundle, place `cover.jpg` or `cover.png` in the same folder as `index.md`.

## 4. Write in Markdown

You can use:

- headings
- paragraphs
- bullet lists
- numbered lists
- links
- images

Example image:

```md
![Figure caption](figure-1.png)
```

## 5. Rebuild the site

```bash
hugo -s "/Users/mahizakir/VS code files are here/COSSEE/cossee_website_hugo_theme/cossee_website" --gc --minify --cacheDir /tmp/hugo_cache
```

## 6. Check the result

Make sure:

- the post appears on `/blog/`
- the title looks right
- the summary looks right
- the cover image shows up
- the post opens correctly
- inline images load correctly

## 7. If something is missing

- no post showing up: check `draft = false`
- no cover image: check the filename and folder location
- no author showing up: check `author` or `authors`
- broken images: make sure the image files are in the same folder as the post

For a fuller explanation, see:

- [blog-submission-guide.md](/Users/mahizakir/VS%20code%20files%20are%20here/COSSEE/cossee_website_hugo_theme/cossee_website/docs/blog-submission-guide.md)
