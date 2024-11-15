#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import abort
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os




app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
CORS(app)

auth = None

@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "error"}), 404

@app.errorhandler(401)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Unauthorized"}), 401

@app.errorhandler(403)
def not_allowed(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Forbidden"}), 403

auth_type = os.getenv('AUTH_TYPE')
if auth_type == 'auth':
    from api.v1.auth.auth import Auth
    auth = Auth()

# Add any other authentication types here if needed
if auth_type == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
else:
    auth = Auth()
@app.before_first_request
def before_request():
    """Filter each request before it reaches the view function."""
    if auth is None:
        return  # No authentication required, skip filtering
    
    # List of paths that do not require authentication
    excluded_paths = ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']
    
    # Check if the request path requires authentication
    if not auth.require_auth(request.path, excluded_paths):
        return  # Skip authentication for excluded paths
    
    # Check for authorization header
    if auth.authorization_header(request) is None:
        abort(401)  # Unauthorized error
    
    # Check for current user
    if auth.current_user(request) is None:
        abort(403)  # Forbidden error

# Define your routes here
@app.route('/api/v1/status', methods=['GET'])
def status():
    return jsonify({"status": "OK"})



        
                
if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
    
