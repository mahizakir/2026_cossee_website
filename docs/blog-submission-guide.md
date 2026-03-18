# Blog Submission Guide

This site supports blog posts written entirely in Markdown. Contributors do not need to edit HTML.

## Fastest Workflow

1. Create a new blog post as a page bundle:
   `hugo new blog/my-post/index.md`
2. Open the new `index.md` file.
3. Fill in the front matter at the top.
4. Write the post content in Markdown.
5. Put the cover image in the same folder and name it `cover.jpg` or `cover.png`.
6. Put any extra images in the same folder and reference them with normal Markdown image syntax.

## Recommended Front Matter

```toml
+++
title = "Your Post Title"
date = 2026-03-18
draft = true
author = "Your Name"
summary = "A short summary for the blog collection page."
cover_image = "cover.jpg"
tags = ["open science", "meta-analysis"]
+++
```

## Notes

- `author` is fine for one author.
- `authors = ["Name One", "Name Two"]` also works for multi-author posts.
- `cover_image` is optional if the post folder already contains a file named `cover.jpg`, `cover.png`, `banner.jpg`, or similar.
- Existing older posts can continue using `banner`; the blog templates now support both styles.
- Regular Markdown features like headings, lists, links, blockquotes, and images all work normally.

## Example Folder Layout

```text
content/
  blog/
    my-post/
      index.md
      cover.jpg
      figure-1.png
      figure-2.png
```

## Example Image Use

```md
![Figure caption](figure-1.png)
```
