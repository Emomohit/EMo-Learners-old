import glob

files = ['e:\\EMO\\index.html', 'e:\\EMO\\about.html', 'e:\\EMO\\internships.html', 'e:\\EMO\\login.html', 'e:\\EMO\\resources.html']

for filepath in files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Replace Syne with Bricolage Grotesque
        content = content.replace(
            'family=Syne:wght@700;800', 
            'family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800'
        )
        content = content.replace(
            "--nyc-font-head: 'Syne', sans-serif;",
            "--nyc-font-head: 'Bricolage Grotesque', sans-serif;"
        )
        content = content.replace(
            "font-family: 'Syne', sans-serif;",
            "font-family: 'Bricolage Grotesque', sans-serif;"
        )
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Updated font in {filepath}")
    except FileNotFoundError:
        pass
