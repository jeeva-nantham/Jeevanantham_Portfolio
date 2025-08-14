# 🌟 Django Portfolio Website

A personal portfolio website built with **Django** and **Tailwind CSS**, showcasing my projects, skills, and experience, with a built-in contact form that sends messages directly to my email.

---

## 📸 Features

- **Modern UI** using Tailwind CSS
- **Responsive Design** for mobile, tablet, and desktop
- **Dynamic Pages** powered by Django templates
- **Contact Form** with email sending via Gmail SMTP
- Project showcase with images and descriptions
- Links to GitHub, LinkedIn, and other socials

---

## 🛠 Tech Stack

- **Backend:** Django (Python)
- **Frontend:** Tailwind CSS, HTML5
- **Database:** SQLite (default, can be replaced with PostgreSQL/MySQL)
- **Email:** Gmail SMTP for contact form
- **Deployment Ready:** Configured for platforms like Render, Railway, or Heroku

---

## 📂 Project Structure

```
django-portfolio/
│
├── portfolio/           # Main Django app
│   ├── templates/       # HTML templates
│   ├── static/          # CSS, JS, Images
│   ├── views.py         # App views
│   ├── urls.py          # URL routing
│   └── forms.py         # Contact form
│
├── staticfiles/         # Collected static files (production)
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/django-portfolio.git
cd django-portfolio
```

### 2️⃣ Create & activate virtual environment
```bash
python -m venv env
source env/bin/activate      # Mac/Linux
env\Scripts\activate         # Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure environment variables  
Create a `.env` file in the root directory and add:
```env
EMAIL_HOST_USER=yourgmail@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### 5️⃣ Run migrations
```bash
python manage.py migrate
```

### 6️⃣ Start the development server
```bash
python manage.py runserver
```

---

## 📧 Contact Form Setup

This project uses **Gmail SMTP**.  
To enable it:
1. Go to your Google Account → Security → App Passwords.
2. Create an **App Password** and use it in `.env`.
3. Update `settings.py` with:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
```

---

## 🚀 Deployment

To deploy, make sure to:
- Set `DEBUG = False` in `settings.py`
- Run:
```bash
python manage.py collectstatic
```
- Configure allowed hosts in `settings.py`

---

## 📜 License
This project is licensed under the MIT License — you’re free to use and modify it.

---

## 👨‍💻 Author
**Jeevanantham S**  
📧 [jeevajeeva6322@gmail.com](mailto:jeevajeeva6322@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/jeevanantham-samkumar-5199381b4) | [GitHub](https://github.com/jeeva-nantham)
