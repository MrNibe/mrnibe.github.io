---
name: Mads Nibe Larsen
description: Research site of an infrared-imaging scientist, set in the grammar of his CV.
colors:
  signal-yellow: "#fdcb36"
  pale-yellow: "#feedb9"
  charcoal: "#2c2d30"
  paper: "#f8f7f7"
  ink: "#231f20"
  graphite-muted: "#6d6e71"
  hairline: "#dcdad8"
  border: "#e3e1e0"
  code-ground: "#efeeed"
  mount-white: "#ffffff"
typography:
  display:
    fontFamily: "Antonio, Arial Narrow, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(3.2rem, 7.4vw, 8.6rem)"
    fontWeight: 400
    lineHeight: 0.88
    letterSpacing: "0.035em"
  headline:
    fontFamily: "Antonio, Arial Narrow, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(1.9rem, 3.4vw, 2.6rem)"
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: "0.05em"
  title:
    fontFamily: "Antonio, Arial Narrow, Helvetica Neue, Arial, sans-serif"
    fontSize: "1.2em"
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: "0.03em"
  body:
    fontFamily: "Alegreya, Georgia, Times, serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.5
    fontFeature: "\"onum\", \"pnum\""
  caption:
    fontFamily: "Alegreya, Georgia, Times, serif"
    fontSize: "0.85em"
    fontWeight: 400
    lineHeight: 1.45
  label:
    fontFamily: "Antonio, Arial Narrow, Helvetica Neue, Arial, sans-serif"
    fontSize: "0.85rem"
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: "0.08em"
rounded:
  none: "0"
  node: "50%"
spacing:
  rule: "2px"
  node: "0.85rem"
  gutter: "clamp(1rem, 4vw, 4rem)"
  section: "clamp(3.5rem, 8vw, 7rem)"
  entry: "2.4em"
components:
  button-primary:
    backgroundColor: "{colors.signal-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "0.85em 1.5em"
  button-primary-hover:
    backgroundColor: "{colors.charcoal}"
    textColor: "{colors.signal-yellow}"
  button-outline:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "0.85em 1.5em"
  button-outline-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
  masthead:
    backgroundColor: "{colors.signal-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
  author-block:
    backgroundColor: "{colors.signal-yellow}"
    textColor: "{colors.ink}"
    padding: "1.6rem 1.2rem 1.4rem"
  timeline-node:
    backgroundColor: "{colors.signal-yellow}"
    rounded: "{rounded.node}"
    size: "{spacing.node}"
  figure-mount:
    backgroundColor: "{colors.mount-white}"
    rounded: "{rounded.none}"
    padding: "0.5rem"
  footer-band:
    backgroundColor: "{colors.charcoal}"
    textColor: "{colors.paper}"
    padding: "3.5rem 0 2.5rem"
---

# Design System: Mads Nibe Larsen

## Overview

**Creative North Star: "The CV, Extended"**

Every page reads as another sheet of the owner's CV. A paper ground carries ink type; Antonio capitals announce sections and entries, Alegreya carries everything a person reads at length. Sections open with a capital heading whose ink rule runs out to the right edge; lists hang from a ruled line with yellow nodes ringed in charcoal, the CV's timeline. Identity is a yellow block (the masthead, the author sidebar); the page closes on a charcoal band. The site should feel like the same person's documents, not a theme with his colors.

The system is flat and typographic. Depth comes from rules, fills and white figure mounts, never from blurred shadow. Yellow is a material, not a voice: it fills, marks and underlines, and never sets text on a light ground. Real research figures and the instrument render are the imagery; nothing decorative stands in for them.

The homepage carries one signature motion: the scanning Fabry-Pérot interferometer assembles as the visitor scrolls, with the chain of the work lighting along a ruled progress line beneath it. Without script or with reduced motion, the still exploded render and every chain step stay fully visible.

**Key Characteristics:**
- Paper ground, ink type, yellow as fill and marker only, charcoal for the closing band.
- Antonio uppercase for headings, labels, navigation and entry titles; Alegreya for prose, venues and captions.
- Section headings carry a 2px rule running to the right edge.
- Lists are ruled timelines with yellow, charcoal-ringed nodes.
- Square corners everywhere except the round nodes.
- No blurred or drop shadows; ring outlines only.

## Colors

A two-color identity (yellow and charcoal) on warm paper, with near-black ink for text and one graphite grey for everything secondary.

### Primary
- **Signal Yellow** (`signal-yellow`): the identity color. Fills the masthead, the author block, the primary button and timeline nodes; draws link underlines, title hover bars and text selection. Never text on paper or white.
- **Pale Yellow** (`pale-yellow`): a 35% tint of Signal Yellow, used only as the mobile nav-icon hover in the theme.

### Secondary
- **Charcoal** (`charcoal`): the closing band (footer), the ring around every node, the timeline line, the scroll progress bar, the primary-button hover fill and the syntax-highlighting ground.

### Neutral
- **Paper** (`paper`): the page ground everywhere; also the text color on charcoal.
- **Ink** (`ink`): all text and headings, section rules, outline buttons, focus rings, active-nav underline.
- **Graphite Muted** (`graphite-muted`): venues, dates in tiles, captions, meta lines, pager labels, unlit chain steps. Excerpts mix ink and graphite 60/40 for a slightly quieter body.
- **Hairline** (`hairline`): 1px ring around figure mounts and poster sheets, the share-row divider, the resting track of the progress rule.
- **Border** (`border`) and **Code Ground** (`code-ground`): the theme's quiet borders and inline-code fill.
- **Mount White** (`mount-white`): only behind figure thumbnails, so research plots sit on their native white.

### Named Rules
**The Yellow Is Material Rule.** Signal Yellow appears as fill, marker, underline or selection. It never sets text on paper or white (insufficient contrast); on charcoal it may color a hovered footer link.

**The Two Blocks Rule.** Yellow blocks say who (masthead, author sidebar); the charcoal band says goodbye (footer). Do not add a third block color.

## Typography

**Display Font:** Antonio (with Arial Narrow, Helvetica Neue, Arial)
**Body Font:** Alegreya (with Georgia, Times)

**Character:** a condensed grotesque in capitals against a calligraphic book serif, exactly as on the CV. Antonio is always uppercase and tracked; Alegreya is never uppercased. Both are self-hosted variable woff2 files (Latin subset, SIL OFL); no third-party font requests.

### Hierarchy
- **Display** (400, clamp(3.2rem, 7.4vw, 8.6rem), 0.88): the name on the homepage only.
- **Headline** (400, about 1.9–3rem by clamp, 1.1, 0.05em): section headings on archive pages and homepage sections, with the trailing ink rule. In posts, h2 uses the same treatment at 1.45em.
- **Title** (400, 1.2em, 1.2, 0.03em): entry titles in timelines, page titles (clamp(1.9rem, 3.2vw, 2.7rem) at 1.08), pager and tile titles. Balanced wrapping.
- **Body** (400, 1rem, 1.5): prose, set with old-style proportional figures. Root size steps 16 / 15 / 16 / 18px across small, medium, large and x-large because Alegreya's x-height is small. Excerpts and venues hold to 68ch.
- **Caption** (italic 400, 0.85em, 1.45): figcaptions in graphite, centered, max 44em; a leading "Fig n:" label switches to Antonio caps in ink.
- **Label** (400, 0.8–0.95rem, 0.06–0.1em tracking, uppercase): navigation, buttons, meta lines, entry links, dates, "Recommended citation" summaries, footer links.

### Named Rules
**The Capitals Speak, the Serif Reads Rule.** Antonio, uppercase and tracked, for anything that names or navigates; Alegreya for anything read as a sentence. Venues and captions are Alegreya italic in graphite.

**The Lining Dates Rule.** Prose uses old-style figures; entry dates switch to lining tabular figures so years align at the right edge.

## Layout

Minimal Mistakes' grid underlies inner pages: a left author sidebar from 1024px and the content column to its right. Archive and timeline content holds to 56rem; prose and excerpts to 68ch. The homepage breaks out of the theme container: sections run to 84rem with a fluid side gutter (clamp(1rem, 4vw, 4rem)) and generous section tops (clamp(3.5rem, 8vw, 7rem)). The masthead and footer also use that gutter at x-large.

Breakpoints are the theme's: 600px small, 768px medium, 1024px large, 1280px x-large. At medium, lab-note entries with a figure become a two-column grid (text, 11rem thumbnail); the footer splits 1.2fr / 1fr. At large, the homepage assembly becomes a 5fr / 7fr split pinned for one extra viewport of scroll, the render bleeding off the right edge. Below 600px, poster strips stack to a single 22rem column.

Grids of figures (related posts, poster grid) use auto-fill columns with a 12rem minimum and 2rem gaps. Entries in a timeline are separated by 2.4em (2em on the homepage).

## Elevation & Depth

The system is flat. There is no blurred shadow anywhere in the Nibe layer; depth is conveyed by fill (yellow and charcoal blocks against paper), by rules (2px ink), and by white mounts ringed with a 1px hairline. `box-shadow` is used only as a crisp zero-blur ring, because it draws an outline without shifting layout.

### Shadow Vocabulary
- **Hairline ring** (`box-shadow: 0 0 0 1px #dcdad8`): figure mounts, poster sheets, the CV sheet at rest.
- **Ink ring** (`box-shadow: 0 0 0 1.5px #231f20`): the same surfaces on hover.
- **Outline button stroke** (`box-shadow: inset 0 0 0 2px #231f20`): the outline button; 1.5px for share buttons.
- **Node ring** (`box-shadow: inset 0 0 0 3px #2c2d30`): timeline and chain nodes; the small meta separator and prize marker use an outer 1.5–2px charcoal ring.

### Named Rules
**The Ring, Not Shadow Rule.** Any edge is a zero-blur ring or a solid rule. A blurred or offset shadow does not belong to this world.

## Shapes

Square by default: buttons, menus, mounts, blocks and sheets have no radius. The only round forms are the CV's markers: 0.85rem timeline nodes, the 0.45em meta separator dots and the prize marker, all yellow ringed in charcoal. Rules are 2px ink (section headings, citation and pager tops, the timeline line in charcoal); hairlines are 1px. The theme's 4px radius survives only in untouched upstream parts.

## Components

### Buttons
Square, capitalised, confident.
- **Shape:** square corners (0).
- **Primary:** Signal Yellow fill, ink Antonio caps at 0.95rem, 0.09em tracking, padding 0.85em 1.5em.
- **Hover / Focus:** primary inverts to charcoal fill with yellow text; outline fills with ink and paper text. Transitions 0.25s on the house ease (cubic-bezier(0.16, 1, 0.3, 1)). Focus is a 2px ink outline offset 3px (yellow on the charcoal footer).
- **Outline:** transparent with a 2px inset ink stroke. Share buttons are the same at 0.8rem with a 1.5px stroke.

### Navigation
- **Masthead:** a slim yellow band, Antonio caps at 0.08em tracking, site title at weight 500 and 0.1em. The current page and hover show a 2px ink underline that scales in from the left (0.35s). The overflow menu is a paper panel with a 2px ink border and yellow hover rows.
- **Pager:** previous/next under a 2px ink top rule; graphite label above an Antonio title that grows a yellow underline bar on hover.

### Links
Ink text with a 0.15em yellow underline offset 0.2em; hover darkens the underline to charcoal. Titles that are links use a growing yellow bar (0.18em) drawn under the text on hover instead.

### Timeline Entry (signature)
The CV's list. A 2px charcoal line runs through all entries; each carries a 0.85rem yellow node with a 3px charcoal ring at its title. Title in Antonio caps left, year at the right in lining figures. Below: venue in graphite Alegreya italic ("Journal article, *Venue*"), an excerpt clamped to 68ch (three lines for lab notes), Antonio entry links with yellow underlines, and a "Recommended citation" disclosure marked with a plus/minus sign. Lab notes with a figure place an 11rem mounted thumbnail beside the text from 768px.

### Figure Mount
White panel, 0.5rem padding, hairline ring, image at 4:3 with `object-fit: contain` so plots are never cropped. Hover changes the ring to ink. Used for lab-note thumbnails and related-post tiles. Post figures (raw `<center><img><figcaption>`) get 2.2em vertical margin and italic graphite captions.

### Author Block
From 1024px the sidebar author card is a yellow block: centered avatar (7.5rem), name in Antonio caps, bio in ink at 0.85rem, then left-aligned contact rows in Antonio caps.

### Footer Band
Charcoal, paper text at 78%. The owner's name is a section heading in paper whose rule is yellow; bio beneath; contact links in Antonio caps turning yellow on hover; a legal line above a 16% paper hairline.

### Assembly Scroll (homepage only)
Name at display size beside the instrument render; a canvas scrubs 30 frames from exploded to assembled as the section scrolls (pinned at 1024px and up, scroll-driven in the stacked layout). Beneath, a hairline track with a charcoal progress bar and four chain steps whose nodes light in sequence; unlit steps sit in graphite with paper nodes. Reduced motion or no script: the still exploded frame and all steps shown lit.

## Do's and Don'ts

### Do:
- **Do** open every section with an Antonio caps heading and a 2px ink rule running to the right edge.
- **Do** set lists of dated work as the ruled timeline with yellow nodes ringed in charcoal.
- **Do** set venues, captions and secondary lines in graphite (#6d6e71) Alegreya italic.
- **Do** mount research figures on white with a 1px hairline ring and never crop them (`object-fit: contain`).
- **Do** keep every transition on cubic-bezier(0.16, 1, 0.3, 1) and turn transitions off under `prefers-reduced-motion`.
- **Do** keep the Sass libsass-compatible: GitHub Pages compiles with sassc, so no Sass modules, no `math.div`, no CSS `min()`/`max()`; `clamp()` is fine.
- **Do** self-host every font; no third-party font or tracking requests.

### Don't:
- **Don't** set yellow text on paper or white.
- **Don't** use blurred or offset drop shadows; edges are rules and zero-blur rings.
- **Don't** round corners on buttons, blocks, mounts or menus; round forms are reserved for nodes and markers.
- **Don't** uppercase Alegreya or set prose in Antonio.
- **Don't** introduce a block color beyond yellow (identity) and charcoal (closing band).
- **Don't** box text entries in filled or bordered cards or icon tiles; text lists hang from the timeline, and only figures sit on mounts.
