import os
import sys
import subprocess
import base64
import io
import datetime
from PIL import Image
import generate_pdf_report as gen

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

def image_to_base64_jpeg(image_path, quality=86, max_size=1400):
    if not os.path.exists(image_path):
        print(f"Warning: Image {image_path} not found")
        return ""
    img = Image.open(image_path)
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")
    if max(img.size) > max_size:
        img.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
    buffer = io.BytesIO()
    img.save(buffer, format="JPEG", quality=quality, optimize=True)
    b64_data = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return f"data:image/jpeg;base64,{b64_data}"

def build_calendar_html(days_subset, title_suffix, total_calendar_days=24):
    """
    days_subset: list of post objects (e.g. days 1 to 24 or days 1 to 12)
    title_suffix: e.g. "Complete 24-Day Edition" or "Part 1 (Dec 1–12 Edition)"
    """
    cover_b64 = image_to_base64_jpeg("img24/image00.png", quality=90, max_size=1500)
    
    # Preload images
    images_b64 = {}
    for p in days_subset:
        path = p["image"]
        if path not in images_b64:
            images_b64[path] = image_to_base64_jpeg(path, quality=86, max_size=1200)

    total_pages = len(days_subset) + 1  # 1 cover + daily pages

    # CSS styles
    css = """
  @page {
    size: A4 portrait;
    margin: 0;
  }
  * {
    box-sizing: border-box;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
  }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    margin: 0;
    padding: 0;
    background: #0A1128;
    color: #1E293B;
  }

  /* FRONT COVER PAGE */
  .cover-page {
    page-break-after: always;
    break-after: page;
    height: 297mm;
    max-height: 297mm;
    box-sizing: border-box;
    padding: 12mm 12mm 8mm 12mm;
    background: radial-gradient(circle at 50% 20%, #162B5B 0%, #0A1128 75%);
    color: #F8FAFC;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    text-align: center;
  }
  .cover-badge {
    display: inline-block;
    padding: 5px 18px;
    background: rgba(197, 160, 89, 0.2);
    border: 1px solid #C5A059;
    border-radius: 20px;
    font-size: 8.5pt;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: #C5A059;
    margin: 0 auto 8px auto;
  }
  .cover-title {
    font-size: 26pt;
    font-weight: 900;
    line-height: 1.15;
    margin: 0 0 6px 0;
    background: linear-gradient(135deg, #FFFFFF 20%, #E9D5A1 60%, #C5A059 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: -0.5px;
  }
  .cover-subtitle {
    font-size: 11pt;
    font-style: italic;
    color: #CBD5E1;
    max-width: 650px;
    margin: 0 auto 12px auto;
    line-height: 1.35;
  }
  .cover-hero-img-box {
    margin: 4px auto 12px auto;
    text-align: center;
    border: 2px solid #C5A059;
    border-radius: 8px;
    padding: 5px;
    background: #050914;
    box-shadow: 0 10px 30px rgba(0,0,0,0.6);
    max-width: 580px;
  }
  .cover-hero-img {
    width: 100%;
    max-height: 330px;
    object-fit: contain;
    border-radius: 6px;
    display: block;
  }
  .cover-meta-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
    max-width: 620px;
    margin: 0 auto 12px auto;
  }
  .cover-meta-card {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(197, 160, 89, 0.35);
    border-radius: 6px;
    padding: 8px 10px;
    text-align: left;
  }
  .cover-meta-card strong {
    color: #C5A059;
    font-size: 7.5pt;
    text-transform: uppercase;
    display: block;
    margin-bottom: 2px;
  }
  .cover-meta-card span {
    font-size: 8.2pt;
    color: #F1F5F9;
  }
  .cover-footer {
    border-top: 1px solid rgba(255, 255, 255, 0.15);
    padding-top: 8px;
    font-size: 7.8pt;
    color: #94A3B8;
    display: flex;
    justify-content: space-between;
  }

  /* DAILY ADVENT CALENDAR PAGE */
  .cal-page {
    page-break-after: always;
    break-after: page;
    height: 297mm;
    max-height: 297mm;
    box-sizing: border-box;
    padding: 8mm 10mm;
    background: #FFFFFF;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  /* Top Date & Window Header */
  .cal-day-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid #0A1128;
    padding-bottom: 6px;
    margin-bottom: 6px;
  }
  .cal-date-badge {
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .day-number-box {
    background: #0A1128;
    color: #C5A059;
    border: 2px solid #C5A059;
    border-radius: 6px;
    font-size: 18pt;
    font-weight: 900;
    width: 44px;
    height: 44px;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 3px 6px rgba(0,0,0,0.15);
  }
  .day-date-text {
    text-align: left;
  }
  .weekday-month {
    font-size: 13pt;
    font-weight: 800;
    color: #0A1128;
    letter-spacing: -0.3px;
    line-height: 1.15;
  }
  .series-tag {
    font-size: 7.8pt;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: #64748B;
    margin-top: 2px;
  }
  .chart-type-pill {
    background: rgba(10, 17, 40, 0.08);
    border: 1px solid #CBD5E1;
    color: #0A1128;
    padding: 5px 12px;
    border-radius: 20px;
    font-size: 8pt;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 1px;
  }

  /* Action Headline Bar */
  .action-headline-bar {
    background: #0A1128;
    border-left: 5px solid #22C55E;
    border-radius: 0 6px 6px 0;
    padding: 7px 12px;
    margin-bottom: 7px;
  }
  .headline-label {
    font-size: 6.8pt;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: #22C55E;
    margin-bottom: 2px;
  }
  .headline-text {
    font-size: 10.5pt;
    font-weight: 800;
    color: #FFFFFF;
    margin: 0;
    line-height: 1.25;
  }

  /* Visual Hero Centerpiece */
  .visual-hero-box {
    background: #050914;
    border: 1px solid #1E293B;
    border-radius: 8px;
    padding: 8px;
    text-align: center;
    box-shadow: 0 4px 14px rgba(0,0,0,0.08);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    flex-grow: 1;
    max-height: 500px;
    margin-bottom: 7px;
  }
  .visual-hero-img {
    max-width: 100%;
    max-height: 460px;
    object-fit: contain;
    border-radius: 4px;
    display: block;
  }
  .visual-caption-row {
    width: 100%;
    display: flex;
    justify-content: space-between;
    padding: 4px 6px 0 6px;
    font-size: 6.8pt;
    color: #94A3B8;
    border-top: 1px solid rgba(255,255,255,0.08);
    margin-top: 4px;
  }
  .visual-caption-row strong {
    color: #E2E8F0;
  }

  /* Bottom Tri-Card Information Grid */
  .cal-bottom-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 8px;
    margin-bottom: 6px;
  }
  .info-card {
    border-radius: 6px;
    padding: 7px 9px;
    font-size: 7.2pt;
    line-height: 1.35;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .card-header-tag {
    font-size: 6.8pt;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin-bottom: 4px;
    display: flex;
    align-items: center;
    gap: 4px;
  }

  .card-lesson {
    background: #FFFBEB;
    border: 1px solid #FCD34D;
    border-top: 3px solid #F59E0B;
  }
  .card-lesson .card-header-tag { color: #B45309; }

  .card-data {
    background: #F0FDF4;
    border: 1px solid #BBF7D0;
    border-top: 3px solid #10B981;
  }
  .card-data .card-header-tag { color: #047857; }

  .card-lore {
    background: #EFF6FF;
    border: 1px solid #BFDBFE;
    border-top: 3px solid #3B82F6;
  }
  .card-lore .card-header-tag { color: #1D4ED8; }

  .quote-italic {
    font-style: italic;
    color: #1E3A8A;
    margin-top: 3px;
    border-left: 2px solid #3B82F6;
    padding-left: 4px;
  }

  /* Calendar Page Footer */
  .cal-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid #E2E8F0;
    padding-top: 4px;
    font-size: 6.8pt;
    color: #64748B;
  }
  """

    # Build Cover Page HTML
    cover_html = f"""
<div class="cover-page">
  <div>
    <div class="cover-badge">Advent Calendar &bull; December 2026</div>
    <h1 class="cover-title">A Christmas Chart Carol</h1>
    <div class="cover-subtitle">
      24 Lessons in Charts & Storytelling with Data through the Life and Works of Charles Dickens
      <br><span style="font-size: 9.5pt; color: #C5A059; font-weight: 700;">{title_suffix}</span>
    </div>
  </div>

  <div class="cover-hero-img-box">
    <img src="{cover_b64}" class="cover-hero-img" alt="A Christmas Chart Carol - Cover Poster image00">
  </div>

  <div class="cover-meta-grid">
    <div class="cover-meta-card">
      <strong>Author & Curator</strong>
      <span>Frank Ellingsen &bull; Tales with Charts</span>
    </div>
    <div class="cover-meta-card">
      <strong>Design Discipline</strong>
      <span>Edward Tufte Data-Ink & FT Visual Vocab</span>
    </div>
    <div class="cover-meta-card">
      <strong>Dataset Scope</strong>
      <span>Novels, Screen Adaptations, 1812–1870 Canon</span>
    </div>
  </div>

  <div class="cover-footer">
    <div>A Christmas Chart Carol &bull; December 2026 Advent Calendar</div>
    <div>Tales with Charts &bull; Portfolio: frank-ellingsen.github.io/chart_tales</div>
    <div>Page 1 of {total_pages}</div>
  </div>
</div>
"""

    # Build Daily Pages
    daily_pages = []
    page_counter = 2
    for p in days_subset:
        day_num = p["id"]
        # December 2026 date
        dt = datetime.date(2026, 12, day_num)
        weekday_name = dt.strftime("%A")
        formatted_date = f"{weekday_name}, {day_num} December 2026"
        
        img_b64 = images_b64[p["image"]]
        short_chart_type = p["chart_type"].split("(")[0].strip()

        page_html = f"""
<div class="cal-page">
  <!-- Top Header -->
  <div class="cal-day-header">
    <div class="cal-date-badge">
      <div class="day-number-box">{day_num:02d}</div>
      <div class="day-date-text">
        <div class="weekday-month">{formatted_date}</div>
        <div class="series-tag">Advent Window {day_num} of {total_calendar_days} &bull; {p['act']}</div>
      </div>
    </div>
    <div class="chart-type-pill">{short_chart_type}</div>
  </div>

  <!-- Action Headline -->
  <div class="action-headline-bar">
    <div class="headline-label">Action Headline &bull; The Key Takeaway</div>
    <div class="headline-text">"{p['headline_lesson']['action_headline']}"</div>
  </div>

  <!-- Hero Visual Centerpiece -->
  <div class="visual-hero-box">
    <img src="{img_b64}" class="visual-hero-img" alt="{p['title']}">
    <div class="visual-caption-row">
      <span>Visual Asset: <strong>{os.path.basename(p['image'])}</strong></span>
      <span>Topic: <strong>{p['title']}</strong></span>
      <span>Discipline: <strong>{p['chart_type']}</strong></span>
    </div>
  </div>

  <!-- Bottom Tri-Grid Information Cards -->
  <div class="cal-bottom-grid">
    <!-- Card 1: Storytelling & Tufte Principle -->
    <div class="info-card card-lesson">
      <div class="card-header-tag">📊 Storytelling & Tufte Principle</div>
      <div>
        <div style="color: #991B1B; margin-bottom: 2px;">❌ <strong>Weak Topic:</strong> {p['headline_lesson']['bad_title']}</div>
        <div style="color: #92400E; margin-bottom: 2px;"><strong>Rule:</strong> {p['headline_lesson']['rule']}</div>
        <div style="color: #78350F; font-size: 6.8pt; font-style: italic;"><strong>Tufte:</strong> {p['storytelling_rule']}</div>
      </div>
    </div>

    <!-- Card 2: Charles Dickens Real Data -->
    <div class="info-card card-data">
      <div class="card-header-tag">📜 Charles Dickens Data Anchor</div>
      <div>
        <div style="font-weight: 700; color: #065F46; margin-bottom: 2px;">{p['dickens_data']['theme']}</div>
        <div style="color: #047857; margin-bottom: 2px;"><strong>Metrics:</strong> {p['dickens_data']['key_metric']}</div>
        <div style="color: #064E3B; font-size: 6.8pt;">{p['dickens_data']['historical_context']}</div>
      </div>
    </div>

    <!-- Card 3: Victorian Lore & Quotation -->
    <div class="info-card card-lore">
      <div class="card-header-tag">💡 Victorian Lore & Quote</div>
      <div>
        <div style="color: #1E40AF; margin-bottom: 2px;"><strong>Fun Fact:</strong> {p['dickens_data']['fun_fact']}</div>
        <div class="quote-italic">{p['quote']}</div>
      </div>
    </div>
  </div>

  <!-- Calendar Page Footer -->
  <div class="cal-footer">
    <div>A Christmas Chart Carol &bull; December 2026 Advent Calendar &bull; Day {day_num} of {total_calendar_days}</div>
    <div>Tales with Charts &bull; Frank Ellingsen</div>
    <div>Page {page_counter} of {total_pages}</div>
  </div>
</div>
"""
        daily_pages.append(page_html)
        page_counter += 1

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>A Christmas Chart Carol — 24-Day Advent Calendar (December 2026)</title>
<style>
{css}
</style>
</head>
<body>
{cover_html}
{"".join(daily_pages)}
</body>
</html>
"""
    return full_html

def render_pdf(html_filename, pdf_filename):
    print(f"Rendering {pdf_filename} with Edge headless...")
    abs_html = os.path.abspath(html_filename)
    abs_pdf = os.path.abspath(pdf_filename)

    cmd = [
        EDGE_PATH,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={abs_pdf}",
        f"file:///{abs_html.replace(os.sep, '/')}"
    ]

    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0 and os.path.exists(pdf_filename):
        size_mb = os.path.getsize(pdf_filename) / (1024 * 1024)
        print(f"SUCCESS: Generated PDF at {pdf_filename} ({size_mb:.2f} MB)")
        return True
    else:
        print(f"ERROR rendering {pdf_filename}: {res.stderr}")
        return False

def main():
    # Filter days 1 to 24 from dickens_posts
    days_1_to_24 = [p for p in gen.dickens_posts if 1 <= p["id"] <= 24]
    days_1_to_12 = [p for p in gen.dickens_posts if 1 <= p["id"] <= 12]

    # 1. Generate Full 24-Day Advent Calendar (1 to 24 Dec 2026) -> 25 pages (Cover + 24 days)
    html_24 = build_calendar_html(days_1_to_24, "Complete 24-Day Calendar (1–24 Dec 2026)", total_calendar_days=24)
    with open("a_christmas_chart_carol_advent_calendar_2026.html", "w", encoding="utf-8") as f:
        f.write(html_24)
    render_pdf("a_christmas_chart_carol_advent_calendar_2026.html", "a_christmas_chart_carol_advent_calendar_2026.pdf")

    # 2. Generate 12-Day Advent Calendar (1 to 12 Dec 2026) -> 13 pages (Cover + 12 days)
    html_12 = build_calendar_html(days_1_to_12, "Part 1 Edition (1–12 Dec 2026)", total_calendar_days=12)
    with open("a_christmas_chart_carol_advent_calendar_1_to_12_dec_2026.html", "w", encoding="utf-8") as f:
        f.write(html_12)
    render_pdf("a_christmas_chart_carol_advent_calendar_1_to_12_dec_2026.html", "a_christmas_chart_carol_advent_calendar_1_to_12_dec_2026.pdf")

if __name__ == "__main__":
    main()
