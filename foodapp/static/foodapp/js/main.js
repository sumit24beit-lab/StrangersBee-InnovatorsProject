// main.js (upgraded): menu data (50+), rendering, filters, and existing helpers

/* ---------- LARGE MENU DATA (50 items) ----------
   For brevity names/images repeat where necessary. Add images into static/images/ with exact filenames.
*/
const MENU_DATA = [
  // Maharashtrian cluster (1-25)
  {id:1, name:'Pav Bhaji', price:120, calories:420, nutrients:'Carbs 60g • Protein 8g', ingredients:'Mashed veg, butter, pav', img:'pavbhaji.jpg', nutri:'starchy', meal:'lunch', type:'heavy', spice:'normal'},
  {id:2, name:'Vada Pav', price:40, calories:280, nutrients:'Carbs 35g • Protein 5g', ingredients:'Potato vada, bun, chutney', img:'vadapav.jpg', nutri:'starchy', meal:'breakfast', type:'light', spice:'spicy'},
  {id:3, name:'Misal Pav', price:90, calories:420, nutrients:'Protein 12g', ingredients:'Sprouted beans, farsan, pav', img:'misalpav.jpg', nutri:'protein', meal:'lunch', type:'heavy', spice:'spicy'},
  {id:4, name:'Kanda Poha', price:60, calories:210, nutrients:'Carbs 40g', ingredients:'Poha, peanuts, onion', img:'poha.jpg', nutri:'starchy', meal:'breakfast', type:'light', spice:'not'},
  {id:5, name:'Sabudana Khichdi', price:80, calories:330, nutrients:'Carbs 65g', ingredients:'Sabudana, peanuts', img:'sabudana_khichdi.jpg', nutri:'starchy', meal:'breakfast', type:'light', spice:'not'},
  {id:6, name:'Puran Poli', price:100, calories:320, nutrients:'Carbs 55g', ingredients:'Wheat, jaggery, dal', img:'puranpoli.jpg', nutri:'starchy', meal:'breakfast', type:'light', spice:'not'},
  {id:7, name:'Ukdiche Modak', price:90, calories:260, nutrients:'Carbs 50g', ingredients:'Rice flour, jaggery', img:'modak.jpg', nutri:'dairy', meal:'breakfast', type:'light', spice:'not'},
  {id:8, name:'Bharli Vangi', price:160, calories:240, nutrients:'Fat 18g', ingredients:'Stuffed brinjal, coconut', img:'bharli_vangi.jpg', nutri:'fruits', meal:'lunch', type:'heavy', spice:'normal'},
  {id:9, name:'Aloo Upkari', price:80, calories:200, nutrients:'Carbs 30g', ingredients:'Potato, mustard', img:'alu_upkari.jpg', nutri:'starchy', meal:'lunch', type:'light', spice:'normal'},
  {id:10, name:'Varan Bhaat', price:130, calories:360, nutrients:'Carbs 70g', ingredients:'Dal, rice, ghee', img:'varan_bhaat.jpg', nutri:'dairy', meal:'lunch', type:'heavy', spice:'not'},
  {id:11, name:'Pithla Bhakri', price:140, calories:380, nutrients:'Protein 12g', ingredients:'Gram flour curry, bhakri', img:'pithla_bhakri.jpg', nutri:'protein', meal:'lunch', type:'heavy', spice:'normal'},
  {id:12, name:'Thalipeeth', price:130, calories:340, nutrients:'Carbs 45g', ingredients:'Multigrain flour', img:'thalipeeth.jpg', nutri:'starchy', meal:'breakfast', type:'heavy', spice:'not'},
  {id:13, name:'Kombdi Vade', price:220, calories:420, nutrients:'Protein 28g', ingredients:'Chicken curry & vade', img:'kombdi_vade.jpg', nutri:'protein', meal:'dinner', type:'heavy', spice:'spicy'},
  {id:14, name:'Shrikhand', price:110, calories:220, nutrients:'Protein 6g', ingredients:'Hung yogurt, saffron', img:'shrikhand.jpg', nutri:'dairy', meal:'dessert', type:'light', spice:'not'},
  {id:15, name:'Solkadhi', price:60, calories:60, nutrients:'Healthy fats', ingredients:'Coconut, kokum', img:'solkadhi.jpg', nutri:'dairy', meal:'lunch', type:'liquid', spice:'not'},
  {id:16, name:'Ampalaya bhaji ', price:100, calories:150, nutrients:'Veg rich', ingredients:'Bitter gourd stir fry', img:'ampalaya_bhaji.jpg', nutri:'fruits', meal:'lunch', type:'light', spice:'normal'},
  {id:17, name:'Malvani Fish Fry', price:260, calories:360, nutrients:'Protein 32g', ingredients:'Bombil fish', img:'malvani_fish.jpg', nutri:'protein', meal:'dinner', type:'heavy', spice:'spicy'},
  {id:18, name:'Patodi', price:110, calories:310, nutrients:'Carbs 45g', ingredients:'Besan rolls', img:'patodi.jpg', nutri:'starchy', meal:'lunch', type:'light', spice:'normal'},
  {id:19, name:'Bombil Fry', price:210, calories:370, nutrients:'Protein 28g', ingredients:'Bombil fry', img:'bombil_fry.jpg', nutri:'protein', meal:'dinner', type:'heavy', spice:'normal'},
  {id:20, name:'Poha Classic', price:80, calories:180, nutrients:'Carbs 34g', ingredients:'Flattened rice', img:'poha.jpg', nutri:'starchy', meal:'breakfast', type:'light', spice:'not'},
  {id:21, name:'Ukdiche Modak (Extra)', price:95, calories:270, nutrients:'Carbs', ingredients:'Rice dumpling', img:'ukdiche_modak.jpg', nutri:'dairy', meal:'dessert', type:'light', spice:'not'},
  {id:22, name:'Patal Puri', price:70, calories:95, nutrients:'Carbs', ingredients:'Crispy patties', img:'patal_puri.jpg', nutri:'starchy', meal:'snack', type:'light', spice:'spicy'},
  {id:23, name:'Kanda Pohe Special', price:75, calories:200, nutrients:'Carbs', ingredients:'Poha with sev', img:'kanda_pohe.jpg', nutri:'starchy', meal:'breakfast', type:'light', spice:'not'},
  {id:24, name:'Puran Poli Deluxe', price:130, calories:350, nutrients:'Carbs', ingredients:'Ghee-rich', img:'puranpoli.jpg', nutri:'starchy', meal:'dessert', type:'light', spice:'not'},
  {id:25, name:'Thali Special', price:260, calories:800, nutrients:'Balanced meal', ingredients:'Full thali', img:'thali.jpg', nutri:'dairy', meal:'dinner', type:'heavy', spice:'normal'},

  // Global / Others (26-50)
  {id:26, name:'Margherita Pizza', price:350, calories:700, nutrients:'Carbs 80g', ingredients:'Tomato, cheese', img:'margherita_pizza.jpg', nutri:'fats', meal:'dinner', type:'heavy', spice:'not'},
  {id:27, name:'Pepperoni Pizza', price:410, calories:760, nutrients:'Protein 25g', ingredients:'Pepperoni, cheese', img:'pepperoni_pizza.jpg', nutri:'fats', meal:'dinner', type:'heavy', spice:'normal'},
  {id:28, name:'Cheese Burst Burger', price:220, calories:540, nutrients:'Protein 22g', ingredients:'Burger, cheese', img:'cheese_burst_burger.jpg', nutri:'fats', meal:'lunch', type:'heavy', spice:'normal'},
  {id:29, name:'Veg Momos', price:140, calories:280, nutrients:'Carbs 40g', ingredients:'Vegetable momos', img:'veg_momos.jpg', nutri:'fruits', meal:'lunch', type:'light', spice:'not'},
  {id:30, name:'Chicken Momos', price:165, calories:320, nutrients:'Protein 18g', ingredients:'Chicken stuffing', img:'veg_momos.jpg', nutri:'protein', meal:'lunch', type:'light', spice:'normal'},
  {id:31, name:'Hakka Noodles', price:160, calories:420, nutrients:'Carbs', ingredients:'Noodles, veg', img:'chinese_noodles.jpg', nutri:'starchy', meal:'dinner', type:'heavy', spice:'normal'},
  {id:32, name:'Fried Rice', price:180, calories:430, nutrients:'Carbs', ingredients:'Rice, veg', img:'fried_rice.jpg', nutri:'starchy', meal:'dinner', type:'heavy', spice:'normal'},
  {id:33, name:'Chicken Fried Rice', price:210, calories:500, nutrients:'Protein', ingredients:'Rice, chicken', img:'fried_rice.jpg', nutri:'protein', meal:'dinner', type:'heavy', spice:'normal'},
  {id:34, name:'Creamy Pasta', price:200, calories:450, nutrients:'Carbs', ingredients:'Pasta, cream', img:'pasta.jpg', nutri:'fats', meal:'lunch', type:'heavy', spice:'not'},
  {id:35, name:'Grilled Sandwich', price:120, calories:330, nutrients:'Carbs', ingredients:'Bread, veggies', img:'food1.jpg', nutri:'starchy', meal:'breakfast', type:'light', spice:'not'},
  {id:36, name:'Caesar Salad', price:150, calories:280, nutrients:'Veg & protein', ingredients:'Lettuce, dressing', img:'food2.jpg', nutri:'fruits', meal:'lunch', type:'light', spice:'not'},
  {id:37, name:'Butter Chicken', price:300, calories:680, nutrients:'Protein', ingredients:'Chicken, butter sauce', img:'chickenbiryani.jpg', nutri:'protein', meal:'dinner', type:'heavy', spice:'normal'},
  {id:38, name:'Paneer Tikka', price:200, calories:420, nutrients:'Protein', ingredients:'Grilled paneer', img:'food3.jpg', nutri:'protein', meal:'lunch', type:'light', spice:'normal'},
  {id:39, name:'Cold Coffee', price:90, calories:160, nutrients:'Carbs', ingredients:'Coffee, milk', img:'coldcoffee.jpg', nutri:'dairy', meal:'breakfast', type:'liquid', spice:'not'},
  {id:40, name:'Lemon Soda', price:60, calories:80, nutrients:'Hydration', ingredients:'Lemon, soda', img:'soda.jpg', nutri:'fats', meal:'snack', type:'liquid', spice:'not'},
  {id:41, name:'Ice Cream Sundae', price:120, calories:340, nutrients:'Sugars', ingredients:'Ice cream, syrup', img:'icecream.jpg', nutri:'dairy', meal:'dessert', type:'light', spice:'not'},
  {id:42, name:'Falooda', price:120, calories:360, nutrients:'Sugars', ingredients:'Falooda, ice cream', img:'falooda.jpg', nutri:'dairy', meal:'dessert', type:'liquid', spice:'not'},
  {id:43, name:'Garlic Bread', price:80, calories:260, nutrients:'Carbs', ingredients:'Bread, garlic butter', img:'food8.jpg', nutri:'starchy', meal:'snack', type:'light', spice:'normal'},
  {id:44, name:'Paneer Butter Masala', price:240, calories:620, nutrients:'Protein', ingredients:'Paneer, tomato gravy', img:'food9.jpg', nutri:'protein', meal:'dinner', type:'heavy', spice:'normal'},
  {id:45, name:'Veg Spring Rolls', price:140, calories:300, nutrients:'Carbs', ingredients:'Veg rolls', img:'food7.jpg', nutri:'starchy', meal:'snack', type:'light', spice:'normal'},
  {id:46, name:'Samosa', price:50, calories:260, nutrients:'Carbs', ingredients:'Potato, pastry', img:'samosa.jpg', nutri:'starchy', meal:'snack', type:'light', spice:'normal'},
  {id:47, name:'Masala Dosa', price:120, calories:400, nutrients:'Carbs', ingredients:'Rice dosa, potato masala', img:'food5.jpg', nutri:'starchy', meal:'breakfast', type:'light', spice:'normal'},
  {id:48, name:'Idli Sambhar', price:90, calories:220, nutrients:'Carbs', ingredients:'Rice idli, sambar', img:'food6.jpg', nutri:'starchy', meal:'breakfast', type:'light', spice:'not'},
  {id:49, name:'Pav Bhaji (Double)', price:190, calories:820, nutrients:'Carbs', ingredients:'Extra butter', img:'pavbhaji.jpg', nutri:'starchy', meal:'dinner', type:'heavy', spice:'spicy'},
  {id:50, name:'Gulab Jamun', price:70, calories:250, nutrients:'Sugars', ingredients:'Milk solids, syrup', img:'gulab_jamun.jpg', nutri:'dairy', meal:'dessert', type:'light', spice:'not'}
];

/* ---------- OFFERS ---------- */
const OFFER_DATA = [
  { id:21, discountPercent:40, itemId:21 }, // modak
  { id:22, discountPercent:50, itemId:22 }, // patal puri
  { id:16, discountPercent:25, itemId:16 }, // ampalaya
  { id:3, discountPercent:15, itemId:3 },  // misal pav
  { id:12, discountPercent:30, itemId:12}, // kombdi vade // poha
  { id:50, discountPercent:17, itemId:50} // gulab jamun
];

/* ---------- UTILS AND RENDERERS ---------- */
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
    const h4 = el('h4'); h4.textContent = p.name;
    const p1 = el('p'); p1.className='muted'; p1.textContent = `${p.name} • ₹${p.price}`;
    a.appendChild(img); a.appendChild(h4); a.appendChild(p1);
    list.appendChild(a);
  });
}
/* ---------RENDER MENU ---------- */
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
function renderRestaurantsGrid(){
  const grid = document.getElementById('restaurantGrid');
  if (!grid) return;
  grid.innerHTML = '';
  const R = [
    {name:'Aishwarya Hotel', cuisine:'Maharashtrian', rating:4.6, cost:350, time:'25-30 min',img:'restaurant.jpg'},
    {name:'Pav & Co', cuisine:'Street Food', rating:4.4, cost:150, time:'20-25 min',img:'restaurant1.jpg'},
    {name:'Malvani Seas', cuisine:'Seafood', rating:4.7, cost:550, time:'35-40 min',img:'restaurant2.jpg'},
    {name:'Urban Pizza', cuisine:'Italian', rating:4.3, cost:450, time:'25-30 min',img:'restaurant3.jpg'},
    {name: "The Grand Thali",cuisine: "Maharashtrian",rating: 4.6,cost: 350,time: "25-30 min",img: "restaurant.jpg",type: "Casual Dining"},
    {name: "Anil Vada Pav",cuisine: "Street Food",rating: 4.4,cost: 150,time: "20-25 min",img: "restaurant1.jpg",type: "Street Stall"},
    {name: "Coastal King",cuisine: "Seafood",rating: 4.7,cost: 550,time: "35-40 min",img: "restaurant2.jpg",type: "Fine Dining"},
    {name: "Ristorante Bella",cuisine: "Italian",rating: 4.3,cost: 450,time: "25-30 min",img: "restaurant3.jpg",type: "Mid-Range"},
    {name: "Highway Dhaba No. 1",cuisine: "North Indian",rating: 3.9,cost: 200,time: "30-40 min",img: "restaurant4.jpg",type: "Dhaba (Roadside)"},
    {name: "Global Kitchen Fusion",cuisine: "Multi-Cuisine",rating: 4.8,cost: 850,time: "45-50 min",img: "restaurant5.jpg",type: "Luxury/Elite"},
    {name: "Quick Bites Subs",cuisine: "Fast Food",rating: 4.1,cost: 250,time: "15-20 min",img: "restaurant6.jpg",type: "Quick Service (QSR)"},
    {name: "The Gourmet Patisserie",cuisine: "Desserts & Bakery",rating: 4.5,cost: 300,time: "20-25 min",img: "restaurant7.jpg",type: "Cafe"},
    {name: "Chai & Chat Corner",cuisine: "Street Food",rating: 4.1,cost: 120,time: "15-20 min",img: "restaurant01.jpg",type: "Street Stall"},
    {name: "Bhel Puri Express",cuisine: "Snacks",rating: 4.3,cost: 150,time: "10-15 min",img: "restaurant02.jpg",type: "Quick Service (QSR)"},
    {name: "Amritsari Tandoor Dhaba",cuisine: "North Indian",rating: 3.8,cost: 220,time: "30-40 min",img: "restaurant03.jpg",type: "Dhaba (Roadside)"},
    {name: "Dosa Palace",cuisine: "South Indian",rating: 4.4,cost: 180,time: "20-25 min",img: "restaurant04.jpg",type: "Casual Eatery"},
    {name: "The Spice Route Bistro",cuisine: "Indian Fusion",rating: 4.5,cost: 450,time: "30-35 min",img: "restaurant05.jpg",type: "Casual Dining"},
    {name: "Bombay Brasserie",cuisine: "Contemporary Indian",rating: 4.6,cost: 500,time: "35-40 min",img: "restaurant06.jpg",type: "Premium Casual"},
    {name: "Pizza Roma",cuisine: "Italian",rating: 4.3,cost: 400,time: "25-30 min",img: "restaurant07.jpg",type: "Casual Dining"},
    {name: "Wok Master",cuisine: "Chinese",rating: 4.2,cost: 380,time: "25-30 min",img: "restaurant08.jpg",type: "Quick Service (QSR)"},
    {name: "The Daily Grind Cafe",cuisine: "Cafe & Coffee",rating: 4.5,cost: 300,time: "15-20 min",img: "restaurant09.jpg",type: "Cafe"},
    {name: "Sweet Surrender Bakery",cuisine: "Desserts & Bakery",rating: 4.7,cost: 350,time: "20-25 min",img: "restaurant10.jpg",type: "Bakery/Patisserie"},
    {name: "Kebab Corner",cuisine: "Mughlai",rating: 4.4,cost: 420,time: "30-35 min",img: "restaurant11.jpg",type: "Specialty"},
    {name: "Green Leaf Vegan",cuisine: "Health Food",rating: 4.6,cost: 320,time: "25-30 min",img: "restaurant12.jpg",type: "Health/Vegan"},
    {name: "The Saffron Room",cuisine: "North Indian",rating: 4.8,cost: 750,time: "40-45 min",img: "restaurant13.jpg",type: "Fine Dining"},
    {name: "Aqua Grill & Bar",cuisine: "Seafood & European",rating: 4.7,cost: 900,time: "45-50 min",img: "restaurant14.jpg",type: "Luxury/Elite"},
    {name: "Mizu Pan-Asian",cuisine: "Japanese/Pan-Asian",rating: 4.9,cost: 1200,time: "50-60 min",img: "restaurant15.jpg",type: "Ultra-Luxury"},
    {name: "The Heritage Feast",cuisine: "Regional Indian",rating: 4.7,cost: 650,time: "35-40 min",img: "restaurant16.jpg",type: "Premium Casual"}
  ];
  R.forEach(r=>{
    const card = el('div','card restaurant-card');
    const img = el('img'); img.src = `/static/foodapp/images/${r.img}`; img.alt=r.name; img.style.width='180px';
    const info = el('div','');
    const h = el('h4'); h.textContent = r.name;
    const p = el('p'); p.className='muted'; p.textContent = `${r.cuisine} • ₹${r.cost} for two • ${r.time}`;
    const btn = el('button','btn'); btn.textContent = 'View Menu'; btn.onclick = ()=> location.href='/menu/';
    info.appendChild(h); 
    info.appendChild(p); 
    info.appendChild(btn);
    card.appendChild(img); 
    card.appendChild(info);
    grid.appendChild(card);
  });
}
/* ---------- FILTERING LOGIC ---------- */
function gatherFilters(){
  const nutri = Array.from(document.querySelectorAll('input[name="nutri"]:checked')).map(i=>i.value);
  const meal = Array.from(document.querySelectorAll('input[name="meal"]:checked')).map(i=>i.value);
  const type = Array.from(document.querySelectorAll('input[name="type"]:checked')).map(i=>i.value);
  const spice = Array.from(document.querySelectorAll('input[name="spice"]:checked')).map(i=>i.value);
  const priceSort = document.querySelector('input[name="priceSort"]:checked') ? document.querySelector('input[name="priceSort"]:checked').value : null;
  return {nutri, meal, type, spice, priceSort};
}

function applyFilters(){
  const f = gatherFilters();
  let result = MENU_DATA.slice();
  if (f.nutri.length) result = result.filter(it => f.nutri.includes(it.nutri));
  if (f.meal.length) result = result.filter(it => f.meal.includes(it.meal));
  if (f.type.length) result = result.filter(it => f.type.includes(it.type));
  if (f.spice.length) result = result.filter(it => f.spice.includes(it.spice));
  if (f.priceSort === 'asc') result.sort((a,b)=>a.price-b.price);
  else if (f.priceSort === 'desc') result.sort((a,b)=>b.price-a.price);
  renderMenu(result);
}

/* ---------- INIT ---------- */
document.addEventListener('DOMContentLoaded', ()=>{
  const buttons = document.querySelectorAll(".filter-btn");

  buttons.forEach(btn => {
    btn.addEventListener("click", () => {
      const targetId = btn.getAttribute("data-target");
      const options = document.getElementById(targetId);

      // Close other open filters
      document.querySelectorAll(".filter-options").forEach(opt => {
        if (opt !== options) opt.classList.remove("show");
      });
      document.querySelectorAll(".filter-btn").forEach(b => {
        if (b !== btn) b.classList.remove("active");
      });

      // Toggle current one
      btn.classList.toggle("active");
      options.classList.toggle("show");
    });
  });

renderMenu(MENU_DATA);
const applyBtn = document.getElementById('applyFilters');
const clearBtn = document.getElementById('clearFilters');
// Ensure applyFilters runs after all data loaded
if (applyBtn) {
  applyBtn.addEventListener('click', (e)=>{
    e.preventDefault();
    if (typeof applyFilters === 'function') applyFilters();
    else console.error("applyFilters() not found");
  });
}
if (clearBtn) {
  clearBtn.addEventListener('click', (e)=>{
    e.preventDefault();
    document.querySelectorAll('input[type="checkbox"]').forEach(i=>i.checked=false);
    document.querySelectorAll('input[name="priceSort"]').forEach(i=>i.checked=false);
    renderMenu(MENU_DATA);
  });
}
  // initial full render
renderFeatured();
renderRestaurantsGrid();
renderOffers();
initSearch();

  // keep previous behaviors: featured & restaurants & offers if present
if (typeof renderFeatured === 'function') try{ renderFeatured(); }catch(e){}
if (typeof renderRestaurantsGrid === 'function') try{ renderRestaurantsGrid(); }catch(e){}
if (typeof renderOffers === 'function') try{ renderOffers(); }catch(e){}
});