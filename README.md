# Dream House - Real Estate Platform

## 📋 Project Overview

**Dream House** is a full-featured real estate web application built with **Django** that enables users to browse, buy, rent, and sell properties. The platform provides an intuitive interface for property listings, agent management, and user interactions with responsive design for mobile, tablet, and desktop devices.

### Main Objective
Create a comprehensive real estate marketplace where:
- Users can **browse properties** (Flats, Houses, Shops, Plots, Land)
- Users can **buy, rent, or sell** properties
- **Real estate agents** can manage and showcase properties
- **Mobile-responsive design** ensures seamless experience across all devices
- **Smooth dropdown navigation** works reliably on touch devices

---

## ✨ Features

### Property Management
- ✅ View properties by category (Flat, House, Shop, Plot, Land)
- ✅ Detailed property listings with images, pricing, and specifications
- ✅ Featured properties showcase
- ✅ Property filtering options (Buy, Rent, Sell)

### User Features
- ✅ User authentication (Sign In / Register)
- ✅ User dashboard
- ✅ Contact information management
- ✅ Request property details

### Agent Management
- ✅ Professional agents showcase
- ✅ Agent profiles with contact details
- ✅ Agent ratings and reviews

### Navigation & UI
- ✅ Fixed navbar with dropdown menus
- ✅ Mobile-responsive hamburger menu
- ✅ Touch-friendly dropdown toggles (fixed for mobile/tablet)
- ✅ Image carousels for property galleries
- ✅ Interactive animations with AOS (Animate On Scroll)

### Pages
- 🏠 **Home** - Landing page with featured properties
- 📖 **About** - About Us, About Our Action, Join Us
- 🏢 **Buying** - Browse properties to buy (Flat, House, Apartment)
- 💰 **Selling** - Properties for sale
- 🔑 **Renting** - Available rental properties
- 👥 **Agents** - Professional real estate agents
- 📞 **Contact** - Contact information and form
- 📋 **Policy** - Privacy & Terms conditions

---

## 🛠 Technologies & Tools Used

### Backend
- **Django 5.0.4** - Web framework
- **Python 3.12** - Programming language
- **SQLite** - Database (default Django database)

### Frontend
- **HTML5** - Markup
- **CSS3** - Styling
- **Bootstrap 4.6.2** - Responsive UI framework
- **jQuery 3.5.1** - JavaScript library

### Frontend Libraries
- **Popper.js** - Positioning library for dropdowns
- **AOS (Animate On Scroll)** - Scroll animations
- **Pillow (PIL)** - Image processing

### Development Tools
- **Virtual Environment** (venv) - Python environment isolation
- **pip** - Package manager

### External CDNs
- Bootstrap CSS/JS
- jQuery
- Popper.js
- AOS
- Font libraries

---

## 📦 Installation & Setup

### Prerequisites
- Python 3.12+
- pip (Python package manager)
- Virtual environment (venv)

### Step 1: Create Virtual Environment
```bash
# Navigate to your project directory
cd c:\Users\abhis\OneDrive\Desktop\Env\myEnv

# Create virtual environment (if not already created)
python -m venv .

# Activate virtual environment
.\Scripts\activate
```

### Step 2: Install Dependencies
```bash
pip install django==5.0.4
pip install pillow
pip install sqlparse
```

### Step 3: Navigate to Project
```bash
cd realestate
```

### Step 4: Apply Migrations
```bash
python manage.py migrate
```

### Step 5: Create Superuser (Admin Account)
```bash
python manage.py createsuperuser
# Follow prompts to create admin account
```

---

## 🚀 Running the Project

### Start Development Server
```bash
python manage.py runserver
```

**Output:**
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### Access the Application
- **Main Site**: [http://127.0.0.1:8000/hom](http://127.0.0.1:8000/hom)
- **Admin Panel**: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

## 📁 Project Structure

```
realestate/
├── myapp/                      # Main Django app
│   ├── migrations/             # Database migrations
│   ├── static/                 # Static files (CSS, JS, images)
│   ├── templates/              # HTML templates
│   │   ├── newpage.html        # Home page
│   │   ├── NavBar.html         # Navigation bar (included)
│   │   ├── Footer.html         # Footer (included)
│   │   ├── Home.html           # Home view
│   │   ├── About_*.html        # About pages
│   │   ├── Buy*.html           # Buy property pages
│   │   ├── Agent*.html         # Agent pages
│   │   └── ...                 # Other templates
│   ├── admin.py                # Admin configurations
│   ├── models.py               # Database models
│   ├── views.py                # View functions
│   ├── urls.py                 # App-level URLs
│   └── tests.py                # Tests
├── realestate/                 # Project configuration
│   ├── settings.py             # Django settings
│   ├── urls.py                 # Project-level URLs
│   ├── wsgi.py                 # WSGI config
│   └── asgi.py                 # ASGI config
├── media/                      # User uploaded files
├── manage.py                   # Django management script
├── db.sqlite3                  # SQLite database
└── README.md                   # This file
```

---

## 🔧 Key Configurations

### Database
- **Type**: SQLite (db.sqlite3)
- **Location**: `realestate/db.sqlite3`

### Media Files
- **Upload Directory**: `media/uploadedFiles/`
- **Configuration**: `MEDIA_ROOT` and `MEDIA_URL` in settings.py

### Templates Directory
- **Path**: `myapp/templates/`
- **Config**: Set in `TEMPLATES['DIRS']` in settings.py

---

## 📱 Mobile & Tablet Support

### Responsive Features
- ✅ Mobile hamburger menu (Bootstrap navbar-toggler)
- ✅ Touch-friendly dropdown toggles (custom JavaScript fix)
- ✅ Responsive Bootstrap grid system
- ✅ Flexible images and media

### Fixed Dropdown Issue
A custom JavaScript fix was implemented to ensure dropdown menus work reliably on mobile/tablet devices:

```javascript
$(document).on('click', '[data-toggle="dropdown"]', function(e) {
  e.preventDefault();
  e.stopPropagation();
  $(this).dropdown('toggle');
});
```

This fix is included in:
- `NavBar.html` (for included pages)
- All individual template files with scripts

---

## 🌐 URL Routes (Sample)

| Route | View | Template | Description |
|-------|------|----------|-------------|
| `/hom` | `newpage` | newpage.html | Home page |
| `/abtac` | About | About_actuion.html | About our action |
| `/abtus` | About | About_Join_Us.html | Join us page |
| `/byflt` | BuyFlat | BuyFlat.html | Buy flat properties |
| `/byapp` | BuyApartment | BuyApartment.html | Buy apartments |
| `/sellft` | SellFlat | SellFlat.html | Sell flat properties |
| `/sell` | SellHouse | SellHouse.html | Sell houses |
| `/cont` | Contact | Contact_Info.html | Contact information |
| `/sin` | Login | (Auth) | Sign in |

---

## 🐛 Troubleshooting

### Issue: Dropdown not working on mobile
**Solution**: Ensure all template files include the dropdown fix JavaScript (already applied to all files).

### Issue: Static files not loading
**Solution**: Run `python manage.py collectstatic` and check `STATIC_ROOT` settings.

### Issue: Database errors
**Solution**: Run `python manage.py migrate` to apply all migrations.

### Issue: Port already in use
**Solution**: Use `python manage.py runserver 8001` to run on different port.

---

## 📚 Common Commands

```bash
# Start server
python manage.py runserver

# Create superuser
python manage.py createsuperuser

# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create new app
python manage.py startapp appname

# Open Django shell
python manage.py shell

# Collect static files
python manage.py collectstatic

# Run tests
python manage.py test
```

---

## 📝 Future Enhancements

- 🔐 Advanced user authentication & authorization
- 💳 Payment gateway integration
- ⭐ Property ratings & reviews
- 🗺 Google Maps integration
- 📧 Email notifications
- 📊 Admin dashboard analytics
- 🔍 Advanced property search filters
- 💬 Live chat support
- 📱 Mobile app version

---

## 👨‍💼 Developer Info

**Project**: Dream House Real Estate Platform  
**Framework**: Django 5.0.4  
**Python Version**: 3.12  
**Status**: In Development

---

## 📄 License

This project is for educational purposes. All rights reserved.

---

## 📞 Support

For issues or questions, please check:
1. The troubleshooting section above
2. Django official documentation: https://docs.djangoproject.com/
3. Bootstrap documentation: https://getbootstrap.com/docs/4.6/

---

**Last Updated**: December 2025  
**Version**: 1.0
