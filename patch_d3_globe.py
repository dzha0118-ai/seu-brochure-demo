import re

path = 'index.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Move summer-practice section to after cover
summer_start = html.find('<section id="summer-practice">')
summer_end = html.find('<!-- CTA -->', summer_start)
summer_section = html[summer_start:summer_end]
html = html[:summer_start] + html[summer_end:]

cover_end = html.find('<!-- WHO WE ARE -->')
html = html[:cover_end] + summer_section + '\n' + html[cover_end:]

# 2. Update nav order: Project second
old_nav = '''    <div class="nav-links">
      <a href="#intro">About</a>
      <a href="#impact-networks">Impact</a>
      <a href="#partnerships">Partners</a>
      <a href="#campuses">Campuses</a>
      <a href="#alumni">Alumni</a>
      <a href="#summer-practice">Project</a>
      <a href="#cta" class="nav-cta">Join SEU</a>
    </div>'''
new_nav = '''    <div class="nav-links">
      <a href="#intro">About</a>
      <a href="#summer-practice">Project</a>
      <a href="#impact-networks">Impact</a>
      <a href="#partnerships">Partners</a>
      <a href="#campuses">Campuses</a>
      <a href="#alumni">Alumni</a>
      <a href="#cta" class="nav-cta">Join SEU</a>
    </div>'''
html = html.replace(old_nav, new_nav)

# 3. Replace globe CSS
old_globe_css = '''    /* Interactive Globe */
    .globe-card{
      background:rgba(255,255,255,.06); border:1px solid rgba(255,255,255,.12);
      border-radius:var(--radius); padding:28px; position:relative;
    }
    .globe-card h3{font-size:20px; font-weight:700; margin-bottom:6px}
    .globe-subtitle{font-size:13px; opacity:.75; margin-bottom:18px}
    .globe-wrap{position:relative; width:100%; aspect-ratio:1; max-width:420px; margin:0 auto}
    #globe-svg{width:100%; height:100%; overflow:visible}
    .globe-bg{fill:#001a3d}
    .globe-ocean{fill:url(#globeGrad)}
    .globe-grid{fill:none; stroke:rgba(255,255,255,.08); stroke-width:1; stroke-linecap:round}
    .globe-equator{fill:none; stroke:rgba(255,255,255,.14); stroke-width:1.5; stroke-linecap:round}
    .globe-arc{fill:none; stroke:var(--gold); stroke-width:1.6; stroke-dasharray:4 4; opacity:.7; animation:arcFlow 2.4s linear infinite; pointer-events:none; transition:opacity .35s}
    @keyframes arcFlow{to{stroke-dashoffset:-16}}
    .globe-point{fill:var(--gold); stroke:#fff; stroke-width:1.4; cursor:pointer; transition:r .2s, fill .2s, stroke-width .2s, opacity .35s}
    .globe-point:hover{fill:#fff; stroke:var(--gold); stroke-width:2.5}
    .globe-center{fill:#fff; filter:drop-shadow(0 0 6px rgba(255,255,255,.6)); transition:opacity .35s}
    .globe-pulse{
      fill:none; stroke:var(--gold); stroke-width:1; opacity:.5; pointer-events:none;
      animation:ringPulse 2.2s ease-out infinite; transition:opacity .35s;
    }
    @keyframes ringPulse{0%{r:5; opacity:.55}100%{r:18; opacity:0}}
    .globe-node{fill:#8ab4f8; stroke:#fff; stroke-width:1.2; cursor:pointer; transition:r .2s, fill .2s, opacity .35s}
    .globe-node:hover{fill:#fff; stroke:#8ab4f8; r:6; stroke-width:2}
    .globe-node-pulse{fill:none; stroke:#8ab4f8; stroke-width:.8; opacity:.35; pointer-events:none; animation:nodePulse 2.5s ease-out infinite; transition:opacity .35s}
    @keyframes nodePulse{0%{r:3; opacity:.4}100%{r:12; opacity:0}}
    .globe-node-arc{fill:none; stroke:#8ab4f8; stroke-width:1; stroke-dasharray:2 3; opacity:.35; animation:arcFlow 3s linear infinite; transition:opacity .35s}
    .globe-label{fill:#fff; font-size:9px; font-weight:600; text-anchor:middle; pointer-events:none; opacity:.9; text-shadow:0 1px 4px rgba(0,0,0,.8); transition:opacity .35s}
    .globe-tooltip{
      position:absolute; background:rgba(255,255,255,.96); color:var(--navy);
      padding:10px 14px; border-radius:8px; font-size:13px; font-weight:500;
      pointer-events:none; opacity:0; transform:translateY(10px); transition:opacity .22s, transform .22s;
      box-shadow:0 10px 30px rgba(0,0,0,.25); max-width:240px; z-index:20; border:1px solid var(--light-gray);
    }
    .globe-tooltip.show{opacity:1; transform:translateY(0)}
    .globe-tooltip strong{display:block; font-size:11px; color:var(--gold); margin-bottom:4px; text-transform:uppercase; letter-spacing:.5px}
    .globe-tooltip small{display:block; font-size:12px; color:var(--gray); margin-top:5px; line-height:1.45}
    .globe-stats{display:flex; justify-content:center; gap:24px; margin-top:18px; flex-wrap:wrap}
    .globe-stat{text-align:center}
    .globe-stat .num{font-size:22px; font-weight:800; color:var(--gold-light)}
    .globe-stat .txt{font-size:11px; opacity:.75; text-transform:uppercase; letter-spacing:.5px}'''

new_globe_css = '''    /* Interactive D3 Globe */
    .globe-card{
      background:rgba(255,255,255,.06); border:1px solid rgba(255,255,255,.12);
      border-radius:var(--radius); padding:28px; position:relative;
      overflow:hidden;
    }
    .globe-card h3{font-size:20px; font-weight:700; margin-bottom:6px}
    .globe-subtitle{font-size:13px; opacity:.75; margin-bottom:18px}
    .globe-wrap{position:relative; width:100%; aspect-ratio:1; max-width:460px; margin:0 auto}
    #globe-svg{width:100%; height:100%; overflow:visible; cursor:grab}
    #globe-svg:active{cursor:grabbing}
    .globe-ocean{fill:url(#globeOcean)}
    .globe-atmosphere{fill:url(#globeAtmosphere); pointer-events:none}
    .globe-graticule{fill:none; stroke:rgba(255,255,255,.10); stroke-width:.6; pointer-events:none}
    .globe-sphere{fill:none; stroke:rgba(201,162,39,.35); stroke-width:1.5; pointer-events:none}
    .globe-country{
      fill:rgba(255,255,255,.10); stroke:rgba(255,255,255,.18); stroke-width:.5;
      transition:fill .25s; cursor:pointer;
    }
    .globe-country:hover{fill:rgba(201,162,39,.35)}
    .globe-arc{
      fill:none; stroke:var(--gold); stroke-width:1.8; stroke-dasharray:5 4;
      opacity:.85; pointer-events:none; animation:arcFlow 2s linear infinite;
      filter:url(#arcGlow);
    }
    .globe-node-arc{
      fill:none; stroke:#5da8ff; stroke-width:1; stroke-dasharray:2 3;
      opacity:.35; pointer-events:none; animation:arcFlow 3s linear infinite;
    }
    @keyframes arcFlow{to{stroke-dashoffset:-18}}
    .globe-point{
      fill:var(--gold); stroke:#fff; stroke-width:1.5; cursor:pointer;
      transition:r .2s, fill .2s, stroke-width .2s;
      filter:url(#pointGlow);
    }
    .globe-point:hover{fill:#fff; stroke:var(--gold); r:9; stroke-width:2.5}
    .globe-center{fill:#fff; stroke:var(--gold); stroke-width:2; filter:url(#pointGlow)}
    .globe-node{
      fill:#5da8ff; stroke:#fff; stroke-width:1.2; cursor:pointer;
      transition:r .2s, fill .2s; filter:url(#nodeGlow);
    }
    .globe-node:hover{fill:#fff; stroke:#5da8ff; r:6; stroke-width:2}
    .globe-pulse{fill:none; stroke:var(--gold); stroke-width:1; opacity:.55; pointer-events:none; animation:ringPulse 2.2s ease-out infinite}
    .globe-node-pulse{fill:none; stroke:#5da8ff; stroke-width:.8; opacity:.35; pointer-events:none; animation:nodePulse 2.8s ease-out infinite}
    @keyframes ringPulse{0%{r:5; opacity:.55}100%{r:22; opacity:0}}
    @keyframes nodePulse{0%{r:3; opacity:.4}100%{r:14; opacity:0}}
    .globe-label{fill:#fff; font-size:9px; font-weight:600; text-anchor:middle; pointer-events:none; opacity:.9; text-shadow:0 1px 4px rgba(0,0,0,.85); transition:opacity .3s}
    .globe-node-label{fill:#9ecbff; font-size:8px; font-weight:500; text-anchor:middle; pointer-events:none; opacity:.75; text-shadow:0 1px 4px rgba(0,0,0,.85); transition:opacity .3s}
    .globe-tooltip{
      position:absolute; background:rgba(255,255,255,.96); color:var(--navy);
      padding:10px 14px; border-radius:8px; font-size:13px; font-weight:500;
      pointer-events:none; opacity:0; transform:translateY(10px); transition:opacity .22s, transform .22s;
      box-shadow:0 10px 30px rgba(0,0,0,.25); max-width:240px; z-index:20; border:1px solid var(--light-gray);
    }
    .globe-tooltip.show{opacity:1; transform:translateY(0)}
    .globe-tooltip strong{display:block; font-size:11px; color:var(--gold); margin-bottom:4px; text-transform:uppercase; letter-spacing:.5px}
    .globe-tooltip small{display:block; font-size:12px; color:var(--gray); margin-top:5px; line-height:1.45}
    .globe-drag-hint{font-size:11px; opacity:.55; text-align:center; margin-top:10px; letter-spacing:.3px}
    .globe-stats{display:flex; justify-content:center; gap:24px; margin-top:18px; flex-wrap:wrap}
    .globe-stat{text-align:center}
    .globe-stat .num{font-size:22px; font-weight:800; color:var(--gold-light)}
    .globe-stat .txt{font-size:11px; opacity:.75; text-transform:uppercase; letter-spacing:.5px}'''

html = html.replace(old_globe_css, new_globe_css)

# 4. Replace globe HTML
old_globe_html = '''        <div class="globe-card">
          <h3>Global Collaboration Network</h3>
          <div class="globe-subtitle">Centered on Nanjing · Accurate geographic positions of SEU partners</div>
          <div class="globe-wrap">
            <svg id="globe-svg" viewBox="0 0 400 400">
              <defs>
                <radialGradient id="globeGrad" cx="35%" cy="30%" r="85%">
                  <stop offset="0%" stop-color="#08418a"/>
                  <stop offset="60%" stop-color="#002F6C"/>
                  <stop offset="100%" stop-color="#00102b"/>
                </radialGradient>
                <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
                  <feGaussianBlur stdDeviation="4" result="coloredBlur"/>
                  <feMerge><feMergeNode in="coloredBlur"/><feMergeNode in="SourceGraphic"/></feMerge>
                </filter>
              </defs>
              <circle cx="200" cy="200" r="190" class="globe-ocean"/>
              <clipPath id="globeClip"><circle cx="200" cy="200" r="190"/></clipPath>
              <g clip-path="url(#globeClip)">
                <g id="globe-grids"></g>
                <g id="globe-arcs"></g>
                <g id="globe-pulses"></g>
                <g id="globe-points"></g>
                <g id="globe-labels"></g>
              </g>
              <circle cx="200" cy="200" r="190" fill="none" stroke="rgba(201,162,39,.35)" stroke-width="1.5"/>
              <circle cx="200" cy="200" r="196" fill="none" stroke="rgba(255,255,255,.06)" stroke-width="2"/>
            </svg>
            <div class="globe-tooltip" id="globe-tooltip"></div>
          </div>
          <div class="globe-stats">
            <div class="globe-stat"><div class="num">5</div><div class="txt">Flagship Partners</div></div>
            <div class="globe-stat"><div class="num">60+</div><div class="txt">Countries</div></div>
            <div class="globe-stat"><div class="num">~2,000</div><div class="txt">Intl Students</div></div>
          </div>
        </div>'''

new_globe_html = '''        <div class="globe-card">
          <h3>Global Collaboration Network</h3>
          <div class="globe-subtitle">Centered on Nanjing · Real-world map · Drag to rotate</div>
          <div class="globe-wrap">
            <svg id="globe-svg" viewBox="0 0 460 460">
              <defs>
                <radialGradient id="globeOcean" cx="35%" cy="30%" r="85%">
                  <stop offset="0%" stop-color="#0a4a9c"/>
                  <stop offset="50%" stop-color="#002F6C"/>
                  <stop offset="100%" stop-color="#000d20"/>
                </radialGradient>
                <radialGradient id="globeAtmosphere" cx="50%" cy="50%" r="50%">
                  <stop offset="80%" stop-color="rgba(201,162,39,0)"/>
                  <stop offset="95%" stop-color="rgba(201,162,39,.18)"/>
                  <stop offset="100%" stop-color="rgba(201,162,39,0)"/>
                </radialGradient>
                <filter id="pointGlow" x="-100%" y="-100%" width="300%" height="300%">
                  <feGaussianBlur stdDeviation="2.5" result="blur"/>
                  <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
                </filter>
                <filter id="nodeGlow" x="-100%" y="-100%" width="300%" height="300%">
                  <feGaussianBlur stdDeviation="2" result="blur"/>
                  <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
                </filter>
                <filter id="arcGlow" x="-50%" y="-50%" width="200%" height="200%">
                  <feGaussianBlur stdDeviation="1.5" result="blur"/>
                  <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
                </filter>
              </defs>
              <circle cx="230" cy="230" r="210" class="globe-ocean"/>
              <circle cx="230" cy="230" r="214" class="globe-atmosphere"/>
              <clipPath id="globeClip"><circle cx="230" cy="230" r="210"/></clipPath>
              <g clip-path="url(#globeClip)">
                <g id="globe-countries"></g>
                <path id="globe-graticule" class="globe-graticule"></path>
                <g id="globe-arcs"></g>
                <g id="globe-pulses"></g>
                <g id="globe-points"></g>
                <g id="globe-labels"></g>
              </g>
              <circle cx="230" cy="230" r="210" class="globe-sphere"/>
            </svg>
            <div class="globe-tooltip" id="globe-tooltip"></div>
          </div>
          <div class="globe-drag-hint">Drag the globe · Scroll to zoom · Hover nodes for details</div>
          <div class="globe-stats">
            <div class="globe-stat"><div class="num">5</div><div class="txt">Flagship Partners</div></div>
            <div class="globe-stat"><div class="num">60+</div><div class="txt">Countries</div></div>
            <div class="globe-stat"><div class="num">~2,000</div><div class="txt">Intl Students</div></div>
          </div>
        </div>'''

html = html.replace(old_globe_html, new_globe_html)

# 5. Replace globe JS
old_globe_js = re.search(r'  // Interactive Globe — accurate orthographic projection centered on Nanjing\n  \(function\(\)\{[\s\S]*?\}\)\(\);', html).group(0)

new_globe_js = '''  // Interactive D3 Globe — real world map, orthographic projection
  (function(){
    var width = 460, height = 460, radius = 210;
    var svg = d3.select('#globe-svg');
    var tooltip = d3.select('#globe-tooltip');

    var nanjing = {name:'Southeast University (SEU)', city:'Nanjing', country:'China', lat:32.060255, lon:118.796877, type:'Home Campus', desc:'Center of SEU global collaboration network.'};

    var partners = [
      {name:'Monash University', city:'Melbourne', country:'Australia', lat:-37.912600, lon:145.134300, type:'Joint Research Institute', desc:'SEU–Monash Joint Research Institute: joint PhD programs and advanced materials research, co-led by Professor Aibing Yu.'},
      {name:'CERN / AMS Experiment', city:'Geneva', country:'Switzerland', lat:46.233000, lon:6.055700, type:'Fundamental Science', desc:'Long-term collaboration with Nobel laureate Samuel Ting on the Alpha Magnetic Spectrometer (AMS) space experiment.'},
      {name:'HKUST', city:'Hong Kong', country:'China', lat:22.337600, lon:114.263000, type:'Space \u0026 Energy Center', desc:'HKUST–SEU Space Robotics \u0026 Energy Center, established in 2024 for lunar exploration and sustainable energy.'},
      {name:'University of Leeds', city:'Leeds', country:'UK', lat:53.806700, lon:-1.555000, type:'Sino-British Alliance', desc:'Secretariat of the Sino-British University Engineering Education and Research Alliance; strategic engineering partnership.'},
      {name:'University of Auckland', city:'Auckland', country:'New Zealand', lat:-36.850900, lon:174.764500, type:'Strategic Partner', desc:'Joint research and student exchange across engineering, science and innovation.'}
    ];

    var globalNodes = [
      {city:'New York', country:'USA', lat:40.7128, lon:-74.0060, type:'Global Scholars', desc:'International students and visiting scholars from the Americas.'},
      {city:'São Paulo', country:'Brazil', lat:-23.5505, lon:-46.6333, type:'Global Scholars', desc:'Research and student exchange across Latin America.'},
      {city:'Cairo', country:'Egypt', lat:30.0444, lon:31.2357, type:'Global Scholars', desc:'Partnerships and scholars from Africa and the Middle East.'},
      {city:'Moscow', country:'Russia', lat:55.7558, lon:37.6173, type:'Global Scholars', desc:'Academic collaboration and exchange across Eurasia.'},
      {city:'Bangkok', country:'Thailand', lat:13.7563, lon:100.5018, type:'Global Scholars', desc:'Southeast Asia outreach and student mobility.'},
      {city:'New Delhi', country:'India', lat:28.6139, lon:77.2090, type:'Global Scholars', desc:'Joint research and talent exchange with South Asian institutions.'},
      {city:'Nairobi', country:'Kenya', lat:-1.2921, lon:36.8219, type:'Global Scholars', desc:'Emerging research and education cooperation in Africa.'}
    ];

    var projection = d3.geoOrthographic()
      .scale(radius)
      .translate([width/2, height/2])
      .clipAngle(90)
      .rotate([-nanjing.lon, -nanjing.lat]);

    var path = d3.geoPath().projection(projection);
    var graticule = d3.geoGraticule().step([30, 30]);

    var countriesGroup = svg.select('#globe-countries');
    var graticulePath = svg.select('#globe-graticule');
    var arcsGroup = svg.select('#globe-arcs');
    var pulsesGroup = svg.select('#globe-pulses');
    var pointsGroup = svg.select('#globe-points');
    var labelsGroup = svg.select('#globe-labels');

    var worldData = null;
    var currentScale = radius;
    var isDragging = false;
    var rotationStart = [0,0];
    var mouseStart = [0,0];

    function showTooltip(e, d){
      tooltip.html('<strong>' + d.type + '</strong>' + (d.name || d.city) + ' · ' + d.city + ', ' + (d.country || 'China') + '<small>' + d.desc + '</small>');
      tooltip.classed('show', true);
      moveTooltip(e);
    }
    function moveTooltip(e){
      var rect = svg.node().getBoundingClientRect();
      var x = e.clientX - rect.left;
      var y = e.clientY - rect.top;
      tooltip.style('left', Math.min(x + 12, rect.width - 240) + 'px')
             .style('top', Math.max(y - 12, 0) + 'px');
    }
    function hideTooltip(){ tooltip.classed('show', false); }

    function arcFeature(a, b){
      var interpolate = d3.geoInterpolate([a.lon, a.lat], [b.lon, b.lat]);
      var coords = [];
      for(var i=0;i<=80;i++){
        var t = i/80;
        var p = interpolate(t);
        // lift middle of arc for 3D feel
        if(t > 0.05 \u0026\u0026 t < 0.95){
          var h = Math.sin(t * Math.PI) * 0.15;
          p = [p[0], p[1] + h];
        }
        coords.push(p);
      }
      return {type:'LineString', coordinates:coords};
    }

    function projectPoint(d){
      return projection([d.lon, d.lat]);
    }

    function renderWorld(){
      if(!worldData) return;
      countriesGroup.selectAll('path')
        .data(worldData.features)
        .join('path')
        .attr('class', 'globe-country')
        .attr('d', path)
        .on('mouseenter', function(e, d){ showTooltip(e, {name:d.properties.name, city:'', country:'', type:'Country', desc:'SEU connects with partners and scholars worldwide.'}); })
        .on('mousemove', moveTooltip)
        .on('mouseleave', hideTooltip);

      graticulePath.datum(graticule()).attr('d', path);
    }

    function renderConnections(){
      arcsGroup.selectAll('.globe-arc').remove();
      arcsGroup.selectAll('.globe-node-arc').remove();
      pulsesGroup.selectAll('*').remove();
      pointsGroup.selectAll('*').remove();
      labelsGroup.selectAll('*').remove();

      // Partner arcs and points
      partners.forEach(function(p){
        var arc = arcFeature(nanjing, p);
        var d = path(arc);
        if(d){
          arcsGroup.append('path')
            .attr('class', 'globe-arc')
            .attr('d', d);
        }

        var pt = projectPoint(p);
        if(pt){
          var g = pulsesGroup.append('g');
          g.append('circle')
            .attr('class', 'globe-pulse')
            .attr('cx', pt[0]).attr('cy', pt[1]).attr('r', 5);

          var pg = pointsGroup.append('g');
          pg.append('circle')
            .attr('class', 'globe-point')
            .attr('cx', pt[0]).attr('cy', pt[1]).attr('r', 5.5)
            .on('mouseenter', function(e){ showTooltip(e, p); })
            .on('mousemove', moveTooltip)
            .on('mouseleave', hideTooltip);

          labelsGroup.append('text')
            .attr('class', 'globe-label')
            .attr('x', pt[0]).attr('y', pt[1] + 18)
            .text(p.city);
        }
      });

      // Global nodes
      globalNodes.forEach(function(n){
        var arc = arcFeature(nanjing, n);
        var d = path(arc);
        if(d){
          arcsGroup.append('path')
            .attr('class', 'globe-node-arc')
            .attr('d', d);
        }
        var pt = projectPoint(n);
        if(pt){
          pulsesGroup.append('circle')
            .attr('class', 'globe-node-pulse')
            .attr('cx', pt[0]).attr('cy', pt[1]).attr('r', 3);

          pointsGroup.append('circle')
            .attr('class', 'globe-node')
            .attr('cx', pt[0]).attr('cy', pt[1]).attr('r', 3.5)
            .on('mouseenter', function(e){ showTooltip(e, n); })
            .on('mousemove', moveTooltip)
            .on('mouseleave', hideTooltip);

          labelsGroup.append('text')
            .attr('class', 'globe-node-label')
            .attr('x', pt[0]).attr('y', pt[1] + 13)
            .text(n.city);
        }
      });

      // Nanjing center
      var centerPt = projectPoint(nanjing);
      if(centerPt){
        pulsesGroup.append('circle')
          .attr('class', 'globe-pulse')
          .attr('cx', centerPt[0]).attr('cy', centerPt[1]).attr('r', 6);
        pointsGroup.append('circle')
          .attr('class', 'globe-point globe-center')
          .attr('cx', centerPt[0]).attr('cy', centerPt[1]).attr('r', 6.5)
          .on('mouseenter', function(e){ showTooltip(e, nanjing); })
          .on('mousemove', moveTooltip)
          .on('mouseleave', hideTooltip);
        labelsGroup.append('text')
          .attr('class', 'globe-label')
          .attr('x', centerPt[0]).attr('y', centerPt[1] - 12)
          .text('Nanjing · SEU');
      }
    }

    function update(){
      projection.scale(currentScale);
      path.projection(projection);
      renderWorld();
      renderConnections();
    }

    // Load world map
    d3.json('https://cdn.jsdelivr.net/npm/world-atlas@2/countries-110m.json').then(function(topology){
      worldData = topojson.feature(topology, topology.objects.countries);
      update();
      startAutoRotate();
    }).catch(function(err){
      console.error('World map load failed:', err);
    });

    // Auto rotation
    var autoRotate = true;
    var lastTime = performance.now();
    function startAutoRotate(){
      function frame(t){
        if(autoRotate \u0026\u0026 !isDragging){
          var dt = t - lastTime;
          var rot = projection.rotate();
          rot[0] += dt * 0.003;
          projection.rotate(rot);
          update();
        }
        lastTime = t;
        requestAnimationFrame(frame);
      }
      requestAnimationFrame(frame);
    }

    // Drag to rotate
    svg.on('mousedown', function(e){
      isDragging = true;
      autoRotate = false;
      rotationStart = projection.rotate();
      mouseStart = [e.clientX, e.clientY];
    });
    d3.select(window).on('mousemove.globe', function(e){
      if(!isDragging) return;
      var dx = e.clientX - mouseStart[0];
      var dy = e.clientY - mouseStart[1];
      var rot0 = rotationStart;
      projection.rotate([rot0[0] + dx * 0.35, rot0[1] - dy * 0.35, rot0[2]]);
      update();
    });
    d3.select(window).on('mouseup.globe', function(){
      isDragging = false;
      setTimeout(function(){ autoRotate = true; }, 2000);
    });

    // Zoom with scroll
    svg.on('wheel', function(e){
      e.preventDefault();
      var delta = e.deltaY > 0 ? -8 : 8;
      currentScale = Math.max(120, Math.min(280, currentScale + delta));
      update();
    }, {passive:false});

    // Pause rotation when hovering tooltip area
    svg.on('mouseenter', function(){ autoRotate = false; });
    svg.on('mouseleave', function(){ if(!isDragging) autoRotate = true; });

  })();'''

html = html.replace(old_globe_js, '  // Interactive D3 Globe — real world map, orthographic projection\n' + new_globe_js)

# 6. Add D3 + TopoJSON scripts before closing </body>
html = html.replace('</body>', '  <script src="https://cdn.jsdelivr.net/npm/d3@7"></script>\n  <script src="https://cdn.jsdelivr.net/npm/topojson-client@3"></script>\n</body>')

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
print('Patched: moved summer-practice, updated nav, replaced globe with D3 real-world map.')
