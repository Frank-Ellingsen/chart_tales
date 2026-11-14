import os
import generate_pdf_report as gen

md_lines = [
    '# A Christmas Chart Carol — 25 LinkedIn Masterclass Posts',
    '### *Lessons in Charts & Storytelling with Data through the Life and Works of Charles Dickens*',
    '**Author:** Frank Ellingsen | *Tales with Charts*',
    '**Visual Assets:** `img24/img0.png` through `img24/image24.png`',
    '**Data Source:** `data/dickens/` (Dickens biography, novels, adaptations, quotes, and fun facts)',
    '**Core Pedagogy:** Action Headlines, Direct Labeling vs Legends, Annotations, Tufte Data-Ink Ratio, FT Visual Vocabulary',
    '',
    '---',
    ''
]

for p in gen.dickens_posts:
    md_lines.append(f"## 🎄 {p['day']} | {p['title']}")
    md_lines.append(f"**Act:** {p['act']}")
    md_lines.append(f"**Visual Asset:** [{os.path.basename(p['image'])}](file:///c:/Users/frank/Desktop/A%20Charts%20Tale/{p['image']})")
    md_lines.append(f"**Visual Vocabulary Category:** {p['chart_type']}")
    md_lines.append(f"**Core Question:** *{p['question']}*")
    md_lines.append('')
    md_lines.append('### 📜 Charles Dickens Real-Life Data Anchor:')
    md_lines.append(f"- **Historical Theme:** {p['dickens_data']['theme']}")
    md_lines.append(f"- **Key Figures & Metrics:** {p['dickens_data']['key_metric']}")
    md_lines.append(f"- **Context:** {p['dickens_data']['historical_context']}")
    md_lines.append(f"- **💡 Fun Fact:** {p['dickens_data']['fun_fact']}")
    md_lines.append(f"- **💬 Famous Quote:** {p['quote']}")
    md_lines.append('')
    md_lines.append('### 📊 Chart & Storytelling Lesson (Headlines, Legends, Labels):')
    md_lines.append(f"- ❌ **Weak Generic Title:** `{p['headline_lesson']['bad_title']}`")
    md_lines.append(f"- ✅ **Action-Driven Headline:** **{p['headline_lesson']['action_headline']}**")
    md_lines.append(f"- **Design Rule:** {p['headline_lesson']['rule']}")
    md_lines.append(f"- **Tufte Takeaway:** {p['storytelling_rule']}")
    md_lines.append('')
    md_lines.append('### 📱 LinkedIn Post Copy (Ready to Publish):')
    md_lines.append('')
    copy = p['post_copy'].replace('<br>', '\n').replace('<strong>', '**').replace('</strong>', '**')
    copy = copy.replace('<em>', '*').replace('</em>', '*').replace('<code>', '`').replace('</code>', '`')
    copy = copy.replace('<ul>', '').replace('</ul>', '').replace('<ol>', '').replace('</ol>', '')
    copy = copy.replace('<li>', '- ').replace('</li>', '')
    md_lines.append(copy)
    md_lines.append('')
    md_lines.append('---')
    md_lines.append('')

with open('linkedin_posts_25_series.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(md_lines))

print('Updated linkedin_posts_25_series.md successfully.')

