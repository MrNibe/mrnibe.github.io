# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Mads Nibe Larsen's personal/research website, served at **madsnibe.com** (see `CNAME`) via GitHub Pages. It is a fork of the **Minimal Mistakes** Jekyll theme (v4.24.0) with the theme source vendored directly into the repo — there is no `remote_theme`, so theme customisations are made by editing `_includes/`, `_layouts/` and `_sass/` in place.

The color scheme is a custom `nibe` skin, a light version of the CV's palette (yellow `#fdcb36`, charcoal `#2c2d30`, paper `#f8f7f7`). Colors are set as variables in `_sass/minimal-mistakes/skins/_nibe.scss`; rules the variables can't reach (yellow masthead, link underlines, buttons, footer) are in `_sass/_nibe-theme.scss`, imported after the theme in `assets/css/main.scss`. Yellow has too little contrast to be used as text on the light background, so it only appears as fills, underlines and markers. Beyond colour, the site copies the CV's grammar: Antonio capitals for titles and labels, section headings with an ink rule running out to the right (`nibe-section-heading` mixin), a ruled timeline with yellow nodes ringed in charcoal for list entries, muted italic venues, a yellow identity block (masthead, author sidebar) and a charcoal closing band (footer). No drop shadows: figures and posters sit on hairline rings. `_sass/_nibe-theme.scss` must stay libsass-compatible because GitHub Pages compiles with sassc (no Sass modules, no CSS `min()`/`max()`; `clamp()` is fine). Visual decisions are recorded in `DESIGN.md`, product context in `PRODUCT.md`. Typography also follows the CV: Antonio (headings, navigation, entry titles) and Alegreya (everything else), self-hosted as variable woff2 files in `assets/fonts/` with their OFL licenses rather than loaded from Google Fonts, which would send visitors' IP addresses to Google.

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

The homepage (`index.md`) uses `_layouts/landing.html`: the "assembly" hero, where `assets/js/assembly.js` scrubs a canvas through `assets/images/fpi/frame-00…29.webp` (frames of `HSTI/images/fpi_animation/fpi_assembly.mp4` keyed to alpha) as the visitor scrolls, then the four latest publications and the posters. Lab notes are deliberately left off the homepage. With reduced motion or no JavaScript it shows frame 00 as a still. If the frame count changes, update `frame_count` in the layout.

`/blogs/` ("All posts") loops `site.posts`, so it includes HSTI posts too. Top-nav links live in `_data/navigation.yml`; standalone pages (`about`, `cv`, `posters`, `HSTI_viewer`, …) live in `_pages/` with explicit `permalink`s.

Post defaults (layout `single`, author profile, read time, share, related) come from `defaults` in `_config.yml`; posts additionally set `layout: single` and usually `classes: wide` in front matter. `excerpt_separator` is a blank line, so the **first paragraph** of a post is the teaser shown on archive pages.

### HSTI posts (the bulk of the content)

- Filename `YYYY-MM-DD-Title_with_underscores.md`; front matter is `layout`, `classes: wide`, `title`, `date`, and optionally `thumb`.
- `thumb: /HSTI/images/thumbs/<post filename>.webp` is the figure shown beside the post on `/HSTI/` and in related posts: one representative figure, white margins trimmed, fitted to 720×540, WebP. Posts without a figure simply omit it.
- The first paragraph is the list excerpt (clamped to three lines); if the post opens with an image, video or heading, the list shows no excerpt, so start posts with a sentence.
- Figures go in `HSTI/images/<topic>/` and are embedded as raw HTML with absolute paths, following the existing pattern:
  ```html
  <center><img src="/HSTI/images/<topic>/file.png" alt="..." width="60%" height="60%">
  <figcaption><b>Fig 1:</b> Caption</figcaption></center>
  ```
- Math is rendered by MathJax 2.7 (configured in `_includes/scripts.html`): inline `$...$` or `\(...\)`, display `$$...$$`. Markdown is kramdown in GFM mode.

### Publications

Front matter fields read by the templates: `title`, `collection: publications`, `permalink`, `excerpt`, `date`, `venue`, `pubtype`, `paperurl`, `citation`. `pubtype` sets the label on the entry: `'thesis'` gives "Ph.D. thesis" and a "Read the thesis" link, `'conference'` gives "Conference paper", and any other value (normally `'journal'`) gives "Journal article". The list entry (`_includes/archive-single.html`) shows the title, year, label and venue, the excerpt, links to the paper and the abstract page, and the citation in a collapsed `<details>`. The publication page (`_layouts/single.html`) shows the same label and venue under the title, and the paper button and citation after the abstract.

### Posters, CV and other files

`_pages/posters.md` and `_pages/cv.md` are hand-written. Posters use 900px WebP previews in `assets/images/posters/` (made from the full JPGs in `assets/images/`) in a `.poster-grid`, each linking to its PDF in `assets/other_files/`; the homepage poster strip uses the same previews. The CV page shows `assets/images/MadsNibeCV.png` with a download button for the PDF.

## Large files

The repo is already large (`.git` ≈ 720 MB, `HSTI/images/` ≈ 145 MB) and every binary is committed directly. GitHub rejects files over 100 MB and warns above 50 MB, so compress PDFs and images before adding them (the thesis is committed as `nibe_thesis_reduced_size.pdf` for this reason).
