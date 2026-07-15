#!/usr/bin/env python3
"""Fix aesthetic inconsistencies across all pages.

For pages WITHOUT data-animate, this script:
1. Adds data-animate to <section class="section"> tags
2. Adds data-animate to key content blocks (h2, h3, p, tables, .mono-block, .card, grids)
3. Does NOT touch inline styles (too many, and they use token vars already)
4. Replaces hardcoded hex colors in JS with token-based approach

For pages with hardcoded hex colors in JS:
- Replace '#B45309' with 'var(--gold)' for warning/warm accent
- Replace '#DC2626' with 'var(--gold-hover)' for critical/danger accent
"""

import re
import os
import glob

# --- Pages that need data-animate added ---
PAGES_WITHOUT_ANIMATE = [
    "src/pages/medical-debt/500-threshold.astro",
    "src/pages/medical-debt/bureau-response.astro",
    "src/pages/medical-debt/dispute-letter.astro",
    "src/pages/medical-debt/goodwill-letter.astro",
    "src/pages/medical-debt/hipaa-removal.astro",
    "src/pages/medical-debt/hospital-financial-assistance.astro",
    "src/pages/medical-debt/index.astro",
    "src/pages/medical-debt/negotiate-hospital-bills.astro",
    "src/pages/medical-debt/overview.astro",
    "src/pages/medical-debt/pay-for-delete.astro",
    "src/pages/medical-debt/rebuild-after.astro",
    "src/pages/medical-debt/validation-letter.astro",
    "src/pages/medical-debt/your-rights.astro",
    "src/pages/privacy.astro",
    "src/pages/resources/fcra-explained.astro",
    "src/pages/resources/fdcpa-explained.astro",
    "src/pages/resources/glossary.astro",
    "src/pages/resources/how-fico-is-calculated.astro",
    "src/pages/terms.astro",
    "src/pages/tools/business-credit-checklist.astro",
    "src/pages/tools/damages-estimator.astro",
    "src/pages/tools/dispute-letter-generator.astro",
    "src/pages/tools/utilization-calculator.astro",
]

# --- Pages with hardcoded hex colors in JS ---
PAGES_WITH_HEX_COLORS = [
    "src/pages/tools/utilization-calculator.astro",
    "src/pages/tools/business-credit-checklist.astro",
]


def add_data_animate_to_section(content):
    """Add data-animate to <section class="section"> tags that don't already have it."""
    # Match <section class="section"> or <section class="section-tight"> without data-animate
    pattern = r'(<section\s+class="(?:section|section-tight)"(?![^>]*data-animate))'
    replacement = r'\1 data-animate'
    return re.sub(pattern, replacement, content)


def add_data_animate_to_inner_sections(content):
    """Add data-animate to key inner elements within sections.
    
    Targets:
    - <span class="section-label"> tags
    - <h2> tags (first one per section)
    - <div class="mono-block" tags
    - <div class="card" tags (not card-flat to avoid breaking form layouts)
    - Grid containers: <div style="display: grid... that are link grids
    - <table> tags
    - <hr class="rule" /> tags (get data-animate for smooth reveal)
    """
    
    # Add to section-label spans that don't already have data-animate
    content = re.sub(
        r'(<span class="section-label")(?![^>]*data-animate)',
        r'\1 data-animate',
        content
    )
    
    # Add to mono-block divs
    content = re.sub(
        r'(<div[^>]*class="[^"]*mono-block[^"]*")(?![^>]*data-animate)',
        r'\1 data-animate',
        content
    )
    
    # Add to <hr class="rule" /> 
    content = re.sub(
        r'(<hr class="rule")(?![^>]*data-animate)',
        r'\1 data-animate',
        content
    )
    
    # Add to <table> tags that don't have data-animate (but not inside <script>)
    # We need to be careful not to touch script content
    # Split by script tags
    parts = re.split(r'(<script[^>]*>.*?</script>)', content, flags=re.DOTALL)
    for i, part in enumerate(parts):
        if not part.startswith('<script'):
            # Add data-animate to tables in non-script parts
            parts[i] = re.sub(
                r'(<table)(?![^>]*data-animate)',
                r'\1 data-animate',
                part
            )
    content = ''.join(parts)
    
    return content


def fix_hex_colors_in_js(content):
    """Replace hardcoded hex colors in JS with token-based CSS variables.
    
    #B45309 (amber/warning) -> var(--gold) 
    #DC2626 (red/critical) -> var(--gold-hover)
    """
    # In JS string contexts (inside <script> tags), replace hex colors
    parts = re.split(r'(<script[^>]*>.*?</script>)', content, flags=re.DOTALL)
    for i, part in enumerate(parts):
        if part.startswith('<script'):
            part = part.replace("#B45309", "var(--gold)")
            part = part.replace("#DC2626", "var(--gold-hover)")
            parts[i] = part
    return ''.join(parts)


def process_file(filepath):
    """Process a single file: add data-animate, fix hex colors."""
    with open(filepath, 'r') as f:
        content = f.read()
    
    original = content
    
    if filepath in PAGES_WITHOUT_ANIMATE or True:  # All files get checked
        content = add_data_animate_to_section(content)
        content = add_data_animate_to_inner_sections(content)
    
    if filepath in PAGES_WITH_HEX_COLORS:
        content = fix_hex_colors_in_js(content)
    
    if content != original:
        with open(filepath, 'w') as f:
            f.write(content)
        return True
    return False


def main():
    base = os.path.expanduser("~/creditcookbook.com")
    
    all_pages = sorted(glob.glob(os.path.join(base, "src/pages/**/*.astro"), recursive=True))
    
    changed = []
    for page in all_pages:
        rel = os.path.relpath(page, base)
        if process_file(page):
            changed.append(rel)
    
    print(f"Processed {len(all_pages)} pages")
    print(f"Changed {len(changed)} files:")
    for c in changed:
        print(f"  - {c}")


if __name__ == "__main__":
    main()
