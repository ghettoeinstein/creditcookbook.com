# PRD: CreditCookbook.com — Full Site Build

**Swiss Design System / Apple-Caliber Motion / $50K Production Bar**

**Owner:** Caleb Pierre Ventures LLC  
**Status:** Active build brief  
**Last updated:** July 15, 2026

---

> This document is a standing brief for an agentic coding tool (e.g. Claude Code). Treat Section 7 (Definition of Done) as the exit condition and Section 8 (QA Gate) as the loop to iterate against. Don't stop to check in except for genuine blockers (Section 10).

---

## 1. Objective

Build creditcookbook.com to a $50,000-agency production standard: Swiss/International Typographic Style design discipline, Apple-product-page-caliber scroll motion, fast, accessible, and structured around the full site tree already scoped (Home, About, Personal Credit Remedy, Business Credit, Recipes, Tools, Resources/Glossary, Newsletter, Contact).

---

## 2. Design Philosophy: Swiss + Apple

These two references are doing different jobs and shouldn't blur together:

### Swiss Design (International Typographic Style) governs the bones:

- Strict underlying grid (column-based, mathematically consistent gutters/margins)
- Sans-serif type discipline (one grotesk-style typeface family, weight variation over typeface variation)
- Asymmetric but rigorously aligned layouts — nothing centered "because it looks nice," everything on-grid
- Objective, functional imagery — no decorative clutter
- Generous negative space as a design element, not empty space
- Strong left-aligned hierarchy; type sizes follow a modular scale, not arbitrary jumps

### Apple governs the motion and interaction layer, not the grid:

- Scroll-driven storytelling — content reveals as you scroll, each section earns its moment
- Restraint: motion clarifies (draws the eye to what matters next), never decorates for its own sake
- Physically plausible easing (no linear, no bounce/elastic default — custom cubic-bezier per Apple's actual feel)
- Parallax depth used sparingly and purposefully, not on every element

### Where gold fits:

Gold is the one deliberate break from strict Swiss neutrality — used only as an accent for emphasis (CTAs, key numbers/stats, dividers, hover states), never as a base color, never covering more than ~10% of any viewport.

---

## 3. Tech Stack

| Layer | Specification |
|-------|--------------|
| **Motion library** | GSAP (with ScrollTrigger plugin) — loaded via CDN (cdnjs.cloudflare.com) for simplicity, OR vendored into `/vendor/gsap/` if zero third-party runtime dependency is preferred. Default to CDN unless site policy requires self-hosting; document the choice in the repo README either way. |
| **Base** | Astro static site generator (already in use — `astro.config.mjs` with `base: '/'`, `site: 'https://creditcookbook.com'`) |
| **Fonts** | Self-hosted or Google Fonts CDN — one grotesk/neo-grotesque family (e.g. Helvetica Neue, Inter, or Söhne class) for Swiss discipline. IBM Plex Mono for monospace/template labels (already in use). |
| **Images** | Modern formats (WebP/AVIF with fallback), lazy-loaded below the fold. |
| **Analytics/forms** | Newsletter capture wired to Buttondown (already configured in EmailCapture component). GA4 tag if applicable. |

---

## 4. Grid & Type System (Swiss discipline)

The build agent must formalize this into a tokens file before writing page code.

### Grid
- 12-column grid, consistent gutter, defined max content width
- Consistent breakpoints: mobile (375px) / tablet (768px) / desktop (1440px) / wide (1920px+)
- Max content width: 1080px (existing) — maintain or justify any change

### Type Scale
- Modular type scale using 1.25 ratio (Major Third) or 1.333 ratio (Perfect Fourth)
- Document every size as a CSS custom property token — never a one-off px value in page code
- Baseline grid for vertical rhythm — line-heights and section spacing snap to 8px base unit

### Color Tokens
| Token | Role | Notes |
|-------|------|-------|
| `--white` / `--bg` | Primary background | Dominant field — pick ONE primary background (white or off-white), not both |
| `--ink` | Primary text color | True near-black, not soft gray |
| `--blue` | Structural accent (existing) | Deep saturated blue — links, section labels, poster blocks |
| `--gold` | Emphasis accent (NEW) | Used ONLY for CTAs, key numbers/stats, dividers, hover states — never as base, never >10% of viewport |
| `--gold-hover` | Gold active/hover variant | Slightly brighter or deeper — pick one |
| `--paper` | Secondary background | Content cards, table zones |
| `--line` | Hairline rule color | 1px borders, dividers |

---

## 5. Motion Spec (GSAP + ScrollTrigger)

### Section Reveals
- Fade + subtle Y-translate on scroll-into-view
- Staggered for grouped elements (card grids)
- ScrollTrigger scrubbing where it reads as "storytelling"
- Simple one-shot reveals where it doesn't need to track scroll position

### Parallax Layers
- Background/midground/foreground moving at distinct scroll speeds
- **Home and About hero sections ONLY** — not applied indiscriminately across every page
- Recipes/Tools pages: fast and utilitarian, not parallax-heavy — users are there to get information quickly

### Hover/Tilt
- Subtle 3D perspective tilt on CTA cards and featured-recipe cards
- CSS transform + GSAP for smoothing
- Capped at small rotation range (max 3-5°) — premium, not gimmicky

### Easing
- Custom cubic-bezier matching Apple's actual feel
- Reference: `cubic-bezier(0.32, 0.72, 0, 1)` (already used on calebpierre.com)
- **Avoid** GSAP's default elastic/bounce eases entirely

### Universal Guardrails
- **`prefers-reduced-motion`:** all ScrollTrigger/parallax effects must have a reduced-motion fallback (simple fade, no movement). No exceptions.
- **No blocking:** GSAP timelines must not hold up input handling. No effect may delay perceived interactivity.
- **Mobile:** parallax degrades to simple fade-ins; no scroll-jacking on touch devices. Stagger reveals collapse to single fade.

---

## 6. Page-Level Scope

### Full Navigation
```
Home · About · Personal Credit Remedy · Business Credit · Recipes · Tools · Resources/Glossary · Newsletter · Contact · Footer (sitemap.xml, llms.txt, legal disclaimer, privacy/terms)
```

### Personal Credit Remedy Subpages
- Know Your Rights (FCRA §609/§611/§623, FDCPA, FCBA, state-level protections)
- The Dispute Process (how reporting works, step-by-step walkthrough, letter templates, MOV requests, timelines)
- Escalation & Enforcement (CFPB, FTC, State AG, small claims, consumer-rights attorneys)
- Credit Building (secured cards, authorized user, rent/utility reporting, utilization, timeline expectations)
- Identity Theft & Fraud (fraud alerts vs. freezes vs. locks, FTC IdentityTheft.gov, recovery plan)

### Business Credit Subpages
- Foundations (entity structure, EIN/DUNS, bank account setup, personal/business separation)
- Building Business Credit (Net-30 vendors, business cards, reporting, Paydex score)
- Business Credit Remedy (disputing errors, UCC filings — legitimate only, vendor escalation)
- Funding Readiness (what lenders check, common disqualifiers)

### Build Priority Order

| Priority | Pages | Motion Budget |
|----------|-------|---------------|
| 1 | **Home** — hero, problem, how-it-works, featured recipes, trust bar, newsletter | Full spectacle — parallax, reveals, tilt |
| 2 | **About** — bio, story, links, CTA | Full spectacle — parallax hero, reveals |
| 3 | **Recipes hub** — top-level template for all recipe pages | Motion-light — reveals only, no parallax |
| 4 | **Personal Credit Remedy** top-level + **Dispute Process** subpage | Motion-light — pattern for remaining subpages |
| 5 | **Business Credit** top-level | Motion-light |
| 6 | **Tools, Resources/Glossary, Newsletter, Contact** | Lighter template pass — utility over spectacle |

> Recipe/Tool/Resource pages should be Swiss-grid-consistent but motion-light — the spectacle budget belongs to Home/About.

---

## 7. Definition of Done

- [ ] Design tokens file exists (grid, type scale, color, spacing) and every page consumes it — no hardcoded one-off values in page CSS
- [ ] Home and About pages fully built with GSAP/ScrollTrigger parallax + reveal motion per Section 5
- [ ] Recipes hub, one full Personal Credit Remedy subpage, and Business Credit top-level built to the same visual system, motion-light per Section 6
- [ ] Gold accent used only in emphasis roles; never exceeds ~10% of any single viewport
- [ ] `prefers-reduced-motion` fully respected sitewide
- [ ] Lighthouse mobile: Performance ≥ 90, Accessibility ≥ 95, Best Practices ≥ 95, on both a motion-heavy page (Home) and a motion-light page (a Recipe page)
- [ ] GSAP loaded via CDN (or vendored — decision documented in repo README) with no console errors
- [ ] Fully responsive at 375px / 768px / 1440px+
- [ ] Footer, sitemap.xml, llms.txt integrated sitewide (reuse existing assets, don't rebuild)
- [ ] LinkedIn/Instagram CTAs present and visually prominent on Home + About; newsletter CTA present as secondary action sitewide
- [ ] Schema.org markup: Person (Caleb Pierre) on About, Organization (CPV) sitewide, Article/HowTo schema on recipe pages where applicable

---

## 8. QA Gate (loop against this until all pass)

1. **Grid audit:** does every page actually sit on the defined grid, or has anything drifted off-column? Fix drift, don't rationalize it.
2. **Motion audit:** scroll through Home/About at normal human speed — anything laggy, disorienting, or gimmicky gets cut or retuned. Scroll through a Recipe page — it should feel fast, not cinematic.
3. **Restraint audit:** for every animation, ask "does removing this reduce clarity or delight?" If no, remove it.
4. **Performance audit:** run Lighthouse on Home and one Recipe page; optimize (image compression, code-split GSAP usage, reduce simultaneous ScrollTrigger instances) until Section 7 thresholds pass.
5. **Accessibility audit:** keyboard navigation works sitewide; reduced-motion fallback tested by actually toggling the OS setting, not just reading the media query.
6. **Consistency audit:** type scale, color tokens, and spacing match across all built pages — no page should look like it came from a different design system.
7. **Link/CTA audit:** every outbound link (LinkedIn, Instagram, newsletter, internal nav) resolves correctly and opens as specified.

---

## 9. Explicitly Out of Scope (this phase)

- Full build-out of every Personal Credit Remedy / Business Credit subpage (one representative subpage per section is enough to lock the pattern; remaining subpages are a follow-on phase using the same template)
- Backend/CMS integration beyond static hosting + newsletter form wiring
- Payment/checkout flows
- Any "sovereign citizen" / "lawful person" / strawman-style content — explicitly excluded; the site's "remedy/enforcement" positioning is scoped to legitimate consumer-protection law (FCRA/FDCPA/CFPB/FTC channels) as established in the site-tree phase

---

## 10. Execution Model & Escalation

### Parallel Workstreams Converging Into Integration

| Agent | Responsibility |
|-------|---------------|
| **Design system agent** | Grid/type/color tokens, motion spec formalization |
| **Copy agent** | Page copy per site tree, Caleb's voice (confident, direct, no fluff) |
| **Build agent** | Implementation (HTML/CSS/JS, GSAP integration), consuming tokens + copy |
| **QA agent** | Runs Section 8 against build agent output, reports failures back for another pass |

### Iterate Autonomously. Only Surface For:

- **Missing brand assets** (headshot, logo, real photography) — ask once, proceed with clearly-marked placeholder otherwise
- **Newsletter ESP/backend** the form should actually submit to — ask once if unknown
- **Ambiguous legal/compliance claim** in copy (e.g. specific statutory damages figures) — ask once; don't invent numbers

Everything else (exact hex values within the approved palette, animation timing, copy phrasing, breakpoint pixel values) — make the call per this spec and keep moving.

### Exit Condition

All Section 7 items checked, Section 8 QA passed on Home + About + Recipes hub + one Remedy subpage + Business Credit top-level. Present the finished, working site — not a proposal or mockup.

---

## Appendix A: Existing Site State

| Asset | Location | Status |
|-------|----------|--------|
| Astro config | `astro.config.mjs` | `base: '/'`, `site: 'https://creditcookbook.com'` |
| Swiss CSS | `src/styles/global.css` | White/blue/black palette, Helvetica Neue + IBM Plex Mono, 12-col grid, hairline rules |
| Base layout | `src/layouts/Base.astro` | Nav, poster block, footer — needs GSAP integration |
| Homepage | `src/pages/index.astro` | Has hero, problem, scenarios, about teaser, email capture |
| About page | `src/pages/about.astro` | Bio, links, CTA |
| Medical Debt cluster | `src/pages/medical-debt/` | 12 pages with dispute letter templates, FAQ schema |
| Personal Credit hub | `src/pages/personal-credit/` | Hub page |
| Business Credit hub | `src/pages/business-credit/` | Hub page |
| Recipes hub | `src/pages/recipes/` | Hub page |
| Tools | `src/pages/tools/` | 4 interactive tools + hub |
| Resources | `src/pages/resources/` | Hub + FICO article + glossary |
| Contact | `src/pages/contact.astro` | Email, GitHub, LinkedIn cards |
| EmailCapture | `src/components/EmailCapture.astro` | Buttondown form |
| GitHub Actions | `.github/workflows/deploy.yml` | Auto-deploy to GitHub Pages on push to main |
| Custom domain | creditcookbook.com | Active, pointing to GitHub Pages |

## Appendix B: Color Token Migration

The existing site uses blue (`#1E3A8A`) as the primary accent. This PRD introduces gold as an emphasis accent. The migration:

| Existing | New Role | Token |
|----------|----------|-------|
| `--blue: #1E3A8A` | Structural accent (links, labels, poster blocks) | Keep as-is |
| *(new)* | Emphasis accent (CTAs, stats, dividers, hover) | `--gold: #C5A572` (or similar — build agent picks exact value within spec) |
| *(new)* | Gold hover/active | `--gold-hover: #B8956A` (or similar) |

> Gold does NOT replace blue. Blue remains the structural accent. Gold is layered on top for emphasis moments only.

## Appendix C: GSAP CDN Setup

```html
<!-- In <head> or before closing </body> -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script>
  gsap.registerPlugin(ScrollTrigger);
  // All motion code here or in separate file
</script>
```

### Reduced Motion Guard

```javascript
const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
if (reduceMotion) {
  // Skip all GSAP animations — show content statically
  document.querySelectorAll('[data-animate]').forEach(el => {
    el.style.opacity = 1;
    el.style.transform = 'none';
  });
} else {
  // Run full GSAP motion suite
}
```

## Appendix D: Site Tree (Full)

```
creditcookbook.com/
├── HOME
│   ├── Hero: "Remedy, not repair"
│   ├── How it works (3-step: Know → Enforce → Build)
│   ├── Featured recipes (top 3-4)
│   ├── Trust bar (open-source, no upsell, GitHub)
│   └── Newsletter capture
├── ABOUT
│   ├── Caleb Pierre bio / authority positioning
│   ├── Why "open-source remedy" vs paid repair
│   └── CTA: LinkedIn / Instagram
├── PERSONAL CREDIT REMEDY
│   ├── Know Your Rights
│   │   ├── FCRA basics (§609, §611, §623)
│   │   ├── FDCPA basics
│   │   ├── FCBA (billing error rights)
│   │   └── State-level consumer protection
│   ├── The Dispute Process
│   │   ├── How credit reporting works
│   │   ├── Step-by-step dispute walkthrough
│   │   ├── Dispute letter templates (by scenario)
│   │   ├── Method of verification (MOV) requests
│   │   └── Timelines & bureau obligations
│   ├── Escalation & Enforcement
│   │   ├── CFPB complaint process
│   │   ├── FTC complaint process
│   │   ├── State AG complaints
│   │   ├── Small claims court (FCRA/FDCPA violations)
│   │   └── When to involve a consumer-rights attorney
│   ├── Credit Building (post-remedy)
│   │   ├── Secured cards / credit-builder loans
│   │   ├── Authorized user strategy
│   │   ├── Rent/utility reporting
│   │   ├── Credit mix & utilization mechanics
│   │   └── Timeline expectations
│   └── Identity Theft & Fraud
│       ├── Fraud alerts vs. freezes vs. locks
│       ├── FTC IdentityTheft.gov walkthrough
│       └── Recovery plan template
├── BUSINESS CREDIT
│   ├── Foundations
│   │   ├── Entity structure (LLC/Corp)
│   │   ├── EIN, DUNS, bank account setup
│   │   └── Separating personal & business credit
│   ├── Building Business Credit
│   │   ├── Net-30 vendor tradelines
│   │   ├── Business credit cards (secured → unsecured)
│   │   ├── Reporting to business bureaus
│   │   └── Business credit score mechanics (Paydex)
│   ├── Business Credit Remedy
│   │   ├── Disputing business credit report errors
│   │   ├── UCC filings (legitimate use only)
│   │   └── Vendor/creditor dispute escalation
│   └── Funding Readiness
│       ├── What lenders check
│       └── Common disqualifiers
├── RECIPES (content hub / programmatic SEO)
│   ├── By problem ("I have a collection account," etc.)
│   ├── By document type (letter templates index)
│   └── By bureau/creditor (major bureaus, collectors)
├── TOOLS
│   ├── Dispute letter generator ✅ (built)
│   ├── Utilization calculator ✅ (built)
│   ├── Statutory damages estimator ✅ (built)
│   └── Business credit readiness checklist ✅ (built)
├── RESOURCES / GLOSSARY
│   ├── Plain-English legal glossary ✅ (built, 36 terms)
│   ├── How FICO is calculated ✅ (built)
│   ├── Links to official sources (CFPB, FTC, bureaus)
│   └── "How to verify anything we tell you"
├── NEWSLETTER
├── CONTACT ✅ (built)
└── FOOTER / SITE INFRA
    ├── Sitemap.xml
    ├── llms.txt
    ├── Legal disclaimer (educational only)
    ├── Privacy policy / Terms
    └── Social: LinkedIn, Instagram
```

---

*End of PRD. This is the standing build brief — execute against Section 7 as the exit condition.*
