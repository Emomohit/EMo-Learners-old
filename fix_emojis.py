import re

with open('e:\\EMO\\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    ("?? EMO Learners", "🚀 EMO Learners"),
    ("?? Follow", "🚀 Follow"),
    ('id="missionMarker">??</div>', 'id="missionMarker">🚀</div>'),
    ("?? Join Telegram", "🚀 Join Telegram"),
    ("?? Subscribe YouTube", "📺 Subscribe YouTube"),
    ("?? Growing Student Community", "📈 Growing Student Community"),
    ("?? AI-Powered Learning", "🤖 AI-Powered Learning"),
    ("?? Career-Focused Resources", "💼 Career-Focused Resources"),
    ("?? 30 Days Python Challenge", "🐍 30 Days Python Challenge"),
    ("?? From 1st July", "📅 From 1st July"),
    ("?? Free to join", "💯 Free to join"),
    ("?? Follow @emolearners", "📌 Follow @emolearners"),
    ("time! ??", "time! 🚀"),
    ("?? Join 50+", "🚀 Join 50+"),
]

for old, new in replacements:
    content = content.replace(old, new)

# Also fix any rogue ?? that might have been missed, just turning them into 🚀 for safety
# Actually, it's safer to just let the specific ones be fixed.
# Wait, let's catch any remaining "?? " and replace with "🚀 "
content = content.replace("?? ", "🚀 ")

with open('e:\\EMO\\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed emojis!")
