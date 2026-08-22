import os
import re

templates_dir = r"c:\Users\bhosa\OneDrive\Desktop\OneClickFood\foodapp\templates"

for filename in os.listdir(templates_dir):
    if filename.endswith(".html") and filename != "base.html":
        filepath = os.path.join(templates_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already refactored
        if "{% extends 'base.html' %}" in content:
            continue
        
        # Extract title
        title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
        title = title_match.group(1).strip() if title_match else "KitchenStation"
        title = title.replace('{% block title %}', '').replace('{% endblock %}', '')
        
        # Extract main content
        main_match = re.search(r'(<main\b[^>]*>.*?)</main>', content, re.IGNORECASE | re.DOTALL)
        if main_match:
            main_content = main_match.group(1) + "\n</main>"
        else:
            print(f"Failed to extract main content for {filename}")
            continue
        
        # Extract inline script for delivery.html if present
        script_content = ""
        for sm in re.finditer(r'(<script[^>]*>.*?</script>)', content, re.IGNORECASE | re.DOTALL):
            s = sm.group(1)
            if 'src=' not in s:
                script_content += "\n" + s

        new_content = f"""{{% extends 'base.html' %}}
{{% load static %}}

{{% block title %}}{title}{{% endblock %}}

{{% block content %}}
{main_content}
{{% endblock %}}
"""
        if script_content.strip():
            new_content += f"""
{{% block extra_js %}}
{script_content}
{{% endblock %}}
"""

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"Refactored {filename}")
