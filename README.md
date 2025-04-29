<h1 align="center">Contact Form API (Django REST Framework) </h1>

A simple REST API built with Django and Django REST Framework to handle contact form submissions.

## 🚀 Features

- Accepts contact form data via a `POST` request
- Fields: `first_name`, `last_name`, `phone`, `email`, `message`
- Validates required fields
- Returns structured JSON responses
- Saves submissions to the database

## 📦 API Endpoint

### `POST /api/contact/submit/`

#### Request Body (JSON)

```json
{
  "first_name": "Rakibul",
  "last_name": "Hassan",
  "phone": "01712345678",
  "email": "rakib@example.com",
  "message": "Hi! This is a test message."
}
```

Success Response
Status: 201 Created

Body:
```
{
  "first_name": "Rakibul",
  "last_name": "Hassan",
  "phone": "01712345678",
  "email": "rakib@example.com",
  "message": "Hi! This is a test message."
}
```
---

## 🛠 Tech Stack
• Python 3.x

• Django

• Django REST Framework

🧪 Setup Instructions
```
# Clone the repository
git clone https://github.com/YOUR_USERNAME/contact-form-api.git
cd contact-form-api
```
```
# (Optional) Create a virtual environment
python -m venv env
source env/bin/activate    # Linux/macOS
env\Scripts\activate       # Windows
```
```
# Install dependencies
pip install -r requirements.txt
```
```
# Run migrations
python manage.py migrate
```
```
# Start development server
python manage.py runserver
```

📬 Contact

Created by Md Rakibul Hassan

Email: rakibulhassanmiyaji27@gmail.com

GitHub: [RR0327](https://github.com/RR0327)

📝 License
This project is open-source and available under the MIT License.

---

