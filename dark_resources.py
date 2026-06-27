import re

with open('e:\\EMO\\resources.html', 'r', encoding='utf-8') as f:
    html = f.read()

dark_css_override = """
/* DARK NEO-BRUTALIST OVERRIDES */
:root {
  --emo-primary: #FF4500;
  --emo-secondary: #00FF66;
  --emo-bg: #0a0a0a;
  --emo-card: #141414;
  --emo-text: #ffffff;
  --emo-border: 2px solid #333;
}
body {
  background: var(--emo-bg) !important;
  color: var(--emo-text) !important;
  font-family: 'Outfit', sans-serif !important;
}
h1, h2, h3, h4, .logo {
  font-family: 'Bricolage Grotesque', sans-serif !important;
  text-transform: uppercase;
}
/* Force the header to be dark */
header {
  background: #000 !important;
  border-bottom: 2px solid #333 !important;
}
header a {
  color: #fff !important;
}
/* Cards */
.resource-card, .tool-card, .card {
  background: var(--emo-card) !important;
  border: var(--emo-border) !important;
  box-shadow: 4px 4px 0px var(--emo-primary) !important;
  border-radius: 0 !important;
  color: #fff !important;
  transition: transform 0.2s, box-shadow 0.2s !important;
}
.resource-card:hover, .tool-card:hover, .card:hover {
  transform: translate(-4px, -4px) !important;
  box-shadow: 8px 8px 0px var(--emo-secondary) !important;
}
/* Fix text colors inside cards */
.resource-card h3, .tool-card h3, .card h3 {
  color: var(--emo-secondary) !important;
}
.resource-card p, .tool-card p, .card p, .description {
  color: #ccc !important;
}
/* Buttons and badges */
.btn, .badge, .tag, button {
  background: var(--emo-primary) !important;
  color: #fff !important;
  border: 2px solid #000 !important;
  border-radius: 0 !important;
  font-family: 'Bricolage Grotesque', sans-serif !important;
  text-transform: uppercase;
}
.btn:hover, button:hover {
  background: var(--emo-secondary) !important;
  color: #000 !important;
}
/* Inputs */
input, .search-input {
  background: #000 !important;
  border: 2px solid #333 !important;
  color: #fff !important;
  border-radius: 0 !important;
}
input:focus, .search-input:focus {
  border-color: var(--emo-primary) !important;
  box-shadow: 4px 4px 0px var(--emo-primary) !important;
}
/* Modals / Overlays */
.modal-content, .popup {
  background: #000 !important;
  border: 2px solid #333 !important;
  box-shadow: 8px 8px 0px var(--emo-primary) !important;
}
"""

if "/* DARK NEO-BRUTALIST OVERRIDES */" not in html:
    html = html.replace('</head>', f'<style>{dark_css_override}</style>\n</head>')
else:
    # Already has overrides, just update them
    html = re.sub(r'/\* DARK NEO-BRUTALIST OVERRIDES \*/.*?</style>', f'{dark_css_override}</style>', html, flags=re.DOTALL)

with open('e:\\EMO\\resources.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Dark theme applied to resources.html")
