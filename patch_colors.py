"""
Replace brochure colors with SEU official brand colors from VI system.
Source: https://seuthesis-word.github.io/seu-vis.html standard color card
"""
import re

path = 'index.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# SEU Official Brand Colors
# Primary: #151E49 (deep navy)
# Gold:    #AD986E (warm metallic)
# Yellow:  #FDD000 (bright)
# Green:   #587558
# Dark:    #231815
# Silver:  #B4B7B9

# ============================================================
# Phase 1: CSS variable definitions
# ============================================================
html = html.replace('--navy:#002F6C', '--navy:#151E49')
html = html.replace('--navy-dark:#001a3d', '--navy-dark:#0B1026')
html = html.replace('--gold:#C9A227', '--gold:#AD986E')
html = html.replace('--gold-light:#e6c76a', '--gold-light:#FDD000')
html = html.replace('--gray:#6b7280', '--gray:#5A5E63')

# ============================================================
# Phase 2: rgba() color values (before hex replacements)
# Navy: #002F6C = rgb(0,47,108)  → #151E49 = rgb(21,30,73)
# Navy dark: #001a3d = rgb(0,26,61) → #0B1026 = rgb(11,16,38)
# Gold: #C9A227 = rgb(201,162,39) → #AD986E = rgb(173,152,110)
# ============================================================
html = html.replace('rgba(0,47,108', 'rgba(21,30,73')
html = html.replace('rgba(0,26,61', 'rgba(11,16,38')
html = html.replace('rgba(201,162,39', 'rgba(173,152,110')

# ============================================================
# Phase 3: Hex color values (CSS and SVG)
# ============================================================
# Navy variants
rep_hex = [
    # old navy → new SEU deep blue
    ('#002F6C', '#151E49'),
    ('#00102b', '#080D1A'),
    ('#001a3d', '#0B1026'),
    ('#000d20', '#060A14'),
    ('#000d28', '#060A14'),
    ('#001845', '#0E1736'),

    # Gold variants
    ('#C9A227', '#AD986E'),
    ('#c9a227', '#AD986E'),
    ('#e6c76a', '#FDD000'),
    ('#E6C76A', '#FDD000'),

    # Globe ocean gradient stops
    ('#0d5db8', '#1A3582'),
    ('#003580', '#131F55'),
    ('#08418a', '#192D6E'),
    ('#0a4a9c', '#1A3078'),
]
for old, new in rep_hex:
    html = html.replace(old, new)

# ============================================================
# Phase 4: Globe star color (was #fff, keep white but subtle)
# ============================================================
# Stars are already white, which is fine

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Colors replaced with SEU official brand palette.')
print('Primary: #151E49 (deep blue)  Gold: #AD986E  Yellow: #FDD000')
