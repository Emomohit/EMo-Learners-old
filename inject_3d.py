import re

with open('e:\\EMO\\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add .tilt-card class to key elements
html = html.replace('class="hero-image"', 'class="hero-image tilt-card"')
html = html.replace('class="bento-card"', 'class="bento-card tilt-card"')
html = html.replace('class="bento-card blue"', 'class="bento-card blue tilt-card"')
html = html.replace('class="bento-card yellow"', 'class="bento-card yellow tilt-card"')

# Add it to the 3 problem cards (since they have inline styles, let's just add it to the divs that have border: 2px solid #000;)
html = re.sub(r'(<div style="border: 2px solid #000;[^>]*display: flex;[^>]*>)', r'\1<!-- tilt-target -->', html)
html = html.replace('<!-- tilt-target -->', '') # Clean up the dummy, wait this is risky. Let's just do a simple replace on the known string
html = html.replace('padding: 2rem; background: #fff; display: flex; flex-direction: column;', 'padding: 2rem; background: #fff; display: flex; flex-direction: column;" class="tilt-card')
html = html.replace('padding: 2rem; background: #00FF66; display: flex; flex-direction: column;', 'padding: 2rem; background: #00FF66; display: flex; flex-direction: column;" class="tilt-card')
html = html.replace('padding: 2rem; background: #000; color: #fff; display: flex; flex-direction: column;', 'padding: 2rem; background: #000; color: #fff; display: flex; flex-direction: column;" class="tilt-card')


# 2. Inject CSS transition for tilt-card
css_injection = """
    /* 3D Tilt CSS */
    .tilt-card {
      transition: transform 0.1s ease-out;
      transform-style: preserve-3d;
      will-change: transform;
    }
    .tilt-card > * {
      transform: translateZ(20px);
    }
"""
html = html.replace('</style>', css_injection + '</style>')

# 3. Inject JS Logic
js_injection = """
  <!-- 3D Tilt Script -->
  <script>
    document.addEventListener("DOMContentLoaded", () => {
      const tiltCards = document.querySelectorAll(".tilt-card");
      
      tiltCards.forEach(card => {
        card.addEventListener("mousemove", (e) => {
          const rect = card.getBoundingClientRect();
          const x = e.clientX - rect.left;
          const y = e.clientY - rect.top;
          
          const centerX = rect.width / 2;
          const centerY = rect.height / 2;
          
          const rotateX = ((y - centerY) / centerY) * -15; // Max 15 deg tilt
          const rotateY = ((x - centerX) / centerX) * 15;
          
          card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(1.02)`;
        });
        
        card.addEventListener("mouseleave", () => {
          card.style.transform = `perspective(1000px) rotateX(0deg) rotateY(0deg) scale(1)`;
          // Smooth return transition
          card.style.transition = "transform 0.5s ease";
          setTimeout(() => {
            card.style.transition = "transform 0.1s ease-out";
          }, 500);
        });
      });
    });
  </script>
</body>
"""

html = html.replace('</body>', js_injection)

with open('e:\\EMO\\index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("3D Interactive Logic Injected!")
