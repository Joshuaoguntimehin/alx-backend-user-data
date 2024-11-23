#!/usr/bin/env python3
"""
Route module for the API
"""

from flask import Flask, jsonify, abort, request
from flask_cors import CORS
import os

from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None

@app.errorhandler(404)
def not_found(error) -> tuple:
    """
    Handler for 404 Not Found errors.

    Args:
        error: The error object.

    Returns:
        A JSON response with an error message and a 404 status code.
    """
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(401)
def unauthorized(error) -> tuple:
    """
    Handler for 401 Unauthorized errors.

    Args:
        error: The error object.

    Returns:
        A JSON response with an error message and a 401 status code.
    """
    return jsonify({"error": "Unauthorized"}), 401

@app.errorhandler(403)
def forbidden(error) -> tuple:
    """
    Handler for 403 Forbidden errors.

    Args:
        error: The error object.

    Returns:
        A JSON response with an error message and a 403 status code.
    """
    return jsonify({"error": "Forbidden"}), 403

auth_type = os.getenv('AUTH_TYPE')
if auth_type == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
else:
    from api.v1.auth.auth import Auth
    auth = Auth()

@app.before_request
def before_request():
    """
    Filter each request before it reaches the view function.
    Handles authentication and authorization.

    Aborts with appropriate error codes if authentication fails.
    """

    if auth is None:
        return  # No authentication required, skip filtering

    # List of paths that do not require authentication
    excluded_paths = [
        '/api/v1/status/',
        '/api/v1/unarequest.current_useruthorized/',
        '/api/v1/forbidden/'
    ]

    # Check if the request path requires authentication
    if not auth.require_auth(request.path, excluded_paths):
        return  # Skip authentication for excluded paths

    # Check for authorization header
    if auth.authorization_header(request) is None:
        abort(401)  # Unauthorized error

    # Check for current user
    if auth.current_user(request) is None:
        abort(403)  # Forbidden error
        # Assign the current user to request.current_user    
        request.current_user = auth.current_user(request)
    else:
        #Ensure request.current_user is always set
        request.current_user = None
@app.route('/api/v1/status', methods=['GET'])
def status():
    """
    Health check route.

    Returns:
        A JSON response indicating the API status.
    """
    return jsonify({"status": "OK"})

if __name__ == "__main__":
    host = os.getenv("API_HOST", "0.0.0.0")
    port = os.getenv("API_PORT", "5000")
    app.run(host=host, port=port)
