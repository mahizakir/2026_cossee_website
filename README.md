# COSSEE Website

This repository contains the Hugo-based website for COSSEE: Collaboration for Open Science and Synthesis in Ecology and Evolution.

## Stack

- [Hugo](https://gohugo.io/)
- theme: `hugo-universal-theme`
- content managed mostly through Markdown, JSON data files, and Hugo layouts

## Repository Structure

- `content/`: site pages and blog posts
- `data/`: structured data used by pages such as People and homepage sections
- `assets/`: supporting source files used by layouts, including People profile detail snippets
- `layouts/`: local Hugo templates and partial overrides
- `static/`: static files served directly, including images and `web_files`
- `docs/`: contributor-facing notes such as the blog submission guide and publishing checklist
- `archetypes/`: starter templates for new content

## Local Development

Run the site locally:

```bash
hugo server -s "/Users/mahizakir/VS code files are here/COSSEE/cossee_website_hugo_theme/cossee_website"
```

Build the site:

```bash
hugo -s "/Users/mahizakir/VS code files are here/COSSEE/cossee_website_hugo_theme/cossee_website" --gc --minify --cacheDir /tmp/hugo_cache
```

## Key Content Workflows

### People Page

The People page is data-driven.

Main files:

- `data/people/members.json`: member cards and metadata
- `data/people/page.json`: page-level settings such as filters and group photo
- `assets/people/details/current/`: full modal content for current members
- `assets/people/details/past/`: full modal content for past members
- `layouts/page/people.html`: page template

### Blog Posts

New blog posts can be written entirely in Markdown.

Recommended workflow:

1. Create a page bundle:
   `hugo new blog/my-post/index.md`
2. Write the post in Markdown.
3. Place `cover.jpg` in the same folder.
4. Set `draft = false` when the post is ready to go live.

Useful files:

- `archetypes/blog.md`
- `docs/blog-submission-guide.md`
- `docs/blog-publishing-checklist.md`

## Theme Note

The site currently uses `themes/hugo-universal-theme` as a git submodule.

## Git Remote

Current GitHub remote:

```bash
git@github.com:mahizakir/2026_cossee_website.git
```
