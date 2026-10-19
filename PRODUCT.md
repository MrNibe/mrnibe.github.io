# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

- **Industry / employers:** recruiters, hiring managers and potential partners checking Mads Nibe Larsen's profile, skills and track record. They skim: who is this, what can he do, where is the proof.
- **Research peers:** spectroscopy and infrared-imaging researchers looking for his papers, methods, results and contact details.

## Product Purpose

The personal research website of Mads Nibe Larsen (madsnibe.com): Research Scientist at Newtec Engineering A/S with a PhD in long-wave infrared (LWIR) hyperspectral imaging. It presents who he is, his publications and posters, his CV, and a long-running series of technical working notes on the hyperspectral thermal camera (HSTI). Success is a visitor leaving with a clear sense of his expertise and an easy path to his papers, CV or contact.

## Positioning

He built the instrument: a low-cost LWIR hyperspectral imager made by putting a scanning Fabry-Pérot interferometer in front of an uncooled microbolometer thermal camera, and worked the whole chain from optics and experiments through physical modelling and inverse problems to the processing software. The HSTI notes are first-hand evidence of that work that no generic profile can copy.

## Operating Context

- Static Jekyll site on GitHub Pages, built from `master`; the vendored Minimal Mistakes theme is edited in place.
- Content is mostly Markdown: 20 HSTI posts with raw-HTML figures and MathJax maths, 8 publications, 3 posters, a CV image linking to the PDF, a Python/Tkinter viewer write-up.
- Visitors arrive from CV/LinkedIn links, paper bylines and search.

## Capabilities and Constraints

- No build step beyond GitHub Pages' own Jekyll; no CI, no Node at deploy time (`assets/js/main.min.js` is committed).
- Fonts are self-hosted; no third-party font or tracking requests (visitor privacy).
- Repo is already very large; new images must be compressed before committing.
- Posts embed figures with absolute paths and inline widths; changes must not break existing post markup.

## Brand Commitments

- Identity follows his CV (`assets/other_files/MadsNibeCV.pdf`): yellow `#fdcb36`, charcoal `#2c2d30`, paper `#f8f7f7`; Antonio for headings/navigation, Alegreya for text. Confirmed by the owner to be kept and elevated, not replaced (2026-10-19).
- Yellow is never used as text on light backgrounds (insufficient contrast); it appears as fills, underlines and markers.

## Evidence on Hand

- Publications: `_publications/` (8 entries, 2021–2026, incl. PhD thesis 2025).
- Posters: `assets/images/*poster*.jpg` with PDFs in `assets/other_files/` (DFS 2022 poster won the EPJ prize for best experimental poster).
- Research imagery: `HSTI/images/` (flame, gemstone, plastics and other hyperspectral figures), `assets/images/hsti_viewer/`.
- Profile photo `assets/images/profile_pic.jpg`; CV PNG/PDF.
- No testimonials, client lists or metrics exist; do not invent any.

## Product Principles

1. Show the work, not adjectives: real figures, papers and results carry credibility.
2. Fast to the proof: an employer finds role, expertise, CV and contact within seconds; a peer finds papers in one click.
3. One identity everywhere: the CV and the site should feel like the same person's documents.
4. The working notes stay readable: maths, figures and long technical posts come first in post layouts.

## Accessibility & Inclusion

WCAG AA contrast for text; respect reduced-motion preferences; keyboard-reachable navigation.
