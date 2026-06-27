import re

with open('e:\\EMO\\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_footer_pattern = r'<footer class="social-links">.*?</footer>'

new_footer = """
  <!-- Comprehensive Footer -->
  <footer style="background: #000; color: #fff; padding: 6rem 2rem 2rem; border-top: 1px solid #000;">
    <div class="container" style="max-width: 1400px; padding: 0;">
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 4rem; margin-bottom: 4rem;">
        <div>
          <div style="font-family: 'Anton', sans-serif; font-size: 2.5rem; text-transform: uppercase; margin-bottom: 1rem; display: flex; align-items: center; gap: 0.5rem;">🚀 EMO Learners</div>
          <p style="font-size: 1.1rem; color: #ccc;">Helping students learn smarter, build skills, and grow their careers.</p>
        </div>
        <div>
          <h4 style="font-family: 'Anton', sans-serif; font-size: 1.5rem; text-transform: uppercase; margin-bottom: 1.5rem; color: #fff600;">Follow</h4>
          <div style="display: flex; flex-direction: column; gap: 1rem;">
            <a href="https://instagram.com/emolearners" target="_blank" style="color: #fff; font-size: 1.1rem; text-decoration: underline;">Instagram</a>
            <a href="https://www.linkedin.com/in/mohit-ahirwar-12bb58386/" target="_blank" style="color: #fff; font-size: 1.1rem; text-decoration: underline;">LinkedIn</a>
            <a href="https://t.me/emolarners" target="_blank" style="color: #fff; font-size: 1.1rem; text-decoration: underline;">Telegram Community</a>
            <a href="https://www.youtube.com/@emolearners" target="_blank" style="color: #fff; font-size: 1.1rem; text-decoration: underline;">YouTube</a>
          </div>
        </div>
        <div>
          <h4 style="font-family: 'Anton', sans-serif; font-size: 1.5rem; text-transform: uppercase; margin-bottom: 1.5rem; color: #0038ff;">Support</h4>
          <div style="display: flex; flex-direction: column; gap: 1rem;">
            <a href="https://t.me/Emomohit" target="_blank" style="color: #fff; font-size: 1.1rem; text-decoration: underline;">Contact Us</a>
            <a href="mailto:hello.emolearners@gmail.com" style="color: #fff; font-size: 1.1rem; text-decoration: underline;">hello.emolearners@gmail.com</a>
            <a href="privacy-policy.html" style="color: #fff; font-size: 1.1rem; text-decoration: underline;">Privacy Policy</a>
          </div>
        </div>
      </div>
      <div style="border-top: 1px solid #333; padding-top: 2rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; color: #888;">
        <span>© 2026 EMO Learners</span>
        <span>Built for students, by students.</span>
      </div>
    </div>
  </footer>
"""

html = re.sub(old_footer_pattern, new_footer, html, flags=re.DOTALL)

with open('e:\\EMO\\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Footer restored!")
