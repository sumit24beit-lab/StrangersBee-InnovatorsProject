# KitchenStation

**A home-cooked food marketplace bringing local cooks and customers together.**

KitchenStation is a Django web application where customers can discover meals prepared by home cooks, place Cash on Delivery (COD) orders, and share feedback about their food experiences. Home cooks can present their kitchens, manage meal listings, and handle incoming orders through dedicated account workflows.

---

## 1. Project Overview

### The problem

Customers looking for homemade food often have no convenient way to discover local home cooks, compare available meals, or order from them through a single experience. At the same time, independent cooks need a practical way to introduce their kitchens and manage their menus and orders.

### The approach

KitchenStation brings both sides together in one marketplace. Customers can browse available meals and verified home cooks, maintain delivery addresses, and place orders. Home cooks can maintain a kitchen profile, publish and update meals, and process order status changes. Reviews and food stories add a customer perspective to the marketplace.

| Audience | What KitchenStation provides |
| --- | --- |
| Customers | Meal and kitchen discovery, saved delivery addresses, COD ordering, order history, and food reviews |
| Home cooks | Kitchen profiles, meal-listing tools, an order dashboard, order status management, and sales summaries |

The platform is designed around the relationship between a customer and a home kitchen—not simply a generic restaurant checkout flow.

---

## 2. Technology Stack

Badges reflect technologies present in the project source and configuration.

![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.2.6-092E20?logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-4169E1?logo=postgresql&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-Templates-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-Styles-1572B6?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-Frontend-F7DF1E?logo=javascript&logoColor=222222)
![Pillow](https://img.shields.io/badge/Pillow-Image%20uploads-5A3E85)

| Technology | Use in KitchenStation |
| --- | --- |
| Python and Django | Server-side application, routing, authentication, forms, ORM, and tests |
| PostgreSQL | Relational database configured as the Django default database backend |
| HTML5 and CSS3 | Django-rendered pages and application styling |
| JavaScript | Interactive browser-side functionality, including cart and order submission behavior |
| Pillow | Image-field support for meal images and customer review photos |

---

## 3. Key Features

### Customer features

- Register and sign in as a customer; authentication uses Django's built-in user system.
- Maintain a customer profile and add, edit, and delete personal delivery addresses.
- Access customer order history.
- Place an order using a saved address and Cash on Delivery.

### Home cook features

- Register a home-cook account with kitchen name, locality, city, cuisine specialty, and kitchen description.
- Manage a kitchen profile and meal listings, including descriptions, ingredients, price, category, image, and food attributes.
- Toggle meal availability.
- View a dashboard with meal and order summaries, manage orders, and progress supported order statuses.
- View sales summaries based on delivered orders. Payout tracking is not configured.

### Food discovery and ordering

- Browse verified home cooks and their profiles.
- Browse available meals from verified kitchens and view meal details.
- Build a cart and submit an order. The server validates the selected meal, its current availability, the customer's saved address, and the order quantity rather than trusting client-provided prices.
- Place separate orders for meals from different home kitchens; a single order is restricted to one kitchen.
- Use Cash on Delivery. Online payment is not available in the current implementation.
- Order totals include a 5% tax and delivery charge rules implemented in the order model.

### Reviews and food stories

- Customers can submit a rating, written review, and optional photo for meals they have received.
- The review form only offers meals associated with delivered orders.
- Customers can submit general feedback or complaints, optionally linked to one of their orders.
- Home cooks can see reviews for their own meals.

### Account management

- Signup validates account details and password confirmation, then creates a customer or home-cook profile according to the selected role.
- Role-based view guards separate customer workflows from cook-management pages.
- Home-cook profiles start unverified; public discovery and meal ordering are limited to verified kitchens.

### Public website

- Public landing and about pages, alongside menu, home-cook, offer, contact, FAQ, and careers pages.
- Dedicated account, customer, and home-cook views use Django templates and application static assets.

---

## 4. How KitchenStation Works

### Customer workflow

1. Create a customer account and sign in.
2. Browse meals and verified home cooks, then add meals from one kitchen to the cart.
3. Maintain a delivery address and provide a valid mobile number during checkout.
4. Submit the order using Cash on Delivery. The application validates the items and calculates prices and totals on the server.
5. Review the order in order history. After the order is delivered, submit a meal review or share feedback.

### Home cook workflow

1. Create a home-cook account with kitchen details. A new cook profile is unverified by default.
2. Complete or update the kitchen profile and wait for verification before the kitchen appears in public discovery and orderable menus.
3. Add meals, describe ingredients and meal attributes, set prices, upload images, and control availability.
4. Use the cook dashboard and orders page to review incoming orders and move them through permitted statuses.
5. Review sales summaries, which count delivered order items for the cook. Payout processing is not configured.

---

## 5. Application Architecture

KitchenStation is a Django project organized into four applications. `oneclick` remains the internal Python package containing the Django project configuration; the product documented here is KitchenStation.

| Application | Responsibility |
| --- | --- |
| `accounts` | Customer and home-cook signup, login and logout, account-role profiles, and signup/login forms |
| `foodapp` | Customer profiles and addresses, meal and order data, ordering, order history, reviews, feedback, and marketplace pages |
| `home_cooks` | Home-cook profiles, public cook and meal discovery, meal management, cook dashboards, order management, and earnings summaries |
| `core` | Public landing and about pages |
| `oneclick` | Django settings, root URL configuration, and WSGI/ASGI entry points |

### Repository layout

```text
.
├── accounts/
│   ├── migrations/
│   ├── templates/accounts/
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── core/
│   ├── migrations/
│   ├── templates/core/
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── foodapp/
│   ├── migrations/
│   ├── static/foodapp/       # CSS, JavaScript, and image assets
│   ├── templates/            # Customer and public pages
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── home_cooks/
│   ├── migrations/
│   ├── static/
│   ├── templates/home_cooks/
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── oneclick/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── manage.py
├── .gitignore
└── README.md
```

---

## 6. Database Design

The project configures Django's default database engine as PostgreSQL. Django models and migrations define the relational schema; the app's business objects are split between customer/order functionality and home-cook/menu functionality.

| Model | Application | Purpose and relationships |
| --- | --- | --- |
| `AccountProfile` | `accounts` | One-to-one extension of Django's user with a `customer` or `home_cook` role |
| `CustomerProfile` | `foodapp` | Customer contact/profile details; associated with addresses, orders, reviews, and feedback |
| `Address` | `foodapp` | A customer's saved delivery address; each address belongs to one customer |
| `HomeCook` | `home_cooks` | One-to-one link to a Django user, with kitchen identity, location, cuisine, description, and verification state |
| `Menu` | `foodapp` | A meal belonging to one home cook, with price, category, ingredients, image, availability, and food attributes |
| `Order` | `foodapp` | Customer order linked to a delivery address; stores status, payment mode, and calculated totals |
| `OrderItem` | `foodapp` | Line item belonging to an order and referencing a menu meal; captures name, price, and quantity at order time |
| `FoodReview` | `foodapp` | A customer's rating/review for a meal, with an optional image |
| `CustomerFeedback` | `foodapp` | A customer feedback or complaint, optionally linked to an order |
| `Offer` | `foodapp` | A discount record associated with a menu item |

An order contains one or more order items. Each meal belongs to a home cook, and the checkout logic requires all items in a customer order to belong to the same kitchen. An order is linked to the customer's chosen address, and order totals are calculated from stored meal prices, tax, and applicable delivery charges.

---

## 7. Installation and Local Setup

### Prerequisites

- Python 3.11 or later.
- PostgreSQL running locally.
- A PostgreSQL database and user that the application can access. The database user also needs permission to create a test database when running Django's test suite.

There is currently no `requirements.txt` or dependency lock file. The commands below install the framework version specified in the Django settings along with the PostgreSQL driver and image-field support used by the source.

### 1. Clone the repository

```bash
git clone https://github.com/sumit24beit-lab/StrangersBee-InnovatorsProject.git
cd StrangersBee-InnovatorsProject
```

### 2. Create and activate a virtual environment

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows PowerShell**

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install the application dependencies

```bash
python -m pip install --upgrade pip
python -m pip install "Django==5.2.6" "psycopg[binary]" Pillow
```

### 4. Configure PostgreSQL

The current `oneclick/settings.py` selects PostgreSQL and contains the database connection configuration directly; the repository does not implement environment-variable-based database configuration. Create a local database and configure the `DATABASES` values in your local settings to match your PostgreSQL instance. Do not commit credentials or use development settings and secrets in a production environment.

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser. The project is configured for local development and does not document a production deployment.

---

## 8. Testing

The project includes Django tests in `accounts`, `foodapp`, and `home_cooks`; `core/tests.py` currently contains no test cases. The tests cover account flows, customer address and order behavior, cook and meal management, order calculations, and order status/earnings logic. No formal coverage percentage is configured or claimed.

With PostgreSQL configured and the virtual environment active, run the full suite with:

```bash
python manage.py test
```

Run an individual app's tests with, for example:

```bash
python manage.py test foodapp
```

---

## 9. Project Screenshots

No dedicated application screenshots are included in the repository. The existing image assets are application media and design assets rather than README-ready screenshots.

---

## 10. Future Enhancements

The following are potential improvements, not features currently claimed as implemented:

- Location-aware home-cook discovery within a configurable 1–5 km radius.
- A clearer order confirmation experience after checkout.
- A persistent order-tracking indicator in the customer experience.
- Real map integration and delivery-location tracking.
- Online payments and cook payout tracking.

---

## 11. Team and Contributions

The repository's existing project attribution identifies **Team StrangersBee Innovators**. No individual author list, contribution policy, or license information is specified here.

For contributions, discuss the proposed change with the project team before opening a pull request. Keep changes focused, preserve role boundaries and order validation, and add or update Django tests when behavior changes.

---
