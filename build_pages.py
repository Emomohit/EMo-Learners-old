import os

# NYC Boilerplate
def get_boilerplate(title, content):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} - EMO Learners</title>
  <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E🚀%3C/text%3E%3C/svg%3E">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <!-- Importing Anton for NYC Massive Headings and Poppins for Body -->
  <link href="https://fonts.googleapis.com/css2?family=Anton&family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {{
      --nyc-blue: #0038ff;
      --nyc-yellow: #fff600;
      --nyc-font-head: 'Anton', sans-serif;
      --nyc-font-body: 'Poppins', sans-serif;
      --nyc-border: 1px solid #000;
    }}
    * {{ margin: 0; padding: 0; box-sizing: border-box; border-radius: 0 !important; }}
    body {{
      font-family: var(--nyc-font-body);
      background: #fff;
      color: #000;
      overflow-x: hidden;
      line-height: 1.5;
    }}
    /* Typography */
    h1, h2, h3, h4 {{
      font-family: var(--nyc-font-head);
      text-transform: uppercase;
      font-weight: 400; /* Anton is naturally heavy */
      line-height: 1;
      letter-spacing: 1px;
    }}
    a {{ text-decoration: none; color: inherit; }}
    
    /* Marquee */
    .marquee {{
      background: var(--nyc-yellow);
      border-bottom: var(--nyc-border);
      padding: 0.5rem 0;
      overflow: hidden;
      white-space: nowrap;
      display: flex;
    }}
    .marquee-text {{
      font-family: var(--nyc-font-head);
      font-size: 1.5rem;
      letter-spacing: 2px;
      animation: scroll 15s linear infinite;
      padding-right: 50px;
    }}
    @keyframes scroll {{ 0% {{ transform: translateX(0); }} 100% {{ transform: translateX(-100%); }} }}
    
    /* Header */
    header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 1rem 2rem;
      border-bottom: var(--nyc-border);
      background: #fff;
    }}
    .logo {{
      font-family: var(--nyc-font-head);
      font-size: 2rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    nav {{ display: flex; gap: 2rem; }}
    nav a {{
      font-weight: 600;
      font-size: 1.1rem;
      -webkit-text-stroke: 0.5px #000;
      color: transparent;
      transition: color 0.2s;
    }}
    nav a:hover, nav a.active {{ color: #000; }}
    
    .nav-actions {{ display: flex; gap: 1rem; align-items: center; }}
    .btn {{
      font-family: var(--nyc-font-head);
      font-size: 1.2rem;
      padding: 0.5rem 1.5rem;
      border: var(--nyc-border);
      cursor: pointer;
      text-transform: uppercase;
      background: var(--nyc-yellow);
      transition: transform 0.1s;
      letter-spacing: 1px;
    }}
    .btn:hover {{ transform: translate(2px, 2px); }}
    .btn-primary {{ background: var(--nyc-blue); color: #fff; }}
    .btn-dark {{ background: #000; color: #fff; }}

    /* Layout Containers */
    .container {{
      max-width: 1200px;
      margin: 0 auto;
      padding: 4rem 2rem;
    }}
    
    {content['extra_css']}
  </style>
</head>
<body>

  <!-- Marquee -->
  <div class="marquee">
    <div class="marquee-text">EMO LEARNERS 🚀 LEARN AI 🚀 BUILD SKILLS 🚀 GET INTERNSHIPS 🚀 EMO LEARNERS 🚀 LEARN AI 🚀 BUILD SKILLS 🚀 GET INTERNSHIPS 🚀</div>
    <div class="marquee-text">EMO LEARNERS 🚀 LEARN AI 🚀 BUILD SKILLS 🚀 GET INTERNSHIPS 🚀 EMO LEARNERS 🚀 LEARN AI 🚀 BUILD SKILLS 🚀 GET INTERNSHIPS 🚀</div>
  </div>

  <!-- Header -->
  <header>
    <a href="/index.html" class="logo">🚀 EMO Learners</a>
    <nav>
      <a href="/index.html">Home</a>
      <a href="/about.html">About</a>
      <a href="/resources.html">Resources</a>
      <a href="/internships.html">Internships</a>
    </nav>
    <div class="nav-actions">
      <a href="/login.html" class="btn btn-primary">Login →</a>
    </div>
  </header>

  {content['body']}

</body>
</html>
"""

# Pages Content
about_content = {
    'extra_css': """
    .about-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; align-items: center; }
    .about-img { width: 100%; border: var(--nyc-border); object-fit: cover; aspect-ratio: 1; }
    .about-text h1 { font-size: 5rem; margin-bottom: 1rem; }
    .about-text p { font-size: 1.2rem; margin-bottom: 2rem; color: #333; }
    @media(max-width: 768px) { .about-grid { grid-template-columns: 1fr; } }
    """,
    'body': """
  <main class="container">
    <div class="about-grid">
      <div class="about-text">
        <h1>ABOUT THE FOUNDER</h1>
        <h2 style="color: var(--nyc-blue); margin-bottom: 1rem;">MOHIT AHIRWAR</h2>
        <p>Founder of EMO Learners. Building a platform that helps students learn AI, develop skills, and discover career opportunities.</p>
        <p>We believe in building real momentum, not just studying for exams. Join the community and start building.</p>
        <div style="display: flex; gap: 1rem; margin-top: 2rem;">
          <a href="https://instagram.com/emolearners" target="_blank" class="btn">Instagram</a>
          <a href="https://t.me/emolarners" target="_blank" class="btn btn-primary">Telegram</a>
        </div>
      </div>
      <div>
        <img src="founder.jpg" alt="Mohit Ahirwar" class="about-img">
      </div>
    </div>
  </main>
    """
}

internships_content = {
    'extra_css': """
    .center-content { text-align: center; max-width: 800px; margin: 0 auto; padding: 6rem 0; }
    .center-content h1 { font-size: 6rem; color: var(--nyc-blue); margin-bottom: 1rem; }
    .center-content p { font-size: 1.5rem; }
    """,
    'body': """
  <main class="container">
    <div class="center-content">
      <h1>INTERNSHIPS</h1>
      <p style="background: var(--nyc-yellow); display: inline-block; padding: 0.5rem 1rem; font-weight: 700; border: var(--nyc-border); margin-top: 2rem;">COMING SOON 🚀</p>
    </div>
  </main>
    """
}

login_content = {
    'extra_css': """
    .login-container { max-width: 500px; margin: 4rem auto; border: var(--nyc-border); padding: 3rem; background: #fafafa; }
    .login-container h1 { font-size: 4rem; text-align: center; margin-bottom: 2rem; }
    .form-group { margin-bottom: 1.5rem; }
    .form-group label { display: block; font-weight: 700; margin-bottom: 0.5rem; }
    .form-group input { width: 100%; padding: 1rem; border: var(--nyc-border); font-family: var(--nyc-font-body); font-size: 1rem; }
    .btn-full { width: 100%; text-align: center; display: block; margin-top: 1rem; }
    """,
    'body': """
  <main class="container">
    <div class="login-container">
      <h1>STUDENT LOGIN</h1>
      <form onsubmit="event.preventDefault(); alert('Login functionality coming soon!');">
        <div class="form-group">
          <label>EMAIL ADDRESS</label>
          <input type="email" placeholder="student@example.com" required>
        </div>
        <div class="form-group">
          <label>PASSWORD</label>
          <input type="password" placeholder="••••••••" required>
        </div>
        <button type="submit" class="btn btn-primary btn-full">LOGIN TO DASHBOARD</button>
      </form>
    </div>
  </main>
    """
}

with open('e:\\EMO\\about.html', 'w', encoding='utf-8') as f: f.write(get_boilerplate('About', about_content))
with open('e:\\EMO\\internships.html', 'w', encoding='utf-8') as f: f.write(get_boilerplate('Internships', internships_content))
with open('e:\\EMO\\login.html', 'w', encoding='utf-8') as f: f.write(get_boilerplate('Login', login_content))

print("Secondary pages created!")
