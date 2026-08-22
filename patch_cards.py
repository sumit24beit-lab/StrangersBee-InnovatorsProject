import os

files_to_patch = [
    'foodapp/templates/customer_profile.html',
    'foodapp/templates/order_tracking.html',
    'foodapp/templates/order_history.html',
    'foodapp/templates/delivery.html',
]

for file_path in files_to_patch:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Simple replacement: add h-auto to ks-card
    content = content.replace('class="ks-card', 'class="ks-card h-auto')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Patched cards.")
