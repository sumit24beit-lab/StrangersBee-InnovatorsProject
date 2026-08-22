with open("foodapp/templates/base.html", "r", encoding="utf-8") as f:
    content = f.read()
content = content.replace("class=\"navbar-nav me-auto mb-2 mb-lg-0\"", "class=\"navbar-nav mx-auto mb-2 mb-lg-0\"")
with open("foodapp/templates/base.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Navbar updated.")
