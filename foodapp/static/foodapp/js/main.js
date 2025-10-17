// main.js: data + rendering + small UI interactions

/* ---------- MENU DATA (26 items) ---------- */
const MENU_DATA = [
  // Maharashtrian (1-20)
  {id:1,name:'Pav Bhaji',restaurant:'Mumbai Spice Street',price:120,calories:420,nutrients:'Carbs 60g • Protein 8g • Fat 12g',ingredients:'Mashed vegetables, butter, pav',img:'pavbhaji.jpg'},
  {id:2,name:'Vada Pav',restaurant:'Ghatkopar Snacks',price:40,calories:280,nutrients:'Carbs 35g • Protein 5g • Fat 12g',ingredients:'Potato, besan, chutney',img:'vadapav.jpg'},
  {id:3,name:'Misal Pav',restaurant:'Taste of Pune',price:90,calories:420,nutrients:'Carbs 55g • Protein 12g • Fat 10g',ingredients:'Sprouted peas mix, farsan, pav',img:'misalpav.jpg'},
  {id:4,name:'Maharashtrian Veg Thali',restaurant:'Maratha Bhojanalaya',price:220,calories:650,nutrients:'Balanced meal',ingredients:'Rice, dal, bhakri, sabzi',img:'thali.jpg'},
  {id:5,name:'Kanda Poha',restaurant:'Morning Bite Café',price:60,calories:210,nutrients:'Carbs 40g • Protein 3g',ingredients:'Poha, onion, peanuts',img:'poha.jpg'},
  {id:6,name:'Sabudana Khichdi',restaurant:'Upwas Delight',price:80,calories:330,nutrients:'Carbs 65g • Protein 5g',ingredients:'Sabudana, peanuts, potato',img:'sabudana_khichdi.jpg'},
  {id:7,name:'Puran Poli',restaurant:'Sweet Spoon Nashik',price:100,calories:320,nutrients:'Carbs 55g • Protein 4g',ingredients:'Wheat, jaggery, chana dal',img:'puranpoli.jpg'},
  {id:8,name:'Ukdiche Modak',restaurant:'Lord Ganesha’s Kitchen',price:90,calories:260,nutrients:'Carbs 50g • Protein 3g',ingredients:'Rice flour, jaggery, coconut',img:'modak.jpg'},
  {id:9,name:'Aluvadi (Patra)',restaurant:'Mumbai Greens',price:70,calories:230,nutrients:'Carbs 28g • Protein 5g',ingredients:'Colocasia leaves, besan',img:'aluvadi.jpg'},
  {id:10,name:'Solkadhi',restaurant:'Kokum Waves',price:60,calories:60,nutrients:'Vitamins & healthy fats',ingredients:'Kokum, coconut milk',img:'solkadhi.jpg'},
  {id:11,name:'Thalipeeth',restaurant:'Village Crunch',price:130,calories:340,nutrients:'Carbs 45g • Protein 8g',ingredients:'Multigrain flour, spices',img:'thalipeeth.jpg'},
  {id:12,name:'Kombdi Vade (Chicken)',restaurant:'Kombdi House',price:220,calories:420,nutrients:'Protein 28g • Carbs 48g',ingredients:'Chicken curry & vade',img:'kombdi_vade.jpg'},
  {id:13,name:'Ukdiche Modak (sweet)',restaurant:'Sweet Bite',price:90,calories:260,nutrients:'Carbs 50g',ingredients:'Rice flour dumpling',img:'ukdiche_modak.jpg'},
  {id:14,name:'Kanda Pohe (special)',restaurant:'Poha Point',price:70,calories:200,nutrients:'Carbs 34g',ingredients:'Poha, peanuts, lemon',img:'kanda_pohe.jpg'},
  {id:15,name:'Shrikhand',restaurant:'Fruity Sweets',price:110,calories:220,nutrients:'Protein 6g • Fat 12g',ingredients:'Hung yogurt, saffron',img:'shrikhand.jpg'},
  {id:16,name:'Ampalaya Bhaji',restaurant:'Healthy Wok',price:100,calories:150,nutrients:'Veg rich',ingredients:'Bitter gourd, spices',img:'ampalaya_bhaji.jpg'},
  {id:17,name:'Malvani Fish Fry',restaurant:'Malvani Seas',price:260,calories:360,nutrients:'Protein 32g',ingredients:'Bombil, Malvani masala',img:'malvani_fish.jpg'},
  {id:18,name:'Patodi',restaurant:'Coastal Bites',price:110,calories:310,nutrients:'Carbs 45g',ingredients:'Besan rolls, coconut',img:'patodi.jpg'},
  {id:19,name:'Bombil Fry',restaurant:'Sea Fry',price:210,calories:370,nutrients:'Protein 28g',ingredients:'Bombil coated & fried',img:'bombil_fry.jpg'},
  {id:20,name:'Poha (Classic)',restaurant:'Morning Express',price:80,calories:180,nutrients:'Carbs 34g',ingredients:'Flattened rice, turmeric',img:'poha.jpg'},

  // Global (21-26)
  {id:21,name:'Margherita Pizza',restaurant:'Slice of Heaven',price:350,calories:700,nutrients:'Carbs 80g • Protein 20g',ingredients:'Dough, tomato, mozzarella',img:'margherita_pizza.jpg'},
  {id:22,name:'Cheese Burst Burger',restaurant:'Grill & Chill',price:220,calories:540,nutrients:'Protein 22g • Fat 28g',ingredients:'Bun, patty, cheese',img:'cheese_burst_burger.jpg'},
  {id:23,name:'Veg Momos',restaurant:'Momo Masti',price:140,calories:280,nutrients:'Carbs 40g • Protein 6g',ingredients:'Veg stuffing, wrapper',img:'veg_momos.jpg'},
  {id:24,name:'Chinese Noodles',restaurant:'Dragon Wok',price:160,calories:420,nutrients:'Carbs 70g',ingredients:'Noodles, veg, sauces',img:'chinese_noodles.jpg'},
  {id:25,name:'Cold Drink (500ml)',restaurant:'FreshFizz Bar',price:70,calories:160,nutrients:'Carbs 40g',ingredients:'Soda, flavor syrup',img:'cold_drink.jpg'},
  {id:26,name:'Fried Rice',restaurant:'Spice Asia',price:180,calories:430,nutrients:'Carbs 72g',ingredients:'Rice, veg, soy',img:'fried_rice.jpg'}
];

/* ---------- OFFERS ---------- */
const OFFER_DATA = [
  { id:21, discountPercent:40, itemId:21 }, // pizza_offer
  { id:22, discountPercent:50, itemId:22 }, // burger
  { id:16, discountPercent:25, itemId:16 }, // ampalaya
  { id:3, discountPercent:15, itemId:3 },  // misal pav
  { id:12, discountPercent:30, itemId:12}, // kombdi vade
  { id:20, discountPercent:20, itemId:20}  // poha
];

/* ---------- HELPERS ---------- */
function el(tag, cls){ const e = document.createElement(tag); if (cls) e.className = cls; return e; }

/* ---------- RENDER: featured restaurants ---------- */
function renderFeatured(){
  const list = document.getElementById('featuredList');
  if (!list) return;
  const picks = [MENU_DATA[2], MENU_DATA[6], MENU_DATA[11], MENU_DATA[21]];
  list.innerHTML = '';
  picks.forEach(p => {
    const a = el('a','card'); a.href = '/menu/';
    const img = el('img'); img.src = `/static/foodapp/images/${p.img}`; img.alt = p.name;
    const h4 = el('h4'); h4.textContent = p.restaurant;
    const p1 = el('p'); p1.className='muted'; p1.textContent = `${p.name} • ₹${p.price}`;
    a.appendChild(img); a.appendChild(h4); a.appendChild(p1);
    list.appendChild(a);
  });
}

/* ---------- RENDER: restaurants grid ---------- */
function renderRestaurantsGrid(){
  const grid = document.getElementById('restaurantGrid');
  if (!grid) return;
  const R = [
    {name:'Spice Empire', cuisine:'Maharashtrian', rating:4.6, cost:350, time:'25-30 min'},
    {name:'Pav & Co', cuisine:'Street Food', rating:4.4, cost:150, time:'20-25 min'},
    {name:'Malvani Seas', cuisine:'Seafood', rating:4.7, cost:550, time:'35-40 min'},
    {name:'Urban Pizza', cuisine:'Italian', rating:4.3, cost:450, time:'25-30 min'}
  ];
  grid.innerHTML = '';
  R.forEach(r=>{
    const card = el('div','card restaurant-card');
    const img = el('img'); img.src = `/static/foodapp/images/restaurant.jpg`; img.alt=r.name; img.style.width='180px';
    const info = el('div','');
    const h = el('h4'); h.textContent = r.name;
    const p = el('p'); p.className='muted'; p.textContent = `${r.cuisine} • ₹${r.cost} for two • ${r.time}`;
    const btn = el('button','btn'); btn.textContent = 'View Menu'; btn.onclick = ()=> location.href='/menu/';
    info.appendChild(h); info.appendChild(p); info.appendChild(btn);
    card.appendChild(img); card.appendChild(info);
    grid.appendChild(card);
  });
}

/* ---------- RENDER: menu ---------- */
function renderMenu(){
  const container = document.getElementById('menuGrid');
  if (!container) return;
  container.innerHTML = '';
  MENU_DATA.forEach(item=>{
    const card = el('div','menu-item');
    const img = el('img'); img.src = `/static/foodapp/images/${item.img}`; img.alt=item.name;
    const meta = el('div','menu-meta');
    const title = el('h4'); title.textContent = item.name;
    const rest = el('div'); rest.className='muted'; rest.textContent = `${item.restaurant} • ₹${item.price}`;
    const mrow = el('div','meta-row'); mrow.textContent = `${item.calories} kcal • ${item.nutrients}`;
    const ing = el('div'); ing.className='muted'; ing.textContent = item.ingredients;
    const bottom = el('div'); bottom.style.display='flex'; bottom.style.justifyContent='space-between'; bottom.style.alignItems='center'; bottom.style.marginTop='8px';
    const price = el('div'); price.innerHTML = `₹${item.price}`;
    const add = el('button','add-btn'); add.textContent='Add to Cart'; add.onclick = ()=> addToCart({id:item.id,name:item.name,price:item.price,img:item.img});
    bottom.appendChild(price); bottom.appendChild(add);

    meta.appendChild(title); meta.appendChild(rest); meta.appendChild(mrow); meta.appendChild(ing); meta.appendChild(bottom);
    card.appendChild(img); card.appendChild(meta);
    container.appendChild(card);
  });
}

/* ---------- RENDER: offers ---------- */
function renderOffers(){
  const grid = document.getElementById('offersGrid');
  if (!grid) return;
  grid.innerHTML = '';
  OFFER_DATA.forEach(o=>{
    const src = MENU_DATA.find(m=>m.id===o.itemId);
    if (!src) return;
    const item = {...src, offerPrice: Math.round(src.price * (1 - o.discountPercent/100)), discountPercent: o.discountPercent};
    const card = el('div','menu-item');
    const img = el('img'); img.src = `/static/foodapp/images/${item.img}`; img.alt=item.name;
    const meta = el('div','menu-meta');
    const title = el('h4'); title.textContent = item.name;
    const mrow = el('div','meta-row'); mrow.textContent = `${item.calories} kcal • ${item.nutrients}`;
    const ing = el('div'); ing.className='muted'; ing.textContent = item.ingredients;
    const bottom = el('div'); bottom.style.display='flex'; bottom.style.justifyContent='space-between'; bottom.style.alignItems='center'; bottom.style.marginTop='8px';
    const priceWrap = el('div'); priceWrap.innerHTML = `<span style="text-decoration:line-through;color:#999;margin-right:8px">₹${item.price}</span><span style="font-weight:700;color:var(--brand)">₹${item.offerPrice}</span>`;
    const add = el('button','add-btn'); add.textContent='Add to Cart'; add.onclick = ()=> addToCart({id:item.id,name:item.name,price:item.offerPrice,img:item.img});
    bottom.appendChild(priceWrap); bottom.appendChild(add);
    const badge = el('div','offer-badge'); badge.textContent = `${item.discountPercent}% OFF`;
    meta.appendChild(title); meta.appendChild(mrow); meta.appendChild(ing); meta.appendChild(bottom);
    const wrapper = el('div'); wrapper.style.position='relative';
    wrapper.appendChild(badge);
    card.appendChild(img); card.appendChild(meta);
    wrapper.appendChild(card);
    grid.appendChild(wrapper);
  });
}

/* ---------- SEARCH & HERO CHIPS ---------- */
function initSearch(){
  const search = document.getElementById('globalSearch');
  const btn = document.getElementById('searchBtn');
  if (btn && search){
    btn.addEventListener('click', ()=> {
      const q = search.value.trim().toLowerCase();
      if (!q){ alert('Type a search term. Try "Misal", "Pizza"'); return; }
      location.href = '/menu/';
      setTimeout(()=> {
        // highlight naive: scroll to first matching element
        const elMatch = Array.from(document.querySelectorAll('.menu-meta h4')).find(h => h.textContent.toLowerCase().includes(q));
        if (elMatch) elMatch.scrollIntoView({behavior:'smooth',block:'center'});
      }, 300);
    });
  }

  document.querySelectorAll('.chip').forEach(ch=>{
    ch.addEventListener('click', ()=> location.href='/menu/');
  });

  const vo = document.getElementById('viewOffers');
  if (vo) vo.addEventListener('click', ()=> location.href='/offers/');
}

/* ---------- INIT ---------- */
document.addEventListener('DOMContentLoaded', function(){
  renderFeatured();
  renderRestaurantsGrid();
  renderMenu();
  renderOffers();
  initSearch();
});
