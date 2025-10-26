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
  {id:16, name:'Ampalaya Bhaji', price:100, calories:150, nutrients:'Veg rich', ingredients:'Bitter gourd stir fry', img:'ampalaya_bhaji.jpg', nutri:'fruits', meal:'lunch', type:'light', spice:'normal'},
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
  {id:27, name:'Pepperoni Pizza', price:410, calories:760, nutrients:'Protein 25g', ingredients:'Pepperoni, cheese', img:'margherita_pizza.jpg', nutri:'fats', meal:'dinner', type:'heavy', spice:'normal'},
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
  {id:43, name:'Garlic Bread', price:80, calories:260, nutrients:'Carbs', ingredients:'Bread, garlic butter', img:'food1.jpg', nutri:'starchy', meal:'snack', type:'light', spice:'normal'},
  {id:44, name:'Paneer Butter Masala', price:240, calories:620, nutrients:'Protein', ingredients:'Paneer, tomato gravy', img:'food2.jpg', nutri:'protein', meal:'dinner', type:'heavy', spice:'normal'},
  {id:45, name:'Veg Spring Rolls', price:140, calories:300, nutrients:'Carbs', ingredients:'Veg rolls', img:'food3.jpg', nutri:'starchy', meal:'snack', type:'light', spice:'normal'},
  {id:46, name:'Samosa', price:50, calories:260, nutrients:'Carbs', ingredients:'Potato, pastry', img:'patal_puri.jpg', nutri:'starchy', meal:'snack', type:'light', spice:'normal'},
  {id:47, name:'Masala Dosa', price:120, calories:400, nutrients:'Carbs', ingredients:'Rice dosa, potato masala', img:'food1.jpg', nutri:'starchy', meal:'breakfast', type:'light', spice:'normal'},
  {id:48, name:'Idli Sambhar', price:90, calories:220, nutrients:'Carbs', ingredients:'Rice idli, sambar', img:'food2.jpg', nutri:'starchy', meal:'breakfast', type:'light', spice:'not'},
  {id:49, name:'Pav Bhaji (Double)', price:190, calories:820, nutrients:'Carbs', ingredients:'Extra butter', img:'pavbhaji.jpg', nutri:'starchy', meal:'dinner', type:'heavy', spice:'spicy'},
  {id:50, name:'Gulab Jamun', price:70, calories:250, nutrients:'Sugars', ingredients:'Milk solids, syrup', img:'shrikhand.jpg', nutri:'dairy', meal:'dessert', type:'light', spice:'not'}
];

/* ---------- UTILS AND RENDERERS ---------- */
function el(tag, cls){ const e = document.createElement(tag); if (cls) e.className = cls; return e; }

function renderMenuList(data){
  const grid = document.getElementById('menuGrid');
  if (!grid) return;
  grid.innerHTML = '';
  data.forEach(item => {
    const card = el('div','menu-item');
    const img = el('img'); img.src = `/static/onestopapp/images/${item.img}`; img.alt = item.name;
    const meta = el('div','menu-meta');
    const title = el('h4'); title.textContent = item.name;
    const rest = el('div'); rest.className='muted'; rest.textContent = `${item.nutrients} • ₹${item.price}`;
    const mrow = el('div','meta-row'); mrow.textContent = `${item.calories} kcal • ${item.ingredients}`;
    const bottom = el('div'); bottom.style.display='flex'; bottom.style.justifyContent='space-between'; bottom.style.alignItems='center';
    const price = el('div'); price.innerHTML = `₹${item.price}`;
    const add = el('button','add-btn'); add.textContent='Add to Cart'; add.onclick = ()=> addToCart({id:item.id,name:item.name,price:item.price,img:item.img});
    bottom.appendChild(price); bottom.appendChild(add);
    meta.appendChild(title); meta.appendChild(rest); meta.appendChild(mrow); meta.appendChild(bottom);
    card.appendChild(img); card.appendChild(meta);
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

  // Nutrient filter (map input names to item.nutri)
  if (f.nutri.length){
    result = result.filter(it => f.nutri.includes(it.nutri));
  }
  // Meal
  if (f.meal.length){
    result = result.filter(it => f.meal.includes(it.meal));
  }
  // Type
  if (f.type.length){
    result = result.filter(it => f.type.includes(it.type));
  }
  // Spice
  if (f.spice.length){
    result = result.filter(it => f.spice.includes(it.spice));
  }
  // Price sort
  if (f.priceSort === 'asc') result.sort((a,b)=>a.price-b.price);
  else if (f.priceSort === 'desc') result.sort((a,b)=>b.price-a.price);

  renderMenuList(result);
}

/* ---------- INIT ---------- */
document.addEventListener('DOMContentLoaded', ()=>{
  // initial full render
  renderMenuList(MENU_DATA);

  const applyBtn = document.getElementById('applyFilters');
  const clearBtn = document.getElementById('clearFilters');
  if (applyBtn) applyBtn.addEventListener('click', applyFilters);
  if (clearBtn) clearBtn.addEventListener('click', ()=>{
    document.querySelectorAll('input[type="checkbox"]').forEach(i=>i.checked=false);
    document.querySelectorAll('input[name="priceSort"]').forEach(i=>i.checked=false);
    renderMenuList(MENU_DATA);
  });

  // keep previous behaviors: featured & restaurants & offers if present
  if (typeof renderFeatured === 'function') try{ renderFeatured(); }catch(e){}
  if (typeof renderRestaurantsGrid === 'function') try{ renderRestaurantsGrid(); }catch(e){}
  if (typeof renderOffers === 'function') try{ renderOffers(); }catch(e){}
});

