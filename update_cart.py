import os

content = """{% extends 'base.html' %}
{% load static %}

{% block title %}KitchenStation — Your Cart{% endblock %}

{% block content %}
<div class="container py-4 cart-page">
  <div class="mb-4">
    <h1 class="display-6 fw-bold">Your Cart</h1>
    <p class="text-muted">Review your items before checkout</p>
  </div>

  <div class="row g-4">
    <!-- Cart Items Section -->
    <div class="col-lg-8">
      <div class="ks-card mb-4" id="cartItemsContainer">
        <!-- JS will render items here -->
        <div id="emptyCartState" class="text-center py-5" style="display: none;">
          <span class="fs-1 mb-3 d-block">🛒</span>
          <h3 class="h5 fw-bold">Your cart is empty</h3>
          <p class="text-muted mb-4">Looks like you haven't added any homemade meals yet.</p>
          <a href="{% url 'menu' %}" class="btn btn-ks-primary">Explore Homemade Meals</a>
        </div>
        
        <div id="cartItems">
          <!-- Item Card Prototype (hidden or handled by JS) -->
          <!--
          <div class="d-flex align-items-center border-bottom pb-3 mb-3">
            <div class="flex-shrink-0">
              <img src="/static/foodapp/images/meal-placeholder.jpg" class="rounded" style="width:80px; height:80px; object-fit:cover;" alt="Meal">
            </div>
            <div class="flex-grow-1 ms-3">
              <h4 class="h6 fw-bold mb-1">Homestyle Paneer Thali</h4>
              <p class="text-muted small mb-2">By Asha's Kitchen</p>
              <h5 class="fw-bold mb-0">₹180</h5>
            </div>
            <div class="d-flex align-items-center">
              <div class="input-group input-group-sm" style="width: 100px;">
                <button class="btn btn-outline-secondary" type="button">-</button>
                <input type="text" class="form-control text-center" value="1">
                <button class="btn btn-outline-secondary" type="button">+</button>
              </div>
              <button class="btn text-danger ms-2"><i class="bi bi-trash"></i></button>
            </div>
          </div>
          -->
        </div>
      </div>
    </div>

    <!-- Order Summary Section -->
    <div class="col-lg-4">
      <div class="ks-card position-sticky" style="top: 100px;">
        <h3 class="h5 fw-bold mb-3 pb-3 border-bottom">Order Summary</h3>
        
        <div id="summaryDetails">
          <div class="d-flex justify-content-between mb-2">
            <span class="text-muted">Subtotal</span>
            <span class="fw-bold">₹0</span>
          </div>
          <div class="d-flex justify-content-between mb-2">
            <span class="text-muted">Delivery Fee</span>
            <span class="fw-bold">₹0</span>
          </div>
          <div class="d-flex justify-content-between mb-3 pb-3 border-bottom text-success" id="discountRow" style="display:none;">
            <span>Discount</span>
            <span class="fw-bold">-₹0</span>
          </div>
          <div class="d-flex justify-content-between mb-4">
            <span class="fs-5 fw-bold">Total</span>
            <span class="fs-5 fw-bold" style="color: var(--ks-primary);">₹0</span>
          </div>
        </div>

        <div class="mb-4">
          <div class="input-group">
            <input type="text" class="form-control" id="couponInput" placeholder="Promo code">
            <button class="btn btn-ks-secondary" type="button" id="applyCoupon">Apply</button>
          </div>
        </div>

        <button class="btn btn-ks-primary w-100 mb-2" id="checkoutBtn">Proceed to Checkout</button>
        <a href="{% url 'menu' %}" class="btn btn-outline-secondary w-100">Continue Shopping</a>
      </div>
    </div>
  </div>
</div>
{% endblock %}
"""

with open("foodapp/templates/cart.html", "w", encoding="utf-8") as f:
    f.write(content)
print("cart.html updated.")
