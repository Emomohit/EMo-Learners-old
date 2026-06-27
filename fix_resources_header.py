import re

with open('e:\\EMO\\resources.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the header in resources.html
new_header = """
  <!-- Header -->
  <header style="display: flex; justify-content: space-between; align-items: center; padding: 1rem 2rem; border-bottom: 1px solid #000; background: #fff; font-family: 'Poppins', sans-serif;">
    <a href="/index.html" style="font-family: 'Anton', sans-serif; font-size: 2rem; display: flex; align-items: center; gap: 0.5rem; text-decoration: none; color: #000; text-transform: uppercase;">🚀 EMO Learners</a>
    <nav style="display: flex; gap: 2rem;">
      <a href="/index.html" style="font-weight: 600; font-size: 1.1rem; color: #000; text-decoration: none;">Home</a>
      <a href="/about.html" style="font-weight: 600; font-size: 1.1rem; color: #000; text-decoration: none;">About</a>
      <a href="/resources.html" style="font-weight: 600; font-size: 1.1rem; color: #000; text-decoration: none;">Resources</a>
      <a href="/internships.html" style="font-weight: 600; font-size: 1.1rem; color: #000; text-decoration: none;">Internships</a>
    </nav>
    <div style="display: flex; gap: 1rem; align-items: center;">
      <a href="/login.html" style="font-family: 'Anton', sans-serif; font-size: 1.2rem; padding: 0.5rem 1.5rem; border: 1px solid #000; cursor: pointer; text-transform: uppercase; background: #0038ff; color: #fff; text-decoration: none; letter-spacing: 1px;">Login →</a>
    </div>
  </header>
"""

# Replace the existing header
content = re.sub(r'<header>.*?</header>', new_header, content, flags=re.DOTALL)

with open('e:\\EMO\\resources.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated resources.html header")
