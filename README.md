📰 Real-Time News Portal
https://img.shields.io/badge/License-MIT-blue.svg
https://img.shields.io/badge/Python-3.8%252B-blue
https://img.shields.io/badge/Django-4.2-brightgreen

A real-time news aggregation portal that delivers live updates via WebSocket, with a REST API for fetching articles and an admin panel for generating mock news.

✨ Key Features
✅ Real-time updates – Live news streaming via WebSocket.
✅ REST API – Fetch articles in JSON format.
✅ Admin-controlled mock data – Generate fake news for testing.
✅ Responsive UI – Built with HTML, CSS, and JavaScript.
✅ User authentication – Secure token-based access for admin actions.

🛠️ Setup & Installation
Prerequisites
Python 3.8+

Django 4.2+

Daphne (ASGI server)

Backend Setup
Create & activate a virtual environment:

bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# OR
venv\Scripts\activate     # Windows
Install dependencies & run migrations:

bash
cd backend/
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # Create admin user
Run the ASGI server (Daphne):

bash
daphne -p 8010 backend.asgi:application
Frontend Setup
bash
cd frontend/
python3 -m http.server 8020  # Serves frontend at http://localhost:8020
🚀 Usage
1. Generate Mock Articles
Step 1: Get Authentication Token
bash
curl --location 'http://localhost:8010/api/token/' \
--header 'Content-Type: application/json' \
--data '{
    "username": "your_admin_username",
    "password": "your_admin_password"
}'
Step 2: Generate Fake News
bash
curl --location --request POST 'http://localhost:8010/api/generate-news/' \
--header 'Authorization: Bearer YOUR_ACCESS_TOKEN'
2. Connect to WebSocket for Real-Time Updates
plaintext
ws://localhost:8010/ws/news/
3. Access the Frontend
Open http://localhost:8020 in your browser to see live news updates.

📡 API Endpoints
Endpoint	Method	Description
/api/token/	POST	Get JWT token for authentication
/api/generate-news/	POST	(Admin) Generate fake news
/api/articles/	GET	Fetch all articles
/ws/news/	WebSocket	Real-time news stream
🖼️ Screenshots (Optional)
(You can add screenshots of the UI here.)

🧰 Tech Stack
Backend: Django, Django REST Framework, Daphne (WebSocket)

Frontend: HTML, CSS, JavaScript

Database: SQLite (default, can be swapped for PostgreSQL)

Authentication: JWT (Django REST SimpleJWT)

🤝 Contributing
Fork the repository.

Create a new branch (git checkout -b feature/your-feature).

Commit changes (git commit -m "Add awesome feature").

Push to the branch (git push origin feature/your-feature).

Open a Pull Request.

📜 License
This project is licensed under the MIT License.

🙏 Acknowledgements
Django Channels for WebSocket support.

Django REST Framework for API building.