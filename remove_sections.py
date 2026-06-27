import re

# Remove Login Button from specific files
files = ['e:\\EMO\\index.html', 'e:\\EMO\\about.html', 'e:\\EMO\\internships.html', 'e:\\EMO\\resources.html']

for filepath in files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove Login Button
        content = re.sub(r'<a href="/login\.html"[^>]*>Login →</a>', '', content)
        
        # In resources.html, it might look slightly different due to style injections
        content = re.sub(r'<a href="/login\.html".*?>Login →</a>', '', content, flags=re.DOTALL)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Login buttons removed from {filepath}")
    except Exception as e:
        print(f"Error on {filepath}: {e}")
