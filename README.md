# My First Django Project

A fully functional Django-based e-commerce web application with user authentication, product management, shopping cart, and Stripe payment integration.

---

## Features

- **User Authentication**
  - Sign up and login functionality
  - Password validation and error handling
  - Superuser/admin support

- **E-Commerce Functionality**
  - Product management (add products with name, price, and image)
  - Shopping cart for users
  - Separate views for men’s and women’s categories
  - Checkout and payment via Stripe

- **Pages**
  - Home
  - About Us
  - Account Management
  - Cart / eCart
  - Feedback
  - Success / Cancel pages for payment flow

- **Stripe Integration**
  - Secure payment handling
  - Checkout session creation
  - Redirect to success or cancel page after payment

---

## Technologies Used

- **Backend:** Python, Django 4.x
- **Database:** MySQL / MariaDB(xampp)
- **Frontend:** HTML, CSS, Django Templates
- **Payment:** Stripe API
- **Other Packages:**
  - `django.contrib.auth` for authentication
  - `stripe` Python library for payments
  - CSRF protection for secure requests

---