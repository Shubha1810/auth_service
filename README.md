# auth_service

UserProject & AuthService - README
Introduction
This repository contains two Flask-based microservices: UserProject and AuthService. These services demonstrate authentication, user management, and inter-service communication using JWT tokens and Docker.
* UserProject handles user signup, login, verification, and database management.
* AuthService validates users by interacting with UserProject and provides an authenticated response.
Both services are containerized using Docker and communicate via API calls.

Prerequisites
Before running the project, ensure you have the following installed:
* Python (>=3.9)
* Docker & Docker Compose
* Git

Cloning the Repository
Clone the project to your local system:
git clone https://github.com/yourusername/userproject.git
cd userproject
Clone the AuthService repository:
git clone https://github.com/yourusername/auth_service.git
cd auth_service

Running UserProject (User Authentication Service)
1. Build and Run with Docker
Navigate to the userproject directory and run:
docker build -t user_app .
docker run -p 4000:4000 user_app
2. Endpoints
* Signup a user: POST /user/signup
* Login user: POST /user/login
* Verify user token: GET /user/verify
* Fetch user details: GET /user/<user_id>

Running AuthService (Authentication Middleware)
1. Build and Run with Docker
Navigate to the auth_service directory and run:
docker build -t auth_service .
docker run -p 5000:5000 auth_service
2. Endpoints
* Hello Route (Requires Authentication): GET /hello
This route verifies the user's authentication status by calling UserProject's /user/verify endpoint.

Running Both Services Together with Docker Compose
To run both UserProject and AuthService simultaneously, create a docker-compose.yml file and add the following:
version: '3.8'
services:
  user_app:
    build: ./userproject
    ports:
      - "4000:4000"

  auth_service:
    build: ./auth_service
    ports:
      - "5000:5000"
    depends_on:
      - user_app
Run both services together with:
docker-compose up --build

Testing the API
Once both services are running, use an API tool like Postman or curl to test the endpoints.
1. Signup a User
curl -X POST "http://localhost:4000/user/signup" -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john@example.com", "password": "password", "dob": "2000-01-01", "phone": "1234567890"}'
2. Login to Get Token
curl -X POST "http://localhost:4000/user/login" -H "Content-Type: application/json" -d '{"email": "john@example.com", "password": "password"}'
Copy the token from the response.
3. Verify Authentication in AuthService
curl -X GET "http://localhost:5000/hello" -H "Authorization: Bearer <token>"
If successful, you will receive a verification response.

Conclusion
This project demonstrates a microservice-based authentication system using Flask, JWT, and Docker. You can extend it further by integrating databases like PostgreSQL or adding role-based authentication.
For any issues or contributions, feel free to raise a pull request or open an issue!
Happy coding! ??


