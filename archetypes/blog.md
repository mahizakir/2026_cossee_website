+++
title = "Post Title"
date = {{ .Date }}
draft = true
author = "Your Name"
summary = "Write a short 1-2 sentence summary for the blog card."
cover_image = "cover.jpg"
tags = ["open science"]
+++

Write your post in Markdown here.

## Suggested Structure

Start with a short opening paragraph that explains what the post is about and why it matters.

## Main Section

Use normal Markdown headings, paragraphs, lists, and links.

- bullet points are fine
- numbered steps are fine
- no HTML is required

## Adding Images

If you create the post as a page bundle, you can place images in the same folder as `index.md`.

Example:

- `content/blog/my-new-post/index.md`
- `content/blog/my-new-post/cover.jpg`
- `content/blog/my-new-post/figure-1.png`

Then you can use:

```md
![Short caption](figure-1.png)
```
