"""
SEU Brochure v3 Patch:
1. Move Cooperation Programs (map-card) to right column for visual balance
2. Add 六朝松 (Six Dynasties Pine) SVG silhouette background effect to intro section
"""
import re

path = 'index.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# ── 1. Partnerships layout rebalance ──
old_left_end = '''          </div>
        </div>
        <div class="map-card">
          <h3>Cooperation Programs</h3>
          <ul class="partner-list">
            <li>SEU–Monash Joint Graduate School (Suzhou) — joint PhD programs &amp; advanced materials</li>
            <li>HKUST–SEU Space Robotics &amp; Energy Center — lunar exploration &amp; sustainable energy</li>
            <li>China-Indonesia College of Elite Engineers — university-enterprise talent model</li>
            <li>Secretariat of Sino-British University Engineering Education &amp; Research Alliance</li>
            <li>160+ partner institutions across 45+ countries — Cambridge, MIT, ETH Zurich, NUS…</li>
          </ul>
        </div>
      </div>

      <div class="cases">'''

new_left_end = '''          </div>
        </div>
      </div>

      <div>
        <div class="map-card">
          <h3>Cooperation Programs</h3>
          <ul class="partner-list">
            <li>SEU–Monash Joint Graduate School (Suzhou) — joint PhD programs &amp; advanced materials</li>
            <li>HKUST–SEU Space Robotics &amp; Energy Center — lunar exploration &amp; sustainable energy</li>
            <li>China-Indonesia College of Elite Engineers — university-enterprise talent model</li>
            <li>Secretariat of Sino-British University Engineering Education &amp; Research Alliance</li>
            <li>160+ partner institutions across 45+ countries — Cambridge, MIT, ETH Zurich, NUS…</li>
          </ul>
        </div>
        <div class="cases">'''

html = html.replace(old_left_end, new_left_end)

# Fix right column closing
old_cases_close = '''          <div class="case-stat">24<span>International Research Platforms · 20 Countries · 60+ Universities</span></div>
        </div>
      </div>
    </div>
  </div>
</section>'''

new_cases_close = '''          <div class="case-stat">24<span>International Research Platforms · 20 Countries · 60+ Universities</span></div>
        </div>
      </div>
      </div>
    </div>
  </div>
</section>'''

html = html.replace(old_cases_close, new_cases_close)

# ── 2. Intro CSS: 六朝松 background ──
old_intro_css = '''    /* Intro */
    #intro{background:var(--white)}'''

new_intro_css = '''    /* Intro — with 六朝松 background */
    #intro{background:var(--white); position:relative; overflow:hidden}
    .pine-bg{
      position:absolute; right:-40px; bottom:-40px; z-index:0;
      width:440px; height:520px; opacity:.85; pointer-events:none;
      animation:pineBreathe 7s ease-in-out infinite;
    }
    @keyframes pineBreathe{
      0%,100%{opacity:.7; transform:scale(1) rotate(0deg)}
      50%{opacity:.95; transform:scale(1.03) rotate(.5deg)}
    }
    #intro .container{position:relative; z-index:1}'''

html = html.replace(old_intro_css, new_intro_css)

# ── 3. Add pine SVG into intro section ──
# Find the intro section opening and add the SVG after it
old_intro_open = '''<!-- WHO WE ARE -->
<section id="intro">
  <div class="container">'''

new_intro_open = '''<!-- WHO WE ARE -->
<section id="intro">
  <!-- 六朝松 — Six Dynasties Pine, ancient symbol of SEU since 1902 -->
  <svg class="pine-bg" viewBox="0 0 440 520" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <linearGradient id="pineTrunk" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="rgba(0,47,108,.10)"/>
        <stop offset="100%" stop-color="rgba(0,47,108,.04)"/>
      </linearGradient>
      <linearGradient id="pineNeedle" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="rgba(0,47,108,.12)"/>
        <stop offset="100%" stop-color="rgba(0,47,108,.03)"/>
      </linearGradient>
    </defs>
    <!-- Trunk -->
    <path d="M208,520 Q210,420 212,380 Q214,340 210,300 Q206,260 208,220 Q210,180 212,140"
          stroke="url(#pineTrunk)" stroke-width="12" fill="none" stroke-linecap="round"/>
    <path d="M212,380 Q195,370 175,360" stroke="url(#pineTrunk)" stroke-width="5" fill="none" stroke-linecap="round"/>
    <path d="M210,300 Q225,280 240,270" stroke="url(#pineTrunk)" stroke-width="4" fill="none" stroke-linecap="round"/>
    <!-- Canopy layers — ancient pine cloud-shaped crown -->
    <ellipse cx="210" cy="140" rx="90" ry="45" fill="url(#pineNeedle)" opacity=".8"/>
    <ellipse cx="180" cy="170" rx="70" ry="35" fill="url(#pineNeedle)" opacity=".7"/>
    <ellipse cx="240" cy="185" rx="60" ry="32" fill="url(#pineNeedle)" opacity=".65"/>
    <ellipse cx="160" cy="210" rx="75" ry="38" fill="url(#pineNeedle)" opacity=".6"/>
    <ellipse cx="250" cy="230" rx="55" ry="30" fill="url(#pineNeedle)" opacity=".5"/>
    <ellipse cx="195" cy="250" rx="80" ry="35" fill="url(#pineNeedle)" opacity=".45"/>
    <ellipse cx="230" cy="280" rx="50" ry="28" fill="url(#pineNeedle)" opacity=".35"/>
    <ellipse cx="175" cy="290" rx="60" ry="30" fill="url(#pineNeedle)" opacity=".3"/>
    <!-- Ground / roots hint -->
    <path d="M150,520 Q170,500 208,510 Q250,500 280,520" stroke="rgba(0,47,108,.05)" stroke-width="2" fill="none"/>
  </svg>
  <div class="container">'''

html = html.replace(old_intro_open, new_intro_open)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print('v3 patched: partnerships rebalanced + 六朝松 SVG pine added.')
