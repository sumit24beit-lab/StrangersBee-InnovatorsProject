// cart.js - localStorage cart and cart UI

const CART_KEY = 'oneclick_cart_v2';

function getCart(){ return JSON.parse(localStorage.getItem(CART_KEY) || '[]'); }
function saveCart(c){ localStorage.setItem(CART_KEY, JSON.stringify(c)); updateCartCount(); }

function updateCartCount(){
  const countEls = document.querySelectorAll('#cartCount, .cart-count');
  const total = getCart().reduce((s,i)=>s+i.qty,0);
  countEls.forEach(el => el.textContent = total);
}

function addToCart(item){
  const cart = getCart();
  const idx = cart.findIndex(i=>i.id===item.id);
  if (idx>=0) cart[idx].qty += 1;
  else cart.push({ id:item.id, name:item.name, price:item.price, qty:1, img:item.img });
  saveCart(cart);
  toast(`${item.name} added to cart`);
}

function toast(msg){
  alert(msg); // simple prototype toast (can be improved)
}

/* ---------- Cart page rendering ---------- */
function renderCartPage(){
  const container = document.getElementById('cartItems');
  const summary = document.getElementById('summaryDetails');
  if (!container || !summary) return;
  const cart = getCart();
  container.innerHTML = '';
  if (cart.length === 0){
    container.innerHTML = '<div class="cart-empty">Your cart is empty. Browse the <a href="/menu/">menu</a>.</div>';
    summary.innerHTML = '<div class="muted">No items</div>';
    return;
  }
  cart.forEach(it=>{
    const div = document.createElement('div'); div.className='cart-item';
    const img = document.createElement('img'); img.src = `/static/foodapp/images/${it.img}`; img.alt=it.name;
    const info = document.createElement('div'); info.style.flex='1';
    const h = document.createElement('h4'); h.textContent = it.name;
    const p = document.createElement('div'); p.className='muted'; p.textContent = `₹${it.price} each`;
    const controls = document.createElement('div'); controls.className='qty';
    const minus = document.createElement('button'); minus.textContent='-'; minus.onclick = ()=> updateQty(it.id, -1);
    const qty = document.createElement('span'); qty.textContent = it.qty; qty.style.margin='0 8px';
    const plus = document.createElement('button'); plus.textContent='+'; plus.onclick = ()=> updateQty(it.id, 1);
    const remove = document.createElement('button'); remove.textContent='Remove'; remove.style.marginLeft='12px'; remove.onclick = ()=> removeItem(it.id);
    controls.appendChild(minus); controls.appendChild(qty); controls.appendChild(plus); controls.appendChild(remove);
    info.appendChild(h); info.appendChild(p); info.appendChild(controls);
    const lineTotal = document.createElement('div'); lineTotal.innerHTML = `<strong>₹${it.price * it.qty}</strong>`;
    div.appendChild(img); div.appendChild(info); div.appendChild(lineTotal);
    container.appendChild(div);
  });
  const subtotal = cart.reduce((s,i)=>s + (i.price*i.qty),0);
  const deliveryFee = subtotal > 500 ? 0 : 40;
  const taxes = Math.round(subtotal * 0.05);
  const total = subtotal + deliveryFee + taxes;
  summary.innerHTML = `
    <div>Subtotal: ₹${subtotal}</div>
    <div>Delivery fee: ₹${deliveryFee}</div>
    <div>Taxes: ₹${taxes}</div>
    <hr>
    <div style="font-weight:800">Total: ₹${total}</div>
  `;
}

/* ---------- Qty, remove, coupon, checkout ---------- */
function updateQty(id, delta){
  const cart = getCart();
  const idx = cart.findIndex(i=>i.id===id);
  if (idx>=0){
    cart[idx].qty += delta;
    if (cart[idx].qty <= 0) cart.splice(idx,1);
    saveCart(cart);
    renderCartPage();
  }
}
function removeItem(id){
  const cart = getCart().filter(i=>i.id!==id);
  saveCart(cart);
  renderCartPage();
}
function applyCoupon(code){
  if (!code) return alert('Enter coupon code');
  if (code.toUpperCase() === 'ONECLICK50'){
    alert('Coupon applied: ₹50 off on orders above ₹500 (prototype)');
  } else {
    alert('Invalid coupon');
  }
}
function proceedToDelivery(){
  location.href = '/delivery/';
}

/* ---------- Delivery page: form handling ---------- */
document.addEventListener('DOMContentLoaded', ()=>{
  updateCartCount();
  // cart page
  if (window.location.pathname.includes('/cart/')){
    renderCartPage();
    const applyBtn = document.getElementById('applyCoupon');
    if (applyBtn) applyBtn.addEventListener('click', ()=> {
      const code = document.getElementById('couponInput').value.trim();
      applyCoupon(code);
    });
    const checkoutBtn = document.getElementById('checkoutBtn');
    if (checkoutBtn) checkoutBtn.addEventListener('click', proceedToDelivery);
  }

  // delivery page handling
  if (window.location.pathname.includes('/delivery/')){
    const summary = document.getElementById('deliverySummary');
    if (summary){
      const cart = getCart();
      const subtotal = cart.reduce((s,i)=>s + (i.price*i.qty),0);
      const deliveryFee = subtotal > 500 ? 0 : 40;
      const taxes = Math.round(subtotal * 0.05);
      const total = subtotal + deliveryFee + taxes;
      summary.innerHTML = `<div><strong>Items:</strong> ${cart.length}</div>
        <div>Subtotal: ₹${subtotal}</div><div>Delivery: ₹${deliveryFee}</div><div>Taxes: ₹${taxes}</div><hr><div style="font-weight:800">To pay: ₹${total}</div>`;
    }

    const form = document.getElementById('deliveryForm');
    if (form){
      form.addEventListener('submit', (e)=>{
        e.preventDefault();
        const name = document.getElementById('custName').value.trim();
        const phone = document.getElementById('custPhone').value.trim();
        const addr = document.getElementById('custAddr').value.trim();
        if (!name || !phone || !addr) return alert('Please fill all fields');
        const orderId = 'OC' + Math.floor(Math.random()*90000 + 10000);
        alert(`Order placed! Your order ID is ${orderId}.`);
        localStorage.removeItem(CART_KEY);
        updateCartCount();
        location.href = '/';
      });
    }
  }
});

