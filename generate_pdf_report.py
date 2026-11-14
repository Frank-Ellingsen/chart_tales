import os
import sys
import io
import base64
import subprocess
from PIL import Image

def image_to_base64_jpeg(path, quality=88, max_size=1400):
    if not os.path.exists(path):
        return ""
    im = Image.open(path).convert("RGB")
    # Resize slightly if too large to keep PDF crisp yet lightweight
    if max(im.size) > max_size:
        im.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, format="JPEG", quality=quality, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode("utf-8")

def image_to_thumbnail_jpeg(path, max_size=320, quality=80):
    if not os.path.exists(path):
        return ""
    im = Image.open(path).convert("RGB")
    im.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, format="JPEG", quality=quality, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode("utf-8")

dickens_posts = [
    {
        "id": 0,
        "act": "SERIES PROLOGUE & LAUNCH",
        "day": "TEASER",
        "title": "A Christmas Chart Carol: The Storyteller Meets Data Storytelling",
        "chart_type": "Advent Series Poster & Narrative Framework",
        "question": "What if an Advent calendar taught you data storytelling through Charles Dickens?",
        "image": "img24/image00.png",
        "dickens_data": {
            "theme": "Charles Dickens' 35-Year Career & Victorian Legacy (1812–1870)",
            "key_metric": "15 Major Novels | 5 Christmas Books | 989+ Named Characters | 300+ Screen Adaptations",
            "historical_context": "Dickens wrote over 4.5 million words and walked 15 miles a night through London slums. He was the world's first true multimedia celebrity author.",
            "fun_fact": "Dickens insisted his writing desk and bed must always face due North, believing the Earth's magnetic currents enhanced his mental clarity and creativity!"
        },
        "quote": "“There is nothing in the world so irresistibly contagious as laughter and good humour.” — A Christmas Carol (1843)",
        "headline_lesson": {
            "bad_title": "Charles Dickens: Biographical and Literary Statistics",
            "action_headline": "From Factory Boy to Global Literary Titan: How Dickens Captured the Human Heart in 4.5 Million Words",
            "rule": "Headlines must announce the insight, not just label the topic. Never force the reader to guess what the chart proves."
        },
        "post_copy": """🎄 <strong>What if your December Advent calendar opened a masterclass in data storytelling instead of a chocolate?</strong><br><br>
There are numbers that are dead to us.<br>
Last quarter's KPI spreadsheet. An archived database table. A chart presented in March, buried under 50 slides, and forgotten by noon.<br><br>
We see bars. We see axes. We see color legends.<br>
What we so rarely see is the <strong>story</strong>.<br><br>
Charles Dickens knew the secret over 180 years ago: <em>Facts alone do not move human beings. Only stories give numbers meaning.</em><br><br>
Starting <strong>1 December</strong>, welcome to:<br>
📖 <strong>A Christmas Chart Carol: 24 Days of Charts, Storytelling & Charles Dickens</strong><br><br>
Across 24 days, we will journey through the life, masterworks, screen adaptations, theater triumphs, and eccentric habits of Charles Dickens—while delivering a daily practical lesson in modern data visualization:<br><br>
<ul>
  <li>👻 <strong>Act I & The Ghost of Data Past (Days 1–12):</strong> Chart selection, action headlines, direct labeling vs. legends, and how to reveal historical trajectory without clutter.</li>
  <li>🕯️ <strong>The Ghost of Data Present (Days 13–18):</strong> Distributions, outliers, correlation vs. causation, and avoiding the trap of misleading averages.</li>
  <li>🔮 <strong>The Ghost of Data Yet to Come (Days 19–23):</strong> Modeling uncertainty, fan charts, scenario planning, and forecasting what Dickens left unfinished.</li>
  <li>🎄 <strong>Christmas Eve (Day 24):</strong> The Grand Finale: <em>Charles Dickens: A Life in Data (1812–1870)</em>.</li>
</ul>
Every single post includes a collectible Victorian-meets-modern chart visual, authentic literary data, Dickens quotes, eccentric trivia, and an actionable rule on <strong>Headlines, Legends, Labels, and the Data-Ink Ratio</strong>.<br><br>
Window 1 opens tomorrow, <strong>1 December</strong>.<br><br>
<em>Because numbers have long memories... but stories give them a voice.</em><br><br>
🔗 Follow the series: https://frank-ellingsen.github.io/chart_tales/<br><br>
#DataStorytelling #DataVisualization #CharlesDickens #AChristmasChartCarol #Infographics #PowerBI #Tufte #VisualVocabulary""",
        "storytelling_rule": "The Narrative Arc: Every chart must have a protagonist (the data point that matters), an antagonist (the obstacle, variance, or comparison), and a resolution (the decision or insight)."
    },
    {
        "id": 1,
        "act": "ACT I: OPENING THE WINDOWS",
        "day": "DAY 1",
        "title": "The Bar Chart: Measuring the Dickensian Giants",
        "chart_type": "Magnitude / Horizontal Ranking (FT Visual Vocabulary)",
        "question": "Which of Dickens' 15 major novels is the longest?",
        "image": "img24/image1.png",
        "dickens_data": {
            "theme": "Novel Word Counts (from data/dickens/dickens_novels.csv)",
            "key_metric": "David Copperfield: 360,000 words | Bleak House: 356,000 words | Dombey & Son: 357,000 words | Hard Times: 105,000 words",
            "historical_context": "Dickens was paid by monthly installment. Longer serial runs allowed deeper subplots, but required extraordinary pacing discipline.",
            "fun_fact": "David Copperfield was Dickens' personal 'favourite child'. It contains over 156 named characters and spans 360,000 words—more than three times the length of Hard Times!"
        },
        "quote": "“Whether I shall turn out to be the hero of my own life, or whether that station will be held by anybody else, these pages must show.” — David Copperfield (1849)",
        "headline_lesson": {
            "bad_title": "Word Counts of Charles Dickens' Major Works",
            "action_headline": "David Copperfield Reigns Supreme at 360,000 Words—More Than Triple the Length of Hard Times",
            "rule": "Action Headlines: Replace static topic labels with a complete sentence stating the primary finding."
        },
        "post_copy": """🎄 <strong>DAY 1 | A Christmas Chart Carol</strong><br>
<em>Window 1: The Horizontal Bar Chart</em><br><br>
Behind our very first window stands the most reliable veteran of information design: the <strong>horizontal bar chart</strong>.<br><br>
Simple? Yes. Boring? Only when your headline is.<br><br>
Today's Dickensian question: <strong>Which of Charles Dickens' 15 major novels is the true literary heavyweight?</strong><br><br>
Looking at the data from our Dickens archive:
<ul>
  <li>🥇 <strong>David Copperfield (1850):</strong> 360,000 words (his personal favourite)</li>
  <li>🥈 <strong>Dombey and Son (1848):</strong> 357,000 words</li>
  <li>🥉 <strong>Bleak House (1853):</strong> 356,000 words</li>
  <li>...</li>
  <li><strong>A Tale of Two Cities (1859):</strong> 135,000 words</li>
  <li><strong>Hard Times (1854):</strong> 105,000 words (his shortest novel)</li>
  <li><strong>A Christmas Carol (1843):</strong> 28,429 words (a focused 6-week sprint!)</li>
</ul>
<strong>📊 Today's Data Storytelling Lesson: Headlines & Horizontal Alignment</strong><br>
<ol>
  <li><strong>Action Headline over Topic Label:</strong> Don't title your slide <em>'Word Count by Novel'</em>. Write: <em>'David Copperfield Reigns Supreme at 360,000 Words.'</em> State the conclusion upfront!</li>
  <li><strong>Horizontal Orientation:</strong> If category names are long (like <em>'The Life and Adventures of Nicholas Nickleby'</em>), horizontal bars allow readers to scan titles naturally from left to right—zero tilted heads, zero neck strain.</li>
  <li><strong>Sort by Magnitude:</strong> Never sort novels alphabetically unless it's a directory. Sorting by word count turns random clutter into an immediate visual ranking.</li>
</ol>
<em>But numbers have long memories.</em><br><br>
Tomorrow, the categories stand upright.<br><br>
#DataStorytelling #DataVisualization #CharlesDickens #BarChart #EdwardTufte #VisualVocabulary""",
        "storytelling_rule": "Horizontal labels preserve reading cadence. When category titles exceed 8 characters, flip your column chart into a horizontal bar chart."
    },
    {
        "id": 2,
        "act": "ACT I: OPENING THE WINDOWS",
        "day": "DAY 2",
        "title": "The Column Chart: A Chronology of Creation (1836–1870)",
        "chart_type": "Discrete Magnitude over Time",
        "question": "How did Dickens distribute his novels across his 35-year career?",
        "image": "img24/image2.png",
        "dickens_data": {
            "theme": "Chronological Novel Output (data/dickens/dickens_novels.csv)",
            "key_metric": "1836 Pickwick Papers to 1870 Edwin Drood | 15 Novels published across 34 years",
            "historical_context": "Dickens published in explosive bursts in his 20s and 30s, often writing two major novels simultaneously (e.g. Oliver Twist and Nicholas Nickleby).",
            "fun_fact": "In 1838, Dickens was simultaneously editing Bentley's Miscellany, writing Oliver Twist monthly, and writing Nicholas Nickleby monthly—all while raising a young family!"
        },
        "quote": "“It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness...” — A Tale of Two Cities (1859)",
        "headline_lesson": {
            "bad_title": "Novels Published by Charles Dickens (1836–1870)",
            "action_headline": "A Relentless Pace: Dickens Published 8 Masterpieces Before Reaching Age 40",
            "rule": "Baseline Integrity: Vertical column charts MUST always start at zero. Truncating the vertical axis exaggerates differences and destroys trust."
        },
        "post_copy": """🎄 <strong>DAY 2 | A Christmas Chart Carol</strong><br>
<em>Window 2: The Column Chart</em><br><br>
Today, the data categories stand upright.<br><br>
The <strong>column chart</strong> is ideal when categories follow a natural sequence through time. When we plot Dickens' 15 major novels along his 35-year writing life (1836 to 1870), a breathtaking creative rhythm appears.<br><br>
In his twenties and thirties, Dickens was an unstoppable torrent:
<ul>
  <li><strong>1836–1841:</strong> 5 major novels in just 5 years (<em>Pickwick, Oliver Twist, Nickleby, Curiosity Shop, Barnaby Rudge</em>).</li>
  <li><strong>1843:</strong> Writes <em>A Christmas Carol</em> in 6 feverish weeks.</li>
  <li><strong>1850s:</strong> The darker, mature architectural masterpieces (<em>Bleak House, Hard Times, Little Dorrit, Tale of Two Cities</em>).</li>
</ul>
<strong>📊 Today's Data Storytelling Lesson: Baseline Integrity & Selective Color</strong><br>
<ol>
  <li><strong>Always Anchor at Zero:</strong> Never truncate the vertical axis of a column chart. Columns encode magnitude through physical height. Cropping the baseline from 0 to 50 deceives the eye.</li>
  <li><strong>Kill the Rainbow:</strong> Don't give each novel a different color. Keep all 14 novels in a muted, elegant slate grey, and use a rich Victorian gold or crimson solely for the hero column: <em>1843 (A Christmas Carol)</em>.</li>
  <li><strong>Direct Date Labeling:</strong> Group columns by decade or publication format to help executive readers grasp eras without squinting at tiny tick marks.</li>
</ol>
<em>But numbers have long memories.</em><br><br>
#DataVisualization #ColumnChart #StorytellingWithData #InformationDesign #CharlesDickens""",
        "storytelling_rule": "The Zero-Baseline Rule: Columns encode value by length from a base. Cropping the baseline turns an objective comparison into an optical illusion."
    },
    {
        "id": 3,
        "act": "ACT I: OPENING THE WINDOWS",
        "day": "DAY 3",
        "title": "The Dot Plot: The Population of Dickens' World",
        "chart_type": "Minimalist Distribution / Category Comparison",
        "question": "How many characters did Dickens crowd into each novel?",
        "image": "img24/image3.png",
        "dickens_data": {
            "theme": "Character Census (data/dickens/dickens_novels.csv)",
            "key_metric": "Pickwick Papers: 260 characters | Bleak House: 178 characters | Hard Times: 44 characters | Total Canon: 989+ named characters",
            "historical_context": "Dickens pulled names directly from Victorian registries, London tombstones, and Court of Chancery records.",
            "fun_fact": "Dickens kept notebooks filled with eccentric names waiting for the right book: 'Pumblechook', 'Wackford Squeers', 'Sweedlepipe', and 'M'Choakumchild'!"
        },
        "quote": "“Charity begins at home, and justice begins next door.” — Martin Chuzzlewit (1844)",
        "headline_lesson": {
            "bad_title": "Character Counts in Dickens Books",
            "action_headline": "From Intimate Drama to Bustling Metropolis: Pickwick Papers Packed 260 Characters into One Story",
            "rule": "Less Ink, More Insight: Strip the heavy ink of a bar down to a single focused dot to let data breathe."
        },
        "post_copy": """🎄 <strong>DAY 3 | A Christmas Chart Carol</strong><br>
<em>Window 3: The Dot Plot</em><br><br>
What happens when you strip the thick, heavy ink of a bar and leave only its critical endpoint?<br><br>
You get a <strong>dot plot</strong>.<br><br>
Charles Dickens did not just write stories; he populated entire civilizations. Across his 15 novels, scholars have cataloged over <strong>989 distinct named characters</strong>.<br><br>
Where did they live?
<ul>
  <li><strong>The Pickwick Papers:</strong> 260 characters (a raucous coaching tour of England)</li>
  <li><strong>Bleak House:</strong> 178 characters (from Lady Dedlock to Jo the crossing sweeper)</li>
  <li><strong>David Copperfield:</strong> 156 characters (Micawber, Uriah Heep, Peggotty)</li>
  <li><strong>Hard Times:</strong> Just 44 characters (a lean, austere critique of industrialism)</li>
</ul>
<strong>📊 Today's Data Storytelling Lesson: The Data-Ink Ratio</strong><br>
Edward Tufte famously defined the <strong>Data-Ink Ratio</strong>:<br>
$$\\text{Data-Ink Ratio} = \\frac{\\text{Ink dedicated to data content}}{\\text{Total ink used in graphic}}$$<br>
When you plot 15 character totals with heavy colored rectangles, the bars create an overwhelming visual slab. With a dot plot:<br>
- The position of the dot conveys 100% of the analytical value.<br>
- Gridlines fade into faint dotted lines.<br>
- Your reader's eyes focus on the spread between the minimalist world of <em>Hard Times (44)</em> and the sprawling crowd of <em>Pickwick (260)</em>.<br><br>
<em>But numbers have long memories.</em><br><br>
#DataInkRatio #EdwardTufte #DotPlot #DataDesign #CharlesDickens""",
        "storytelling_rule": "Every drop of ink must earn its place. Strip decorative borders and heavy fills to let the true variance stand out in clean relief."
    },
    {
        "id": 4,
        "act": "ACT I: OPENING THE WINDOWS",
        "day": "DAY 4",
        "title": "The Lollipop Chart: From London Fog to Hollywood Screen",
        "chart_type": "Magnitude / Modernized Ranking",
        "question": "Which Dickens books have generated the most film, stage, and TV adaptations?",
        "image": "img24/image4.png",
        "dickens_data": {
            "theme": "Adaptations Analysis (data/dickens/dickens_adaptations.csv)",
            "key_metric": "A Christmas Carol: 135+ adaptations | Oliver Twist: 38 | Great Expectations: 34 | David Copperfield: 26 | Barnaby Rudge: 6",
            "historical_context": "Dickens is the second most adapted writer in the English language, surpassed only by William Shakespeare.",
            "fun_fact": "The earliest surviving screen adaptation is the 1901 British silent film 'Scrooge; or, Marley's Ghost'—only 620 feet of film (about 5 minutes) survive today!"
        },
        "quote": "“I will honour Christmas in my heart, and try to keep it all the year.” — A Christmas Carol (1843)",
        "headline_lesson": {
            "bad_title": "Number of Adaptations per Dickens Novel",
            "action_headline": "A Holiday Phenomenon: A Christmas Carol Has Inspired Over 135 Adaptations—Nearly Quadruple Any Other Work",
            "rule": "Label Directly at the Node: In a lollipop chart, place data values right inside or beside the circular node so no Y-axis lookup is required."
        },
        "post_copy": """🎄 <strong>DAY 4 | A Christmas Chart Carol</strong><br>
<em>Window 4: The Lollipop Chart</em><br><br>
Today's chart looks as though it dressed up for Christmas.<br><br>
The <strong>lollipop chart</strong> combines a slender stem with an accented circular head. It was born as a lighter, stylish alternative to dense bars when presenting ranked lists.<br><br>
Dickens was the world's first multimedia pop culture icon. More than <strong>300 film, television, and stage adaptations</strong> have brought his words to life:<br>
<ul>
  <li>⭐ <strong>A Christmas Carol:</strong> 135+ adaptations (Alastair Sim, Muppets, Bill Murray, Jim Carrey, Will Ferrell!)</li>
  <li>🥈 <strong>Oliver Twist:</strong> 38 adaptations (including the 6-Oscar-winning 1968 musical <em>Oliver!</em>)</li>
  <li>🥉 <strong>Great Expectations:</strong> 34 adaptations (David Lean's 1946 masterpiece, Alfonso Cuarón)</li>
  <li><strong>David Copperfield:</strong> 26 adaptations</li>
  <li><strong>Barnaby Rudge:</strong> Just 6 adaptations</li>
</ul>
<strong>📊 Today's Data Storytelling Lesson: Labeling at the Point of Impact</strong><br>
<ol>
  <li><strong>Avoid Y-Axis Round-Tripping:</strong> Don't force your viewer to look at a circle, trace down to the axis, and estimate whether it's 130 or 140. Place the number <code>135</code> directly beside or inside the lollipop head!</li>
  <li><strong>The Lollipop Rule:</strong> Use it when you have 10+ items and traditional bars would feel like a heavy barcode. But ensure the circular node doesn't mislead the eye regarding where the measurement ends.</li>
</ol>
<em>But numbers have long memories.</em><br><br>
#LollipopChart #DataStorytelling #CharlesDickens #FilmHistory #AChristmasCarol""",
        "storytelling_rule": "Place data values directly at the point of interest. Reducing eye saccades (ocular jumping between chart and axis) doubles reader comprehension speed."
    },
    {
        "id": 5,
        "act": "ACT I: OPENING THE WINDOWS",
        "day": "DAY 5",
        "title": "The Line Chart: The Cumulative Words of a Lifetime",
        "chart_type": "Change over Time / Cumulative Trajectory",
        "question": "How did Dickens build his 4.5-million-word legacy over 35 years?",
        "image": "img24/image5.png",
        "dickens_data": {
            "theme": "Career Word Output (data/dickens/dickens_biography.csv)",
            "key_metric": "1836 (300k words) -> 1845 (1.5M words) -> 1855 (3.0M words) -> 1870 (4.5M words)",
            "historical_context": "Dickens wrote exclusively with quill pens and blue-black ink, often producing 2,000 words before lunch every morning.",
            "fun_fact": "Dickens was so intensely bonded with his characters that when Little Nell died in The Old Curiosity Shop, he wrote to a friend: 'I am nearly broken-hearted... I am slowly writing her death now.'"
        },
        "quote": "“The most important thing in life is to stop saying 'I wish' and start saying 'I will'.” — Charles Dickens",
        "headline_lesson": {
            "bad_title": "Cumulative Word Count of Dickens (1835–1870)",
            "action_headline": "The S-Curve of Genius: Dickens Authored 4.5 Million Words with an Unbroken 35-Year Momentum",
            "rule": "Kill the Legend: Label the end of the trendline directly in text (e.g. '4.5M Cumulative Words') instead of a floating legend box."
        },
        "post_copy": """🎄 <strong>DAY 5 | A Christmas Chart Carol</strong><br>
<em>Window 5: The Line Chart</em><br><br>
With today's window, time officially enters our narrative.<br><br>
The <strong>line chart</strong> connects continuous sequential observations. It is the premier storytelling tool for momentum, trajectory, and acceleration.<br><br>
Look at the cumulative word trajectory of Charles Dickens from his debut in 1836 to his untimely death in 1870:
<ul>
  <li><strong>1836–1840:</strong> The rocket launch—1.2 million words written before turning 30.</li>
  <li><strong>1841–1855:</strong> Steady, relentless mid-career ascent at ~150,000 words per year.</li>
  <li><strong>1858–1870:</strong> Output flattens slightly as he pours his vitality into grueling public theatrical reading tours.</li>
</ul>
<strong>📊 Today's Data Storytelling Lesson: Direct Labeling & Milestone Callouts</strong><br>
👉 <strong>Kill the Floating Legend Box!</strong><br>
When you place a legend box in the top-right corner with 3 colored squares, you force the reader's eyes to bounce back and forth like a ping-pong ball.<br>
1. <strong>Direct Labeling:</strong> Write <code>Total Canon Output (4.5M words)</code> right at the end of the line.<br>
2. <strong>Annotate Inflection Points:</strong> Place a tiny text pointer at 1843: <em>'A Christmas Carol published (Dec 19)'</em>. An annotated line chart doesn't just show movement; it explains history.<br><br>
<em>But numbers have long memories.</em><br><br>
#LineChart #DataVisualization #Tufte #DirectLabeling #CharlesDickens""",
        "storytelling_rule": "Eliminate floating legends. Direct labeling at the terminus of a line reduces cognitive friction and guides the reader's gaze effortlessly."
    },
    {
        "id": 6,
        "act": "ACT I: OPENING THE WINDOWS",
        "day": "DAY 6",
        "title": "The Area Chart: The Victorian Publishing Explosion",
        "chart_type": "Change over Time / Readership Volume Buildup",
        "question": "How did Dickens' weekly journals expand the reading public?",
        "image": "img24/image6.png",
        "dickens_data": {
            "theme": "Readership & Circulation Growth (data/dickens/dickens_biography.csv)",
            "key_metric": "Pickwick Part 1: 500 copies -> Pickwick Part 15: 40,000 copies -> Household Words: 100,000 weekly circulation",
            "historical_context": "Dickens essentially created mass-market serialization, democratizing literature for factory workers, shopkeepers, and aristocracy alike.",
            "fun_fact": "When Part 1 of Pickwick was published in 1836, only 500 copies were printed. After Dickens introduced the comedic character Sam Weller in Part 4, demand exploded to 40,000 copies a month!"
        },
        "quote": "“Subdue your appetites, my dears, and you've conquered human nature.” — Nicholas Nickleby (1839)",
        "headline_lesson": {
            "bad_title": "Magazine Circulation Figures 1836–1865",
            "action_headline": "Democratizing the Written Word: Dickens' Weekly Periodicals Reached an Unprecedented 100,000 Victorian Homes",
            "rule": "Area Shading & Transparency: Area charts represent volume and mass. Always keep fill opacity between 30% and 50% so gridlines and trends remain visible."
        },
        "post_copy": """🎄 <strong>DAY 6 | A Christmas Chart Carol</strong><br>
<em>Window 6: The Area Chart</em><br><br>
A line shows movement. An <strong>area chart</strong> gives that movement physical weight.<br><br>
By shading the region beneath the curve, the area chart draws visceral attention to volume, mass, and cumulative scale.<br><br>
In 1836, Victorian fiction was a luxury for the wealthy, sold in expensive three-volume sets ('three-deckers') costing 31 shillings—more than a laborer's weekly wage. Dickens shattered this monopoly:
<ul>
  <li><strong>1836:</strong> Monthly parts at 1 shilling each (40,000 copies/month).</li>
  <li><strong>1850:</strong> Launches <em>Household Words</em> at 2 pence weekly—reaching <strong>100,000 families every single week</strong>.</li>
  <li><strong>1859:</strong> Launches <em>All the Year Round</em>, featuring <em>A Tale of Two Cities</em> and <em>Great Expectations</em>, shattering all circulation records.</li>
</ul>
<strong>📊 Today's Data Storytelling Lesson: Volume & Controlled Opacity</strong><br>
- Area charts are magnificent when visualizing cumulative volume (readership, cash flow, population).<br>
- <strong>Design Warning:</strong> Heavy opaque color blocks obscure the truth. Use subtle translucent gradients (30–40% opacity) so the underlying grid and axis remain legible.<br><br>
The first six windows of our Advent calendar are now open.<br>
Tonight, the temperature in the study drops.<br>
The clock strikes midnight. The first spirit arrives.<br><br>
<em>But numbers have long memories.</em><br><br>
#AreaChart #DataDesign #InformationDesign #CharlesDickens #PublishingHistory""",
        "storytelling_rule": "Volume needs breathing room. Set area fills to transparent tints to emphasize accumulation without creating an impenetrable wall of color."
    },
    {
        "id": 7,
        "act": "ACT II: THE GHOST OF DATA PAST",
        "day": "DAY 7",
        "title": "The Slope Chart: The Great Shift of 1858",
        "chart_type": "Change over Time / Before vs. After Transformation",
        "question": "How did Dickens' income stream transform when he took to the stage?",
        "image": "img24/image7.png",
        "dickens_data": {
            "theme": "Income Transformation: Publishing Royalties vs Reading Tours (1850 vs 1868)",
            "key_metric": "1850: 85% Publishing / 15% Other -> 1868: 72% Live Theatrical Readings / 28% Publishing",
            "historical_context": "In 1858, following his separation from his wife Catherine, Dickens launched professional solo reading tours, acting out all characters himself.",
            "fun_fact": "Dickens performed the violent murder of Nancy by Bill Sikes from Oliver Twist with such terrifying realism that women routinely fainted in the audience, and his doctor measured his pulse soaring to 124 bpm!"
        },
        "quote": "“Electric communication will never be a substitute for the face of someone who with their soul encourages another person to be brave and true.” — Charles Dickens",
        "headline_lesson": {
            "bad_title": "Dickens Revenue Sources: 1850 compared to 1868",
            "action_headline": "The Author Becomes the Actor: In Ten Years, Live Stage Readings Overtook Book Royalties as Dickens' #1 Revenue Engine",
            "rule": "The Slope Chart Rule: Strip away all intermediary years to focus exclusively on two pivotal eras. Slope angle reveals the speed and direction of change."
        },
        "post_copy": """🎄 <strong>DAY 7 | A Christmas Chart Carol</strong><br>
<em>Window 7: The Slope Chart</em><br>
👻 <strong>Enter The Ghost of Data Past</strong><br><br>
The first spirit grasps our hand and pulls us backward.<br><br>
A <strong>slope chart</strong> strips away intermediary noise to focus ruthlessly on two defining moments: <strong>Before vs. After</strong>.<br><br>
In 1858, Charles Dickens did something no major novelist had ever dared: he stepped onto the public stage as a solo performer, acting out every character in his books with dramatic stage lighting, props, and vocal acrobatics.<br><br>
Look at how his income structure transformed between 1850 and 1868:
<ul>
  <li>📉 <strong>Book Royalties Share:</strong> Plunged from 85% $\\rightarrow$ 28% of annual earnings.</li>
  <li>📈 <strong>Live Performance Fees:</strong> Soared from 0% $\\rightarrow$ <strong>72% of total earnings</strong> (his 1867 American reading tour grossed over $228,000—millions in today's currency!).</li>
</ul>
<strong>📊 Today's Data Storytelling Lesson: The Power of the Vector</strong><br>
<ol>
  <li><strong>Slopes Tell Direction:</strong> The human eye detects line angle instantly. Steep upward slopes scream growth; downward slopes show sunsetting legacy streams.</li>
  <li><strong>Label Both Ends Directly:</strong> Label the category name and value right beside each point on the left and right axes. No legend needed!</li>
</ol>
Two moments can tell an unforgettable story—if they are the right two moments.<br><br>
<em>But numbers have long memories.</em><br><br>
#SlopeChart #DataStorytelling #FinancialHistory #CharlesDickens #TheaterHistory""",
        "storytelling_rule": "Slope charts isolate the delta. When intermediate data points distract from a strategic turning point, connect the two benchmark years with a direct slope."
    },
    {
        "id": 8,
        "act": "ACT II: THE GHOST OF DATA PAST",
        "day": "DAY 8",
        "title": "The Dumbbell Chart: The Serialization Gap",
        "chart_type": "Deviation / Target vs. Actual Page Count",
        "question": "How strictly did Dickens hit his monthly serial page quotas?",
        "image": "img24/image8.png",
        "dickens_data": {
            "theme": "Installment Page Budgets (data/dickens/dickens_novels.csv)",
            "key_metric": "Standard Quota: 32 printed pages per monthly part | Actual range: 28 to 36 pages",
            "historical_context": "Victorian serial printing required each monthly part to fill exactly two 16-page printing sheets (32 pages). Over-running meant wasted paper; under-running meant blank spaces.",
            "fun_fact": "When Dickens found himself two pages short of his 32-page quota while proofing Bleak House, he would rapidly write brilliant extra comedic dialogue for Harold Skimpole or Inspector Bucket right in the printer's shop!"
        },
        "quote": "“Annual income twenty pounds, annual expenditure nineteen nineteen and six, result happiness. Annual income twenty pounds, annual expenditure twenty pounds ought and six, result misery.” — David Copperfield (1850)",
        "headline_lesson": {
            "bad_title": "Monthly Target vs Actual Pages in Bleak House",
            "action_headline": "Precision Under Pressure: How Dickens Conquered the Rigorous 32-Page Monthly Serialization Quota",
            "rule": "The Dumbbell Barbell: The length of the bar represents the variance. The reader's eye naturally measures the distance between the two dots."
        },
        "post_copy": """🎄 <strong>DAY 8 | A Christmas Chart Carol</strong><br>
<em>Window 8: The Dumbbell Chart</em><br><br>
Target and Reality met beneath the mistletoe. They did not always agree.<br><br>
The <strong>dumbbell plot</strong> (barbell chart) places two distinct points on a single axis—Target/Plan ($\circ$) and Actual Result ($\bullet$)—and connects them with a horizontal bar. The width of that bar is the <strong>variance</strong>.<br><br>
In Victorian publishing, monthly serialization was a mathematical high-wire act:
- Every monthly installment of <em>Bleak House</em> and <em>David Copperfield</em> had to fill <strong>exactly 32 printed pages</strong> (two folded printing sheets).
- If Dickens wrote 30 pages, the printer had blank space.
- If he wrote 34 pages, the binding was ruined.
- Look at the dumbbell variances: early parts show small deficits (-2 pages) that Dickens frantically padded at proof stage; climax installments burst through with extra double-numbers!<br><br>
<strong>📊 Today's Data Storytelling Lesson: Focusing on the Gap</strong><br>
Traditional grouped bar charts put two fat columns side by side, forcing viewers to compare heights. The dumbbell plot shifts focus directly to the <strong>connecting span</strong>.<br>
- One dot color for Planned Quota.<br>
- One high-contrast dot for Actual Published Output.<br>
- The bar length is the operational gap you need to explain.<br><br>
<em>But numbers have long memories.</em><br><br>
#DumbbellChart #DataDesign #VarianceAnalysis #Publishing #CharlesDickens""",
        "storytelling_rule": "The Barbell Focus: When tracking plan vs. reality, minimize the markers and let the connecting line measure the operational variance directly."
    },
    {
        "id": 9,
        "act": "ACT II: THE GHOST OF DATA PAST",
        "day": "DAY 9",
        "title": "The Indexed Line Chart: The Victorian Rivalry (Base 100)",
        "chart_type": "Change over Time / Relative Growth Velocity",
        "question": "How did Dickens' fame and sales accelerate compared to his literary rivals?",
        "image": "img24/image9.png",
        "dickens_data": {
            "theme": "Literary Velocity: Dickens vs Thackeray vs George Eliot vs Trollope (1840–1865)",
            "key_metric": "Indexed to 100 at 1840 | Dickens: Index 450 | Thackeray: Index 180 | Trollope: Index 210",
            "historical_context": "William Makepeace Thackeray (author of Vanity Fair) was Dickens' chief rival. While critically celebrated, Thackeray's circulation was dwarfed by Dickens' mass appeal.",
            "fun_fact": "Thackeray once auditioned to be Dickens' illustrator for The Pickwick Papers in 1836, but was rejected! Later in life, they had a bitter public feud that was only resolved in the lobby of the Athenaeum Club months before Thackeray's death."
        },
        "quote": "“Have a heart that never hardens, and a temper that never tires, and a touch that never hurts.” — Our Mutual Friend (1865)",
        "headline_lesson": {
            "bad_title": "Comparative Book Sales Index 1840–1865",
            "action_headline": "In a League of His Own: Dickens' Popularity Quadrupled While Contemporary Giants Grew Steadily",
            "rule": "The Base-100 Normalization Rule: When comparing entities of vastly different starting scales, rebase them to 100 at Day Zero to measure pure growth velocity."
        },
        "post_copy": """🎄 <strong>DAY 9 | A Christmas Chart Carol</strong><br>
<em>Window 9: The Indexed Line Chart</em><br><br>
How do you compare the popularity of authors who published in different formats, at different price points, with different starting audiences?<br><br>
<strong>Rebase everything to 100 at the starting line.</strong><br><br>
In 1840, we index the Victorian literary landscape to 100:
<ul>
  <li>🚀 <strong>Charles Dickens:</strong> Surges from Index 100 $\\rightarrow$ <strong>Index 450</strong> by 1860.</li>
  <li>📘 <strong>Anthony Trollope:</strong> Steady, prolific growth from Index 100 $\\rightarrow$ Index 210.</li>
  <li>🎩 <strong>William Makepeace Thackeray:</strong> High critical acclaim with <em>Vanity Fair</em>, reaching Index 180.</li>
</ul>
<strong>📊 Today's Data Storytelling Lesson: Normalizing the Playing Field</strong><br>
<ol>
  <li><strong>Never Use Dual Y-Axes:</strong> Dual axes with conflicting scales deceive readers and invite manipulation.</li>
  <li><strong>Index to 100:</strong> Setting a shared baseline shifts the conversation from <em>'Who has the biggest nominal number?'</em> to <strong>'Who is accelerating fastest?'</strong></li>
  <li><strong>Direct Line End-Labels:</strong> Label author names right at the end of the curves—never in a disconnected legend box!</li>
</ol>
<em>But numbers have long memories.</em><br><br>
#IndexedChart #DataStorytelling #VictorianLiterature #DataAnalytics #CharlesDickens""",
        "storytelling_rule": "Base-100 indexing eliminates unfair scale advantages, allowing readers to compare pure growth velocity across competitors."
    },
    {
        "id": 10,
        "act": "ACT II: THE GHOST OF DATA PAST",
        "day": "DAY 10",
        "title": "Small Multiples: Pacing the Masterpieces",
        "chart_type": "Multi-Panel Comparison / Chapter Word Densities",
        "question": "How did chapter pacing differ between Pickwick, Copperfield, Bleak House, and Great Expectations?",
        "image": "img24/image10.png",
        "dickens_data": {
            "theme": "Chapter Structure Architecture across 4 Novels",
            "key_metric": "Pickwick: 57 chapters (erratic episodic pacing) | Great Expectations: 59 chapters (tight, suspenseful weekly arcs)",
            "historical_context": "Novels serialized weekly (like Great Expectations) required razor-sharp chapter cliffhangers, while monthly novels had room for sprawling atmospheric detours.",
            "fun_fact": "Dickens famously changed the ending of Great Expectations after his fellow novelist Edward Bulwer-Lytton read the manuscript and begged him not to leave Pip and Estella permanently estranged!"
        },
        "quote": "“Take nothing on its looks; take everything on evidence. There's no better rule.” — Great Expectations (1861)",
        "headline_lesson": {
            "bad_title": "Chapter Word Counts Across Four Novels",
            "action_headline": "From Rambling Picaresque to Taut Thriller: How Dickens Perfected Chapter Pacing Over 25 Years",
            "rule": "Small Multiples (Trellis) Rule: Lock the X and Y axes across all panels identically. Shared scale enables instant pattern comparison."
        },
        "post_copy": """🎄 <strong>DAY 10 | A Christmas Chart Carol</strong><br>
<em>Window 10: Small Multiples (Trellis Display)</em><br><br>
Have you ever tried to plot four 60-chapter novels on a single line chart?<br><br>
It becomes an illegible nest of colored spaghetti.<br><br>
Enter <strong>Small Multiples</strong>—Edward Tufte's gold standard for comparing rich structures.<br><br>
Instead of tangling lines together, we build a 2x2 grid of clean, synchronized micro-charts showing chapter-by-chapter word counts:
<ul>
  <li><strong>Panel 1: The Pickwick Papers (1836):</strong> Wild, spiky, erratic episodic adventures.</li>
  <li><strong>Panel 2: David Copperfield (1849):</strong> Rhythmic, deliberate balance of comedy and grief.</li>
  <li><strong>Panel 3: Bleak House (1852):</strong> Complex dual narration (omniscient present tense alternating with Esther Summerson).</li>
  <li><strong>Panel 4: Great Expectations (1860):</strong> Smooth, compressed, suspenseful weekly discipline.</li>
</ul>
<strong>📊 Today's Data Storytelling Lesson: Shared Scale Discipline</strong><br>
- <strong>Identical Axes:</strong> Keep the horizontal scale (Chapters 1 to 60) and vertical scale (0 to 8,000 words) strictly identical across all panels.<br>
- <strong>Instant Pattern Recognition:</strong> Because scales are locked, your reader instantly perceives how Dickens tightened his craft over 25 years.<br><br>
<em>But numbers have long memories.</em><br><br>
#SmallMultiples #Tufte #DataDesign #InformationArchitecture #CharlesDickens""",
        "storytelling_rule": "Standardize small multiples. When all panels share identical axes and visual styling, the human brain detects structural patterns in milliseconds."
    },
    {
        "id": 11,
        "act": "ACT II: THE GHOST OF DATA PAST",
        "day": "DAY 11",
        "title": "The Calendar Heatmap: The Night Walker's London",
        "chart_type": "Temporal Density / Daily Activity Heatmap",
        "question": "When and where did Dickens do his most intense creative walking?",
        "image": "img24/image11.png",
        "dickens_data": {
            "theme": "Dickens' 15-Mile Nightly London Walks (data/dickens/dickens_biography.csv)",
            "key_metric": "Daily average: 12 to 20 miles walked between 10:00 PM and 3:00 AM across London alleys",
            "historical_context": "Suffering from severe insomnia and manic creative energy, Dickens stalked the foggy Victorian streets from Covent Garden to the Thames docks to observe night vagrants and thieves.",
            "fun_fact": "Dickens once walked 30 miles from his home in Tavistock House in central London all the way to his country retreat at Gads Hill Place in Kent in the dead of night, arriving at dawn!"
        },
        "quote": "“The day was dying in the city... the night was coming on; and the river, cold and dark, flowed through the midst of it.” — Our Mutual Friend (1865)",
        "headline_lesson": {
            "bad_title": "Daily Mileage Recorded by Charles Dickens",
            "action_headline": "Stalking the City: Dickens Walked 20 Miles Through the Darkest Alleys of London to Fuel His Plots",
            "rule": "Color as Density: In calendar heatmaps, use single-hue sequential palettes (e.g. pale cream to deep nocturnal indigo) to convey effort without visual chaos."
        },
        "post_copy": """🎄 <strong>DAY 11 | A Christmas Chart Carol</strong><br>
<em>Window 11: The Calendar Heatmap</em><br><br>
Where did Dickens' inspiration come from?<br><br>
It came from his boots.<br><br>
A <strong>calendar heatmap</strong> arranges daily data into standard 7-day calendar weeks, using color saturation to reveal behavioral rhythms.<br><br>
When we map Dickens' recorded daily walking distances across his writing seasons:
<ul>
  <li>Standard days glow in steady green (5–8 miles of daytime walking).</li>
  <li>Late autumn and winter months explode into deep nocturnal indigo: <strong>15 to 20 miles per night</strong>, walking between 11:00 PM and 4:00 AM through rain, snow, and Thames fog.</li>
  <li>These nocturnal expeditions through London's opium dens, workhouses, and butcher markets were where he met the real-life models for Fagin, Bill Sikes, and Ebenezer Scrooge.</li>
</ul>
<strong>📊 Today's Data Storytelling Lesson: Color as Quantitative Signal</strong><br>
- Avoid jarring multi-color rainbows in heatmaps.<br>
- Use a single, continuous color ramp (e.g. from soft parchment to dark ink).<br>
- Color is not decoration; it is the lantern that reveals human habit and operational rhythm.<br><br>
<em>But numbers have long memories.</em><br><br>
#Heatmap #CalendarHeatmap #DataAnalytics #HumanBehavior #CharlesDickens""",
        "storytelling_rule": "Use sequential single-hue ramps in heatmaps. Rainbow palettes introduce artificial step-changes; continuous hue intensity reflects true natural volume."
    },
    {
        "id": 12,
        "act": "ACT II: THE GHOST OF DATA PAST",
        "day": "DAY 12",
        "title": "The Bump Chart: The Shifting Canon",
        "chart_type": "Ranking / Positional Trajectory Over Eras",
        "question": "How have public and critical rankings of Dickens' novels evolved over 150 years?",
        "image": "img24/image12.png",
        "dickens_data": {
            "theme": "Historical Popularity & Critical Rankings (1850, 1900, 1950, 2026)",
            "key_metric": "Pickwick: #1 in 1850 -> #8 in 2026 | Bleak House: #7 in 1850 -> #2 in 2026 | A Christmas Carol: Steadfast #1-3 across all eras",
            "historical_context": "Victorian readers prized Dickens' warm comedic picaresque tales; 20th and 21st-century critics elevated his dark, satirical social critiques like Bleak House.",
            "fun_fact": "When The Old Curiosity Shop was serialized in 1841, thousands of readers in New York stormed the harbor pier to shout at incoming British ships: 'Is Little Nell alive?'"
        },
        "quote": "“Reflect upon your present blessings—of which every man has many—not on your past misfortunes, of which all men have some.” — Sketches by Boz (1836)",
        "headline_lesson": {
            "bad_title": "Ranking of Dickens Novels Over Time",
            "action_headline": "The Rise of Bleak House: How 20th-Century Critics Elevated Dickens' Darkest Satire to the Top Tier",
            "rule": "Bump Chart Clarity: Emphasize the top 3 and bottom 3 lines with high contrast, and mute the middle ranks in light grey to prevent visual clutter."
        },
        "post_copy": """🎄 <strong>DAY 12 | A Christmas Chart Carol</strong><br>
<em>Window 12: The Bump Chart</em><br><br>
History is not only about absolute quantities. It is about <strong>position and rank</strong>.<br><br>
A <strong>bump chart</strong> tracks changes in rank over time, prioritizing relative standing over raw counts.<br><br>
Watch how literary history reshuffled Dickens' masterworks across 150 years:
<ul>
  <li>🎩 <strong>The Pickwick Papers:</strong> Held Rank #1 in 1850 (Victorian favorite) $\\rightarrow$ slipped to Rank #8 today.</li>
  <li>⚖️ <strong>Bleak House:</strong> Ranked #7 in his lifetime $\\rightarrow$ soared to Rank #2 today as modern critics recognized its unmatched social critique.</li>
  <li>🕯️ <strong>A Christmas Carol:</strong> The eternal champion—never dropping out of the Top 3 across any generation.</li>
</ul>
<strong>📊 Today's Data Storytelling Lesson: Managing Multi-Line Clutter</strong><br>
A bump chart with 10 intertwined lines can quickly look like tangled Christmas tinsel.<br>
1. <strong>Selective Highlighting:</strong> Bold only the 2 or 3 lines that carry the historical thesis (e.g. <em>Bleak House</em> rising and <em>Pickwick</em> falling).<br>
2. <strong>Direct Labels on Both Flanks:</strong> Put rank numbers on the left (1850) and right (Today) so the reader never has to trace lines back across the page.<br><br>
And so the first spirit departs.<br>
The past has spoken. Now, candlelight fills the room.<br><br>
<em>But numbers have long memories.</em><br><br>
#BumpChart #Rankings #DataStorytelling #LiteraryCanon #CharlesDickens""",
        "storytelling_rule": "Accent the climbers and fallers. In ranking charts, highlight the storylines that changed most dramatically while muting stable mid-pack paths."
    },
    {
        "id": 13,
        "act": "ACT III: THE GHOST OF DATA PRESENT",
        "day": "DAY 13",
        "title": "The Histogram: The Anatomy of a Chapter",
        "chart_type": "Distribution / Continuous Frequency Bins",
        "question": "What does the distribution of Dickens' chapter lengths look like?",
        "image": "img24/image13.png",
        "dickens_data": {
            "theme": "Chapter Length Distributions across All 15 Novels",
            "key_metric": "Median chapter: 3,850 words | Minimum: 1,120 words | Maximum: 8,450 words | Severe positive skew",
            "historical_context": "Serial publication forced Dickens to write chapters that could be absorbed in a single evening's family reading session around the hearth.",
            "fun_fact": "Victorian families gathered around the fireplace every Sunday evening to have the literate family member read the latest Dickens chapter aloud—Dickens wrote with spoken cadence in mind!"
        },
        "quote": "“There is a wisdom of the head, and a wisdom of the heart.” — Hard Times (1854)",
        "headline_lesson": {
            "bad_title": "Histogram of Dickens Chapter Lengths",
            "action_headline": "Crafted for the Hearth: Most Chapters Cluster at 3,800 Words—The Exact Length of a Victorian Evening Read",
            "rule": "The Bin Width Rule: Bin widths make or break histograms. Too narrow creates noisy sawteeth; too wide obscures natural modal peaks."
        },
        "post_copy": """🎄 <strong>DAY 13 | A Christmas Chart Carol</strong><br>
<em>Window 13: The Histogram</em><br>
🕯️ <strong>Enter The Ghost of Data Present</strong><br><br>
The second spirit enters with the warm glow of candlelight, asking us to look at the shape of our data.<br><br>
We love the comfort of an 'average.'<br>
<em>'Dickens' average chapter is 4,100 words.'</em><br>
It sounds tidy. It sounds precise.<br><br>
<strong>It is completely misleading.</strong><br><br>
A <strong>histogram</strong> groups continuous observations into intervals (bins), showing the true spread and distribution of reality:<br>
<ul>
  <li>The distribution is heavily right-skewed.</li>
  <li>There is an overwhelming peak (the mode) between <strong>3,500 and 4,000 words</strong>. Why? Because that was the exact time limit for reading aloud to a family before the candles burned down!</li>
  <li>A long right tail stretches up to 8,000+ words—saved exclusively for dramatic trial climaxes and serial finales.</li>
</ul>
<strong>📊 Today's Data Storytelling Lesson: Never Settle for the Mean</strong><br>
- A single average erases nuance. A histogram shows the human intent behind the numbers.<br>
- <strong>Label the Peak (Mode):</strong> Put an annotation over the central cluster explaining <em>why</em> it peaks there.<br><br>
<em>But numbers have long memories.</em><br><br>
#Histogram #Statistics #DataDistribution #StorytellingWithData #CharlesDickens""",
        "storytelling_rule": "The average conceals; the distribution reveals. Always inspect the histogram to see whether a single metric hides multiple distinct operational modes."
    },
    {
        "id": 14,
        "act": "ACT III: THE GHOST OF DATA PRESENT",
        "day": "DAY 14",
        "title": "The Box Plot: Spreads, Medians, and Outliers",
        "chart_type": "Distribution / 5-Number Summary & Outlier Dots",
        "question": "How did chapter length variance differ across early vs. late Dickens works?",
        "image": "img24/image14.png",
        "dickens_data": {
            "theme": "Quartile Spreads of Chapter Lengths across 4 Eras",
            "key_metric": "Early works (1836–41) IQR: 2,400 words | Late masterpieces (1860–65) IQR: 980 words (tight discipline)",
            "historical_context": "As Dickens matured, his control over narrative pacing tightened dramatically. The wild swings of his youth gave way to masterly architectural precision.",
            "fun_fact": "Dickens had a secret door in his study at Gads Hill disguised as a bookcase. The fake spines had humorous titles he invented, like 'The Art of Cutting the Teeth' and 'Cat's Lives in 9 Volumes'!"
        },
        "quote": "“A day wasted on others is not wasted on one's self.” — A Tale of Two Cities (1859)",
        "headline_lesson": {
            "bad_title": "Boxplot of Chapter Lengths by Publication Era",
            "action_headline": "Mastering the Craft: How Dickens Slashed Narrative Volatility in Half to Perfect His Late Suspense Novels",
            "rule": "Outlier Dots Are Stories: Don't treat outlier dots beyond the box-plot whiskers as statistical errors—annotate them as key plot twists!"
        },
        "post_copy": """🎄 <strong>DAY 14 | A Christmas Chart Carol</strong><br>
<em>Window 14: The Box Plot</em><br><br>
What is normal? What is unusual? How much volatility hides behind an average?<br><br>
The <strong>box plot</strong> (box-and-whisker) summarizes an entire distribution using five critical numbers:
- Minimum
- 25th percentile (Q1)
- Median (Q2)
- 75th percentile (Q3)
- Maximum & Outliers ($\bullet$)<br><br>
Comparing chapter word distributions across Dickens' career reveals a startling transformation:
<ul>
  <li><strong>Early Picaresque Era (Pickwick, Nickleby):</strong> Broad boxes, sprawling whiskers, and wild variance (Interquartile Range = 2,400 words).</li>
  <li><strong>Late Suspense Era (Tale of Two Cities, Great Expectations):</strong> Compact, tight boxes (IQR = 980 words). Pacing became clockwork.</li>
  <li>Look at the outlier dots: the murder of Nancy in <em>Oliver Twist</em> and the storm at Yarmouth in <em>David Copperfield</em> sit far above the top whisker as intentional, monumental set-pieces!</li>
</ul>
<strong>📊 Today's Data Storytelling Lesson: Outliers are Not Errors</strong><br>
In data science, we often rush to clean or trim outliers. In data storytelling, <strong>an outlier is usually where the best story begins</strong>. Annotate the outlier dot!<br><br>
<em>But numbers have long memories.</em><br><br>
#BoxPlot #DataAnalytics #DataStorytelling #Outliers #CharlesDickens""",
        "storytelling_rule": "Every outlier has a name. Never delete or ignore outlier dots in a box plot; add an annotation explaining the exceptional event that caused it."
    },
    {
        "id": 15,
        "act": "ACT III: THE GHOST OF DATA PRESENT",
        "day": "DAY 15",
        "title": "The Scatter Plot: Length vs. Longevity",
        "chart_type": "Correlation / Bivariate Relationship",
        "question": "Does the length of a Dickens novel correlate with how many films it inspired?",
        "image": "img24/image15.png",
        "dickens_data": {
            "theme": "Novel Word Count vs Adaptation Count (data/dickens/dickens_novels.csv)",
            "key_metric": "A Christmas Carol (28k words -> 135 adaptations) | Bleak House (356k words -> 18 adaptations) | r = -0.42 (Negative correlation!)",
            "historical_context": "Modern media producers gravitate toward Dickens' concise, emotionally universal tales rather than his sprawling 350,000-word multi-plot epics.",
            "fun_fact": "Dickens pet raven 'Grip' was so beloved that when it died in 1841, Dickens had it taxidermied and mounted above his desk. Edgar Allan Poe reviewed Dickens' novel Barnaby Rudge (which starred Grip) and was inspired to write his famous poem 'The Raven'!"
        },
        "quote": "“No one is useless in this world who lightens the burdens of another.” — Doctor Marigold (1865)",
        "headline_lesson": {
            "bad_title": "Scatterplot: Word Count vs. Adaptations",
            "action_headline": "Brevity Breeds Immortality: Dickens' Shortest Masterpiece Generated Nearly 4x More Adaptations Than His Longest Epics",
            "rule": "Quadrants & Trendlines: Divide scatter plots into 4 narrative quadrants with subtle reference lines (e.g. High Adaptations / Low Word Count)."
        },
        "post_copy": """🎄 <strong>DAY 15 | A Christmas Chart Carol</strong><br>
<em>Window 15: The Scatter Plot</em><br><br>
Do longer, epic novels generate more cinematic adaptations?<br><br>
A <strong>scatter plot</strong> places every item onto a Cartesian grid (X = Novel Word Count, Y = Total Adaptations), allowing us to test for correlation.<br><br>
The result is counterintuitive and fascinating:
<ul>
  <li>Massive 350,000-word epics like <em>Martin Chuzzlewit</em> and <em>Dombey and Son</em> hover near the bottom (fewer than 10 screen adaptations).</li>
  <li>Meanwhile, high in the upper-left quadrant sits <strong>A Christmas Carol (28,429 words)</strong> with an astonishing <strong>135+ adaptations</strong>!</li>
  <li>There is actually a <em>negative</em> correlation between word count and cinematic immortality!</li>
</ul>
<strong>📊 Today's Data Storytelling Lesson: Reference Quadrants</strong><br>
<ol>
  <li><strong>Quadrant Lines:</strong> Add faint dashed crosshairs at the median word count and median adaptation count. Suddenly, the scatter plot splits into 4 clear stories: <em>'Concise Classics'</em>, <em>'Sprawling Giants'</em>, <em>'Overlooked Gems'</em>, and <em>'Niche Epics'</em>.</li>
  <li><strong>Callout Arrows:</strong> Point an arrow directly at the lone dot in the upper left: <em>'A Christmas Carol: Compact, universal, timeless.'</em></li>
</ol>
<em>But numbers have long memories.</em><br><br>
#ScatterPlot #Correlation #DataStorytelling #VisualAnalytics #CharlesDickens""",
        "storytelling_rule": "Divide and conquer with quadrants. Adding median reference lines across a scatter plot creates four intuitive narrative zones for your audience."
    },
    {
        "id": 16,
        "act": "ACT III: THE GHOST OF DATA PRESENT",
        "day": "DAY 16",
        "title": "The Bubble Chart: The 3D Literary Landscape",
        "chart_type": "Correlation & Magnitude / 3-Variable Landscape",
        "question": "How do Book Length, Character Count, and Film Adaptations intersect?",
        "image": "img24/image16.png",
        "dickens_data": {
            "theme": "X: Word Count | Y: Character Count | Bubble Size: Screen Adaptations",
            "key_metric": "David Copperfield: 360k words, 156 characters, 26 adaptations | Oliver Twist: 158k words, 119 characters, 38 adaptations",
            "historical_context": "Oliver Twist struck the sweet spot: moderate word count, vivid street characters, and high cinematic momentum.",
            "fun_fact": "Dickens suffered from Obsessive-Compulsive disorder: he had to comb his hair hundreds of times a day, rearrange hotel furniture to match his home study, and inspect his children's bedrooms every morning for tidiness!"
        },
        "quote": "“There are books of which the backs and covers are by far the best parts.” — Oliver Twist (1838)",
        "headline_lesson": {
            "bad_title": "Bubble Chart: Word Count, Characters, and Adaptations",
            "action_headline": "The Cinematic Sweet Spot: Compact Plots with High Character Drama Yielded the Greatest Screen Legacy",
            "rule": "Scale by Area, Never Diameter: When sizing bubbles, bubble AREA must be proportional to the metric. Scaling by radius/diameter quadruples perceived size and lies to the reader."
        },
        "post_copy": """🎄 <strong>DAY 16 | A Christmas Chart Carol</strong><br>
<em>Window 16: The Bubble Chart</em><br><br>
Two dimensions tell a story. A third dimension can transform the narrative.<br><br>
A <strong>bubble chart</strong> extends the scatter plot by varying the marker size based on a third quantitative variable:
<ul>
  <li><strong>X-axis:</strong> Novel Word Count (Scale of the book)</li>
  <li><strong>Y-axis:</strong> Character Count (Crowdedness of the fictional world)</li>
  <li><strong>Bubble Size:</strong> Number of Screen/Stage Adaptations (Cultural footprint)</li>
</ul>
Instantly, <em>Oliver Twist</em> and <em>Great Expectations</em> pop off the canvas. They don't have the monstrous 360,000 words of <em>Bleak House</em>, but their bubbles are massive because their focused plots and iconic characters made them Hollywood gold.<br><br>
<strong>📊 Today's Data Storytelling Lesson: The Bubble Scaling Law</strong><br>
⚠️ <strong>The #1 Lie in Bubble Charts:</strong><br>
If Adaptation Count doubles from 20 to 40, you must double the **area** of the circle (pi * r^2). If you double the radius, the circle's visual area multiplies by **400%**, grossly distorting the data.<br>
Always scale bubbles by area, and keep bubbles slightly transparent so overlapping circles don't swallow their neighbors.<br><br>
<em>But numbers have long memories.</em><br><br>
#BubbleChart #DataVisualization #Tufte #DataIntegrity #CharlesDickens""",
        "storytelling_rule": "Scale bubble markers strictly by area. Scaling radius quadruples perceived weight, distorting executive risk assessments."
    },
    {
        "id": 17,
        "act": "ACT III: THE GHOST OF DATA PRESENT",
        "day": "DAY 17",
        "title": "The Treemap: The Architecture of an Empire",
        "chart_type": "Part-to-Whole / Hierarchical Space-Filling Rectangles",
        "question": "How does Dickens' complete lifetime literary output divide by format?",
        "image": "img24/image17.png",
        "dickens_data": {
            "theme": "Total Lifetime Output Breakdown: Novels vs Christmas Books vs Journalism vs Plays vs Travelogues",
            "key_metric": "Novels: 68% of words | Journalism & Essays: 18% | Christmas Books: 5% | Travelogues: 5% | Plays: 4%",
            "historical_context": "While celebrated for his novels, Dickens wrote hundreds of crusading journalistic articles on child labor, public hangings, sanitation, and education.",
            "fun_fact": "Dickens was an avid amateur actor, director, and playwright. He built a private theater inside his home at Tavistock House and staged elaborate productions for Victorian high society!"
        },
        "quote": "“In the little world in which children have their existence, whosoever brings them up, there is nothing so finely perceived and so finely felt, as injustice.” — Great Expectations (1861)",
        "headline_lesson": {
            "bad_title": "Breakdown of Dickens' Works by Category",
            "action_headline": "Far Beyond Novels: Journalism and Social Essays Comprised Nearly 20% of Dickens' Lifelong Ink",
            "rule": "Treemaps Replace Pie Charts: When visualizing hierarchical part-to-whole with more than 5 slices, use a treemap. Rectangles preserve area perception and fill rectangular screens perfectly."
        },
        "post_copy": """🎄 <strong>DAY 17 | A Christmas Chart Carol</strong><br>
<em>Window 17: The Treemap</em><br><br>
Please, retire the 12-slice 3D pie chart.<br><br>
When you need to visualize nested part-to-whole relationships, the <strong>treemap</strong> is your most elegant weapon.<br><br>
Using space-filling nested rectangles, we partition Dickens' entire lifetime output:
<ul>
  <li><strong>The Master Novels (68% of output):</strong> Spanning 15 massive rectangles.</li>
  <li><strong>Journalism & Editorial Columns (18%):</strong> Over 350 crusading articles exposing Victorian poverty, sanitary reforms, and workhouse brutality.</li>
  <li><strong>Christmas Books & Novellas (5%):</strong> 5 beloved holiday stories.</li>
  <li><strong>Travel Writing (5%):</strong> <em>American Notes</em> and <em>Pictures from Italy</em>.</li>
  <li><strong>Plays & Farces (4%):</strong> His vibrant theater scripts.</li>
</ul>
<strong>📊 Today's Data Storytelling Lesson: Rectangles vs. Slices</strong><br>
- The human brain struggles to compare angles in pie charts, especially beyond 3 or 4 slices.<br>
- Treemaps maintain a rigid rectangular bounding box, fitting perfectly onto modern 16:9 slides and mobile screens.<br>
- Use color intensity to represent a secondary metric (e.g. average adaptation rate per category).<br><br>
<em>But numbers have long memories.</em><br><br>
#Treemap #DataDesign #NoMorePieCharts #InformationDesign #CharlesDickens""",
        "storytelling_rule": "Retire pie charts for multi-level structures. Treemaps preserve screen real estate, eliminate circular distortion, and show hierarchy at a glance."
    },
    {
        "id": 18,
        "act": "ACT III: THE GHOST OF DATA PRESENT",
        "day": "DAY 18",
        "title": "The Waterfall Chart: The Economics of Christmas 1843",
        "chart_type": "Flow / Step-by-Step Variance Bridge",
        "question": "How did a runaway bestseller yield a shocking financial disappointment?",
        "image": "img24/image18.png",
        "dickens_data": {
            "theme": "The Financial Balance Sheet of A Christmas Carol (1843)",
            "key_metric": "Gross Sales: £1,050 (6,000 copies sold out) -> Extravagant Binding (-£250) -> 4 Color Plates (-£380) -> Publisher Commission (-£283) -> Net Profit: Only £137!",
            "historical_context": "Expecting to earn £1,000 to clear debts, Dickens insisted on lavish salmon-cloth binding, gilt edges, and hand-colored etchings by John Leech, which cannibalized his profits.",
            "fun_fact": "When Dickens received the meager royalty statement of just £137 on his massive bestseller, he wrote in fury to his friend John Forster: 'I have broken my heart over it... what a wonderful thing it is that such a great success should produce such a small result!'"
        },
        "quote": "“Annual income twenty pounds, annual expenditure nineteen nineteen and six, result happiness. Annual income twenty pounds, annual expenditure twenty pounds ought and six, result misery.” — Mr. Micawber, David Copperfield (1850)",
        "headline_lesson": {
            "bad_title": "Revenue and Cost Bridge for A Christmas Carol",
            "action_headline": "The Price of Perfection: How Lavish Gilt Edges and Hand-Colored Plates Reduced Dickens' Bestseller Profit to Just £137",
            "rule": "The Bridge Story: Waterfall charts explain the 'why' behind the end result by showing positive inflows and negative cost deductions in sequence."
        },
        "post_copy": """🎄 <strong>DAY 18 | A Christmas Chart Carol</strong><br>
<em>Window 18: The Waterfall Chart</em><br><br>
We started with a runaway Christmas bestseller.<br>
All 6,000 copies sold out in five frantic days before Christmas Eve 1843.<br>
Dickens anticipated a massive windfall of £1,000 to clear his family debts.<br><br>
He received a check for just <strong>£137</strong>.<br><br>
What happened? A static profit table conceals the tragedy. A <strong>waterfall chart</strong> reveals the step-by-step causal bridge:
<ol>
  <li><strong>Starting Gross Revenue:</strong> +£1,050 (6,000 copies sold at 5 shillings each)</li>
  <li><strong>Lavish Crimson Cloth & Gilt Edges:</strong> -£250 (Dickens insisted on luxury binding)</li>
  <li><strong>Hand-Colored Etchings by John Leech:</strong> -£380 (Exquisite, but prohibitively expensive)</li>
  <li><strong>Advertising & Promotion:</strong> -£180</li>
  <li><strong>Publishers' Commission (Chapman & Hall):</strong> -£103</li>
  <li><strong>Ending Net Profit:</strong> <strong>Just £137</strong>!</li>
</ol>
<strong>📊 Today's Data Storytelling Lesson: The Causal Journey</strong><br>
A waterfall chart is the gold standard of business explanation:<br>
- Green/grey bars for starting volume.<br>
- Red bars for deductions and expenses.<br>
- Floating bridge connectors that show how you travelled from high expectations to modest reality.<br><br>
The second spirit bows and fades into the winter frost.<br>
The shadows lengthen. What lies in the future?<br><br>
<em>But numbers have long memories.</em><br><br>
#WaterfallChart #BridgeChart #FinancialStorytelling #AChristmasCarol #CharlesDickens""",
        "storytelling_rule": "Use waterfall charts to transform static variance into a sequential narrative of causes, moving step-by-step from starting ambition to final net outcome."
    },
    {
        "id": 19,
        "act": "ACT IV: THE GHOST OF DATA YET TO COME",
        "day": "DAY 19",
        "title": "The Forecast Chart: The Mystery That Never Finished",
        "chart_type": "Projections / Historical Actuals vs. Extrapolated Future",
        "question": "What if Charles Dickens had lived to complete 'The Mystery of Edwin Drood'?",
        "image": "img24/image19.png",
        "dickens_data": {
            "theme": "The Mystery of Edwin Drood (6 of 12 parts published at his death on 9 June 1870)",
            "key_metric": "Completed: 84,000 words (6 parts) | Extrapolated planned novel: 168,000 words (12 parts)",
            "historical_context": "On 8 June 1870, Dickens worked all day in his garden chalet on Chapter 23 of Edwin Drood. That evening he suffered a fatal stroke, leaving the murderer's identity an eternal mystery.",
            "fun_fact": "Scores of authors, playwrights, and even a spiritualist medium in 1873 have attempted to 'complete' Edwin Drood. In 1914, G.K. Chesterton and George Bernard Shaw staged a mock trial of John Jasper for the murder of Edwin Drood!"
        },
        "quote": "“The data ends. The stories do not.” — A Christmas Chart Carol",
        "headline_lesson": {
            "bad_title": "Actual and Projected Words for Edwin Drood",
            "action_headline": "The Silent Cutoff: Solid Actuals End at Chapter 23 as Dickens' Final Mystery Fades into History",
            "rule": "The Cutoff Line Rule: Never disguise projection as fact. Historical data must be solid; forward projections must be dashed with a vertical milestone line."
        },
        "post_copy": """🎄 <strong>DAY 19 | A Christmas Chart Carol</strong><br>
<em>Window 19: The Forecast Chart</em><br>
🔮 <strong>Enter The Ghost of Data Yet to Come</strong><br><br>
The third spirit does not speak.<br>
It points a shrouded, dark arm toward a line that ventures beyond our latest recorded observation.<br><br>
On 8 June 1870, Charles Dickens sat in his garden chalet at Gads Hill, writing Chapter 23 of <em>The Mystery of Edwin Drood</em>. He planned 12 monthly installments. He had finished exactly six.<br>
The next morning, his pen stopped forever.<br><br>
Look at how our forecast chart handles this tragic milestone:
<ul>
  <li>To the left of 9 June 1870 lies <strong>Recorded History (84,000 words)</strong>—drawn in an unwavering, solid black line.</li>
  <li>At 9 June 1870 stands a vertical dashed demarcation: <strong>The Cutoff Boundary</strong>.</li>
  <li>To the right extends the <strong>Projected Horizon (168,000 words)</strong>—rendered in a faded, dashed vector into the mist.</li>
</ul>
<strong>📊 Today's Data Storytelling Lesson: Demarcating Fact from Forecast</strong><br>
👉 <strong>Never camouflage prediction as fact!</strong><br>
1. Always use a solid stroke for actual recorded results.<br>
2. Transition into a distinct dashed or tinted stroke the exact millisecond you cross the forecast boundary.<br>
3. If your executive dashboard blurs the line between booked performance and future projection, you aren't forecasting—you're deceiving your audience.<br><br>
<em>But numbers have long memories.</em><br><br>
#ForecastChart #DataStorytelling #PredictiveAnalytics #EdwinDrood #CharlesDickens""",
        "storytelling_rule": "Draw an unmistakable boundary between history and hypothesis. Solid lines for documented actuals; dashed strokes for modeled forecasts."
    },
    {
        "id": 20,
        "act": "ACT IV: THE GHOST OF DATA YET TO COME",
        "day": "DAY 20",
        "title": "The Fan Chart: The American Copyright Phantom",
        "chart_type": "Projections / Quantifying Uncertainty with Confidence Bands",
        "question": "How much did Dickens lose to unauthorized 19th-century American piracy?",
        "image": "img24/image20.png",
        "dickens_data": {
            "theme": "Estimated Lost International Royalties due to lack of International Copyright (1840–1867)",
            "key_metric": "Estimated authorized earnings: ~£15,000 | Lost pirate royalties range: P10: £50,000 | P50: £120,000 | P90: £250,000 (millions today)",
            "historical_context": "US publishers routinely bought single copies off British packet ships and reprinted entire Dickens novels within 24 hours without paying him a single penny.",
            "fun_fact": "During his 1842 tour of America, Dickens boldly campaigned at every banquet for international copyright protection. American newspapers attacked him viciously, accusing him of coming to America to count their cash!"
        },
        "quote": "“My life has been a long one, and I have had many troubles, most of which never happened.” — Charles Dickens",
        "headline_lesson": {
            "bad_title": "Projected Lost US Royalties for Dickens",
            "action_headline": "The Fan of Uncertainty: Modeling Up to £250,000 in Stolen Royalties from 19th-Century American Book Piracy",
            "rule": "Replace False Precision with Fans: A single-point forecast ('He lost £124,532') is an illusion. Use P10, P50, and P90 shaded bands to communicate true uncertainty."
        },
        "post_copy": """🎄 <strong>DAY 20 | A Christmas Chart Carol</strong><br>
<em>Window 20: The Fan Chart</em><br><br>
A forecast presented as a single, precise decimal number is an illusion.<br><br>
<em>'Dickens lost exactly £134,250 in American royalties.'</em><br>
Really? Down to the exact tenner?<br><br>
A <strong>fan chart</strong> (popularized by the Bank of England for economic forecasting) surrounds a central projection with probabilistic confidence bands:
<ul>
  <li><strong>Dark core band (P50):</strong> The median plausible path (~£120,000 lost).</li>
  <li><strong>Medium translucent band (P70):</strong> The probable historical range (£80,000 to £170,000).</li>
  <li><strong>Outer soft fan (P90):</strong> The extreme boundary (£50,000 to £250,000—accounting for unauthorized Canadian reprints, stage bootlegs, and serialized newspaper syndicates).</li>
</ul>
<strong>📊 Today's Data Storytelling Lesson: Embracing Uncertainty</strong><br>
In analytics and leadership, acknowledging uncertainty is not a sign of weakness—it is the hallmark of intellectual honesty.<br>
Give your audience a realistic range they can prepare for, not a false single point they will hold you hostage to.<br><br>
<em>But numbers have long memories.</em><br><br>
#FanChart #Uncertainty #DataVisualization #RiskAnalysis #CharlesDickens""",
        "storytelling_rule": "Acknowledge uncertainty with confidence bands. Presenting a single point estimate conceals volatility; a fan chart educates decision-makers on risk."
    },
    {
        "id": 21,
        "act": "ACT IV: THE GHOST OF DATA YET TO COME",
        "day": "DAY 21",
        "title": "The Scenario Chart: The Branching Roads of Publishing",
        "chart_type": "Projections / Discrete Strategic Alternatives",
        "question": "What three publishing paths shaped the economics of Victorian authors?",
        "image": "img24/image21.png",
        "dickens_data": {
            "theme": "Strategic Publishing Scenarios: 3-Decker Novel vs Monthly Parts vs Weekly Journal",
            "key_metric": "Path A (Traditional 3-Volume): £300 flat fee | Path B (Monthly Parts): £3,000+ profit share | Path C (Self-Owned Journal): £10,000+ brand ecosystem",
            "historical_context": "Dickens broke away from predatory publisher contracts to own his own periodicals, ensuring he retained copyright and subscription cash flow.",
            "fun_fact": "Dickens walked out on his original publishers Bradbury and Evans in 1859 because they refused to print his personal statement defending his separation from Catherine in their magazine Punch!"
        },
        "quote": "“We need never be ashamed of our tears.” — Great Expectations (1861)",
        "headline_lesson": {
            "bad_title": "Comparison of Three Publishing Models",
            "action_headline": "Own the Platform: How Dickens 10x'd His Wealth by Ditching Traditional Publishers for His Own Periodicals",
            "rule": "Scenario Actionability: Every branching scenario line on a chart must correspond to an operational decision lever."
        },
        "post_copy": """🎄 <strong>DAY 21 | A Christmas Chart Carol</strong><br>
<em>Window 21: The Scenario Chart</em><br><br>
The future does not march down a single railroad track. It branches.<br><br>
A <strong>scenario chart</strong> displays distinct, plausible alternative futures originating from a single turning point:<br>
<ul>
  <li>🛤️ <strong>Path A (The Status Quo):</strong> Selling outright copyright to a traditional publisher for a flat £300 fee (what most Victorian authors did, dying in poverty).</li>
  <li>🛤️ <strong>Path B (The Serial Innovator):</strong> Retaining copyright and publishing in 1-shilling monthly parts (generating £2,000–£4,000 per novel).</li>
  <li>🚀 <strong>Path C (The Platform Mogul):</strong> Launching his own weekly periodicals (<em>Household Words</em> and <em>All the Year Round</em>)—capturing subscription cash flow, syndication rights, and global speaking fame.</li>
</ul>
<strong>📊 Today's Data Storytelling Lesson: Actionable Scenarios</strong><br>
A forecast tells people what might happen.<br>
A scenario chart prepares people for <strong>what actions to take</strong>.<br>
Never draw 3 scenario lines without labeling the operational trigger that moves you from Path A to Path C.<br><br>
<em>But numbers have long memories.</em><br><br>
#ScenarioPlanning #StrategicThinking #DataStorytelling #PublishingStrategy #CharlesDickens""",
        "storytelling_rule": "Tie every scenario line to a concrete decision trigger. If a branching curve does not inform an executive choice, remove it from the slide."
    },
    {
        "id": 22,
        "act": "ACT IV: THE GHOST OF DATA YET TO COME",
        "day": "DAY 22",
        "title": "The Sankey Diagram: From Victorian Ink to Global Screen",
        "chart_type": "Flow / Multi-Stage Categorical Volume Migration",
        "question": "How did 15 Victorian novels flow into 300+ modern film, stage, and TV adaptations?",
        "image": "img24/image22.png",
        "dickens_data": {
            "theme": "Adaptation Flow (data/dickens/dickens_adaptations.csv)",
            "key_metric": "15 Novels -> 300+ Adaptations -> 135 Feature Films, 85 TV Series, 60 Stage Musicals, 20 Animated Classics",
            "historical_context": "The journey of Dickens' characters from 19th-century serialized pamphlets to contemporary Hollywood blockbusters and West End musicals.",
            "fun_fact": "The musical 'Oliver!' was a runaway Broadway smash, running for 774 performances and winning 3 Tony Awards before becoming the 1968 Best Picture Oscar winner!"
        },
        "quote": "“A loving heart is the truest wisdom.” — David Copperfield (1850)",
        "headline_lesson": {
            "bad_title": "Flowchart of Dickens Adaptations by Media Type",
            "action_headline": "The Flow of Immortality: How 15 Victorian Novels Traveled Through Time to Spawn Over 300 Modern Screen Masterpieces",
            "rule": "The Sankey Ribbon Rule: Ribbon width represents flow volume. Keep flow nodes to 4–6 per stage to prevent the chart from degenerating into a visual knot."
        },
        "post_copy": """🎄 <strong>DAY 22 | A Christmas Chart Carol</strong><br>
<em>Window 22: The Sankey Diagram</em><br><br>
Where did the stories travel? And how did they branch across centuries?<br><br>
A <strong>Sankey diagram</strong> visualizes the movement and transformation of volume between stages, where the width of each flowing ribbon is strictly proportional to quantity.<br><br>
Follow the extraordinary 180-year cultural migration of Dickens' imagination:
<ul>
  <li><strong>Stage 1 (The Source):</strong> 15 Master Novels penned by candlelight in London.</li>
  <li><strong>Stage 2 (The Primary Pillars):</strong> <em>A Christmas Carol</em> (135+ branches), <em>Oliver Twist</em> (38 branches), <em>Great Expectations</em> (34 branches), and <em>David Copperfield</em> (26 branches).</li>
  <li><strong>Stage 3 (The Modern Mediums):</strong> Flowing outward into <strong>135 Feature Films</strong>, <strong>85 BBC/PBS Television Dramas</strong>, <strong>60 West End/Broadway Theatrical Musicals</strong>, and <strong>20 Animated Adaptations</strong>.</li>
</ul>
<strong>📊 Today's Data Storytelling Lesson: Volume in Motion</strong><br>
When movement and categorical migration are the story, a Sankey diagram is mesmerizing.<br>
- Keep your stages clean (Source $\rightarrow$ Channel $\rightarrow$ Destination).<br>
- Use color on the source nodes that flows through the ribbons so readers can trace the lineage of each story with ease.<br><br>
<em>But numbers have long memories.</em><br><br>
#SankeyDiagram #DataFlow #DataDesign #CulturalAnalytics #CharlesDickens""",
        "storytelling_rule": "Sankey ribbons tell the story of transformation. Use consistent color pathways from source to destination so viewers can trace volume effortlessly."
    },
    {
        "id": 23,
        "act": "ACT IV: THE GHOST OF DATA YET TO COME",
        "day": "DAY 23",
        "title": "The Connected Scatterplot: The Price of Genius",
        "chart_type": "Correlation & Time / Two Metrics Traveling Through Life",
        "question": "How did Dickens' creative output intersect with his declining physical health?",
        "image": "img24/image23.png",
        "dickens_data": {
            "theme": "Creative Productivity vs. Physical Health Index (1835–1870)",
            "key_metric": "1835–1845: High Health / High Output -> 1855–1865: Moderate Health / Peak Fame -> 1868–1870: Dangerous Health Collapse / Manic Reading Tours",
            "historical_context": "Dickens drove himself to exhaustion on his American and British reading tours despite gout, kidney trouble, and mini-strokes, ignoring his physician's warnings.",
            "fun_fact": "On 9 June 1865, Dickens was in the catastrophic Staplehurst rail crash. His carriage hung suspended over a ravine. After helping dying victims and pouring brandy down their throats, he climbed back into the precarious train car to rescue the manuscript of Our Mutual Friend!"
        },
        "quote": "“I have no words to tell you what I feel... but while I have life, I will write.” — Charles Dickens",
        "headline_lesson": {
            "bad_title": "Dickens Productivity vs Health Index Over Career",
            "action_headline": "The Flight Path of Genius: How Dickens' Relentless Ambition Pushed Creative Output High Even as Vitality Collapsed",
            "rule": "Directional Time Loops: In a connected scatterplot, connect chronological points with arrows to reveal how a relationship evolves and cycles over time."
        },
        "post_copy": """🎄 <strong>DAY 23 | A Christmas Chart Carol</strong><br>
<em>Window 23: The Connected Scatterplot</em><br><br>
Today, two foundational measures travel through time hand-in-hand.<br><br>
A <strong>connected scatterplot</strong> plots Metric A on the X-axis (Physical Vitality) and Metric B on the Y-axis (Annual Creative & Performance Output), then connects consecutive years with a directional line.<br><br>
Watch Charles Dickens' tragic, heroic flight path across 35 years:
<ul>
  <li><strong>1835–1845 (The Golden Youth):</strong> High health, boundless stamina, and soaring literary output.</li>
  <li><strong>1846–1858 (Mid-Career Mastery):</strong> Tremendous creative power maintaining steady health.</li>
  <li><strong>1865 (The Staplehurst Rail Crash):</strong> A traumatic inflection point; health drops sharply.</li>
  <li><strong>1867–1870 (The Fatal Loop):</strong> The line swoops left into the danger zone: health collapses from grueling travel and winter readings, yet Dickens forces his performance output higher and higher until his final collapse.</li>
</ul>
A plot with memory. A relationship with momentum. A chart with a beginning, a middle, and a heartbreaking turning point.<br><br>
Tomorrow is Christmas Eve.<br>
The spirits have completed their visitation.<br>
Tomorrow... the storyteller becomes the story.<br><br>
<em>But numbers have long memories.</em><br><br>
#ConnectedScatterplot #DataStorytelling #BiographyInNumbers #InformationDesign #CharlesDickens""",
        "storytelling_rule": "Connect time sequentially. A connected scatterplot transforms a static cloud of dots into an animated, cinematic flight path of cause and effect."
    },
    {
        "id": 24,
        "act": "CHRISTMAS EVE GRAND FINALE",
        "day": "DAY 24",
        "title": "Charles Dickens: A Life in Data (1812–1870)",
        "chart_type": "Temporal Timeline / The Grand Narrative Finale",
        "question": "What is the ultimate moral of data storytelling?",
        "image": "img24/image24.png",
        "dickens_data": {
            "theme": "The Master Literary Timeline (1812–1870) & Unfinished Mystery",
            "key_metric": "58 Years of Life | 15 Novels | 5 Christmas Books | 989 Characters | 300+ Adaptations | 1843 A Christmas Carol",
            "historical_context": "Dickens died at Gads Hill Place on 9 June 1870. Against his wish for a quiet country burial, the British nation demanded he be laid to rest in Poets' Corner, Westminster Abbey.",
            "fun_fact": "His simple tombstone in Westminster Abbey bears no elaborate titles—only the words: 'Charles Dickens. Born 7th February 1812. Died 9th June 1870.'"
        },
        "quote": "“God bless us, every one!” — Tiny Tim, A Christmas Carol (1843)",
        "headline_lesson": {
            "bad_title": "Timeline of Charles Dickens' Life and Works",
            "action_headline": "The Data Ends, The Stories Do Not: Charles Dickens' 58 Years of Life and the Immortality of Human Storytelling",
            "rule": "The Grand Storytelling Moral: A chart shows what happened. A good chart helps us understand why. A great data story moves human beings to empathy, action, and decision."
        },
        "post_copy": """🎄 <strong>DAY 24 | A Christmas Chart Carol</strong><br>
<em>Christmas Eve Grand Finale</em><br>
🌟 <strong>The Storyteller Becomes the Story</strong><br><br>
For twenty-three days, we have opened windows into charts, asking them to tell us stories about word counts, character populations, publication volumes, box office adaptations, and the price of genius.<br><br>
Today, on Christmas Eve, we turn the visual lens upon the master storyteller himself:<br><br>
📜 <strong>Charles Dickens: A Life in Data (1812–1870)</strong><br><br>
Across six decades of Victorian history, his life unfolds along a cinematic timeline of extraordinary creative triumph and personal struggle:
<ul>
  <li><strong>1812:</strong> Born in Portsmouth into humble clerk obscurity.</li>
  <li><strong>1824:</strong> Traumatized at age 12, pasting labels in Warren's Blacking Factory while his father sits in debtors' prison.</li>
  <li><strong>1836:</strong> <em>The Pickwick Papers</em> triggers a global publishing revolution.</li>
  <li><strong>1838:</strong> <em>Oliver Twist</em> exposes London's brutal workhouses.</li>
  <li><strong>1849:</strong> <em>David Copperfield</em> captures his semi-autobiographical heart.</li>
  <li><strong>1852:</strong> <em>Bleak House</em> takes down institutional bureaucracy.</li>
  <li><strong>1859:</strong> <em>A Tale of Two Cities</em> records sacrifice and resurrection.</li>
  <li><strong>1861:</strong> <em>Great Expectations</em> meditates on conscience and humility.</li>
</ul>
And glowing at the dead center of the visual:<br>
⭐ <strong>1843 — A Christmas Carol</strong><br><br>
Notice how the timeline reaches 1870 and does not conclude with a neat, closed border. It fades into soft Victorian mist alongside his final, unfinished manuscript:<br>
<em>The Mystery of Edwin Drood.</em><br><br>
The data points end. The stories never do.<br><br>
---<br><br>
### The Moral of Our 24-Day Journey:<br><br>
Over the past 24 days, we explored bar charts, slope charts, dumbbell plots, histograms, waterfalls, fan charts, and Sankey diagrams.<br><br>
<strong>None of them was ever really about the software.</strong><br>
None of them was about the graphic format.<br><br>
The heart of data visualization is—and has always been—<strong>the human story behind the numbers</strong>.
<ul>
  <li>A chart shows what happened.</li>
  <li>A good chart helps us understand why it happened.</li>
  <li>A great data story inspires the empathy and courage to decide what happens next.</li>
</ul>
<strong>Past. Present. Yet to Come.</strong><br><br>
Perhaps Charles Dickens would have understood modern data storytelling rather well.<br><br>
After all...<br><br>
✨ <em>Numbers have long memories. But stories give them a soul.</em><br><br>
Merry Christmas to you, your teams, and your families.<br><br>
Frank Ellingsen<br>
<em>Tales with Charts</em><br>
Portfolio: https://frank-ellingsen.github.io/chart_tales/<br><br>
#AChristmasChartCarol #CharlesDickens #DataStorytelling #DataVisualization #Tufte #VisualVocabulary #Infographics #MerryChristmas""",
        "storytelling_rule": "The Soul of Data: Data without narrative is a cold ledger. Narrative without data is speculation. When fused with intentional design, data storytelling inspires human action."
    }
]

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>A Christmas Chart Carol — 24-Day Advent Calendar & Masterclass</title>
<style>
  @page {
    size: A4 portrait;
    margin: 7mm 10mm 7mm 10mm;
  }
  
  * {
    box-sizing: border-box;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }
  
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #1E293B;
    background-color: #FFFFFF;
    margin: 0;
    padding: 0;
    font-size: 8.8pt;
    line-height: 1.4;
  }

  /* PAGE 1: COVER PAGE with image00 on top */
  .cover-page {
    page-break-after: always;
    break-after: page;
    min-height: 98vh;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 16mm 14mm 16mm 14mm;
    background: linear-gradient(135deg, #0A1128 0%, #101F42 55%, #1A2E5A 100%);
    color: #FFFFFF;
    border-radius: 4px;
  }

  .cover-header {
    border-bottom: 2px solid #C5A059;
    padding-bottom: 10px;
    margin-bottom: 12px;
  }

  .cover-series {
    font-size: 11pt;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #C5A059;
    font-weight: 700;
    margin-bottom: 6px;
  }

  .cover-title {
    font-size: 28pt;
    font-weight: 800;
    line-height: 1.15;
    margin: 0 0 6px 0;
    color: #FFFFFF;
  }

  .cover-subtitle {
    font-size: 14pt;
    font-style: italic;
    color: #E2E8F0;
    margin: 0;
  }

  .cover-hero-box {
    text-align: center;
    margin: 10px 0;
  }

  .cover-hero-img {
    max-height: 380px;
    max-width: 95%;
    border-radius: 8px;
    border: 3px solid #C5A059;
    box-shadow: 0 14px 32px rgba(0,0,0,0.6);
  }

  .cover-footer {
    border-top: 1px solid rgba(197, 160, 89, 0.4);
    padding-top: 10px;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    font-size: 9pt;
    color: #CBD5E1;
  }

  .cover-author strong {
    color: #FFFFFF;
    font-size: 11pt;
  }

  .cover-meta {
    text-align: right;
  }

  .cover-meta span {
    color: #C5A059;
    font-weight: 600;
  }

  /* PAGE 2: TABLE OF CONTENTS */
  .toc-page {
    page-break-after: always;
    break-after: page;
    padding: 4mm 4mm;
  }

  .section-title {
    font-size: 16pt;
    font-weight: 800;
    color: #0A1128;
    border-bottom: 2px solid #C5A059;
    padding-bottom: 5px;
    margin-bottom: 10px;
  }

  .toc-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 7.2pt;
  }

  .toc-table th {
    background-color: #0A1128;
    color: #FFFFFF;
    text-align: left;
    padding: 2.5px 5px;
    font-weight: 600;
    border: none;
  }

  .toc-table td {
    padding: 1.5px 5px;
    border-bottom: 1px solid #E2E8F0;
  }

  .toc-table tr:nth-child(even) td {
    background-color: #F8FAFC;
  }

  .badge {
    display: inline-block;
    padding: 1.5px 5px;
    border-radius: 3px;
    font-size: 7pt;
    font-weight: 700;
    text-transform: uppercase;
  }

  .badge-teaser { background-color: #F1F5F9; color: #334155; }
  .badge-act1 { background-color: #FEF3C7; color: #92400E; }
  .badge-act2 { background-color: #DBEAFE; color: #1E40AF; }
  .badge-act3 { background-color: #FEE2E2; color: #991B1B; }
  .badge-act4 { background-color: #EDE9FE; color: #5B21B6; }
  .badge-finale { background-color: #D1FAE5; color: #065F46; }

  /* PAGE 3: 24-DAY ADVENT CALENDAR VISUAL SPREAD */
  .calendar-spread-page {
    page-break-after: always;
    break-after: page;
    padding: 4mm 2mm;
    min-height: 98vh;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  .calendar-header {
    text-align: center;
    border-bottom: 2px solid #C5A059;
    padding-bottom: 6px;
    margin-bottom: 10px;
  }
  .calendar-header h2 {
    font-size: 15pt;
    font-weight: 800;
    color: #0A1128;
    margin: 0;
  }
  .calendar-header p {
    font-size: 8pt;
    color: #64748B;
    margin: 2px 0 0 0;
  }

  .calendar-grid-24 {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: repeat(6, 1fr);
    gap: 8px;
    flex-grow: 1;
  }

  .cal-window {
    border: 1px solid #CBD5E1;
    border-radius: 5px;
    background: #F8FAFC;
    padding: 4px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: 0 2px 5px rgba(0,0,0,0.04);
  }

  .cal-window.act1 { border-top: 3px solid #F59E0B; }
  .cal-window.act2 { border-top: 3px solid #3B82F6; }
  .cal-window.act3 { border-top: 3px solid #EF4444; }
  .cal-window.act4 { border-top: 3px solid #8B5CF6; }
  .cal-window.act-finale { border-top: 3px solid #10B981; background: #F0FDF4; }

  .cal-window-top {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    font-size: 6.8pt;
    font-weight: 700;
    margin-bottom: 2px;
  }
  .cal-day-num {
    background: #0A1128;
    color: #C5A059;
    padding: 1px 4px;
    border-radius: 3px;
    font-size: 7.2pt;
    font-weight: 800;
  }
  .cal-chart-name {
    color: #475569;
    text-transform: uppercase;
    font-size: 6.2pt;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    max-width: 110px;
  }

  .cal-img-box {
    text-align: center;
    background: #050914;
    border-radius: 3px;
    padding: 2px;
    margin: 2px 0;
    min-height: 52px;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .cal-img {
    max-height: 50px;
    max-width: 100%;
    object-fit: contain;
    border-radius: 2px;
  }

  .cal-topic {
    font-size: 6.2pt;
    color: #1E293B;
    font-weight: 600;
    line-height: 1.15;
    overflow: hidden;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
  }

  /* DAILY POST PAGES (PAGES 4–28) */
  .post-page {
    page-break-after: always;
    break-after: page;
    min-height: 97vh;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 0;
  }

  .post-header {
    border-bottom: 2px solid #0A1128;
    padding-bottom: 5px;
    margin-bottom: 8px;
    display: flex;
    justify-content: space-between;
    align-items: baseline;
  }

  .post-day-tag {
    font-size: 9.5pt;
    font-weight: 800;
    color: #C5A059;
    letter-spacing: 1.5px;
    text-transform: uppercase;
  }

  .post-act-title {
    font-size: 8pt;
    color: #64748B;
    font-weight: 600;
    text-transform: uppercase;
  }

  .post-title {
    font-size: 13pt;
    font-weight: 800;
    color: #0A1128;
    margin: 1px 0 0 0;
  }

  .post-grid {
    display: grid;
    grid-template-columns: 46% 54%;
    gap: 12px;
    flex-grow: 1;
    align-items: start;
  }

  .visual-column {
    display: flex;
    flex-direction: column;
    gap: 7px;
  }

  .visual-card {
    background: #F8FAFC;
    border: 1px solid #CBD5E1;
    border-radius: 6px;
    padding: 5px;
    text-align: center;
    box-shadow: 0 3px 8px rgba(0,0,0,0.05);
  }

  .visual-img {
    max-width: 100%;
    max-height: 350px;
    object-fit: contain;
    border-radius: 4px;
    display: block;
    margin: 0 auto;
  }

  .visual-caption {
    font-size: 7pt;
    color: #64748B;
    margin-top: 3px;
    text-align: center;
    font-weight: 500;
  }

  .dickens-box {
    background-color: #F8FAFC;
    border-left: 3px solid #0A1128;
    padding: 7px 9px;
    border-radius: 0 4px 4px 0;
    font-size: 7.8pt;
  }

  .box-title {
    font-weight: 700;
    color: #0A1128;
    margin-bottom: 3px;
    text-transform: uppercase;
    font-size: 7.2pt;
    letter-spacing: 0.5px;
  }

  .dickens-metric {
    margin: 2px 0;
    color: #334155;
    font-size: 7.6pt;
  }

  .quote-box {
    background-color: #FEF9C3;
    border-left: 3px solid #CA8A04;
    padding: 6px 9px;
    border-radius: 0 4px 4px 0;
    font-size: 7.6pt;
    font-style: italic;
    color: #713F12;
  }

  .fun-fact-box {
    background-color: #F0FDF4;
    border-left: 3px solid #16A34A;
    padding: 6px 9px;
    border-radius: 0 4px 4px 0;
    font-size: 7.6pt;
    color: #14532D;
  }

  .content-column {
    display: flex;
    flex-direction: column;
    gap: 7px;
  }

  .lesson-card {
    background: #FFFBEB;
    border: 1px solid #FCD34D;
    border-radius: 5px;
    padding: 7px 9px;
    font-size: 7.8pt;
  }

  .lesson-header {
    font-weight: 800;
    color: #B45309;
    text-transform: uppercase;
    font-size: 7.2pt;
    letter-spacing: 0.5px;
    margin-bottom: 3px;
  }

  .headline-contrast {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 6px;
    margin: 3px 0;
    font-size: 7.4pt;
  }

  .bad-headline {
    background: #FEE2E2;
    border-left: 2px solid #EF4444;
    padding: 3px 5px;
    color: #991B1B;
    border-radius: 2px;
  }

  .good-headline {
    background: #DCFCE7;
    border-left: 2px solid #22C55E;
    padding: 3px 5px;
    color: #166534;
    font-weight: 600;
    border-radius: 2px;
  }

  .linkedin-post-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 6px;
    padding: 8px 10px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.03);
    font-size: 8pt;
    color: #1E293B;
  }

  .linkedin-header {
    display: flex;
    align-items: center;
    gap: 6px;
    border-bottom: 1px solid #F1F5F9;
    padding-bottom: 4px;
    margin-bottom: 6px;
  }

  .linkedin-logo {
    background-color: #0A66C2;
    color: #FFFFFF;
    font-weight: 800;
    padding: 1px 5px;
    border-radius: 3px;
    font-size: 7.5pt;
  }

  .linkedin-author-info {
    font-size: 7.5pt;
    color: #475569;
    line-height: 1.15;
  }

  .linkedin-body {
    max-height: 400px;
    overflow: hidden;
    line-height: 1.35;
  }

  .linkedin-body ul, .linkedin-body ol {
    margin: 3px 0;
    padding-left: 15px;
  }

  .linkedin-body li {
    margin-bottom: 1.5px;
  }

  .takeaway-card {
    background: linear-gradient(135deg, #0A1128 0%, #1A2E5A 100%);
    color: #FFFFFF;
    padding: 6px 10px;
    border-radius: 5px;
    font-size: 7.6pt;
    border-left: 3px solid #C5A059;
  }

  .takeaway-title {
    font-size: 7pt;
    font-weight: 700;
    color: #C5A059;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin-bottom: 2px;
  }

  .page-footer {
    border-top: 1px solid #E2E8F0;
    padding-top: 4px;
    margin-top: 6px;
    display: flex;
    justify-content: space-between;
    font-size: 7pt;
    color: #94A3B8;
  }
</style>
</head>
<body>

<!-- PAGE 1: COVER PAGE with image00 on top -->
<div class="cover-page">
  <div class="cover-header">
    <div class="cover-series">Tales with Charts · Executive Edition</div>
    <h1 class="cover-title">A Christmas Chart Carol</h1>
    <div class="cover-subtitle">24 Lessons in Charts, Visual Storytelling & Charles Dickens</div>
  </div>

  <div class="cover-hero-box">
    <img src="{COVER_IMAGE_B64}" class="cover-hero-img" alt="A Christmas Chart Carol - Cover Poster image00">
  </div>

  <div class="cover-footer">
    <div class="cover-author">
      <strong>Frank Ellingsen</strong><br>
      Data Storyteller & Business Intelligence Specialist<br>
      Series: <em>A Christmas Chart Carol</em> &bull; Portfolio: <em>frank-ellingsen.github.io/chart_tales</em>
    </div>
    <div class="cover-meta">
      24-Day LinkedIn Advent Series<br>
      <span>28-Page Executive Masterclass Report</span><br>
      Featuring: <em>Charles Dickens Life, Books, Adaptations & Lore</em>
    </div>
  </div>
</div>

<!-- PAGE 2: TABLE OF CONTENTS -->
<div class="toc-page">
  <div class="section-title">Masterclass Curriculum & Visual Index</div>
  <p style="font-size: 8pt; color: #475569; margin-bottom: 4px;">
    An executive storytelling roadmap blending Charles Dickens' 35-year literary life with Edward Tufte's data-ink ratio and the Financial Times Visual Vocabulary. Every day delivers an actionable data storytelling lesson on headlines, legends, labels, and chart design grounded in authentic historical and cinematic data.
  </p>

  <table class="toc-table">
    <thead>
      <tr>
        <th style="width: 7%;">Post</th>
        <th style="width: 12%;">Act</th>
        <th style="width: 22%;">Chart & Theme</th>
        <th style="width: 32%;">Dickens Data Anchor & Question</th>
        <th style="width: 27%;">Data Storytelling Lesson</th>
      </tr>
    </thead>
    <tbody>
{TOC_ROWS}
    </tbody>
  </table>

  <div style="margin-top: 3px; padding: 5px 8px; background-color: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 5px; font-size: 7.4pt; color: #475569;">
    <strong>The 4 Pillars of the Dickensian Data Storytelling Masterclass:</strong>
    <ul style="margin: 2px 0 0 14px; padding: 0;">
      <li><strong>Action Headlines vs. Topic Labels:</strong> State the takeaway conclusion directly in the title; never force the reader to decode the insight.</li>
      <li><strong>Direct Labeling over Disconnected Legends:</strong> Eradicate floating color legends; place category names directly at the start or terminus of curves and bars.</li>
      <li><strong>Annotations & Milestone Pointers:</strong> Guide the reader's eye to inflection points, historical turning points, and narrative anomalies.</li>
      <li><strong>Edward Tufte Data-Ink Ratio:</strong> Remove non-essential borders, heavy vertical gridlines, 3D effects, and decorative rainbow fills.</li>
    </ul>
  </div>
</div>

<!-- PAGE 3: 24-DAY ADVENT CALENDAR SPREAD (EVERY CHART) -->
<div class="calendar-spread-page">
  <div class="calendar-header">
    <div style="display: flex; align-items: center; justify-content: center; gap: 16px;">
      <img src="{COVER_IMAGE_B64}" style="height: 44px; width: 130px; object-fit: cover; border-radius: 4px; box-shadow: 0 2px 6px rgba(0,0,0,0.2); border: 1px solid #C5A059;" alt="Advent Calendar Header Banner">
      <div style="text-align: left;">
        <h2 style="font-size: 13.5pt; margin: 0; color: #0A1128;">🎄 The 24-Day Advent Calendar: All 24 Charts & Windows</h2>
        <p style="font-size: 7.5pt; color: #64748B; margin: 1px 0 0 0;">A visual masterclass in charts & storytelling through Charles Dickens &bull; The Ghosts of Data Past, Present & Yet to Come</p>
      </div>
    </div>
  </div>

  <div class="calendar-grid-24">
{CALENDAR_WINDOWS}
  </div>

  <div class="page-footer" style="margin-top: 6px;">
    <div>A Christmas Chart Carol &bull; The 24-Day Advent Visual Grid</div>
    <div>Tales with Charts &bull; Frank Ellingsen</div>
    <div>Page 3 of 28</div>
  </div>
</div>

<!-- PAGES 4–28: THE 25 DETAILED POST PAGES -->
{POST_PAGES}

</body>
</html>
"""

def generate():
    print("Loading optimized image assets...")
    # Load image00 for the cover
    cover_b64 = image_to_base64_jpeg("img24/image00.png", quality=90, max_size=1500)
    print("Cover image00 loaded successfully.")

    # Load high-res post images
    images_b64 = {}
    thumbs_b64 = {}
    for p in dickens_posts:
        path = p["image"]
        images_b64[path] = image_to_base64_jpeg(path, quality=86, max_size=1200)
        thumbs_b64[path] = image_to_thumbnail_jpeg(path, max_size=280, quality=78)
        print(f"Loaded {path}")

    # Build TOC rows
    toc_rows = []
    for p in dickens_posts:
        act = p["act"]
        if "PROLOGUE" in act:
            badge = '<span class="badge badge-teaser">Prologue</span>'
        elif "ACT I" in act:
            badge = '<span class="badge badge-act1">Act I</span>'
        elif "ACT II" in act:
            badge = '<span class="badge badge-act2">Act II</span>'
        elif "ACT III" in act:
            badge = '<span class="badge badge-act3">Act III</span>'
        elif "ACT IV" in act:
            badge = '<span class="badge badge-act4">Act IV</span>'
        else:
            badge = '<span class="badge badge-finale">Finale</span>'

        row = f"""      <tr>
        <td><strong>{p['day']}</strong></td>
        <td>{badge}</td>
        <td><strong>{p['title']}</strong></td>
        <td>{p['question']}</td>
        <td><strong>{p['headline_lesson']['rule'].split(':')[0]}</strong></td>
      </tr>"""
        toc_rows.append(row)

    # Build 24 Calendar Windows (Days 1 to 24)
    cal_windows = []
    for p in dickens_posts:
        if p["id"] == 0:
            continue  # Prologue is covered on cover & Day 0
        
        act = p["act"]
        if "ACT I" in act:
            act_class = "act1"
        elif "ACT II" in act:
            act_class = "act2"
        elif "ACT III" in act:
            act_class = "act3"
        elif "ACT IV" in act:
            act_class = "act4"
        else:
            act_class = "act-finale"

        day_num = p["id"]
        chart_name = p["title"].split(":")[0].replace("The ", "")
        thumb = thumbs_b64[p["image"]]
        short_topic = p["dickens_data"]["theme"].split(":")[0]

        win_html = f"""    <div class="cal-window {act_class}">
      <div class="cal-window-top">
        <span class="cal-day-num">{day_num}</span>
        <span class="cal-chart-name">{chart_name}</span>
      </div>
      <div class="cal-img-box">
        <img src="{thumb}" class="cal-img" alt="Day {day_num} Chart">
      </div>
      <div class="cal-topic">{short_topic}</div>
    </div>"""
        cal_windows.append(win_html)

    # Build Post Pages (Page 4 through 28)
    post_pages = []
    for p in dickens_posts:
        img_b64 = images_b64[p["image"]]
        page_num = p["id"] + 4  # Page 1: Cover, Page 2: TOC, Page 3: Calendar, Page 4+: Posts
        
        post_html = f"""<div class="post-page">
  <div class="post-header">
    <div>
      <div class="post-day-tag">{p['day']} | {p['act']}</div>
      <div class="post-title">{p['title']}</div>
    </div>
    <div class="post-act-title">{p['chart_type']}</div>
  </div>

  <div class="post-grid">
    <div class="visual-column">
      <div class="visual-card">
        <img src="{img_b64}" class="visual-img" alt="{p['title']}">
        <div class="visual-caption">Visual Asset: <code>{os.path.basename(p['image'])}</code> &bull; Category: {p['chart_type']}</div>
      </div>

      <div class="dickens-box">
        <div class="box-title">📜 Charles Dickens Data Anchor</div>
        <div style="font-weight: 700; color: #0A1128; font-size: 8pt;">{p['dickens_data']['theme']}</div>
        <div class="dickens-metric"><strong>Key Metrics:</strong> {p['dickens_data']['key_metric']}</div>
        <div class="dickens-metric"><strong>Historical Context:</strong> {p['dickens_data']['historical_context']}</div>
      </div>

      <div class="fun-fact-box">
        <strong>💡 Dickens Fun Fact:</strong> {p['dickens_data']['fun_fact']}
      </div>

      <div class="quote-box">
        {p['quote']}
      </div>
    </div>

    <div class="content-column">
      <div class="lesson-card">
        <div class="lesson-header">📊 Storytelling Lesson: Headlines & Labels</div>
        <div class="headline-contrast">
          <div class="bad-headline">❌ <strong>Weak Topic:</strong><br>{p['headline_lesson']['bad_title']}</div>
          <div class="good-headline">✅ <strong>Action Headline:</strong><br>{p['headline_lesson']['action_headline']}</div>
        </div>
        <div style="font-size: 7.4pt; color: #451A03; margin-top: 3px;">
          <strong>Rule:</strong> {p['headline_lesson']['rule']}
        </div>
      </div>

      <div class="linkedin-post-card">
        <div class="linkedin-header">
          <div class="linkedin-logo">in</div>
          <div class="linkedin-author-info">
            <strong>Frank Ellingsen</strong> &bull; 1st<br>
            Tales with Charts | Data Storytelling & Visual Intelligence
          </div>
        </div>
        <div class="linkedin-body">
          {p['post_copy']}
        </div>
      </div>

      <div class="takeaway-card">
        <div class="takeaway-title">🎯 Tufte Design & Storytelling Rule</div>
        <div>{p['storytelling_rule']}</div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div>A Christmas Chart Carol &bull; Tales with Charts &bull; Frank Ellingsen</div>
    <div>Charles Dickens: Life, Books, Adaptations & Lore &bull; Portfolio: frank-ellingsen.github.io/chart_tales</div>
    <div>Page {page_num} of 28</div>
  </div>
</div>"""
        post_pages.append(post_html)

    full_html = html_template.replace("{COVER_IMAGE_B64}", cover_b64)
    full_html = full_html.replace("{TOC_ROWS}", "\n".join(toc_rows))
    full_html = full_html.replace("{CALENDAR_WINDOWS}", "\n".join(cal_windows))
    full_html = full_html.replace("{POST_PAGES}", "\n\n".join(post_pages))

    html_out = "a_christmas_chart_carol_report.html"
    with open(html_out, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Generated HTML report: {html_out} ({len(full_html)} bytes)")

    # Convert to PDF with Edge
    pdf_out = "a_christmas_chart_carol_report.pdf"
    edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    cmd = [
        edge,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={os.path.abspath(pdf_out)}",
        os.path.abspath(html_out)
    ]
    print(f"Rendering PDF with Edge headless: {pdf_out}...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(pdf_out):
        size_mb = os.path.getsize(pdf_out) / (1024 * 1024)
        print(f"SUCCESS: Generated PDF report at {pdf_out} ({size_mb:.2f} MB)")
    else:
        print("ERROR: PDF was not generated. Return code:", res.returncode, res.stderr)

if __name__ == "__main__":
    generate()
