import re

filepath = r"c:\Users\bhosa\OneDrive\Desktop\OneClickFood\foodapp\templates\home.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the nested {% block content %} and {% endblock %} inside <main class="main">
content = re.sub(r'<main class="main">\s*{%\s*block content\s*%}', '<main class="main">', content)
content = re.sub(r'{%\s*endblock\s*%}\s*</main>', '</main>', content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("home.html fixed.")
