# 📰 Real-Time News Portal  
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)  
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)  
[![Django](https://img.shields.io/badge/Django-4.2-brightgreen)](https://www.djangoproject.com/)  

A real-time news aggregation portal that delivers live updates via WebSocket with REST API endpoints.

---

## ✨ Key Features  
- 🔴 **Live Updates**: WebSocket-powered real-time news streaming  
- 📡 **REST API**: JSON endpoints for article management  
- 🛠️ **Admin Tools**: Generate mock news for testing  
- 📱 **Responsive UI**: Works on all devices  
- 🔐 **Secure Auth**: JWT token authentication  

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js (optional for frontend builds)

### Installation
```bash
# Clone repo
git clone https://github.com/yourusername/real-time-news.git
cd real-time-news

# Backend setup
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows

pip install -r requirements.txt
cd backend
python manage.py migrate
python manage.py createsuperuser
daphne -p 8010 backend.asgi:application

# Frontend (in new terminal)
cd frontend
python -m http.server 8020
```

### 📡 API Documentation
#### Authentication
```bash
curl -X POST 'http://localhost:8010/api/token/' \
-H 'Content-Type: application/json' \
-d '{"username":"admin","password":"yourpassword"}'
```

#### Generate Fake News
```bash
curl --location --request POST 'http://localhost:8010/api/generate-news/' \
--header 'Authorization: Bearer YOUR_ACCESS_TOKEN'
```

#### WebSocket Connection
```javascript
const socket = new WebSocket('ws://localhost:8010/ws/news/');
```


### 🛠️ Tech Stack
#### Backend:
- Django 4.2
- Django Channels
- Daphne ASGI
- Redis

#### Frontend:
- Vanilla JavaScript
- HTML5/CSS3