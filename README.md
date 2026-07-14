# CreditCookbook

Open-source credit education system. Dispute letters, bureau response scripts, and credit-repair playbooks — free, versioned, and inspectable.

**The repo is the product.** Openness is the growth mechanism.

## Stack
- **Framework:** Astro (static site generator)
- **Hosting:** GitHub Pages (auto-deploys on push to `main`)
- **Design:** Swiss / International Typographic Style (white / blue / black)
- **Email:** Buttondown (newsletter + template lead magnet)
- **Monetization:** Affiliate partnerships + newsletter

## Structure
```
src/
├── pages/
│   ├── index.astro          # Landing page
│   └── medical-debt/       # Cluster 01: Medical Debt (12 pages)
│       ├── index.astro      # Cluster hub + FAQ (schema.org)
│       ├── overview.astro
│       ├── your-rights.astro
│       ├── dispute-letter.astro
│       ├── hipaa-removal.astro
│       ├── negotiate-hospital-bills.astro
│       ├── hospital-financial-assistance.astro
│       ├── validation-letter.astro
│       ├── pay-for-delete.astro
│       ├── goodwill-letter.astro
│       ├── 500-threshold.astro
│       ├── bureau-response.astro
│       └── rebuild-after.astro
├── layouts/
│   └── Base.astro          # Swiss layout (nav, poster block, footer)
├── components/
│   └── EmailCapture.astro  # Newsletter capture
└── styles/
    └── global.css          # Swiss design system
```

## Development
```bash
npm install
npm run dev      # Local dev server
npm run build    # Build to dist/
```

## License
MIT — see LICENSE file.

## Owner
Caleb Pierre Ventures LLC
