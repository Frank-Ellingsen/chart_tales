import json
import pandas as pd
import generate_pdf_report as gen

# Load CSV datasets
df_nov = pd.read_csv('data/dickens/dickens_novels.csv')
novels_data = df_nov.to_dict(orient='records')

df_ad = pd.read_csv('data/dickens/dickens_adaptations.csv')
adaptations_data = df_ad.to_dict(orient='records')

df_bio = pd.read_csv('data/dickens/dickens_biography.csv')
bio_data = df_bio.to_dict(orient='records')

posts_data = gen.dickens_posts

# Convert to JSON for client-side interactivity
novels_json = json.dumps(novels_data)
adaptations_json = json.dumps(adaptations_data)
bio_json = json.dumps(bio_data)
posts_json = json.dumps([{
    'id': p['id'],
    'day': p['day'],
    'act': p['act'],
    'title': p['title'],
    'chart_type': p['chart_type'],
    'question': p['question'],
    'image': p['image'],
    'theme': p['dickens_data']['theme'],
    'key_metric': p['dickens_data']['key_metric'],
    'fun_fact': p['dickens_data']['fun_fact'],
    'quote': p['quote'],
    'bad_title': p['headline_lesson']['bad_title'],
    'action_headline': p['headline_lesson']['action_headline'],
    'rule': p['headline_lesson']['rule'],
    'storytelling_rule': p['storytelling_rule'],
    'post_copy': p['post_copy'].replace('\"', '&quot;')
} for p in posts_data])

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>A Christmas Chart Carol — Tales with Charts | Charles Dickens Data & Masterclass</title>
<style>
  :root {{
    --bg-dark: #0A1128;
    --bg-card: #101F42;
    --bg-card-hover: #162B5B;
    --accent-gold: #C5A059;
    --accent-gold-light: #E9D5A1;
    --text-primary: #F8FAFC;
    --text-secondary: #94A3B8;
    --text-muted: #64748B;
    --border-color: rgba(197, 160, 89, 0.25);
    --border-card: #1E293B;
    --badge-act1: #F59E0B;
    --badge-act2: #3B82F6;
    --badge-act3: #EF4444;
    --badge-act4: #8B5CF6;
    --badge-finale: #10B981;
  }}

  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }}

  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    background-color: var(--bg-dark);
    color: var(--text-primary);
    line-height: 1.6;
    font-size: 15px;
    padding-bottom: 80px;
  }}

  a {{
    color: var(--accent-gold);
    text-decoration: none;
    transition: color 0.2s;
  }}
  a:hover {{
    color: var(--accent-gold-light);
    text-decoration: underline;
  }}

  /* Navigation Bar */
  .navbar {{
    position: sticky;
    top: 0;
    z-index: 100;
    background: rgba(10, 17, 40, 0.92);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid var(--border-color);
    padding: 14px 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}
  .nav-brand {{
    font-size: 1.15rem;
    font-weight: 800;
    letter-spacing: 1px;
    color: #FFFFFF;
    display: flex;
    align-items: center;
    gap: 8px;
  }}
  .nav-brand span {{
    color: var(--accent-gold);
  }}
  .nav-links {{
    display: flex;
    gap: 20px;
    font-size: 0.9rem;
    font-weight: 600;
  }}
  .nav-links a {{
    color: var(--text-secondary);
  }}
  .nav-links a:hover, .nav-links a.active {{
    color: var(--accent-gold);
    text-decoration: none;
  }}

  .container {{
    max-width: 1240px;
    margin: 0 auto;
    padding: 0 20px;
  }}

  /* Hero Section */
  .hero-section {{
    padding: 48px 0 36px 0;
    text-align: center;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  }}
  .hero-tag {{
    display: inline-block;
    padding: 4px 14px;
    background: rgba(197, 160, 89, 0.15);
    border: 1px solid var(--accent-gold);
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: var(--accent-gold);
    margin-bottom: 14px;
  }}
  .hero-title {{
    font-size: 2.8rem;
    font-weight: 800;
    letter-spacing: -0.5px;
    line-height: 1.15;
    margin-bottom: 12px;
    background: linear-gradient(135deg, #FFFFFF 30%, #E2E8F0 60%, var(--accent-gold) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }}
  .hero-subtitle {{
    font-size: 1.25rem;
    color: var(--text-secondary);
    max-width: 820px;
    margin: 0 auto 24px auto;
    font-style: italic;
  }}
  .hero-actions {{
    display: flex;
    justify-content: center;
    gap: 14px;
    flex-wrap: wrap;
    margin-top: 20px;
  }}
  .btn {{
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 10px 20px;
    border-radius: 6px;
    font-weight: 700;
    font-size: 0.9rem;
    cursor: pointer;
    transition: all 0.2s;
    text-decoration: none;
  }}
  .btn-primary {{
    background: var(--accent-gold);
    color: #0A1128;
    border: 1px solid var(--accent-gold);
  }}
  .btn-primary:hover {{
    background: var(--accent-gold-light);
    color: #0A1128;
    text-decoration: none;
    box-shadow: 0 4px 16px rgba(197, 160, 89, 0.35);
  }}
  .btn-secondary {{
    background: rgba(255, 255, 255, 0.06);
    color: #FFFFFF;
    border: 1px solid rgba(255, 255, 255, 0.2);
  }}
  .btn-secondary:hover {{
    background: rgba(255, 255, 255, 0.12);
    text-decoration: none;
  }}

  /* Featured Dual Artworks Section */
  .section {{
    padding: 56px 0;
  }}
  .section-header {{
    margin-bottom: 28px;
  }}
  .section-title {{
    font-size: 1.8rem;
    font-weight: 800;
    color: #FFFFFF;
    display: flex;
    align-items: center;
    gap: 12px;
  }}
  .section-title::before {{
    content: "";
    display: inline-block;
    width: 6px;
    height: 28px;
    background: var(--accent-gold);
    border-radius: 3px;
  }}
  .section-desc {{
    font-size: 0.95rem;
    color: var(--text-secondary);
    margin-top: 6px;
  }}

  .dual-artwork-grid {{
    display: grid;
    grid-template-columns: 1.4fr 1fr;
    gap: 24px;
    align-items: stretch;
  }}
  @media (max-width: 900px) {{
    .dual-artwork-grid {{
      grid-template-columns: 1fr;
    }}
  }}

  .artwork-card {{
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 12px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    box-shadow: 0 10px 30px rgba(0,0,0,0.35);
    transition: transform 0.25s, box-shadow 0.25s;
  }}
  .artwork-card:hover {{
    transform: translateY(-4px);
    box-shadow: 0 16px 40px rgba(0,0,0,0.5);
  }}
  .artwork-img-box {{
    background: #050914;
    padding: 12px;
    text-align: center;
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 280px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  }}
  .artwork-img {{
    max-width: 100%;
    max-height: 440px;
    object-fit: contain;
    border-radius: 6px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.4);
  }}
  .artwork-info {{
    padding: 20px;
    flex-grow: 1;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}
  .artwork-badge {{
    font-size: 0.75rem;
    font-weight: 700;
    text-transform: uppercase;
    color: var(--accent-gold);
    letter-spacing: 1px;
    margin-bottom: 6px;
  }}
  .artwork-title {{
    font-size: 1.25rem;
    font-weight: 700;
    color: #FFFFFF;
    margin-bottom: 6px;
  }}
  .artwork-meta {{
    font-size: 0.85rem;
    color: var(--text-secondary);
    margin-bottom: 14px;
  }}
  .artwork-meta code {{
    background: rgba(255,255,255,0.08);
    padding: 2px 6px;
    border-radius: 4px;
    color: var(--accent-gold-light);
  }}

  /* Data Lookup Section */
  .data-lookup-wrapper {{
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 12px;
    padding: 24px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.25);
  }}
  .tab-bar {{
    display: flex;
    gap: 8px;
    border-bottom: 2px solid rgba(255, 255, 255, 0.1);
    margin-bottom: 20px;
    overflow-x: auto;
    padding-bottom: 6px;
  }}
  .tab-btn {{
    background: none;
    border: none;
    color: var(--text-secondary);
    padding: 8px 16px;
    font-size: 0.9rem;
    font-weight: 700;
    cursor: pointer;
    border-radius: 6px;
    transition: all 0.2s;
    white-space: nowrap;
  }}
  .tab-btn:hover {{
    color: #FFFFFF;
    background: rgba(255, 255, 255, 0.05);
  }}
  .tab-btn.active {{
    color: var(--accent-gold);
    background: rgba(197, 160, 89, 0.15);
    border-bottom: 2px solid var(--accent-gold);
  }}

  .search-box-row {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 16px;
    margin-bottom: 16px;
    flex-wrap: wrap;
  }}
  .search-input {{
    background: rgba(10, 17, 40, 0.8);
    border: 1px solid rgba(255, 255, 255, 0.15);
    color: #FFFFFF;
    padding: 10px 16px;
    border-radius: 6px;
    font-size: 0.9rem;
    min-width: 280px;
    flex-grow: 1;
    max-width: 480px;
  }}
  .search-input:focus {{
    outline: none;
    border-color: var(--accent-gold);
    box-shadow: 0 0 0 2px rgba(197, 160, 89, 0.2);
  }}
  .filter-count {{
    font-size: 0.85rem;
    color: var(--text-muted);
  }}

  .table-responsive {{
    overflow-x: auto;
    border-radius: 8px;
    border: 1px solid rgba(255, 255, 255, 0.08);
  }}
  .data-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 0.85rem;
    text-align: left;
  }}
  .data-table th {{
    background: #0A1128;
    color: var(--accent-gold);
    padding: 10px 14px;
    font-weight: 700;
    text-transform: uppercase;
    font-size: 0.75rem;
    letter-spacing: 0.8px;
    cursor: pointer;
    user-select: none;
    border-bottom: 1px solid var(--border-color);
  }}
  .data-table th:hover {{
    color: #FFFFFF;
  }}
  .data-table td {{
    padding: 10px 14px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    color: var(--text-primary);
  }}
  .data-table tr:hover td {{
    background: rgba(255, 255, 255, 0.03);
  }}

  .badge-tag {{
    display: inline-block;
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 0.75rem;
    font-weight: 700;
  }}
  .rating-badge {{
    background: rgba(245, 158, 11, 0.15);
    color: #FBBF24;
    border: 1px solid rgba(245, 158, 11, 0.3);
  }}

  /* 25-Day Grid */
  .masterclass-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
    gap: 20px;
  }}

  .masterclass-card {{
    background: var(--bg-card);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 10px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    transition: transform 0.2s, border-color 0.2s;
  }}
  .masterclass-card:hover {{
    transform: translateY(-3px);
    border-color: var(--accent-gold);
  }}
  .card-img-wrap {{
    background: #050914;
    padding: 12px;
    text-align: center;
    border-bottom: 1px solid rgba(255, 255, 255, 0.06);
    position: relative;
  }}
  .card-img {{
    max-height: 200px;
    max-width: 100%;
    object-fit: contain;
    border-radius: 4px;
  }}
  .card-badge {{
    position: absolute;
    top: 10px;
    left: 10px;
    padding: 3px 8px;
    border-radius: 4px;
    font-size: 0.7rem;
    font-weight: 800;
    text-transform: uppercase;
    background: var(--bg-dark);
    color: var(--accent-gold);
    border: 1px solid var(--accent-gold);
  }}
  .card-body {{
    padding: 16px;
    flex-grow: 1;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}
  .card-day {{
    font-size: 0.75rem;
    font-weight: 800;
    color: var(--accent-gold);
    text-transform: uppercase;
    letter-spacing: 1px;
  }}
  .card-title {{
    font-size: 1.05rem;
    font-weight: 700;
    color: #FFFFFF;
    margin: 4px 0 8px 0;
    line-height: 1.3;
  }}
  .card-question {{
    font-size: 0.85rem;
    color: var(--text-secondary);
    margin-bottom: 10px;
  }}
  .card-headline-box {{
    background: rgba(0, 0, 0, 0.25);
    border-left: 3px solid #22C55E;
    padding: 6px 10px;
    border-radius: 0 4px 4px 0;
    font-size: 0.8rem;
    margin-bottom: 12px;
    color: #E2E8F0;
  }}
  .card-rule {{
    font-size: 0.78rem;
    color: var(--accent-gold-light);
    font-style: italic;
    margin-bottom: 12px;
  }}
  .card-btn {{
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(255, 255, 255, 0.15);
    color: #FFFFFF;
    padding: 8px 12px;
    border-radius: 5px;
    font-size: 0.8rem;
    font-weight: 600;
    cursor: pointer;
    transition: background 0.2s;
    text-align: center;
    width: 100%;
  }}
  .card-btn:hover {{
    background: rgba(197, 160, 89, 0.2);
    border-color: var(--accent-gold);
    color: var(--accent-gold);
  }}

  /* Modal */
  .modal-overlay {{
    display: none;
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(0,0,0,0.85);
    backdrop-filter: blur(8px);
    z-index: 1000;
    align-items: center;
    justify-content: center;
    padding: 20px;
  }}
  .modal-overlay.active {{
    display: flex;
  }}
  .modal-content {{
    background: var(--bg-card);
    border: 1px solid var(--accent-gold);
    border-radius: 12px;
    max-width: 800px;
    width: 100%;
    max-height: 90vh;
    overflow-y: auto;
    padding: 28px;
    position: relative;
    box-shadow: 0 20px 60px rgba(0,0,0,0.7);
  }}
  .modal-close {{
    position: absolute;
    top: 18px;
    right: 20px;
    font-size: 1.5rem;
    background: none;
    border: none;
    color: var(--text-secondary);
    cursor: pointer;
  }}
  .modal-close:hover {{
    color: #FFFFFF;
  }}

  /* Footer */
  footer {{
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    padding: 36px 0;
    margin-top: 60px;
    text-align: center;
    font-size: 0.85rem;
    color: var(--text-muted);
  }}
  footer a {{
    color: var(--accent-gold);
  }}
</style>
</head>
<body>

<!-- Navigation -->
<nav class="navbar">
  <div class="nav-brand">
    <span>🎄</span> Tales with Charts · <span>A Christmas Chart Carol</span>
  </div>
  <div class="nav-links">
    <a href="#artworks">Featured Artworks</a>
    <a href="#data-lookup">Data Lookup</a>
    <a href="#masterclass">24-Day Masterclass</a>
    <a href="https://frank-ellingsen.github.io/chart_tales/a_christmas_chart_carol_advent_calendar_2026.pdf" download="a_christmas_chart_carol_advent_calendar_2026.pdf" target="_blank">📅 Advent Calendar PDF</a>
    <a href="https://github.com/Frank-Ellingsen/chart_tales" target="_blank">GitHub Repo</a>
  </div>
</nav>

<!-- Hero -->
<header class="hero-section">
  <div class="container">
    <div class="hero-tag">A 24-Day LinkedIn Advent Series &bull; December 2026</div>
    <h1 class="hero-title">A Christmas Chart Carol</h1>
    <p class="hero-subtitle">
      The Ghosts of Data Past, Present and Yet to Come: Lessons in Charts & Storytelling with Data through the Life and Works of Charles Dickens
    </p>
    <div class="hero-actions">
      <a href="https://frank-ellingsen.github.io/chart_tales/a_christmas_chart_carol_advent_calendar_2026.pdf" download="a_christmas_chart_carol_advent_calendar_2026.pdf" class="btn btn-primary" style="background: linear-gradient(135deg, #C5A059 0%, #B8860B 100%); color: #0A1128; font-weight: 800;">📅 Download 24-Day Advent Calendar (PDF)</a>
      <a href="#artworks" class="btn btn-secondary">🎨 Explore Visuals</a>
      <a href="#data-lookup" class="btn btn-secondary">🔍 Dickens Data Lookup</a>
    </div>
  </div>
</header>

<!-- Featured Dual Artworks Section -->
<section id="artworks" class="section">
  <div class="container">
    <div class="section-header">
      <h2 class="section-title">Featured Master Artworks</h2>
      <p class="section-desc">
        High-resolution visual anchor artworks pairing Victorian Christmas atmosphere with modern data storytelling aesthetics.
      </p>
    </div>

    <div class="dual-artwork-grid">
      <!-- Card 1: image00.png -->
      <div class="artwork-card">
        <div class="artwork-img-box">
          <img src="img24/image00.png" class="artwork-img" alt="A Christmas Chart Carol - Cinematic Master Banner">
        </div>
        <div class="artwork-info">
          <div>
            <div class="artwork-badge">Featured Artwork 01 · Landscape Banner</div>
            <h3 class="artwork-title">A Christmas Chart Carol: The Storyteller Meets Data Storytelling</h3>
            <p class="artwork-meta">
              File: <code>img24/image00.png</code> &bull; Resolution: <strong>1536 &times; 1024</strong> (3:2 Aspect Ratio)
            </p>
            <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 12px;">
              The grand cinematic series banner. Depicts Victorian snowy London with warm candlelight, illuminated Advent calendar windows, and subtle spectral charts emerging from the London fog.
            </p>
          </div>
          <div>
            <a href="img24/image00.png" target="_blank" class="btn btn-secondary" style="font-size: 0.8rem; padding: 6px 14px;">🔎 View Full Resolution</a>
          </div>
        </div>
      </div>

      <!-- Card 2: image001.png -->
      <div class="artwork-card">
        <div class="artwork-img-box">
          <img src="img24/image001.png" class="artwork-img" alt="A Christmas Chart Carol - Collector's Portrait Card">
        </div>
        <div class="artwork-info">
          <div>
            <div class="artwork-badge">Featured Artwork 02 · Portrait Cover Card</div>
            <h3 class="artwork-title">The Ghosts of Data Past, Present & Yet to Come</h3>
            <p class="artwork-meta">
              File: <code>img24/image001.png</code> &bull; Resolution: <strong>1024 &times; 1536</strong> (2:3 Aspect Ratio)
            </p>
            <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 12px;">
              The collector's edition vertical portrait. Designed for mobile feeds and publication cover pages, highlighting the three data visitations in rich Victorian crimson and gold.
            </p>
          </div>
          <div>
            <a href="img24/image001.png" target="_blank" class="btn btn-secondary" style="font-size: 0.8rem; padding: 6px 14px;">🔎 View Full Resolution</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Interactive Data Lookup Section -->
<section id="data-lookup" class="section" style="background: rgba(0,0,0,0.25);">
  <div class="container">
    <div class="section-header">
      <h2 class="section-title">Charles Dickens Data Lookup</h2>
      <p class="section-desc">
        Explore structured datasets from <code>data/dickens/</code> powering all 25 daily charts, lessons, and narratives.
      </p>
    </div>

    <div class="data-lookup-wrapper">
      <div class="tab-bar">
        <button class="tab-btn active" onclick="switchTab('novels')">📚 Master Novels ({len(novels_data)})</button>
        <button class="tab-btn" onclick="switchTab('adaptations')">🎬 Film, TV & Theater Adaptations ({len(adaptations_data)})</button>
        <button class="tab-btn" onclick="switchTab('biography')">⏳ Biographical Milestones ({len(bio_data)})</button>
        <button class="tab-btn" onclick="switchTab('lore')">💡 Quotes & Fun Facts</button>
      </div>

      <div class="search-box-row">
        <input type="text" id="searchInput" class="search-input" placeholder="Search by title, character, year, or keyword..." oninput="filterData()">
        <div id="resultCount" class="filter-count">Showing all records</div>
      </div>

      <div class="table-responsive" id="tableContainer">
        <!-- Injected via JavaScript -->
      </div>
    </div>
  </div>
</section>

<!-- 25-Day Visual Gallery & Masterclass -->
<section id="masterclass" class="section">
  <div class="container">
    <div class="section-header">
      <h2 class="section-title">The 25-Day Visual Masterclass</h2>
      <p class="section-desc">
        Daily lessons in Headlines, Direct Labeling vs Legends, Annotations, and Tufte's Data-Ink Ratio.
      </p>
    </div>

    <div class="masterclass-grid" id="masterclassGrid">
      <!-- Populated via JavaScript -->
    </div>
  </div>
</section>

<!-- LinkedIn Post Modal -->
<div id="postModal" class="modal-overlay" onclick="closeModal(event)">
  <div class="modal-content" onclick="event.stopPropagation()">
    <button class="modal-close" onclick="closeModal()">&times;</button>
    <div id="modalBody"></div>
  </div>
</div>

<!-- Footer -->
<footer>
  <div class="container">
    <p>
      <strong>A Christmas Chart Carol</strong> &bull; Created by <strong>Frank Ellingsen</strong> | <em>Tales with Charts</em>
    </p>
    <p style="margin-top: 6px;">
      Grounded in the works of Charles Dickens, Edward Tufte's Data-Ink Ratio, and the Financial Times Visual Vocabulary.
    </p>
    <p style="margin-top: 8px;">
      <a href="https://github.com/Frank-Ellingsen/chart_tales" target="_blank">GitHub: Frank-Ellingsen/chart_tales</a> &bull; 
      <a href="https://frank-ellingsen.github.io/chart_tales/a_christmas_chart_carol_advent_calendar_2026.pdf" download="a_christmas_chart_carol_advent_calendar_2026.pdf" target="_blank">📅 Download 24-Day Advent Calendar PDF</a> &bull; 
      <a href="https://frank-ellingsen.github.io/datafrank.github.io/" target="_blank">Portfolio</a>
    </p>
  </div>
</footer>

<script>
  const novelsData = {novels_json};
  const adaptationsData = {adaptations_json};
  const bioData = {bio_json};
  const postsData = {posts_json};

  let currentTab = 'novels';

  function switchTab(tab) {{
    currentTab = tab;
    document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
    event.target.classList.add('active');
    document.getElementById('searchInput').value = '';
    renderTable();
  }}

  function renderTable(filterText = '') {{
    const container = document.getElementById('tableContainer');
    const countEl = document.getElementById('resultCount');
    const query = filterText.toLowerCase().trim();

    if (currentTab === 'novels') {{
      const filtered = novelsData.filter(d => 
        d.title.toLowerCase().includes(query) || 
        d.key_theme.toLowerCase().includes(query) ||
        String(d.year_start).includes(query)
      );
      countEl.innerText = `Showing ${{filtered.length}} of ${{novelsData.length}} novels`;

      let html = `<table class="data-table">
        <thead>
          <tr>
            <th>Title</th>
            <th>Years</th>
            <th>Type</th>
            <th>Word Count</th>
            <th>Characters</th>
            <th>Adaptations</th>
            <th>Key Theme</th>
          </tr>
        </thead>
        <tbody>`;
      filtered.forEach(d => {{
        html += `<tr>
          <td><strong>${{d.title}}</strong></td>
          <td>${{d.year_start}}${{d.year_end !== d.year_start ? '–' + d.year_end : ''}}</td>
          <td><span class="badge-tag" style="background: rgba(197,160,89,0.15); color: var(--accent-gold);">${{d.type}}</span></td>
          <td><strong>${{Number(d.word_count).toLocaleString()}}</strong></td>
          <td>${{d.characters}}</td>
          <td><span class="badge-tag rating-badge">${{d.adaptations}}</span></td>
          <td style="color: var(--text-secondary);">${{d.key_theme}}</td>
        </tr>`;
      }});
      html += `</tbody></table>`;
      container.innerHTML = html;

    }} else if (currentTab === 'adaptations') {{
      const filtered = adaptationsData.filter(d => 
        d.title.toLowerCase().includes(query) || 
        d.work.toLowerCase().includes(query) ||
        d.medium.toLowerCase().includes(query) ||
        d.notable_feature.toLowerCase().includes(query)
      );
      countEl.innerText = `Showing ${{filtered.length}} of ${{adaptationsData.length}} adaptations`;

      let html = `<table class="data-table">
        <thead>
          <tr>
            <th>Production Title</th>
            <th>Source Work</th>
            <th>Year</th>
            <th>Medium</th>
            <th>IMDb</th>
            <th>Notable Features</th>
          </tr>
        </thead>
        <tbody>`;
      filtered.forEach(d => {{
        html += `<tr>
          <td><strong>${{d.title}}</strong></td>
          <td><em>${{d.work}}</em></td>
          <td>${{d.year}}</td>
          <td><span class="badge-tag" style="background: rgba(59,130,246,0.15); color: #60A5FA;">${{d.medium}}</span></td>
          <td><span class="badge-tag rating-badge">⭐ ${{d.imdb_rating}}</span></td>
          <td style="color: var(--text-secondary);">${{d.notable_feature}}</td>
        </tr>`;
      }});
      html += `</tbody></table>`;
      container.innerHTML = html;

    }} else if (currentTab === 'biography') {{
      const filtered = bioData.filter(d => 
        d.event.toLowerCase().includes(query) || 
        d.notes.toLowerCase().includes(query) ||
        String(d.year).includes(query)
      );
      countEl.innerText = `Showing ${{filtered.length}} of ${{bioData.length}} milestones`;

      let html = `<table class="data-table">
        <thead>
          <tr>
            <th>Year</th>
            <th>Age</th>
            <th>Milestone Event</th>
            <th>Key Metric</th>
            <th>Historical Context & Notes</th>
          </tr>
        </thead>
        <tbody>`;
      filtered.forEach(d => {{
        html += `<tr>
          <td><strong style="color: var(--accent-gold);">${{d.year}}</strong></td>
          <td>${{d.age}}</td>
          <td><strong>${{d.event}}</strong></td>
          <td>${{d.metric_name}}: <strong>${{Number(d.metric_value).toLocaleString()}}</strong></td>
          <td style="color: var(--text-secondary);">${{d.notes}}</td>
        </tr>`;
      }});
      html += `</tbody></table>`;
      container.innerHTML = html;

    }} else if (currentTab === 'lore') {{
      const filtered = postsData.filter(p => 
        p.fun_fact.toLowerCase().includes(query) || 
        p.quote.toLowerCase().includes(query) ||
        p.title.toLowerCase().includes(query)
      );
      countEl.innerText = `Showing ${{filtered.length}} lore entries`;

      let html = `<table class="data-table">
        <thead>
          <tr>
            <th style="width: 15%;">Day & Work</th>
            <th style="width: 45%;">💡 Dickens Eccentric Lore & Fun Fact</th>
            <th style="width: 40%;">💬 Famous Quote</th>
          </tr>
        </thead>
        <tbody>`;
      filtered.forEach(p => {{
        html += `<tr>
          <td><strong>${{p.day}}</strong><br><small style="color: var(--text-muted);">${{p.title}}</small></td>
          <td style="color: #BBF7D0;">${{p.fun_fact}}</td>
          <td style="color: #FEF08A; font-style: italic;">${{p.quote}}</td>
        </tr>`;
      }});
      html += `</tbody></table>`;
      container.innerHTML = html;
    }}
  }}

  function filterData() {{
    const text = document.getElementById('searchInput').value;
    renderTable(text);
  }}

  // Render Masterclass 25-Day Grid
  function renderMasterclass() {{
    const grid = document.getElementById('masterclassGrid');
    let html = '';
    postsData.forEach(p => {{
      html += `<div class="masterclass-card">
        <div class="card-img-wrap">
          <span class="card-badge">${{p.day}}</span>
          <img src="${{p.image}}" class="card-img" alt="${{p.title}}">
        </div>
        <div class="card-body">
          <div>
            <div class="card-day">${{p.act}} &bull; ${{p.chart_type}}</div>
            <h3 class="card-title">${{p.title}}</h3>
            <p class="card-question">❓ <em>${{p.question}}</em></p>
            <div class="card-headline-box">
              <span style="color: #4ADE80; font-weight: 700;">Action Headline:</span><br>
              ${{p.action_headline}}
            </div>
            <p class="card-rule">💡 ${{p.rule}}</p>
          </div>
          <div>
            <button class="card-btn" onclick="openModal(${{p.id}})">📱 View Full LinkedIn Post Copy</button>
          </div>
        </div>
      </div>`;
    }});
    grid.innerHTML = html;
  }}

  function openModal(id) {{
    const p = postsData.find(item => item.id === id);
    if (!p) return;

    const modalBody = document.getElementById('modalBody');
    modalBody.innerHTML = `
      <div style="font-size: 0.8rem; font-weight: 800; color: var(--accent-gold); text-transform: uppercase;">
        ${{p.day}} | ${{p.act}} &bull; ${{p.chart_type}}
      </div>
      <h2 style="font-size: 1.5rem; color: #FFFFFF; margin: 4px 0 12px 0;">${{p.title}}</h2>
      
      <div style="background: rgba(0,0,0,0.3); border-left: 3px solid #22C55E; padding: 10px 14px; border-radius: 4px; margin-bottom: 16px;">
        <strong style="color: #4ADE80;">✅ Action-Driven Headline:</strong><br>
        ${{p.action_headline}}
      </div>

      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-bottom: 16px;">
        <div style="background: rgba(255,255,255,0.04); padding: 12px; border-radius: 6px; font-size: 0.85rem;">
          <strong style="color: var(--accent-gold);">📜 Dickens Data Anchor:</strong><br>
          ${{p.key_metric}}
        </div>
        <div style="background: rgba(255,255,255,0.04); padding: 12px; border-radius: 6px; font-size: 0.85rem;">
          <strong style="color: #FBBF24;">💬 Famous Quote:</strong><br>
          <em>${{p.quote}}</em>
        </div>
      </div>

      <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; padding: 16px; margin-bottom: 16px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
          <strong style="color: #60A5FA;">📱 LinkedIn Post Text (Ready to Copy):</strong>
          <button class="btn btn-primary" style="padding: 4px 12px; font-size: 0.75rem;" onclick="copyPostText()">📋 Copy Text</button>
        </div>
        <div id="copyTarget" style="font-size: 0.9rem; line-height: 1.5; color: #E2E8F0; white-space: pre-line;">
${{p.post_copy.replace(/<br>/g, '\\n').replace(/<strong>/g, '').replace(/<\\/strong>/g, '').replace(/<em>/g, '').replace(/<\\/em>/g, '').replace(/<ul>/g, '').replace(/<\\/ul>/g, '').replace(/<ol>/g, '').replace(/<\\/ol>/g, '').replace(/<li>/g, '• ').replace(/<\\/li>/g, '').replace(/&quot;/g, '"')}}
        </div>
      </div>

      <div style="background: rgba(197, 160, 89, 0.15); border-left: 3px solid var(--accent-gold); padding: 10px 14px; border-radius: 4px; font-size: 0.85rem;">
        <strong style="color: var(--accent-gold);">🎯 Tufte Design & Storytelling Rule:</strong><br>
        ${{p.storytelling_rule}}
      </div>
    `;

    document.getElementById('postModal').classList.add('active');
  }}

  function closeModal(e) {{
    document.getElementById('postModal').classList.remove('active');
  }}

  function copyPostText() {{
    const text = document.getElementById('copyTarget').innerText;
    navigator.clipboard.writeText(text).then(() => {{
      alert('LinkedIn Post copied to clipboard!');
    }});
  }}

  // Initial Load
  window.onload = function() {{
    renderTable();
    renderMasterclass();
  }};
</script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Generated clean, interactive index.html ({len(html_content)} bytes)")
