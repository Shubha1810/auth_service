import requests
from flask import request, jsonify, Blueprint

hello_routes = Blueprint('hello_routes', __name__)


@hello_routes.route("/hello", methods=["GET"])
def hello():
    # Assuming token is passed as Authorization header from the client
    token = request.headers.get("Authorization")

    if not token:
        return jsonify({"error": "Authorization token is required"}), 401

    # URL of the verify_user route from the userproject
    verify_url = "http://user_app:4000/user/verify"  # Use container name instead of localhost

    # Call the verify_user route in userproject
    response = requests.get(verify_url, headers={"Authorization": token})

    if response.status_code == 200:
        user_data = response.json()
        return jsonify({
            "message": "Hello from auth_user project!",
            "verification": user_data
        }), 200
    else:
        return jsonify({"error": "User verification failed", "details": response.json()}), response.status_code
