
/* =========================================================
   KitchenStation - Homemade Meals, Rendering, Search & Filters
   ========================================================= */

/* ---------- MENU DATA ---------- */

let MENU_DATA = [
  {id:1, name:'Homestyle Paneer Thali', restaurant:"Asha's Kitchen", cuisine:'North Indian', price:180, calories:480, nutrients:'Protein 22g • Carbs 55g', ingredients:'Paneer curry, 3 whole-wheat phulkas, yellow dal, steamed rice & fresh salad', img:'thali.jpg', nutri:'healthy', meal:'lunch', type:'heavy', spice:'normal'},
  {id:2, name:'Veg Dum Biryani', restaurant:"Riya's Home Kitchen", cuisine:'South Indian', price:150, calories:420, nutrients:'Carbs 60g • Protein 10g', ingredients:'Fragrant basmati rice layered with fresh vegetables and homemade whole spices, served with raita', img:'chickenbiryani.jpg', nutri:'protein', meal:'dinner', type:'heavy', spice:'normal'},
  {id:3, name:'Crispy Masala Dosa', restaurant:"Meera's Kitchen", cuisine:'South Indian', price:90, calories:280, nutrients:'Carbs 42g • Protein 6g', ingredients:'Fermented rice-lentil crepe filled with spiced potato bhaji, served with coconut chutney & sambar', img:'food5.jpg', nutri:'starchy', meal:'breakfast', type:'light', spice:'normal'},
  {id:4, name:'Homestyle Chicken Curry & Vade', restaurant:"Rahul's Kitchen", cuisine:'Maharashtrian', price:220, calories:520, nutrients:'Protein 32g • Carbs 40g', ingredients:'Slow-cooked country chicken in traditional Malvani masala with 2 multigrain kombdi vade', img:'kombdi_vade.jpg', nutri:'protein', meal:'dinner', type:'heavy', spice:'spicy'},
  {id:5, name:'Authentic Puran Poli Thali', restaurant:"Sunita's Kitchen", cuisine:'Maharashtrian', price:140, calories:460, nutrients:'Carbs 65g • Iron 8mg', ingredients:'2 soft puran polis stuffed with chana dal & jaggery, served with katachi amti and pure ghee', img:'puranpoli.jpg', nutri:'starchy', meal:'lunch', type:'heavy', spice:'not'},
  {id:6, name:'Punjabi Rajma Chawal', restaurant:"Asha's Kitchen", cuisine:'North Indian', price:140, calories:410, nutrients:'Protein 18g • Carbs 58g', ingredients:'Overnight-simmered red kidney beans in thick tomato-ginger gravy served with jeera rice', img:'varan_bhaat.jpg', nutri:'protein', meal:'lunch', type:'heavy', spice:'normal'},
  {id:7, name:'Aloo Paratha with Homemade Curd', restaurant:"Asha's Kitchen", cuisine:'North Indian', price:100, calories:340, nutrients:'Carbs 48g • Protein 8g', ingredients:'2 whole-wheat parathas stuffed with spiced potatoes, served with fresh churned butter and mango pickle', img:'food1.jpg', nutri:'starchy', meal:'breakfast', type:'light', spice:'normal'},
  {id:8, name:'Pithla Bhakri & Thecha', restaurant:"Aishwarya's Kitchen", cuisine:'Maharashtrian', price:140, calories:380, nutrients:'Protein 14g • Fiber 9g', ingredients:'Traditional gram-flour curry tempered with garlic, served with 2 jowar bhakris and spicy mirchi thecha', img:'pithla_bhakri.jpg', nutri:'protein', meal:'lunch', type:'heavy', spice:'spicy'},
  {id:9, name:'Steamed Idli Sambhar (4 pcs)', restaurant:"Riya's Home Kitchen", cuisine:'South Indian', price:90, calories:220, nutrients:'Carbs 44g • Protein 7g', ingredients:'Pillowy soft fermented rice-urad dal idlis served with vegetable-loaded sambar and coconut chutney', img:'food6.jpg', nutri:'healthy', meal:'breakfast', type:'light', spice:'not'},
  {id:10, name:'Kanda Poha with Roasted Peanuts', restaurant:"Meera's Kitchen", cuisine:'Maharashtrian', price:60, calories:210, nutrients:'Carbs 38g • Iron 4mg', ingredients:'Flattened rice tossed with caramelized onions, mustard seeds, green chillies, curry leaves & sev', img:'poha.jpg', nutri:'starchy', meal:'breakfast', type:'light', spice:'not'},
  {id:11, name:'Sabudana Khichdi with Dahi', restaurant:"Meera's Kitchen", cuisine:'Maharashtrian', price:80, calories:320, nutrients:'Carbs 58g • Energy Boost', ingredients:'Tapioca pearls sautéed with roasted crushed peanuts, cumin and green chillies, served with fresh curd', img:'sabudana_khichdi.jpg', nutri:'healthy', meal:'breakfast', type:'light', spice:'not'},
  {id:12, name:'Malvani Bombil Fry Thali', restaurant:"Malvani Kitchen", cuisine:'Maharashtrian', price:240, calories:440, nutrients:'Protein 30g • Healthy Fats', ingredients:'Crispy rava-crusted fresh fish, served with solkadhi, steamed rice, and phulkas', img:'bombil_fry.jpg', nutri:'protein', meal:'dinner', type:'heavy', spice:'spicy'},
  {id:13, name:'Varan Bhaat with Toop & Limboo', restaurant:"Sunita's Kitchen", cuisine:'Maharashtrian', price:130, calories:350, nutrients:'Carbs 62g • Protein 11g', ingredients:'Homestyle tuvar dal over fragrant steamed rice with a generous dollop of homemade cow ghee & lemon', img:'varan_bhaat.jpg', nutri:'healthy', meal:'lunch', type:'light', spice:'not'},
  {id:14, name:'Bharli Vangi & Chapati', restaurant:"Asha's Kitchen", cuisine:'Maharashtrian', price:160, calories:310, nutrients:'Fiber 8g • Protein 7g', ingredients:'Baby brinjals stuffed with roasted peanut, sesame & coconut masala, served with 3 soft chapatis', img:'bharli_vangi.jpg', nutri:'healthy', meal:'dinner', type:'heavy', spice:'normal'},
  {id:15, name:'Thalipeeth with Makkhan', restaurant:"Sunita's Kitchen", cuisine:'Maharashtrian', price:130, calories:330, nutrients:'Multigrain • Fiber 12g', ingredients:'Savory multigrain roasted flatbread made with bhajani flour, served with white butter & garlic chutney', img:'thalipeeth.jpg', nutri:'healthy', meal:'breakfast', type:'heavy', spice:'not'},
  {id:16, name:'Gujarati Kadhi & Moong Khichdi', restaurant:"Hansa's Kitchen", cuisine:'Gujarati', price:120, calories:310, nutrients:'Protein 13g • Easy Digest', ingredients:'Sweet & tangy yogurt kadhi paired with comforting moong dal khichdi, papad and pickle', img:'varan_bhaat.jpg', nutri:'healthy', meal:'dinner', type:'light', spice:'not'},
  {id:17, name:'Methi Thepla with Chunda (4 pcs)', restaurant:"Hansa's Kitchen", cuisine:'Gujarati', price:90, calories:260, nutrients:'Iron rich • Carbs 40g', ingredients:'Soft spiced whole-wheat flatbreads kneaded with fresh fenugreek leaves, served with sweet mango chunda', img:'thalipeeth.jpg', nutri:'healthy', meal:'breakfast', type:'light', spice:'not'},
  {id:18, name:'Khaman Dhokla (Plate)', restaurant:"Hansa's Kitchen", cuisine:'Gujarati', price:70, calories:180, nutrients:'Protein 8g • Low Fat', ingredients:'Steamed savory gram flour sponge cakes tempered with mustard, green chillies & fresh coriander', img:'patodi.jpg', nutri:'healthy', meal:'snack', type:'light', spice:'not'},
  {id:19, name:'Steamed Ukdiche Modak (2 pcs)', restaurant:"Sunita's Kitchen", cuisine:'Maharashtrian', price:90, calories:240, nutrients:'Jaggery & Coconut', ingredients:'Traditional steamed rice-flour dumplings filled with freshly grated coconut, jaggery and fragrant cardamom', img:'modak.jpg', nutri:'sweets', meal:'dessert', type:'light', spice:'not'},
  {id:20, name:'Kesar Pista Shrikhand (200g)', restaurant:"Sunita's Kitchen", cuisine:'Maharashtrian', price:110, calories:230, nutrients:'Calcium • Probiotics', ingredients:'Creamy hung curd infused with saffron strands, crushed pistachios, cardamom and natural sweetness', img:'shrikhand.jpg', nutri:'sweets', meal:'dessert', type:'light', spice:'not'},
  {id:21, name:'Hot Gulab Jamun (2 pcs)', restaurant:"Asha's Kitchen", cuisine:'North Indian', price:70, calories:250, nutrients:'Milk Solids', ingredients:'Soft homemade khoya dumplings fried in pure ghee and soaked in warm rose-infused sugar syrup', img:'gulab_jamun.jpg', nutri:'sweets', meal:'dessert', type:'light', spice:'not'},
  {id:22, name:'Authentic Solkadhi (300ml)', restaurant:"Malvani Kitchen", cuisine:'Maharashtrian', price:60, calories:75, nutrients:'Natural Digestive', ingredients:'Refreshing digestive drink prepared with fresh coconut milk, wild kokum extract, garlic and green chillies', img:'solkadhi.jpg', nutri:'healthy', meal:'lunch', type:'liquid', spice:'not'},
  {id:23, name:'Aluvadi (Colocasia Rolls - 6 pcs)', restaurant:"Sunita's Kitchen", cuisine:'Maharashtrian', price:80, calories:210, nutrients:'Fiber • Iron', ingredients:'Colocasia leaves layered with spiced gram flour paste, steamed and crisped with sesame seeds', img:'aluvadi.jpg', nutri:'healthy', meal:'snack', type:'light', spice:'normal'},
  {id:24, name:'Homemade Samosas with Chutney (2 pcs)', restaurant:"Meera's Kitchen", cuisine:'North Indian', price:50, calories:260, nutrients:'Carbs 35g', ingredients:'Crispy flaky pastry stuffed with seasoned potatoes, green peas and roasted whole spices, served with tamarind chutney', img:'samosa.jpg', nutri:'starchy', meal:'snack', type:'light', spice:'normal'},
  {id:25, name:'Fresh Pav Bhaji (Homestyle Butter)', restaurant:"Meera's Kitchen", cuisine:'Maharashtrian', price:120, calories:390, nutrients:'Veg loaded • Protein 9g', ingredients:'Mashed garden vegetables cooked with home-blended spices and pure butter, served with 2 warm toasted pavs', img:'pavbhaji.jpg', nutri:'starchy', meal:'dinner', type:'heavy', spice:'normal'}
];

// Use real Django database meals when supplied by menu.html
const databaseMenuElement = document.getElementById('menu-data');
if(databaseMenuElement) {
  try {
    const databaseMeals = JSON.parse(databaseMenuElement.textContent);
    if (Array.isArray(databaseMeals)) {
      MENU_DATA = databaseMeals;
    }
  } catch (error) {
    console.error('Unable to read database menu data:', error);
  }
}

/* ---------- OFFERS ---------- */
/* itemId must match an ID in MENU_DATA. */
const OFFER_DATA = [
  {id:1, discountPercent:40, itemId:19}, // Ukdiche Modak
  {id:2, discountPercent:20, itemId:18}, // Khaman Dhokla
  {id:3, discountPercent:25, itemId:16}, // Gujarati Kadhi & Moong Khichdi
  {id:4, discountPercent:15, itemId:3},  // Masala Dosa
  {id:5, discountPercent:30, itemId:12}, // Malvani Bombil Fry Thali
  {id:6, discountPercent:17, itemId:21}  // Gulab Jamun
];

/* ---------- SHARED STATE ---------- */

let activeSearchQuery = '';
let activeCategory = 'all';

/* ---------- HELPERS ---------- */

function el(tag, cls) {
  const element = document.createElement(tag);

  if (cls) {
    element.className = cls;
  }

  return element;
}

function normalizeText(value) {
  return String(value || '').trim().toLowerCase().replace(/\s+/g, ' ');
}

function getMealImagePath(path) {
  if (!path) {
    return '/static/foodapp/images/food5.jpg';
  }

  if (path.startsWith('/') || /^https?:\/\//i.test(path)) {
    return path;
  }

  return `/static/foodapp/images/${path}`;
}

/* ---------- FEATURED MEALS ---------- */

function renderFeatured() {
  // Support either existing featured-meal container ID.
  const list =
    document.getElementById('mealsList') ||
    document.getElementById('featuredList');

  if (!list) return;

  const featuredIds = [1, 3, 5, 21];
  const featuredMeals = MENU_DATA.filter(item =>
    featuredIds.includes(item.id)
  );

  list.innerHTML = '';

  featuredMeals.forEach(item => {
    const col = el('div', 'col-md-6 col-lg-3');
    const card = el('article', 'ks-card h-100 d-flex flex-column');

    const img = el('img', 'ks-meal-img');
    img.src = getMealImagePath(item.img);
    img.alt = item.name;
    img.loading = 'lazy';

    const title = el('h3', 'h5 fw-bold mb-2');
    title.textContent = item.name;

    const cook = el('p', 'text-muted small mb-2');
    cook.textContent = `By ${item.restaurant}`;

    const cuisineLine = el('p', 'mb-3');
    const cuisineBadge = el('span', 'ks-badge');
    cuisineBadge.textContent = item.cuisine;
    cuisineLine.appendChild(cuisineBadge);

    const bottom = el(
      'div',
      'mt-auto pt-3 border-top d-flex justify-content-between align-items-center'
    );

    const price = el('strong', 'fs-5');
    price.textContent = `₹${item.price}`;

    const viewLink = el('a', 'btn btn-ks-secondary btn-sm');
    viewLink.href = '/menu/';
    viewLink.textContent = 'View Meals';

    bottom.append(price, viewLink);
    card.append(img, title, cook, cuisineLine, bottom);
    col.appendChild(card);
    list.appendChild(col);
  });
}

/* ---------- MENU RENDERING ---------- */

function renderMenu(data = MENU_DATA) {
  const container = document.getElementById('menuGrid');

  if (!container) return;

  container.innerHTML = '';

  if (!data.length) {
    const emptyColumn = el('div', 'col-12');
    const message = el('div', 'ks-card text-center p-4');

    const heading = el('h3', 'h5 fw-bold');
    heading.textContent = 'No meals found';

    const description = el('p', 'text-muted mb-0');
    description.textContent =
      'Try a different search term or adjust your filters.';

    message.append(heading, description);
    emptyColumn.appendChild(message);
    container.appendChild(emptyColumn);
    return;
  }

  data.forEach(item => {
    const col = el('div', 'col-md-4 col-sm-6');

    const card = el('article', 'ks-card h-100 d-flex flex-column');

    const img = el('img', 'ks-meal-img');
    img.src = getMealImagePath(item.img);
    img.alt = item.name;
    img.loading = 'lazy';

    const title = el('h3', 'h5 fw-bold mb-1');
    title.textContent = item.name;

    const cook = el('p', 'text-muted small mb-1');
    cook.textContent = `By ${item.restaurant || 'Local Home Cook'}`;

    const tags = el('div', 'mb-2');

    const cuisineTag = el('span', 'ks-badge me-1');
    cuisineTag.textContent = item.cuisine || item.meal;

    const dietLabels = {
      healthy: 'Healthy',
      protein: 'Protein Rich',
      starchy: 'Homestyle',
      sweets: 'Sweet'
    };

    const dietTag = el('span', 'ks-badge');
    dietTag.textContent = dietLabels[item.nutri] || 'Homestyle';

    tags.append(cuisineTag, dietTag);

    const description = el('p', 'small mb-3 text-muted');
    description.textContent = item.ingredients;

    const bottom = el(
      'div',
      'mt-auto pt-3 border-top d-flex justify-content-between align-items-center'
    );

    const price = el('strong', 'fs-5');
    price.textContent = `₹${item.price}`;

    const addButton = el('button', 'btn btn-ks-primary btn-sm');
    addButton.type = 'button';
    addButton.textContent = 'Add';

    addButton.addEventListener('click', () => {
      if (typeof addToCart === 'function') {
        addToCart({
          id: item.id,
          name: item.name,
          price: item.price,
          img: item.img
        });
      } else {
        console.warn(
          'addToCart() is unavailable. Check that cart.js is loaded.'
        );
      }
    });

    bottom.append(price, addButton);
    card.append(img, title, cook, tags, description, bottom);
    col.appendChild(card);
    container.appendChild(col);
  });
}

/* ---------- HOME COOKS / RESTAURANT GRID ---------- */

function renderRestaurantsGrid() {
  const grid = document.getElementById('restaurantGrid');

  if (!grid) return;

  const cooks = [
    {
      name: "Asha's Kitchen",
      cuisine: 'North Indian',
      location: 'Andheri West',
      rating: 4.8,
      desc: 'Specializes in homemade thalis and parathas.',
      img: 'thali.jpg'
    },
    {
      name: "Riya's Home Kitchen",
      cuisine: 'South Indian',
      location: 'Powai',
      rating: 4.7,
      desc: 'Traditional South Indian meals with homemade chutneys.',
      img: 'food5.jpg'
    },
    {
      name: "Meera's Kitchen",
      cuisine: 'Homestyle Snacks',
      location: 'Bandra',
      rating: 4.9,
      desc: 'Wholesome everyday meals and snacks prepared with care.',
      img: 'misalpav.jpg'
    },
    {
      name: "Sunita's Kitchen",
      cuisine: 'Maharashtrian',
      location: 'Dadar',
      rating: 4.9,
      desc: 'Traditional Maharashtrian delicacies and family recipes.',
      img: 'puranpoli.jpg'
    }
  ];

  grid.innerHTML = '';

  cooks.forEach(cook => {
    const col = el('div', 'col-md-6 col-lg-4');
    const card = el('article', 'ks-card h-100 d-flex flex-column text-center');

    const imageWrapper = el(
      'div',
      'mb-3 d-flex justify-content-center'
    );

    const img = el('img', 'ks-avatar');
    img.src = getMealImagePath(cook.img);
    img.alt = cook.name;
    img.loading = 'lazy';
    imageWrapper.appendChild(img);

    const title = el('h3', 'h4 fw-bold mb-1');
    title.textContent = cook.name;

    const location = el('p', 'text-muted small mb-2');
    location.textContent = `⌖ ${cook.location}`;

    const tags = el('div', 'mb-2');
    const cuisineTag = el('span', 'ks-badge');
    cuisineTag.textContent = cook.cuisine;
    tags.appendChild(cuisineTag);

    const description = el('p', 'small mb-3 text-muted');
    description.textContent = cook.desc;

    const bottom = el(
      'div',
      'mt-auto pt-3 border-top d-flex justify-content-between align-items-center'
    );

    const rating = el('span', 'ks-badge-accent ks-badge');
    rating.textContent = `★ ${cook.rating}`;

    const link = el('a', 'btn btn-ks-secondary btn-sm');
    link.href = '/menu/';
    link.textContent = 'View Menu';

    bottom.append(rating, link);
    card.append(imageWrapper, title, location, tags, description, bottom);
    col.appendChild(card);
    grid.appendChild(col);
  });
}

/* ---------- OFFER RENDERING ---------- */

function renderOffers() {
  // Support common container IDs; do nothing if the current page has none.
  const container =
    document.getElementById('offersGrid') ||
    document.getElementById('offersList') ||
    document.getElementById('offersContainer') ||
    document.getElementById('offers-grid') ||
    document.querySelector('[data-offers-grid]');

  if (!container) return;

  container.innerHTML = '';

  OFFER_DATA.forEach(offer => {
    const item = MENU_DATA.find(meal => meal.id === offer.itemId);

    // Ignore offers whose item ID no longer exists.
    if (!item) return;

    const discountedPrice = Math.round(
      item.price * (1 - offer.discountPercent / 100)
    );

    const col = el('div', 'col-md-6 col-lg-4');
    const card = el('article', 'ks-card h-100 d-flex flex-column');

    const image = el('img', 'ks-meal-img');
    image.src = getMealImagePath(item.img);
    image.alt = item.name;
    image.loading = 'lazy';

    const offerBadge = el('span', 'ks-badge-accent ks-badge mb-2');
    offerBadge.textContent = `${offer.discountPercent}% OFF`;

    const title = el('h3', 'h5 fw-bold mb-1');
    title.textContent = item.name;

    const cook = el('p', 'text-muted small mb-2');
    cook.textContent = `By ${item.restaurant}`;

    const description = el('p', 'small text-muted mb-3');
    description.textContent = item.ingredients;

    const priceRow = el(
      'div',
      'mt-auto pt-3 border-top d-flex justify-content-between align-items-center'
    );

    const prices = el('div');

    const originalPrice = el('span', 'text-muted text-decoration-line-through me-2');
    originalPrice.textContent = `₹${item.price}`;

    const salePrice = el('strong', 'fs-5');
    salePrice.textContent = `₹${discountedPrice}`;

    prices.append(originalPrice, salePrice);

    const viewLink = el('a', 'btn btn-ks-primary btn-sm');
    viewLink.href = '/menu/';
    viewLink.textContent = 'View Meals';

    priceRow.append(prices, viewLink);
    card.append(image, offerBadge, title, cook, description, priceRow);
    col.appendChild(card);
    container.appendChild(col);
  });
}

/* ---------- FILTER COLLECTION ---------- */

function gatherFilters() {
  const checkedValues = name =>
    Array.from(
      document.querySelectorAll(`input[name="${name}"]:checked`)
    ).map(input => input.value);

  const selectedSort = document.querySelector(
    'input[name="priceSort"]:checked'
  );

  return {
    nutri: checkedValues('nutri'),
    meal: checkedValues('meal'),
    type: checkedValues('type'),
    spice: checkedValues('spice'),
    priceSort: selectedSort ? selectedSort.value : null
  };
}

/* ---------- CATEGORY MATCHING ---------- */

function matchesCategory(item, category) {
  const normalizedCategory = normalizeText(category);
  const cuisine = normalizeText(item.cuisine);
  const meal = normalizeText(item.meal);
  const nutrition = normalizeText(item.nutri);

  switch (normalizedCategory) {
    case '':
    case 'all':
      return true;

    case 'north indian':
    case 'south indian':
    case 'maharashtrian':
    case 'gujarati':
      return cuisine === normalizedCategory;

    case 'healthy / diet':
    case 'healthy':
    case 'diet':
      return nutrition === 'healthy' || item.type === 'light';

    case 'snacks':
    case 'snack':
      return meal === 'snack';

    case 'sweets':
    case 'sweet':
      return meal === 'dessert' || nutrition === 'sweets';

    default:
      // Unknown button labels do not accidentally exclude all meals.
      return true;
  }
}

/* ---------- COMBINED FILTERING ---------- */

function getFilteredMeals() {
  const filters = gatherFilters();
  const query = normalizeText(activeSearchQuery);

  let results = MENU_DATA.filter(item => {
    const matchesSearch = !query || [
      item.name,
      item.restaurant,
      item.cuisine,
      item.ingredients,
      item.meal,
      item.nutri,
      item.nutrients
    ].some(value => normalizeText(value).includes(query));

    const matchesNutrition =
      !filters.nutri.length || filters.nutri.includes(item.nutri);

    const matchesMeal =
      !filters.meal.length || filters.meal.includes(item.meal);

    const matchesType =
      !filters.type.length || filters.type.includes(item.type);

    const matchesSpice =
      !filters.spice.length || filters.spice.includes(item.spice);

    return (
      matchesSearch &&
      matchesCategory(item, activeCategory) &&
      matchesNutrition &&
      matchesMeal &&
      matchesType &&
      matchesSpice
    );
  });

  if (filters.priceSort === 'asc') {
    results.sort((a, b) => a.price - b.price);
  } else if (filters.priceSort === 'desc') {
    results.sort((a, b) => b.price - a.price);
  }

  return results;
}

function applyFilters() {
  renderMenu(getFilteredMeals());
}

/* ---------- SEARCH ---------- */

function initSearch() {
  const searchInput = document.getElementById('mealSearchInput');
  const searchButton = document.getElementById('searchBtn');

  if (!searchInput) return;

  const search = () => {
    activeSearchQuery = searchInput.value;
    applyFilters();
  };

  searchInput.addEventListener('input', search);

  if (searchButton) {
    searchButton.addEventListener('click', search);
  }
}

/* ---------- CATEGORY BUTTONS ---------- */

function initCategoryFilters() {
  const container = document.getElementById('categoryFilters');

  if (!container) return;

  const buttons = Array.from(container.querySelectorAll('button'));

  buttons.forEach(button => {
    button.addEventListener('click', () => {
      const label = normalizeText(button.textContent);
      activeCategory = label || 'all';

      buttons.forEach(otherButton => {
        otherButton.classList.remove('btn-ks-primary');
        otherButton.classList.add('btn-outline-secondary');
        otherButton.setAttribute('aria-pressed', 'false');
      });

      button.classList.remove('btn-outline-secondary');
      button.classList.add('btn-ks-primary');
      button.setAttribute('aria-pressed', 'true');

      applyFilters();
    });
  });
}

/* ---------- DROPDOWN FILTER CONTROLS ---------- */

function initFilterDropdowns() {
  const buttons = document.querySelectorAll('.filter-btn');

  buttons.forEach(button => {
    button.addEventListener('click', () => {
      const targetId = button.getAttribute('data-target');
      const options = targetId
        ? document.getElementById(targetId)
        : null;

      if (!options) return;

      document.querySelectorAll('.filter-options').forEach(option => {
        if (option !== options) {
          option.classList.remove('show');
        }
      });

      document.querySelectorAll('.filter-btn').forEach(otherButton => {
        if (otherButton !== button) {
          otherButton.classList.remove('active');
        }
      });

      button.classList.toggle('active');
      options.classList.toggle('show');
    });
  });
}

/* ---------- APPLY / CLEAR FILTER BUTTONS ---------- */

function initApplyAndClearButtons() {
  const applyButton = document.getElementById('applyFilters');
  const clearButton = document.getElementById('clearFilters');

  if (applyButton) {
    applyButton.addEventListener('click', event => {
      event.preventDefault();
      applyFilters();
    });
  }

  if (clearButton) {
    clearButton.addEventListener('click', event => {
      event.preventDefault();

      document
        .querySelectorAll(
          'input[name="nutri"], input[name="meal"], input[name="type"], input[name="spice"], input[name="priceSort"]'
        )
        .forEach(input => {
          input.checked = false;
        });

      const searchInput = document.getElementById('mealSearchInput');

      if (searchInput) {
        searchInput.value = '';
      }

      activeSearchQuery = '';
      activeCategory = 'all';

      const categoryContainer = document.getElementById('categoryFilters');

      if (categoryContainer) {
        categoryContainer.querySelectorAll('button').forEach(button => {
          const isAll = normalizeText(button.textContent) === 'all';

          button.classList.toggle('btn-ks-primary', isAll);
          button.classList.toggle('btn-outline-secondary', !isAll);
          button.classList.toggle('active', isAll);
          button.setAttribute('aria-pressed', String(isAll));
        });
      }

      applyFilters();
    });
  }
}

/* ---------- INITIALIZATION ---------- */

document.addEventListener('DOMContentLoaded', () => {
  initFilterDropdowns();
  initSearch();
  initCategoryFilters();
  initApplyAndClearButtons();

  if (document.getElementById('menuGrid')) {
    renderMenu(getFilteredMeals());
  }

  renderFeatured();
  renderRestaurantsGrid();
  renderOffers();
});