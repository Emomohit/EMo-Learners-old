import re

with open('e:\\EMO\\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# New dense NYC-style sections to add
new_sections = """

  <!-- The Problem Section (NYC Style) -->
  <section class="problem-section" style="padding: 6rem 2rem; border-bottom: 1px solid #000; background: #fff;">
    <div class="container" style="max-width: 1400px; padding: 0;">
      <div style="text-align: center; margin-bottom: 4rem;">
        <div style="background: #000; color: #fff; display: inline-block; padding: 0.5rem 1rem; font-family: 'Anton', sans-serif; font-size: 1.5rem; margin-bottom: 1rem; text-transform: uppercase;">// The Reality</div>
        <h2 style="font-family: 'Anton', sans-serif; font-size: clamp(3rem, 6vw, 6rem); color: #000; line-height: 1; text-transform: uppercase;">THE COLLEGE SYSTEM <br><span style="color: #0038ff;">IS BROKEN.</span></h2>
      </div>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
        
        <div style="border: 1px solid #000; padding: 2rem; background: #fff; display: flex; flex-direction: column; gap: 1rem;">
          <div style="font-size: 3rem;">📚</div>
          <h3 style="font-family: 'Anton', sans-serif; font-size: 2.5rem; text-transform: uppercase;">Outdated Syllabus</h3>
          <p style="font-size: 1.1rem; font-weight: 500;">Learning 10-year-old theory won't get you a job today. The industry moves fast, college doesn't.</p>
        </div>

        <div style="border: 1px solid #000; padding: 2rem; background: #fff600; display: flex; flex-direction: column; gap: 1rem;">
          <div style="font-size: 3rem;">📉</div>
          <h3 style="font-family: 'Anton', sans-serif; font-size: 2.5rem; text-transform: uppercase;">No Real Skills</h3>
          <p style="font-size: 1.1rem; font-weight: 500;">Degrees don't build software. Companies hire for what you can build, not what you can memorize.</p>
        </div>

        <div style="border: 1px solid #000; padding: 2rem; background: #000; color: #fff; display: flex; flex-direction: column; gap: 1rem;">
          <div style="font-size: 3rem;">🤯</div>
          <h3 style="font-family: 'Anton', sans-serif; font-size: 2.5rem; text-transform: uppercase;">Info Overload</h3>
          <p style="font-size: 1.1rem; font-weight: 500; color: #ccc;">Too many YouTube tutorials, no clear roadmap. You end up in tutorial hell making zero progress.</p>
        </div>

      </div>
    </div>
  </section>

  <!-- Comparison Section (NYC Style) -->
  <section style="padding: 6rem 2rem; border-bottom: 1px solid #000; background: #fafafa;">
    <div class="container" style="max-width: 1200px; padding: 0;">
      <h2 style="font-family: 'Anton', sans-serif; font-size: clamp(3rem, 6vw, 5rem); text-align: center; margin-bottom: 4rem; text-transform: uppercase;">WE ARE NOT YOUR <br><span style="color: #0038ff;">AVERAGE COLLEGE</span></h2>
      
      <div style="border: 1px solid #000; background: #fff;">
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; border-bottom: 1px solid #000; background: #000; color: #fff; font-family: 'Anton', sans-serif; font-size: 1.5rem; text-transform: uppercase; text-align: center;">
          <div style="padding: 1.5rem; border-right: 1px solid #333;">Feature</div>
          <div style="padding: 1.5rem; border-right: 1px solid #333; color: #ff4444;">Traditional College</div>
          <div style="padding: 1.5rem; color: #fff600;">EMO Learners</div>
        </div>
        
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; border-bottom: 1px solid #000; text-align: center; font-weight: 600; font-size: 1.2rem;">
          <div style="padding: 1.5rem; border-right: 1px solid #000; display: flex; align-items: center; justify-content: center;">Focus</div>
          <div style="padding: 1.5rem; border-right: 1px solid #000; background: #fff0f0;">Passing Exams 📝</div>
          <div style="padding: 1.5rem; background: #f0fff0;">Building Skills 🚀</div>
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; border-bottom: 1px solid #000; text-align: center; font-weight: 600; font-size: 1.2rem;">
          <div style="padding: 1.5rem; border-right: 1px solid #000; display: flex; align-items: center; justify-content: center;">Tools Used</div>
          <div style="padding: 1.5rem; border-right: 1px solid #000; background: #fff0f0;">Pen & Paper 🖋️</div>
          <div style="padding: 1.5rem; background: #f0fff0;">Modern AI & Tech Stack 🤖</div>
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; text-align: center; font-weight: 600; font-size: 1.2rem;">
          <div style="padding: 1.5rem; border-right: 1px solid #000; display: flex; align-items: center; justify-content: center;">Pace</div>
          <div style="padding: 1.5rem; border-right: 1px solid #000; background: #fff0f0;">4 Years 🐢</div>
          <div style="padding: 1.5rem; background: #f0fff0;">Learn at your speed ⚡</div>
        </div>
      </div>
    </div>
  </section>

  <!-- Visual Break / Image Section -->
  <section style="border-bottom: 1px solid #000; display: flex;">
    <div style="flex: 1; border-right: 1px solid #000; padding: 4rem; display: flex; align-items: center; justify-content: center; background: #0038ff; color: #fff;">
        <h2 style="font-family: 'Anton', sans-serif; font-size: 4rem; text-transform: uppercase; line-height: 1;">JOIN A TRIBE OF <br><span style="color: #fff600;">BUILDERS.</span></h2>
    </div>
    <div style="flex: 1;">
        <img src="community.png" alt="Community" style="width: 100%; height: 100%; object-fit: cover; display: block;">
    </div>
  </section>

  <!-- Call to Action -->
  <section style="padding: 6rem 2rem; background: #fff600; border-bottom: 1px solid #000; text-align: center;">
    <h2 style="font-family: 'Anton', sans-serif; font-size: clamp(4rem, 8vw, 7rem); text-transform: uppercase; margin-bottom: 2rem; line-height: 0.9;">READY TO <br>LEVEL UP?</h2>
    <p style="font-size: 1.5rem; font-weight: 600; margin-bottom: 3rem; max-width: 600px; margin-left: auto; margin-right: auto;">Stop waiting for the perfect time. Start building your skills today with EMO Learners.</p>
    <a href="/login.html" class="btn btn-dark" style="font-size: 2rem; padding: 1.5rem 4rem;">JOIN NOW 🚀</a>
  </section>

"""

# Inject right after the Challenge Banner
html = html.replace('<!-- Bento Features -->', new_sections + '\n  <!-- Bento Features -->')

with open('e:\\EMO\\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Injected old sections with NYC styling!")
