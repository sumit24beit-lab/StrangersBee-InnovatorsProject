import os

content = """{% extends 'base.html' %}
{% load static %}

{% block title %}KitchenStation — Homemade Meals{% endblock %}

{% block content %}
<div class="container py-4">
  <!-- Header & Search -->
  <div class="text-center mb-5">
    <h1 class="display-5 fw-bold mb-3">Discover Homemade Meals</h1>
    <p class="lead text-muted mb-4">Find freshly prepared food from verified local home cooks.</p>
    
    <div class="row justify-content-center">
      <div class="col-md-8">
        <div class="input-group mb-3 ks-card p-2 flex-row border-0" style="background: transparent; box-shadow: none;">
          <input type="text" class="form-control" placeholder="Search for meals, cuisines, or ingredients..." id="mealSearchInput" style="height: 50px;">
          <button class="btn btn-ks-primary px-4" type="button" id="searchBtn">Search</button>
        </div>
      </div>
    </div>
  </div>

  <!-- Filters / Categories -->
  <div class="mb-5">
    <div class="d-flex flex-wrap gap-2 justify-content-center" id="categoryFilters">
      <button class="btn btn-ks-primary rounded-pill">All</button>
      <button class="btn btn-outline-secondary rounded-pill">North Indian</button>
      <button class="btn btn-outline-secondary rounded-pill">South Indian</button>
      <button class="btn btn-outline-secondary rounded-pill">Maharashtrian</button>
      <button class="btn btn-outline-secondary rounded-pill">Gujarati</button>
      <button class="btn btn-outline-secondary rounded-pill">Healthy / Diet</button>
      <button class="btn btn-outline-secondary rounded-pill">Snacks</button>
      <button class="btn btn-outline-secondary rounded-pill">Sweets</button>
    </div>
  </div>

  <!-- Meals Grid -->
  <div class="row g-4 mb-5" id="menuGrid">
    <!-- These would normally be rendered via JS/Django, providing placeholders here -->
    
    <div class="col-md-4 col-sm-6">
      <div class="ks-card">
        <h3 class="h5 fw-bold mb-1">Homestyle Paneer Thali</h3>
        <p class="text-muted small mb-1">By Asha's Kitchen</p>
        <div class="mb-2">
          <span class="ks-badge">North Indian</span>
          <span class="ks-badge">Veg</span>
        </div>
        <p class="small mb-3">Authentic paneer sabzi with 3 rotis, dal, and rice. Freshly made.</p>
        <div class="mt-auto pt-3 border-top d-flex justify-content-between align-items-center">
          <strong class="fs-5">₹180</strong>
          <button class="btn btn-ks-primary btn-sm">Add</button>
        </div>
      </div>
    </div>

    <div class="col-md-4 col-sm-6">
      <div class="ks-card">
        <h3 class="h5 fw-bold mb-1">Veg Biryani</h3>
        <p class="text-muted small mb-1">By Riya's Home Kitchen</p>
        <div class="mb-2">
          <span class="ks-badge">South Indian</span>
          <span class="ks-badge">Veg</span>
        </div>
        <p class="small mb-3">Homemade spices and fresh preparation. Served with raita.</p>
        <div class="mt-auto pt-3 border-top d-flex justify-content-between align-items-center">
          <strong class="fs-5">₹150</strong>
          <button class="btn btn-ks-primary btn-sm">Add</button>
        </div>
      </div>
    </div>

    <div class="col-md-4 col-sm-6">
      <div class="ks-card">
        <h3 class="h5 fw-bold mb-1">Masala Dosa</h3>
        <p class="text-muted small mb-1">By Meera's Kitchen</p>
        <div class="mb-2">
          <span class="ks-badge">South Indian</span>
          <span class="ks-badge">Veg</span>
        </div>
        <p class="small mb-3">Crispy dosa with homemade potato bhaji, sambar, and coconut chutney.</p>
        <div class="mt-auto pt-3 border-top d-flex justify-content-between align-items-center">
          <strong class="fs-5">₹90</strong>
          <button class="btn btn-ks-primary btn-sm">Add</button>
        </div>
      </div>
    </div>
    
    <div class="col-md-4 col-sm-6">
      <div class="ks-card">
        <h3 class="h5 fw-bold mb-1">Chicken Curry (Home Style)</h3>
        <p class="text-muted small mb-1">By Rahul's Kitchen</p>
        <div class="mb-2">
          <span class="ks-badge-accent ks-badge">Non-Veg</span>
        </div>
        <p class="small mb-3">Slow-cooked chicken curry using family recipe. Comes with 2 parathas.</p>
        <div class="mt-auto pt-3 border-top d-flex justify-content-between align-items-center">
          <strong class="fs-5">₹220</strong>
          <button class="btn btn-ks-primary btn-sm">Add</button>
        </div>
      </div>
    </div>

  </div>

  <!-- Story CTA -->
  <section class="mb-5 bg-white p-5 border rounded text-center" style="box-shadow: var(--ks-shadow); border-radius: var(--ks-radius);">
    <h2 class="h3 fw-bold mb-3">Every Meal Has a Story</h2>
    <p class="text-muted mb-4 max-w-md mx-auto">When you order on KitchenStation, you're not just getting food. You're supporting local home cooks sharing their passion, culture, and family recipes with the community.</p>
    <a href="{% url 'restaurant' %}" class="btn btn-ks-secondary">Meet Our Home Cooks</a>
  </section>

</div>
{% endblock %}
"""

with open("foodapp/templates/menu.html", "w", encoding="utf-8") as f:
    f.write(content)
print("menu.html updated.")
