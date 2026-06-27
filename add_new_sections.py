import re

with open('e:\\EMO\\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_content = """

  <!-- Infinite Tech Carousel -->
  <style>
    .tech-carousel { background: #121212; color: #00FF66; padding: 2rem 0; overflow: hidden; white-space: nowrap; display: flex; border-bottom: 2px solid #000; border-top: 2px solid #000; box-shadow: var(--emo-shadow); position: relative; z-index: 10; margin-top: -2px; }
    .tech-track { display: flex; animation: scroll-fast 10s linear infinite; font-family: var(--nyc-font-head); font-size: 3rem; text-transform: uppercase; }
    .tech-item { margin: 0 2rem; }
    @keyframes scroll-fast { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }
  </style>
  <div class="tech-carousel">
    <div class="tech-track">
      <div class="tech-item">PYTHON</div><div class="tech-item">★</div>
      <div class="tech-item">AI TOOLS</div><div class="tech-item">★</div>
      <div class="tech-item">MACHINE LEARNING</div><div class="tech-item">★</div>
      <div class="tech-item">DATA SCIENCE</div><div class="tech-item">★</div>
      <div class="tech-item">REACT</div><div class="tech-item">★</div>
      <!-- Duplicate for infinite scroll loop -->
      <div class="tech-item">PYTHON</div><div class="tech-item">★</div>
      <div class="tech-item">AI TOOLS</div><div class="tech-item">★</div>
      <div class="tech-item">MACHINE LEARNING</div><div class="tech-item">★</div>
      <div class="tech-item">DATA SCIENCE</div><div class="tech-item">★</div>
      <div class="tech-item">REACT</div><div class="tech-item">★</div>
    </div>
  </div>

  <!-- Stats Section -->
  <section style="padding: 6rem 2rem; background: #fff; border-bottom: 2px solid #000;">
    <div class="container" style="max-width: 1400px; padding: 0;">
      <h2 style="font-family: var(--nyc-font-head); font-size: clamp(3rem, 6vw, 5rem); text-align: center; margin-bottom: 4rem; text-transform: uppercase;">THE NUMBERS DON'T LIE.</h2>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
        <div class="tilt-card" style="border: 2px solid #000; box-shadow: var(--emo-shadow); background: #00FF66; padding: 3rem; text-align: center;">
          <h3 style="font-family: var(--nyc-font-head); font-size: 6rem; margin-bottom: 1rem; line-height: 1;">100+</h3>
          <p style="font-size: 1.5rem; font-weight: 600; text-transform: uppercase;">Curated AI Tools</p>
        </div>
        <div class="tilt-card" style="border: 2px solid #000; box-shadow: var(--emo-shadow); background: #FF4500; color: #fff; padding: 3rem; text-align: center;">
          <h3 style="font-family: var(--nyc-font-head); font-size: 6rem; margin-bottom: 1rem; line-height: 1;">500+</h3>
          <p style="font-size: 1.5rem; font-weight: 600; text-transform: uppercase;">Active Students</p>
        </div>
        <div class="tilt-card" style="border: 2px solid #000; box-shadow: var(--emo-shadow); background: #121212; color: #fff; padding: 3rem; text-align: center;">
          <h3 style="font-family: var(--nyc-font-head); font-size: 6rem; margin-bottom: 1rem; line-height: 1;">30</h3>
          <p style="font-size: 1.5rem; font-weight: 600; text-transform: uppercase;">Days to Learn Python</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Wall of Love Section -->
  <section style="padding: 6rem 2rem; background: #fafafa; border-bottom: 2px solid #000;">
    <div class="container" style="max-width: 1400px; padding: 0;">
      <h2 style="font-family: var(--nyc-font-head); font-size: clamp(3rem, 6vw, 5rem); text-align: center; margin-bottom: 4rem; text-transform: uppercase;">WALL OF LOVE ❤️</h2>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
        <div class="tilt-card" style="border: 2px solid #000; box-shadow: var(--emo-shadow); background: #fff; padding: 2rem;">
          <p style="font-size: 1.2rem; font-weight: 500; margin-bottom: 2rem;">"The Python challenge completely changed how I learn. It's practical and doesn't waste time on useless theory."</p>
          <div style="display: flex; align-items: center; gap: 1rem;">
            <div style="width: 50px; height: 50px; background: #FF4500; border-radius: 50%; border: 2px solid #000;"></div>
            <div>
              <h4 style="font-family: var(--nyc-font-head); font-size: 1.5rem;">Rahul S.</h4>
              <p style="font-size: 0.9rem; font-weight: 600;">Computer Science Student</p>
            </div>
          </div>
        </div>
        <div class="tilt-card" style="border: 2px solid #000; box-shadow: var(--emo-shadow); background: #00FF66; padding: 2rem;">
          <p style="font-size: 1.2rem; font-weight: 500; margin-bottom: 2rem;">"Finally a platform that gives Indian students what they actually need. The curated AI tools saved me 100s of hours."</p>
          <div style="display: flex; align-items: center; gap: 1rem;">
            <div style="width: 50px; height: 50px; background: #121212; border-radius: 50%; border: 2px solid #000;"></div>
            <div>
              <h4 style="font-family: var(--nyc-font-head); font-size: 1.5rem; color: #121212;">Priya M.</h4>
              <p style="font-size: 0.9rem; font-weight: 600;">BCA Student</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- FAQ Section -->
  <section style="padding: 6rem 2rem; background: #121212; color: #fff; border-bottom: 2px solid #000;">
    <div class="container" style="max-width: 1000px; padding: 0;">
      <h2 style="font-family: var(--nyc-font-head); font-size: clamp(3rem, 6vw, 5rem); text-align: center; margin-bottom: 4rem; text-transform: uppercase; color: #00FF66;">FREQUENTLY ASKED.</h2>
      
      <div style="display: flex; flex-direction: column; gap: 1.5rem;">
        <div class="tilt-card" style="border: 2px solid #fff; box-shadow: var(--emo-shadow); padding: 2rem; background: #000;">
          <h3 style="font-family: var(--nyc-font-head); font-size: 2rem; margin-bottom: 1rem; text-transform: uppercase;">Is EMO Learners completely free?</h3>
          <p style="font-size: 1.1rem; color: #ccc;">Yes! All the challenges, roadmaps, and community access are 100% free. We believe in open education.</p>
        </div>
        <div class="tilt-card" style="border: 2px solid #fff; box-shadow: var(--emo-shadow); padding: 2rem; background: #000;">
          <h3 style="font-family: var(--nyc-font-head); font-size: 2rem; margin-bottom: 1rem; text-transform: uppercase;">Do I need prior coding knowledge?</h3>
          <p style="font-size: 1.1rem; color: #ccc;">Not at all. The 30 Days Python Challenge starts from absolute zero and builds you up to an advanced level.</p>
        </div>
        <div class="tilt-card" style="border: 2px solid #fff; box-shadow: var(--emo-shadow); padding: 2rem; background: #000;">
          <h3 style="font-family: var(--nyc-font-head); font-size: 2rem; margin-bottom: 1rem; text-transform: uppercase;">When do internships open?</h3>
          <p style="font-size: 1.1rem; color: #ccc;">Internships are currently "Coming Soon". Join our Telegram community to be the first to know when we launch them.</p>
        </div>
      </div>
    </div>
  </section>

"""

# Let's inject this before the "Visual Break / Image Section"
pattern = r'<!-- Visual Break / Image Section -->'
if '<!-- Visual Break / Image Section -->' in html:
    html = html.replace('<!-- Visual Break / Image Section -->', new_content + '\n  <!-- Visual Break / Image Section -->')
else:
    print("Could not find insertion point!")

with open('e:\\EMO\\index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Added new mega sections!")
