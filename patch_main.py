import re

with open("foodapp/static/foodapp/js/main.js", "r", encoding="utf-8") as f:
    content = f.read()

# Replace renderMenu function
new_renderMenu = """function renderMenu(data) {
  if (!data) data = MENU_DATA;
  const container = document.getElementById('menuGrid');
  if (!container) return;
  container.innerHTML = '';
  data.forEach(item => {
    const col = el('div', 'col-md-4 col-sm-6');
    const card = el('div', 'ks-card');
    
    const img = el('img'); 
    img.src = `/static/foodapp/images/${item.img}`; 
    img.alt = item.name;

    const title = el('h3', 'h5 fw-bold mb-1'); 
    title.textContent = item.name;

    const rest = el('p', 'text-muted small mb-1'); 
    rest.textContent = `By ${item.restaurant || 'Local Home Cook'}`;

    const tags = el('div', 'mb-2');
    const tag1 = el('span', 'ks-badge me-1'); tag1.textContent = item.meal;
    const tag2 = el('span', 'ks-badge'); tag2.textContent = item.nutri;
    tags.appendChild(tag1); tags.appendChild(tag2);

    const desc = el('p', 'small mb-3 text-muted'); 
    desc.textContent = item.ingredients;

    const bottom = el('div', 'mt-auto pt-3 border-top d-flex justify-content-between align-items-center');
    const price = el('strong', 'fs-5'); price.textContent = `₹${item.price}`;
    
    const add = el('button', 'btn btn-ks-primary btn-sm'); 
    add.textContent = 'Add';
    add.onclick = () => { if(typeof addToCart === 'function') addToCart({id:item.id,name:item.name,price:item.price,img:item.img}); };

    bottom.appendChild(price); bottom.appendChild(add);

    card.appendChild(img);
    card.appendChild(title);
    card.appendChild(rest);
    card.appendChild(tags);
    card.appendChild(desc);
    card.appendChild(bottom);

    col.appendChild(card);
    container.appendChild(col);
  });
}
"""

content = re.sub(r'function renderMenu\b.*?\}\s*(?=function renderRestaurantsGrid)', new_renderMenu, content, flags=re.DOTALL)

with open("foodapp/static/foodapp/js/main.js", "w", encoding="utf-8") as f:
    f.write(content)
print("Updated main.js")
