import glob
import re

files = ['e:\\EMO\\index.html', 'e:\\EMO\\about.html', 'e:\\EMO\\internships.html', 'e:\\EMO\\login.html', 'e:\\EMO\\resources.html']

for filepath in files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 1. Update Fonts Link
        content = re.sub(
            r'<link href="https://fonts\.googleapis\.com/css2\?family=Anton&family=Poppins.*?rel="stylesheet">',
            '<link href="https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=Outfit:wght@400;500;600;700&display=swap" rel="stylesheet">',
            content
        )
        
        # 2. Update CSS Variables declaration
        content = re.sub(
            r':root\s*\{[^}]*\}',
            """:root {
      --nyc-blue: #121212; /* Switched to Dark for better contrast with Orange */
      --nyc-yellow: #FF4500; /* Electric Orange */
      --nyc-font-head: 'Syne', sans-serif;
      --nyc-font-body: 'Outfit', sans-serif;
      --nyc-border: 2px solid #000;
      --emo-shadow: 6px 6px 0px #000;
    }""",
            content
        )
        
        # 3. Add shadow to cards/buttons in global CSS if it matches
        content = content.replace('border-radius: 0 !important;', 'border-radius: 0 !important;')
        
        # Add box-shadows to buttons
        content = content.replace('box-shadow: 4px 4px 0px #000 !important;', 'box-shadow: var(--emo-shadow) !important;')
        content = content.replace('border: 1px solid #000', 'border: 2px solid #000')
        
        # 4. Replace inline color hardcodes
        content = content.replace('#0038ff', '#121212') # Deep dark instead of blue
        content = content.replace('#fff600', '#00FF66') # Cyber green for highlights
        
        # Fix specific button classes that relied on old colors
        # The marquee uses --nyc-yellow, which is now Orange. Text should be white or black. Let's make it black.
        # Buttons using .btn-primary were blue, now they are #121212.
        
        # Give a consistent shadow to .bento-card, problem-section cards, etc.
        content = content.replace('.bento-card { background: #fff; border: var(--nyc-border);', '.bento-card { background: #fff; border: var(--nyc-border); box-shadow: var(--emo-shadow);')
        content = content.replace('border: 1px solid #000;', 'border: 2px solid #000; box-shadow: var(--emo-shadow);')
        
        # Fix the text-transform from Anton (which is naturally heavy and tight) 
        # to Syne which needs a bit more tracking and bolding.
        content = content.replace("font-family: 'Anton', sans-serif;", "font-family: 'Syne', sans-serif; font-weight: 800; letter-spacing: -1px;")
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Updated {filepath}")
    except FileNotFoundError:
        print(f"Skipping {filepath} (Not Found)")
