# ShopEasy — Django Internship Week 2 Task

A demo e-commerce style website built with Django to practice templates,
template inheritance, static files, context data, template tags/filters,
and URL naming.

## Features Implemented

- Base template ('base.html') with template inheritance ('{% extends %}', '{% block %}')
- Reusable navbar and footer using '{% include %}'
- Pages: Home, About, Contact, Product List, Product Detail, Custom 404
- Product model with Django admin support
- Static files (CSS, JS, images) properly configured
- Media files (product images) configured with 'MEDIA_URL' / 'MEDIA_ROOT'
- Context data passed from views to templates
- Template tags used: '{% if %}', '{% for %}', '{% block %}', '{% extends %}', '{% include %}', '{% url %}'
- Template filters used: 'upper', 'title, 'truncatechars', 'date', 'pluralize`
- Named URLs used throughout (`{% url 'product_detail' product.pk %}')
- Templates organized under `templates/shop/`
- ## Project Structure
'''
internship/
├── internship/          # Project settings
├── shop/                 # Main app (models, views, urls)
├── templates/             # All HTML templates
│   ├── base.html
│   ├── 404.html
│   ├── includes/          # navbar, footer
│   └── shop/               # app-specific pages
├── static/                # CSS, JS, images
└── manage.py
​'''

## Setup & Run

bash
# Clone the repo
git clone <https://github.com/Ganesh-Sunar/shopeasy.git>
cd internship

# Create virtual environment
python -m venv venv
venv\Scripts\activate      # Windows

# Install dependencies
pip install django pillow

# Run migrations
python manage.py migrate

# Create superuser (to add products via admin)
python manage.py createsuperuser

# Run server
python manage.py runserver
Visit `http://127.0.0.1:8000/
## Screenshots

See 'Week2_Screenshots.pdf' for screenshots of all pages.

## Author
Internship Week 2 Task Submission.
