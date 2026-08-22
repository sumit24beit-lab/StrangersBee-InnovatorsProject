with open("foodapp/templates/contact.html", "r", encoding="utf-8") as f:
    content = f.read()
content = content.replace("class=\"ks-card\"", "class=\"ks-card h-auto\"")
with open("foodapp/templates/contact.html", "w", encoding="utf-8") as f:
    f.write(content)
