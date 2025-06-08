Food Health Guide Backend
A Django REST API backend for a food and health guide app tailored for Indian users.
It manages user profiles, subscriptions, personalized diet and exercise plans, and supports JWT authentication, CORS, and interactive API documentation.
Features
Custom User Model: With health and lifestyle fields (age, gender, height, weight, health conditions, activity level, dietary preferences)
Subscription Management: Track user subscriptions and payment status
Personalized Diet & Exercise Plans: CRUD endpoints for user-specific plans
JWT Authentication: Secure, stateless API access
CORS Support: For frontend-backend integration
Admin Panel: Manage users, plans, and subscriptions
Interactive API Docs: Swagger and Redoc at /swagger/ and /redoc/
Ready for Indian payment gateway integration and further personalization logic
Getting Started
1. Clone the repository
Apply
food_health_guide
2. Set up a virtual environment
Apply
activate
3. Install dependencies
Apply
txt
4. Apply migrations
Apply
migrate
5. Create a superuser
Apply
createsuperuser
6. Collect static files
Apply
noinput
7. Run the development server
Apply
runserver
API Endpoints
Admin Panel: /admin/
Users: /api/users/
Subscriptions: /api/subscriptions/
Diet Plans: /api/diet-plans/
Exercise Plans: /api/exercise-plans/
API Docs: /swagger/ (Swagger UI), /redoc/ (Redoc)
Authentication
Uses JWT (JSON Web Token) authentication.
(Add /api/token/ and /api/token/refresh/ endpoints for login/refresh if not present.)
Environment Variables
Configure your database and secret keys in food_health_guide_backend/settings.py as needed.
Development Notes
CORS is enabled for all origins (for development). Restrict this in production.
Static files are collected to /staticfiles/.
Custom user model is used (users.User).
Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.
License
MIT (or your preferred license)
