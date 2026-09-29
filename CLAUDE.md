# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Mads Nibe Larsen's personal/research website, served at **madsnibe.com** (see `CNAME`) via GitHub Pages. It is a fork of the **Minimal Mistakes** Jekyll theme (v4.24.0) with the theme source vendored directly into the repo — there is no `remote_theme`, so theme customisations are made by editing `_includes/`, `_layouts/` and `_sass/` in place.

Upstream-theme leftovers that are not part of the site: `README.md`, `CHANGELOG.md`, `docs/`, `test/`, `screenshot*.png`, `staticman.yml`, and `.github/` (including the `bad-pr.yml` workflow). `docs/` and `test/` are excluded from the build in `_config.yml`.

## Commands

```bash
bundle exec jekyll serve        # local preview at http://localhost:4000 (auto-rebuilds)
bundle exec jekyll build        # one-off build into _site/ (~2 s)
npm run build:js                # only needed after editing assets/js/_main.js or plugins; regenerates the committed assets/js/main.min.js
```

There are no tests or linters for the site itself. Verifying a change means building it and checking the output page. The build prints a wall of Sass `percentage()` / slash-division deprecation warnings from the vendored susy/breakpoint libraries — these are expected and harmless.

## Deployment

GitHub Pages builds directly from `master`; there is no CI build step. **Pushing to `master` publishes to the live site.** `_site/` is gitignored and any local copy is stale build output.

## Content architecture

Permalinks are `/:categories/:title/`, and Jekyll assigns a category automatically from any directory that contains a `_posts/` folder. That drives the site's structure:

| Source | Category | URL | Listed on |
| --- | --- | --- | --- |
| `HSTI/_posts/*.md` | `HSTI` | `/HSTI/<slug>/` | `/HSTI/` (`_pages/HSTI.md` loops `site.categories.HSTI`) |
| `_posts/*.md` | none | `/<slug>/` | only `/blogs/` |
| `Photography/_posts/` | `Photography` | — | empty; `/photography/` is hidden from nav |
| `_publications/*.md` | collection | `/publication/<name>` (set per file) | `/publications/` (`site.publications reversed`) |

`/blogs/` ("All posts") loops `site.posts`, so it includes HSTI posts too. Top-nav links live in `_data/navigation.yml`; standalone pages (`about`, `cv`, `posters`, `HSTI_viewer`, …) live in `_pages/` with explicit `permalink`s.

Post defaults (layout `single`, author profile, read time, share, related) come from `defaults` in `_config.yml`; posts additionally set `layout: single` and usually `classes: wide` in front matter. `excerpt_separator` is a blank line, so the **first paragraph** of a post is the teaser shown on archive pages.

### HSTI posts (the bulk of the content)

- Filename `YYYY-MM-DD-Title_with_underscores.md`; front matter is just `layout`, `classes: wide`, `title`, `date`.
- Figures go in `HSTI/images/<topic>/` and are embedded as raw HTML with absolute paths, following the existing pattern:
  ```html
  <center><img src="/HSTI/images/<topic>/file.png" alt="..." width="60%" height="60%">
  <figcaption><b>Fig 1:</b> Caption</figcaption></center>
  ```
- Math is rendered by MathJax 2.7 (configured in `_includes/scripts.html`): inline `$...$` or `\(...\)`, display `$$...$$`. Markdown is kramdown in GFM mode.

### Publications

Front matter fields read by the templates: `title`, `collection: publications`, `permalink`, `excerpt`, `date`, `venue`, `pubtype`, `paperurl`, `citation`. `pubtype: 'thesis'` switches the archive entry to a graduation-cap icon and "Ph.D. thesis, <venue>" wording; any other value (currently `'journal'`) renders as a journal article. This logic lives in `_includes/archive-single.html` (styled by `.pub-type-icon` in `_sass/minimal-mistakes/_archive.scss`).

### Posters, CV and other files

`_pages/posters.md` and `_pages/cv.md` are hand-written: a JPG/PNG preview in `assets/images/` links to the PDF in `assets/other_files/`.

## Large files

The repo is already large (`.git` ≈ 720 MB, `HSTI/images/` ≈ 145 MB) and every binary is committed directly. GitHub rejects files over 100 MB and warns above 50 MB, so compress PDFs and images before adding them (the thesis is committed as `nibe_thesis_reduced_size.pdf` for this reason).
