
/* =========================================================
   KitchenStation - Cart and Checkout
   File: foodapp/static/foodapp/js/cart.js
   ========================================================= */

const CART_KEY = 'oneclick_cart_v2';
function getCartImageSource(img) {
  if (!img) {
    return '/static/foodapp/images/food5.jpg';
  }
  if (img.startsWith('/') || /^https?:\/\//i.test(img)) {
    return img;
  }
  return `/static/foodapp/images/${img}`;
}

/* ---------- Cart storage ---------- */

function getCart() {
  try {
    const cart = JSON.parse(localStorage.getItem(CART_KEY) || '[]');
    return Array.isArray(cart) ? cart : [];
  } catch (error) {
    console.error('Unable to read cart:', error);
    return [];
  }
}

function saveCart(cart) {
  localStorage.setItem(CART_KEY, JSON.stringify(cart));
  updateCartCount();
}

function updateCartCount() {
  const countEls = document.querySelectorAll('#cartCount, .cart-count');
  const total = getCart().reduce(
    (sum, item) => sum + Number(item.qty || 0),
    0
  );

  countEls.forEach(el => {
    el.textContent = total;
  });
}

function addToCart(item) {
  const cart = getCart();
  const index = cart.findIndex(existing => existing.id === item.id);

  if (index >= 0) {
    cart[index].qty += 1;
  } else {
    cart.push({
      id: item.id,
      name: item.name,
      price: Number(item.price),
      qty: 1,
      img: item.img
    });
  }

  saveCart(cart);
  toast(`${item.name} added to cart`);
}

function toast(message) {
  alert(message);
}

/* ---------- Shared price calculations ---------- */

function calculateCartTotals(cart) {
  const subtotal = cart.reduce(
    (sum, item) =>
      sum + Number(item.price) * Number(item.qty),
    0
  );

  const deliveryFee = subtotal > 500 ? 0 : (cart.length ? 40 : 0);
  const taxes = Math.round(subtotal * 0.05);
  const total = subtotal + deliveryFee + taxes;

  return { subtotal, deliveryFee, taxes, total };
}

/* ---------- Cart page rendering ---------- */

function renderCartPage() {
  const container = document.getElementById('cartItems');
  const summary = document.getElementById('summaryDetails');

  if (!container || !summary) return;

  const cart = getCart();
  container.innerHTML = '';

  if (cart.length === 0) {
    container.innerHTML = `
      <div class="cart-empty">
        Your cart is empty.
        <a href="/menu/">Browse the menu</a>.
      </div>
    `;

    summary.innerHTML = '<div class="muted">No items</div>';
    return;
  }

  cart.forEach(item => {
    const row = document.createElement('div');
    row.className = 'cart-item';

    const image = document.createElement('img');
    image.className = 'ks-cart-thumb';
    image.src = getCartImageSource(item.img);
    image.alt = item.name;

    const info = document.createElement('div');
    info.style.flex = '1';

    const heading = document.createElement('h4');
    heading.textContent = item.name;

    const price = document.createElement('div');
    price.className = 'muted';
    price.textContent = `₹${item.price} each`;

    const controls = document.createElement('div');
    controls.className = 'qty';

    const minus = document.createElement('button');
    minus.type = 'button';
    minus.textContent = '-';
    minus.className = 'btn btn-sm btn-ks-secondary px-2 py-0';
    minus.addEventListener('click', () => updateQty(item.id, -1));

    const quantity = document.createElement('span');
    quantity.textContent = item.qty;
    quantity.className = 'fw-bold';
    quantity.style.margin = '0 12px';

    const plus = document.createElement('button');
    plus.type = 'button';
    plus.textContent = '+';
    plus.className = 'btn btn-sm btn-ks-secondary px-2 py-0';
    plus.addEventListener('click', () => updateQty(item.id, 1));

    const remove = document.createElement('button');
    remove.type = 'button';
    remove.textContent = 'Remove';
    remove.className = 'btn btn-sm btn-outline-danger ms-3';
    remove.addEventListener('click', () => removeItem(item.id));

    controls.append(minus, quantity, plus, remove);
    info.append(heading, price, controls);

    const lineTotal = document.createElement('div');
    const strong = document.createElement('strong');
    strong.textContent =
      `₹${Number(item.price) * Number(item.qty)}`;

    lineTotal.appendChild(strong);
    row.append(image, info, lineTotal);
    container.appendChild(row);
  });

  const totals = calculateCartTotals(cart);

  summary.innerHTML = `
    <div>Subtotal: ₹${totals.subtotal}</div>
    <div>Delivery fee: ₹${totals.deliveryFee}</div>
    <div>Taxes: ₹${totals.taxes}</div>
    <hr>
    <div style="font-weight:800">Total: ₹${totals.total}</div>
  `;
}

/* ---------- Quantity and removal ---------- */

function updateQty(id, delta) {
  const cart = getCart();
  const index = cart.findIndex(item => item.id === id);

  if (index === -1) return;

  cart[index].qty += delta;

  if (cart[index].qty <= 0) {
    cart.splice(index, 1);
  }

  saveCart(cart);
  renderCartPage();
}

function removeItem(id) {
  const cart = getCart().filter(item => item.id !== id);
  saveCart(cart);
  renderCartPage();
}

function applyCoupon(code) {
  if (!code) {
    alert('Enter coupon code');
    return;
  }

  if (code.toUpperCase() === 'ONECLICK50') {
    alert(
      'Coupon applied: ₹50 off on orders above ₹500 (prototype only)'
    );
  } else {
    alert('Invalid coupon');
  }
}

function proceedToDelivery() {
  window.location.href = '/delivery/';
}

/* ---------- Checkout page rendering ---------- */

function renderCheckoutPage() {
  const container = document.getElementById('order-items-preview');

  if (!container) return;

  const cart = getCart();
  container.innerHTML = '';

  const subtotalElement = document.getElementById('summ-sub');
  const deliveryElement = document.getElementById('summ-del');
  const totalElement = document.getElementById('summ-tot');
  const discountRow = document.getElementById('summ-discount-row');
  const placeOrderButton = document.getElementById('placeOrderBtn');

  if (cart.length === 0) {
    container.innerHTML = `
      <p class="text-muted">Your cart is empty.</p>
      <a href="/menu/" class="btn btn-outline-secondary">
        Browse meals
      </a>
    `;

    if (subtotalElement) subtotalElement.textContent = '₹0';
    if (deliveryElement) deliveryElement.textContent = '₹0';
    if (totalElement) totalElement.textContent = '₹0';

    if (discountRow) discountRow.style.display = 'none';
    if (placeOrderButton) placeOrderButton.disabled = true;

    return;
  }

  if (placeOrderButton) placeOrderButton.disabled = false;

  cart.forEach(item => {
    const row = document.createElement('div');
    row.className =
      'd-flex align-items-center gap-3 mb-2 checkout-item';

    row.style.minHeight = '0';
    row.style.padding = '4px 0';

    const image = document.createElement('img');
    image.src = getCartImageSource(item.img);
    image.alt = item.name;

    image.style.width = '70px';
    image.style.height = '90px';
    image.style.minWidth = '70px';
    image.style.objectFit = 'cover';
    image.style.objectPosition = 'center';
    image.style.borderRadius = '10px';
    image.style.flexShrink = '0';
    image.style.border =
      '1px solid rgba(45, 45, 45, 0.12)';

    image.addEventListener('error', () => {
      image.style.display = 'none';
    });

    const details = document.createElement('div');
    details.className = 'flex-grow-1';
    details.style.minWidth = '0';

    const name = document.createElement('div');
    name.className = 'fw-bold';
    name.textContent = item.name;
    name.style.overflowWrap = 'anywhere';

    const quantity = document.createElement('div');
    quantity.className = 'text-muted small';
    quantity.textContent = `Qty: ${item.qty}`;

    const price = document.createElement('div');
    price.className = 'fw-bold';
    price.style.flexShrink = '0';
    price.textContent =
      `₹${Number(item.price) * Number(item.qty)}`;

    details.append(name, quantity);
    row.append(image, details, price);
    container.appendChild(row);
  });

  const totals = calculateCartTotals(cart);

  if (discountRow) {
    discountRow.classList.remove('d-flex');
    discountRow.style.display = 'none';
  }

  if (subtotalElement) {
    subtotalElement.textContent = `₹${totals.subtotal}`;
  }

  if (deliveryElement) {
    deliveryElement.textContent = `₹${totals.deliveryFee}`;
  }

  if (totalElement) {
    totalElement.textContent = `₹${totals.total}`;
  }
}

/* ---------- Prototype order placement ---------- */

async function handlePlaceOrder() {
  const cart = getCart();

  if (cart.length === 0) {
    alert('Your cart is empty. Please add a meal first.');
    return;
  }

  const form = document.getElementById('deliveryForm');

  if (!form || !form.reportValidity()) {
    return;
  }

  const terms = document.getElementById('termsCheck');

  if (!terms || !terms.checked) {
    alert(
      'Please agree to the Terms & Conditions and Cancellation Policy.'
    );
    if (terms) terms.focus();
    return;
  }

  const phone = document.getElementById('custPhone')?.value.trim();
  const addressSelect = document.getElementById('custAddress');
  const addressId = addressSelect?.value;

  if (!phone) {
    alert('Please enter your phone number');
    return;
  }

  if(!addressId) {
    alert('Please select a saved delivery address.');
    addressSelect?.focus();
    return;
  }

  const paymentInput = document.querySelector(
    'input[name="paymentMethod"]:checked'
  );

  if (!paymentInput || paymentInput.value !== 'cod') {
    alert('Please select Cash on Delivery.');
    return;
  }

  const csrfToken = form.querySelector(
    '[name="csrfmiddlewaretoken"]'
  )?.value;

  if(!csrfToken) {
    alert('Security token is missing. Refresh the page and try again.');
    return;
  }

  const placeOrderButton = document.getElementById('placeOrderBtn');
  const originalButtonText = placeOrderButton?.textContent;

  if(placeOrderButton) {
    placeOrderButton.disabled = true;
    placeOrderButton.textContent = 'Placing Order...';
  }

  try {
    const response = await fetch(form.dataset.placeOrderUrl, {
      method: 'POST',
      credentials: 'same-origin',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken,
        'Accept': 'application/json'
      },
      body: JSON.stringify({
        phone: phone,
        address_id: Number(addressId),
        payment_method: paymentInput.value,
        items: cart.map(item => ({
          id: item.id,
          qty: Number(item.qty)
        }))
      })
    });

    let result;

    try {
      result = await response.json();
    } catch {
      throw new Error(
        'The server returned an unexpected response. Please try again.'
      );
    }

    if(!response.ok) {
      throw new Error(
        result.error || 'Unable to place your order.'
      );
    }

    if(!result.success || !result.redirect_url) {
      throw new Error('The server did not confirm the order.');
    }

    // Clear the cart only after the server confirms success.
    localStorage.removeItem(CART_KEY);
    updateCartCount();

    alert(`Order placed successfully!\nOrder ID: KS-${result.order_id}`);
    window.location.href = result.redirect_url;

  } catch(error) {
    console.error('order placement failed:', error);
    alert(error.message || 'Unable to place your order. Please try again.');
  } finally {
    if (placeOrderButton) {
      placeOrderButton.disabled = false;
      placeOrderButton.textContent = originalButtonText;
    }
  }
}

/* ---------- Page initialization ---------- */

document.addEventListener('DOMContentLoaded', () => {
  updateCartCount();
  document.querySelectorAll('add-to-cart-btn').forEach(button => {
    button.addEventListener('click', () => {
      const item = {
        id: Number(button.dataset.id),
        name: button.dataset.name,
        price: Number(button.dataset.price),
        img: button.dataset.img
      };
      if (
        !Number.isInteger(item.id) || item.id <=0 ||
        !Number.isFinite(item.price) || item.price < 0
      ) {
        alert('Invalid meal details. Please refresh the menu.');
        return;
      }
      addToCart(item);
    });
  });

  // Cart page
  if (window.location.pathname.includes('/cart/')) {
    renderCartPage();

    const applyButton = document.getElementById('applyCoupon');

    if (applyButton) {
      applyButton.addEventListener('click', () => {
        const input = document.getElementById('couponInput');
        applyCoupon(input ? input.value.trim() : '');
      });
    }

    const checkoutButton = document.getElementById('checkoutBtn');

    if (checkoutButton) {
      checkoutButton.addEventListener('click', proceedToDelivery);
    }
  }

  // Checkout page
  if (document.getElementById('order-items-preview')) {
    renderCheckoutPage();

    const placeOrderButton =
      document.getElementById('placeOrderBtn');

    if (placeOrderButton) {
      placeOrderButton.addEventListener(
        'click',
        handlePlaceOrder
      );
    }
  }

  // Legacy delivery page
  if (
    window.location.pathname.includes('/delivery/') &&
    document.getElementById('deliveryForm')
  ) {
    const form = document.getElementById('deliveryForm');

    form.addEventListener('submit', event => {
      event.preventDefault();

      const name = document.getElementById('custName').value.trim();
      const phone = document.getElementById('custPhone').value.trim();
      const address = document.getElementById('custAddr').value.trim();

      if (!name || !phone || !address) {
        alert('Please fill in all fields.');
        return;
      }

      const cart = getCart();

      if (cart.length === 0) {
        alert('Your cart is empty.');
        return;
      }

      const orderId =
        'KS' + Math.floor(10000 + Math.random() * 90000);

      alert(
        `Prototype order placed. Order ID: ${orderId}\n` +
        'This order has not been saved to the database.'
      );

      localStorage.removeItem(CART_KEY);
      updateCartCount();
      window.location.href = '/';
    });
  }
});