# CreditCookbook

**Open-source credit education.** Dispute letters, bureau response scripts, and credit-repair playbooks — free, versioned, and inspectable.

The repo is the product. Openness is the growth mechanism: it earns backlinks, stars, and trust that a closed content site can't.

## Live Site
**[ghettoeinstein.github.io/creditcookbook.com/](https://ghettoeinstein.github.io/creditcookbook.com/)**

## Built By
**Caleb Pierre** — security engineer, fintech CTO, AI automation specialist.
- Website: [calebpierre.com](https://calebpierre.com)
- LinkedIn: [linkedin.com/in/calebpierre](https://linkedin.com/in/calebpierre)
- Instagram: [@emperorpierre](https://instagram.com/emperorpierre)
- GitHub: [github.com/ghettoeinstein](https://github.com/ghettoeinstein)

## Tech Stack
- **Framework:** Astro (static site generator — 14 pages in 343ms)
- **Hosting:** GitHub Pages (auto-deploys on push to `main`, zero cost)
- **Design:** Swiss / International Typographic Style
  - Palette: white `#FFFFFF` / blue `#1E3A8A` / black `#0A0A0A` / paper `#F5F5F5`
  - Typography: Helvetica Neue (display+body) + IBM Plex Mono (templates/labels)
  - Layout: 12-col grid, hairline rules, no border-radius, sharp corners
  - Signature: blue poster title block on each scenario page
- **Email:** Buttondown (newsletter + template lead magnet)
- **Monetization:** Affiliate partnerships + newsletter (no paid tier)

## Project Structure
```
src/
├── pages/
│   ├── index.astro              # Landing page (hero, problem, scenarios, builder bio, email)
│   ├── about.astro               # Builder page — full bio, all links, lead magnet
│   └── medical-debt/            # Cluster 01: Medical Debt (12 pages)
│       ├── index.astro          # Cluster hub + FAQ (schema.org FAQPage)
│       ├── overview.astro       # What medical debt is + 2023 rule changes
│       ├── your-rights.astro    # FCRA, HIPAA, FDCPA — three statutes
│       ├── dispute-letter.astro # FCRA §1681i dispute letter template
│       ├── hipaa-removal.astro  # 5-step HIPAA removal strategy + validation letter
│       ├── negotiate-hospital-bills.astro    # Bill negotiation script
│       ├── hospital-financial-assistance.astro # Charity care programs
│       ├── validation-letter.astro # FDCPA §1692g validation request
│       ├── pay-for-delete.astro  # When to use, when to avoid + letter
│       ├── goodwill-letter.astro # Goodwill removal request template
│       ├── 500-threshold.astro   # The 2023 $500 exclusion rule
│       ├── bureau-response.astro # MOV letter, CFPB complaint, outcome scripts
│       └── rebuild-after.astro  # Score recovery timeline + 5-step rebuild
├── layouts/
│   └── Base.astro               # Swiss layout (nav, poster block, footer)
├── components/
│   └── EmailCapture.astro       # Newsletter capture (Buttondown)
└── styles/
    └── global.css               # Swiss design system
```

## Content Clusters

| Cluster | Status | Pages |
|---------|--------|-------|
| 01 — Medical Debt | ✅ Live | 12 |
| 02 — Collections | Coming soon | — |
| 03 — Late Payments | Coming soon | — |
| 04 — Hard Inquiries | Coming soon | — |

## Development
```bash
npm install
npm run dev      # Local dev server at localhost:4321
npm run build    # Build to dist/
```

## Deployment
Push to `main` → GitHub Actions builds → deploys to GitHub Pages automatically.

## Monetization Model
- **Affiliate:** 2–3 curated partners (credit monitoring, secured cards, credit-builder loans) placed contextually at reader intent — not banner ads
- **Newsletter:** Email captured via template lead-magnet; biweekly send pairing one practical tip with one relevant affiliate mention
- **No paid tier.** No login. No client dashboards. The repo is the product.

## License
MIT — see [LICENSE](LICENSE).

## Owner
Caleb Pierre Ventures LLC
