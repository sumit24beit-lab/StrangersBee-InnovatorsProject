import re

with open("foodapp/static/foodapp/js/main.js", "r", encoding="utf-8") as f:
    content = f.read()

new_renderRestaurantsGrid = """function renderRestaurantsGrid(){
  const grid = document.getElementById('restaurantGrid');
  if (!grid) return;
  grid.innerHTML = '';
  const R = [
    {name:'Aishwarya Hotel', cuisine:'Maharashtrian', rating:4.6, cost:350, time:'25-30 min',img:'restaurant.jpg'},
    {name:'Pav & Co', cuisine:'Street Food', rating:4.4, cost:150, time:'20-25 min',img:'restaurant1.jpg'},
    {name:'Malvani Seas', cuisine:'Seafood', rating:4.7, cost:550, time:'35-40 min',img:'restaurant2.jpg'},
    {name:'Urban Pizza', cuisine:'Italian', rating:4.3, cost:450, time:'25-30 min',img:'restaurant3.jpg'}
  ];
  R.forEach(r => {
    const col = el('div', 'col-md-6 col-lg-4');
    const card = el('div', 'ks-card text-center');
    
    const imgWrapper = el('div', 'mb-3');
    const img = el('img', 'rounded-circle border'); 
    img.src = `/static/foodapp/images/${r.img}`; 
    img.alt = r.name; 
    img.style.width = '100px';
    img.style.height = '100px';
    img.style.objectFit = 'cover';
    img.style.marginBottom = '0';
    imgWrapper.appendChild(img);

    const title = el('h3', 'h4 fw-bold mb-1'); title.textContent = r.name;
    const loc = el('p', 'text-muted small mb-2'); loc.innerHTML = `<i class="bi bi-geo-alt"></i> Local`;
    
    const tags = el('div', 'mb-2');
    const tag1 = el('span', 'ks-badge'); tag1.textContent = r.cuisine;
    tags.appendChild(tag1);

    const bottom = el('div', 'mt-auto pt-3 border-top d-flex justify-content-between align-items-center');
    const rating = el('span', 'ks-badge-accent ks-badge'); rating.textContent = `★ ${r.rating}`;
    const btn = el('button', 'btn btn-ks-secondary btn-sm'); btn.textContent = 'View Menu';
    btn.onclick = () => location.href = '/menu/';

    bottom.appendChild(rating); bottom.appendChild(btn);

    card.appendChild(imgWrapper);
    card.appendChild(title);
    card.appendChild(loc);
    card.appendChild(tags);
    card.appendChild(bottom);

    col.appendChild(card);
    grid.appendChild(col);
  });
}
"""

new_renderOffers = """function renderOffers(){
  const grid = document.getElementById('offersGrid');
  if (!grid) return;
  grid.innerHTML = '';
  OFFER_DATA.forEach(o => {
    const src = MENU_DATA.find(m => m.id === o.itemId);
    if (!src) return;
    const item = {...src, offerPrice: Math.round(src.price * (1 - o.discountPercent/100)), discountPercent: o.discountPercent};
    
    const col = el('div', 'col-md-6');
    const card = el('div', 'ks-card position-relative overflow-hidden');
    
    const badge = el('div', 'position-absolute top-0 end-0 text-white px-3 py-1 fw-bold');
    badge.style.backgroundColor = 'var(--ks-accent)';
    badge.style.borderBottomLeftRadius = 'var(--ks-radius-sm)';
    badge.textContent = `${item.discountPercent}% OFF`;
    
    const title = el('h3', 'h4 fw-bold mb-2'); title.textContent = item.name;
    const rest = el('p', 'text-muted small mb-3'); rest.textContent = `By Local Kitchen`;
    const desc = el('p', 'mb-4'); desc.textContent = `Special discount on ${item.name}!`;

    const bottom = el('div', 'd-flex justify-content-between align-items-center mt-auto');
    const priceDiv = el('div');
    const oldPrice = el('span', 'text-muted text-decoration-line-through small me-2'); oldPrice.textContent = `₹${item.price}`;
    const newPrice = el('span', 'fs-5 fw-bold'); newPrice.style.color = 'var(--ks-accent)'; newPrice.textContent = `₹${item.offerPrice}`;
    priceDiv.appendChild(oldPrice); priceDiv.appendChild(newPrice);
    
    const addBtn = el('button', 'btn btn-ks-accent btn-sm'); addBtn.textContent = 'Order Now';
    addBtn.onclick = () => { if(typeof addToCart === 'function') addToCart({id:item.id,name:item.name,price:item.offerPrice,img:item.img}); };

    bottom.appendChild(priceDiv); bottom.appendChild(addBtn);

    card.appendChild(badge);
    card.appendChild(title);
    card.appendChild(rest);
    card.appendChild(desc);
    card.appendChild(bottom);

    col.appendChild(card);
    grid.appendChild(col);
  });
}
"""

content = re.sub(r'function renderRestaurantsGrid\b.*?\}\s*(?=function gatherFilters|/\* ---------- FILTERING)', new_renderRestaurantsGrid, content, flags=re.DOTALL)
content = re.sub(r'function renderOffers\b.*?\}\s*(?=function el|function renderFeatured|const OFFER_DATA|/\* ---------- UTILS)', new_renderOffers, content, flags=re.DOTALL)

with open("foodapp/static/foodapp/js/main.js", "w", encoding="utf-8") as f:
    f.write(content)
print("Updated main.js grids")
