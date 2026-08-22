import os

contact_content = """{% extends 'base.html' %}
{% load static %}

{% block title %}KitchenStation — Contact Support{% endblock %}

{% block content %}
<div class="container py-4">
  <div class="text-center mb-5">
    <h1 class="display-6 fw-bold mb-3">Contact Support</h1>
    <p class="text-muted">We're here to help you with your homemade food orders.</p>
  </div>

  <div class="row g-4 mb-5">
    <div class="col-md-4">
      <div class="ks-card text-center p-4">
        <span class="fs-1 mb-2 d-block">📦</span>
        <h3 class="h6 fw-bold">Order Issues</h3>
        <p class="text-muted small mb-0">Help with an active or past order.</p>
      </div>
    </div>
    <div class="col-md-4">
      <div class="ks-card text-center p-4">
        <span class="fs-1 mb-2 d-block">🍳</span>
        <h3 class="h6 fw-bold">Cook Feedback</h3>
        <p class="text-muted small mb-0">Share your experience with a home cook.</p>
      </div>
    </div>
    <div class="col-md-4">
      <div class="ks-card text-center p-4">
        <span class="fs-1 mb-2 d-block">💬</span>
        <h3 class="h6 fw-bold">General Query</h3>
        <p class="text-muted small mb-0">Anything else you need help with.</p>
      </div>
    </div>
  </div>

  <div class="row g-5">
    <div class="col-lg-7">
      <div class="ks-card">
        <h3 class="h5 fw-bold mb-4 border-bottom pb-2">Send us a message</h3>
        <form id="contactForm">
          {% csrf_token %}
          <div class="mb-3">
            <label class="form-label text-muted small">Name</label>
            <input type="text" class="form-control" required>
          </div>
          <div class="mb-3">
            <label class="form-label text-muted small">Email</label>
            <input type="email" class="form-control" required>
          </div>
          <div class="mb-3">
            <label class="form-label text-muted small">Message</label>
            <textarea class="form-control" rows="5" required></textarea>
          </div>
          <button type="submit" class="btn btn-ks-primary w-100">Send Message</button>
        </form>
      </div>
    </div>
    <div class="col-lg-5">
      <div class="ks-card mb-4 bg-light">
        <h3 class="h6 fw-bold mb-3">KitchenStation HQ</h3>
        <p class="small text-muted mb-1"><i class="bi bi-envelope"></i> support@kitchenstation.com</p>
        <p class="small text-muted mb-0"><i class="bi bi-telephone"></i> +91 98765 43210</p>
      </div>
      <div class="ks-card bg-light">
        <h3 class="h6 fw-bold mb-3">Working Hours</h3>
        <p class="small text-muted mb-1">Monday - Sunday</p>
        <p class="small fw-bold mb-0">8:00 AM - 10:00 PM</p>
      </div>
    </div>
  </div>
</div>
{% endblock %}
"""

offers_content = """{% extends 'base.html' %}
{% load static %}

{% block title %}KitchenStation — Offers{% endblock %}

{% block content %}
<div class="container py-4">
  <div class="text-center mb-5">
    <h1 class="display-6 fw-bold mb-3">Special Offers & Combos</h1>
    <p class="text-muted">Discover great deals on homemade food in your neighborhood.</p>
  </div>

  <div class="row g-4 mb-5">
    <div class="col-md-6">
      <div class="ks-card position-relative overflow-hidden" style="background-color: rgba(201, 106, 74, 0.1); border-color: var(--ks-accent);">
        <div class="position-absolute top-0 end-0 bg-accent text-white px-3 py-1 fw-bold" style="background-color: var(--ks-accent); border-bottom-left-radius: var(--ks-radius-sm);">
          20% OFF
        </div>
        <h3 class="h4 fw-bold mb-2">Weekend Special Thali</h3>
        <p class="text-muted small mb-3">By Asha's Kitchen</p>
        <p class="mb-4">Get 20% off on special weekend thalis. Pre-order now!</p>
        <div class="d-flex justify-content-between align-items-center mt-auto">
          <div>
            <span class="text-muted text-decoration-line-through small me-2">₹250</span>
            <span class="fs-5 fw-bold" style="color: var(--ks-accent);">₹200</span>
          </div>
          <button class="btn btn-ks-accent btn-sm">Order Now</button>
        </div>
      </div>
    </div>
    
    <div class="col-md-6">
      <div class="ks-card position-relative overflow-hidden" style="background-color: rgba(95, 141, 78, 0.1); border-color: var(--ks-primary);">
        <div class="position-absolute top-0 end-0 bg-primary text-white px-3 py-1 fw-bold" style="background-color: var(--ks-primary); border-bottom-left-radius: var(--ks-radius-sm);">
          FREE DESSERT
        </div>
        <h3 class="h4 fw-bold mb-2">Family Combo Deal</h3>
        <p class="text-muted small mb-3">By Riya's Home Kitchen</p>
        <p class="mb-4">Order any family biryani pack and get a complimentary homemade gulab jamun.</p>
        <div class="d-flex justify-content-between align-items-center mt-auto">
          <span class="fs-5 fw-bold" style="color: var(--ks-primary);">₹650</span>
          <button class="btn btn-ks-primary btn-sm">Order Now</button>
        </div>
      </div>
    </div>
  </div>
</div>
{% endblock %}
"""

with open("foodapp/templates/contact.html", "w", encoding="utf-8") as f: f.write(contact_content)
with open("foodapp/templates/offers.html", "w", encoding="utf-8") as f: f.write(offers_content)

print("Contact and Offers templates updated.")
