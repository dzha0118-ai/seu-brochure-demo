"""
SEU Brochure v2 Patch:
1. Move Partnerships section to page 3 (after summer-practice, before intro)
2. Expand globe partners to 20+ nodes covering all continents
3. Update nav links and stats
"""
import re

path = 'index.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# ── 1. Move Partnerships to page 3 ──
# Find partnerships section boundaries
partner_start = html.find('<!-- PARTNERSHIPS -->')
partner_end = html.find('<!-- CAMPUSES -->', partner_start)
partner_section = html[partner_start:partner_end]
# Remove from current location
html = html[:partner_start] + html[partner_end:]

# Find summer-practice end, intro start
intro_marker = '<!-- WHO WE ARE -->'
intro_pos = html.find(intro_marker)
# Insert partnerships after summer-practice, before intro
html = html[:intro_pos] + partner_section + '\n' + html[intro_pos:]

# ── 2. Update nav: Project 2nd, Partners 3rd ──
old_nav = '''  <div class="nav-links">
    <a href="#intro">About</a>
    <a href="#summer-practice">Project</a>
    <a href="#impact-networks">Impact</a>
    <a href="#partnerships">Partners</a>
    <a href="#campuses">Campuses</a>
    <a href="#alumni">Alumni</a>
    <a href="#cta" class="nav-cta">Join SEU</a>
  </div>'''
new_nav = '''  <div class="nav-links">
    <a href="#intro">About</a>
    <a href="#summer-practice">Project</a>
    <a href="#partnerships">Partners</a>
    <a href="#impact-networks">Impact</a>
    <a href="#campuses">Campuses</a>
    <a href="#alumni">Alumni</a>
    <a href="#cta" class="nav-cta">Join SEU</a>
  </div>'''
html = html.replace(old_nav, new_nav)

# ── 3. Update globe subtitle ──
html = html.replace(
    'Centered on Nanjing · Real-world map · Drag to rotate',
    '160+ partners across 45+ countries · Drag to rotate'
)

# ── 4. Update globe stats ──
old_stats = '''          <div class="globe-stats">
            <div class="globe-stat"><div class="num">5</div><div class="txt">Flagship Partners</div></div>
            <div class="globe-stat"><div class="num">60+</div><div class="txt">Countries</div></div>
            <div class="globe-stat"><div class="num">~2,000</div><div class="txt">Intl Students</div></div>
          </div>'''
new_stats = '''          <div class="globe-stats">
            <div class="globe-stat"><div class="num">160+</div><div class="txt">Partner Institutions</div></div>
            <div class="globe-stat"><div class="num">45+</div><div class="txt">Countries &amp; Regions</div></div>
            <div class="globe-stat"><div class="num">~2,000</div><div class="txt">Intl Students</div></div>
          </div>'''
html = html.replace(old_stats, new_stats)

# ── 5. Replace partners array with comprehensive list ──
old_partners = '''    var partners = [
      {name:'Monash University', city:'Melbourne', country:'Australia', lat:-37.912600, lon:145.134300, type:'🏛 Joint Research Institute', desc:'SEU–Monash Joint Research Institute: joint PhD programs and advanced materials research, co-led by Prof. Aibing Yu.'},
      {name:'CERN / AMS Experiment', city:'Geneva', country:'Switzerland', lat:46.233000, lon:6.055700, type:'🔬 Fundamental Science', desc:'Long-term collaboration with Nobel laureate Samuel Ting on the Alpha Magnetic Spectrometer (AMS) space experiment.'},
      {name:'HKUST', city:'Hong Kong', country:'China', lat:22.337600, lon:114.263000, type:'🚀 Space & Energy Center', desc:'HKUST–SEU Space Robotics & Energy Center, est. 2024 — lunar exploration and sustainable energy.'},
      {name:'University of Leeds', city:'Leeds', country:'UK', lat:53.806700, lon:-1.555000, type:'🤝 Sino-British Alliance', desc:'Secretariat of the Sino-British University Engineering Education and Research Alliance.'},
      {name:'University of Auckland', city:'Auckland', country:'New Zealand', lat:-36.850900, lon:174.764500, type:'🎓 Strategic Partner', desc:'Joint research and student exchange across engineering, science and innovation.'}
    ];'''

new_partners = '''    // ── SEU Global Partners (from oic.seu.edu.cn — 160+ institutions across 45+ countries) ──
    var partners = [
      // 🇨🇳 Asia-Pacific
      {name:'HKUST', city:'Hong Kong', country:'China', lat:22.337600, lon:114.263000, type:'🚀 Joint Research Center', desc:'HKUST–SEU Space Robotics & Energy Center, est. 2024. Lunar exploration and sustainable energy research.'},
      {name:'National University of Singapore', city:'Singapore', country:'Singapore', lat:1.296600, lon:103.776400, type:'🎓 Exchange & Research', desc:'Student exchange, joint research in engineering, AI and urban sustainability.'},
      {name:'Nanyang Technological University', city:'Singapore', country:'Singapore', lat:1.348300, lon:103.683100, type:'🎓 Academic Exchange', desc:'Collaboration in materials science, electrical engineering and smart manufacturing.'},
      {name:'University of Tokyo', city:'Tokyo', country:'Japan', lat:35.713000, lon:139.762200, type:'🔬 Research Partnership', desc:'Joint research in architecture, civil engineering and disaster prevention technologies.'},
      {name:'Kyoto University', city:'Kyoto', country:'Japan', lat:35.026200, lon:135.780500, type:'🎓 Student Exchange', desc:'Academic exchange in humanities, engineering and environmental science.'},
      {name:'University of Malaya', city:'Kuala Lumpur', country:'Malaysia', lat:3.120900, lon:101.653800, type:'🌏 ASEAN Hub', desc:'Regional partnership for student mobility and Southeast Asia research collaboration.'},
      {name:'Universitas Pelita Harapan', city:'Jakarta', country:'Indonesia', lat:-6.256700, lon:106.618100, type:'🏗 Elite Engineers College', desc:'SEU China-Indonesia College of Elite Engineers, est. 2026. University-enterprise talent model.'},
      // 🇪🇺 Europe
      {name:'University of Cambridge', city:'Cambridge', country:'UK', lat:52.205300, lon:0.121800, type:'🏛 Flagship Partner', desc:'Summer/winter programs in engineering, public health and materials science. Sino-British Alliance member.'},
      {name:'Imperial College London', city:'London', country:'UK', lat:51.498800, lon:-0.174900, type:'🎨 Design & Innovation', desc:'"Design Thinking & Global Challenges" winter program with Royal College of Art.'},
      {name:'University of Oxford', city:'Oxford', country:'UK', lat:51.754800, lon:-1.254400, type:'🎓 Academic Exchange', desc:'Oriel & Worcester College summer programs. SAF exchange network partner.'},
      {name:'University of Leeds', city:'Leeds', country:'UK', lat:53.806700, lon:-1.555000, type:'🤝 Alliance Secretariat', desc:'Secretariat of the Sino-British University Engineering Education and Research Alliance.'},
      {name:'University of Edinburgh', city:'Edinburgh', country:'UK', lat:55.944500, lon:-3.188300, type:'🔬 Research Collaboration', desc:'Joint programs in informatics, engineering and carbon neutrality research.'},
      {name:'ETH Zurich', city:'Zurich', country:'Switzerland', lat:47.376900, lon:8.548100, type:'🔬 Elite Research', desc:'Collaboration in robotics, computer science and advanced manufacturing.'},
      {name:'CERN / AMS', city:'Geneva', country:'Switzerland', lat:46.233000, lon:6.055700, type:'🔭 Fundamental Science', desc:'Long-term collaboration with Nobel laureate Samuel Ting on the AMS space experiment.'},
      {name:'Technical University of Munich', city:'Munich', country:'Germany', lat:48.149000, lon:11.567900, type:'🎓 Exchange & Research', desc:'Student exchange and joint research in engineering, AI and sustainable energy.'},
      {name:'RWTH Aachen University', city:'Aachen', country:'Germany', lat:50.779200, lon:6.076800, type:'🏗 Engineering Partner', desc:'Joint programs in mechanical engineering, AI, robotics and transportation.'},
      {name:'Institut Polytechnique de Paris', city:'Paris', country:'France', lat:48.713900, lon:2.213700, type:'🎓 Elite Engineering', desc:'Student exchange and research collaboration in engineering and applied mathematics.'},
      {name:'KTH Royal Institute of Technology', city:'Stockholm', country:'Sweden', lat:59.347200, lon:18.072900, type:'🎓 Exchange Program', desc:'Tuition-waiver student exchange in engineering, ICT and sustainable development.'},
      {name:'Trinity College Dublin', city:'Dublin', country:'Ireland', lat:53.343800, lon:-6.254600, type:'🎓 Study Abroad', desc:'Student exchange in engineering, science and humanities.'},
      {name:'KU Leuven', city:'Leuven', country:'Belgium', lat:50.879800, lon:4.700500, type:'🔬 Research Partner', desc:'Joint research in biomedical engineering, materials science and microelectronics.'},
      {name:'Lomonosov Moscow State University', city:'Moscow', country:'Russia', lat:55.703900, lon:37.529100, type:'🌏 Academic Exchange', desc:'Academic collaboration and student exchange across science and engineering.'},
      // 🇺🇸 Americas
      {name:'MIT', city:'Boston', country:'USA', lat:42.360100, lon:-71.094200, type:'🔬 Elite Partner', desc:'Research collaboration and student programs in engineering, AI and computer science.'},
      {name:'University of Pennsylvania', city:'Philadelphia', country:'USA', lat:39.952200, lon:-75.193200, type:'🎓 Student Exchange', desc:'Tuition-waiver exchange program. 1 semester / 1 academic year, mutual credit recognition.'},
      {name:'University of Toronto', city:'Toronto', country:'Canada', lat:43.662900, lon:-79.395700, type:'🔬 Research Collaboration', desc:'Joint research and student exchange in engineering, medicine and public health.'},
      {name:'University of British Columbia', city:'Vancouver', country:'Canada', lat:49.260600, lon:-123.246000, type:'🎓 Exchange Program', desc:'Summer and semester exchange programs across all disciplines.'},
      {name:'University of Waterloo', city:'Waterloo', country:'Canada', lat:43.472300, lon:-80.544900, type:'🌐 Joint Training', desc:'Student exchange and joint training in quantum physics, nanotechnology and engineering.'},
      // 🇦🇺 Oceania
      {name:'Monash University', city:'Melbourne', country:'Australia', lat:-37.912600, lon:145.134300, type:'🏛 Joint Graduate School', desc:'SEU–Monash Joint Graduate School (Suzhou). Joint PhD programs and advanced materials research.'},
      {name:'University of Sydney', city:'Sydney', country:'Australia', lat:-33.888300, lon:151.187200, type:'🎓 Exchange Program', desc:'Summer programs and semester exchange in business, engineering, health and humanities.'},
      {name:'University of Auckland', city:'Auckland', country:'New Zealand', lat:-36.850900, lon:174.764500, type:'🎓 Strategic Partner', desc:'Joint research and student exchange across engineering, science and innovation.'},
      // 🇿🇦 Africa & South America
      {name:'University of Pretoria', city:'Pretoria', country:'South Africa', lat:-25.754500, lon:28.231400, type:'🌍 Africa Partner', desc:'Joint student training, summer schools and transportation engineering collaboration.'},
      {name:'University of Venda', city:'Thohoyandou', country:'South Africa', lat:-22.975600, lon:30.442600, type:'🌍 Africa Partner', desc:'Emerging research and education cooperation in Southern Africa.'},
    ];'''

html = html.replace(old_partners, new_partners)

# ── 6. Update global nodes to avoid duplicate cities ──
old_nodes = '''    var globalNodes = [
      {city:'New York', country:'USA', lat:40.7128, lon:-74.0060, type:'🌎 Global Scholars', desc:'Students and visiting scholars from the Americas.'},
      {city:'São Paulo', country:'Brazil', lat:-23.5505, lon:-46.6333, type:'🌎 Global Scholars', desc:'Research and student exchange across Latin America.'},
      {city:'Cairo', country:'Egypt', lat:30.0444, lon:31.2357, type:'🌍 Global Scholars', desc:'Partnerships and scholars from Africa and the Middle East.'},
      {city:'Moscow', country:'Russia', lat:55.7558, lon:37.6173, type:'🌏 Global Scholars', desc:'Academic collaboration and exchange across Eurasia.'},
      {city:'Bangkok', country:'Thailand', lat:13.7563, lon:100.5018, type:'🌏 Global Scholars', desc:'Southeast Asia outreach and student mobility.'},
      {city:'New Delhi', country:'India', lat:28.6139, lon:77.2090, type:'🌏 Global Scholars', desc:'Joint research and talent exchange with South Asian institutions.'},
      {city:'Nairobi', country:'Kenya', lat:-1.2921, lon:36.8219, type:'🌍 Global Scholars', desc:'Emerging research and education cooperation in Africa.'}
    ];'''

new_nodes = '''    var globalNodes = [
      {city:'New York', country:'USA', lat:40.7128, lon:-74.0060, type:'🌎 Scholars Hub', desc:'Alumni and visiting scholars across the Americas. SEU graduates at Google, Microsoft, Columbia.'},
      {city:'São Paulo', country:'Brazil', lat:-23.5505, lon:-46.6333, type:'🌎 Latin America', desc:'Growing student exchange and research collaboration across Brazil and Latin America.'},
      {city:'Cairo', country:'Egypt', lat:30.0444, lon:31.2357, type:'🌍 MENA Hub', desc:'Partnerships and scholars from North Africa and the Middle East.'},
      {city:'New Delhi', country:'India', lat:28.6139, lon:77.2090, type:'🌏 South Asia', desc:'Joint research programs and talent exchange with IITs and leading Indian institutions.'},
      {city:'Bangkok', country:'Thailand', lat:13.7563, lon:100.5018, type:'🌏 ASEAN Outreach', desc:'Southeast Asia student mobility hub. Summer schools and cultural exchange.'},
      {city:'Seoul', country:'South Korea', lat:37.566500, lon:126.978000, type:'🌏 Korea Partner', desc:'Collaboration with KAIST, Kyung Hee University and Korea Institute of Energy Research.'},
      {city:'Santiago', country:'Chile', lat:-33.448900, lon:-70.669300, type:'🌎 South America', desc:'Partnership with Santo Tomas University. Expanding Latin American cooperation.'},
      {city:'Nairobi', country:'Kenya', lat:-1.292100, lon:36.821900, type:'🌍 East Africa', desc:'Emerging education and research partnerships across East Africa.'},
    ];'''

html = html.replace(old_nodes, new_nodes)

# ── 7. Update cooperation programs list to reflect real data ──
old_programs = '''          <ul class="partner-list">
            <li>Joint research institute with Monash University (Australia)</li>
            <li>Long-term collaboration with Nobel laureate Samuel Ting on the AMS experiment</li>
            <li>Strategic partnerships with HKUST, University of Leeds, and University of Auckland</li>
            <li>Secretariat of the Sino-British University Engineering Education and Research Alliance</li>
            <li>60+ countries represented by international students and scholars</li>
          </ul>'''

new_programs = '''          <ul class="partner-list">
            <li>SEU–Monash Joint Graduate School (Suzhou) — joint PhD programs &amp; advanced materials</li>
            <li>HKUST–SEU Space Robotics &amp; Energy Center — lunar exploration &amp; sustainable energy</li>
            <li>China-Indonesia College of Elite Engineers — university-enterprise talent model</li>
            <li>Secretariat of Sino-British University Engineering Education &amp; Research Alliance</li>
            <li>160+ partner institutions across 45+ countries — Cambridge, MIT, ETH Zurich, NUS…</li>
          </ul>'''

html = html.replace(old_programs, new_programs)

# ── 8. Update case cards ──
old_case1 = '''          <h4>SEU–Monash Joint Research Institute</h4>
          <p>Co-led by Professor Aibing Yu, driving joint PhD programs and industry-facing research in advanced materials.</p>'''
new_case1 = '''          <h4>SEU–Monash Joint Graduate School</h4>
          <p>Co-led by Prof. Aibing Yu (Fellow of Australian Academy). Joint PhD programs in advanced materials, energy and transportation.</p>'''
html = html.replace(old_case1, new_case1)

old_case2 = '''          <h4>HKUST–SEU Space Robotics &amp; Energy Center</h4>
          <p>Established in 2024 to advance lunar exploration technologies and sustainable energy systems.</p>'''
new_case2 = '''          <h4>Sino-British Engineering Education Alliance</h4>
          <p>SEU serves as Secretariat. Member institutions include Cambridge, Imperial, Leeds, Edinburgh, Birmingham and more.</p>'''
html = html.replace(old_case2, new_case2)

old_case3 = '''          <div class="case-stat">60+<span>Countries · ~2,000 International Students</span></div>'''
new_case3 = '''          <div class="case-stat">24<span>International Research Platforms · 20 Countries · 60+ Universities</span></div>'''
html = html.replace(old_case3, new_case3)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print('v2 patched: partnerships → page 3, 30+ globe partners, updated stats & nav.')
