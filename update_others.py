import os

hist_content = """{% extends 'base.html' %}
{% load static %}

{% block title %}KitchenStation — Order History{% endblock %}

{% block content %}
<div class="container py-4">
  <div class="d-flex justify-content-between align-items-center mb-4">
    <h1 class="display-6 fw-bold mb-0">Order History</h1>
  </div>
  
  <div class="row">
    <div class="col-lg-8 mx-auto">
      <div class="ks-card mb-3 p-3">
        <div class="d-flex justify-content-between align-items-center border-bottom pb-2 mb-2">
          <div>
            <span class="badge bg-success mb-1">Delivered</span>
            <p class="text-muted small mb-0">#KS-84920 • 22 Aug 2026</p>
          </div>
          <div class="text-end">
            <h4 class="h6 fw-bold mb-0">₹360</h4>
          </div>
        </div>
        <div class="d-flex justify-content-between align-items-center">
          <div>
            <p class="mb-1 fw-bold">Asha's Kitchen</p>
            <p class="small text-muted mb-0">2x Homestyle Paneer Thali</p>
          </div>
          <button class="btn btn-ks-primary btn-sm">Reorder</button>
        </div>
      </div>

      <div class="ks-card mb-3 p-3">
        <div class="d-flex justify-content-between align-items-center border-bottom pb-2 mb-2">
          <div>
            <span class="badge bg-success mb-1">Delivered</span>
            <p class="text-muted small mb-0">#KS-84110 • 15 Aug 2026</p>
          </div>
          <div class="text-end">
            <h4 class="h6 fw-bold mb-0">₹150</h4>
          </div>
        </div>
        <div class="d-flex justify-content-between align-items-center">
          <div>
            <p class="mb-1 fw-bold">Riya's Home Kitchen</p>
            <p class="small text-muted mb-0">1x Veg Biryani</p>
          </div>
          <button class="btn btn-ks-primary btn-sm">Reorder</button>
        </div>
      </div>
    </div>
  </div>
</div>
{% endblock %}
"""

cook_content = """{% extends 'base.html' %}
{% load static %}

{% block title %}KitchenStation — Cook Profile{% endblock %}

{% block content %}
<div class="container py-4">
  <div class="ks-card p-0 overflow-hidden mb-5 border-0 shadow-none">
    <div style="height: 200px; background: url('{% static 'foodapp/images/cook_placeholder.jpg' %}') center/cover;"></div>
    <div class="px-4 pb-4 position-relative">
      <img src="{% static 'foodapp/images/cook_placeholder.jpg' %}" alt="Cook" class="rounded-circle border border-4 border-white position-absolute" style="width: 120px; height: 120px; top: -60px; object-fit: cover;">
      
      <div class="pt-5 mt-2 d-flex justify-content-between align-items-start">
        <div>
          <h1 class="h3 fw-bold mb-1">Asha's Kitchen</h1>
          <p class="text-muted mb-2"><i class="bi bi-geo-alt"></i> Andheri West • <span class="ks-badge">North Indian</span></p>
          <p class="mb-0 max-w-md">"Cooking authentic North Indian food from my home for 15 years. My food is prepared with cold-pressed oils and no artificial colors."</p>
        </div>
        <div class="text-end">
          <span class="ks-badge-accent ks-badge d-block mb-2 text-center fs-5 py-2">★ 4.8</span>
          <p class="text-muted small mb-0">120+ Ratings</p>
        </div>
      </div>
    </div>
  </div>

  <h2 class="h4 fw-bold mb-4 border-bottom pb-2">Meals by Asha</h2>
  
  <div class="row g-4">
    <div class="col-md-4">
      <div class="ks-card">
        <h3 class="h5 fw-bold mb-1">Homestyle Paneer Thali</h3>
        <p class="text-muted small mb-3">Fresh paneer gravy with 3 rotis, dal, and rice.</p>
        <div class="mt-auto pt-3 border-top d-flex justify-content-between align-items-center">
          <strong class="fs-5">₹180</strong>
          <button class="btn btn-ks-primary btn-sm">Add</button>
        </div>
      </div>
    </div>
    <div class="col-md-4">
      <div class="ks-card">
        <h3 class="h5 fw-bold mb-1">Rajma Chawal</h3>
        <p class="text-muted small mb-3">Authentic punjabi rajma cooked overnight, served with jeera rice.</p>
        <div class="mt-auto pt-3 border-top d-flex justify-content-between align-items-center">
          <strong class="fs-5">₹140</strong>
          <button class="btn btn-ks-primary btn-sm">Add</button>
        </div>
      </div>
    </div>
    <div class="col-md-4">
      <div class="ks-card opacity-75">
        <h3 class="h5 fw-bold mb-1">Aloo Paratha (2 pcs)</h3>
        <p class="text-muted small mb-3">Stuffed with seasoned potatoes, served with homemade curd and pickle.</p>
        <div class="mt-auto pt-3 border-top d-flex justify-content-between align-items-center">
          <strong class="fs-5 text-muted">₹100</strong>
          <span class="text-danger small fw-bold">Sold Out</span>
        </div>
      </div>
    </div>
  </div>
</div>
{% endblock %}
"""

meal_content = """{% extends 'base.html' %}
{% load static %}

{% block title %}KitchenStation — Meal Detail{% endblock %}

{% block content %}
<div class="container py-5">
  <div class="row g-5">
    <div class="col-md-6">
      <img src="{% static 'foodapp/images/meal-placeholder.jpg' %}" alt="Meal" class="img-fluid rounded" style="border: 2px solid var(--ks-border); box-shadow: var(--ks-shadow); width:100%;">
    </div>
    <div class="col-md-6">
      <div class="mb-2">
        <span class="ks-badge">Veg</span>
        <span class="ks-badge">North Indian</span>
      </div>
      <h1 class="display-6 fw-bold mb-2">Homestyle Paneer Thali</h1>
      <p class="text-muted mb-3">By <a href="#" class="text-decoration-none fw-bold" style="color: var(--ks-primary);">Asha's Kitchen</a></p>
      
      <h2 class="h3 fw-bold mb-4" style="color: var(--ks-accent);">₹180</h2>
      
      <p class="mb-4">Enjoy a wholesome, freshly prepared North Indian thali straight from Asha's kitchen. Made with high-quality ingredients, cold-pressed mustard oil, and authentic homemade masalas.</p>
      
      <div class="ks-card bg-light p-3 mb-4">
        <h4 class="h6 fw-bold mb-2">What's included:</h4>
        <ul class="mb-0 text-muted small">
          <li>Paneer Butter Masala (250ml)</li>
          <li>Yellow Dal Tadka (250ml)</li>
          <li>3 Whole Wheat Phulkas (with Ghee)</li>
          <li>Steamed Rice</li>
          <li>Salad & Pickle</li>
        </ul>
      </div>

      <div class="d-flex gap-3 align-items-center">
        <div class="input-group" style="width: 120px;">
          <button class="btn btn-outline-secondary" type="button">-</button>
          <input type="text" class="form-control text-center" value="1">
          <button class="btn btn-outline-secondary" type="button">+</button>
        </div>
        <button class="btn btn-ks-primary flex-grow-1">Add to Cart</button>
      </div>
    </div>
  </div>
</div>
{% endblock %}
"""

cust_content = """{% extends 'base.html' %}
{% load static %}

{% block title %}KitchenStation — My Profile{% endblock %}

{% block content %}
<div class="container py-4">
  <div class="row g-4">
    <div class="col-md-4">
      <div class="ks-card text-center mb-4">
        <div class="mb-3">
          <div class="d-inline-flex align-items-center justify-content-center bg-secondary text-white rounded-circle" style="width: 80px; height: 80px; font-size: 2rem; font-weight: bold;">
            JD
          </div>
        </div>
        <h2 class="h5 fw-bold mb-1">John Doe</h2>
        <p class="text-muted small">john.doe@example.com</p>
        <button class="btn btn-outline-secondary btn-sm w-100 mt-2">Edit Profile</button>
      </div>
      
      <div class="ks-card p-3">
        <ul class="nav flex-column gap-2">
          <li class="nav-item">
            <a href="#" class="nav-link text-dark fw-bold bg-light rounded"><i class="bi bi-person me-2"></i> Account Info</a>
          </li>
          <li class="nav-item">
            <a href="#" class="nav-link text-dark"><i class="bi bi-geo-alt me-2"></i> Saved Addresses</a>
          </li>
          <li class="nav-item">
            <a href="#" class="nav-link text-dark"><i class="bi bi-bag me-2"></i> Order History</a>
          </li>
          <li class="nav-item">
            <a href="#" class="nav-link text-danger"><i class="bi bi-box-arrow-right me-2"></i> Logout</a>
          </li>
        </ul>
      </div>
    </div>
    
    <div class="col-md-8">
      <div class="ks-card">
        <h3 class="h5 fw-bold mb-4 border-bottom pb-3">Personal Information</h3>
        <form>
          <div class="row g-3">
            <div class="col-md-6">
              <label class="form-label text-muted small">Full Name</label>
              <input type="text" class="form-control" value="John Doe">
            </div>
            <div class="col-md-6">
              <label class="form-label text-muted small">Phone Number</label>
              <input type="tel" class="form-control" value="+91 9876543210">
            </div>
            <div class="col-12">
              <label class="form-label text-muted small">Email Address</label>
              <input type="email" class="form-control" value="john.doe@example.com" disabled>
            </div>
          </div>
          <div class="mt-4 text-end">
            <button type="button" class="btn btn-ks-primary">Save Changes</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</div>
{% endblock %}
"""

with open("foodapp/templates/order_history.html", "w", encoding="utf-8") as f: f.write(hist_content)
with open("foodapp/templates/cook_profile.html", "w", encoding="utf-8") as f: f.write(cook_content)
with open("foodapp/templates/meal_detail.html", "w", encoding="utf-8") as f: f.write(meal_content)
with open("foodapp/templates/customer_profile.html", "w", encoding="utf-8") as f: f.write(cust_content)

print("Remaining templates updated.")
