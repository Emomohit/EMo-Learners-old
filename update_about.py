with open('e:\\EMO\\about.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add the portfolio button next to Telegram button
portfolio_btn = '<a href="#" target="_blank" class="btn" style="background: #00FF66; color: #000;">View Portfolio 🚀</a>'
html = html.replace('<a href="https://t.me/emolarners" target="_blank" class="btn btn-primary">Telegram</a>', 
                    '<a href="https://t.me/emolarners" target="_blank" class="btn btn-primary">Telegram</a>\n          ' + portfolio_btn)

with open('e:\\EMO\\about.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Portfolio link added to about.html!")
