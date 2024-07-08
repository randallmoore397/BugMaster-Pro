import os
from Application import db,bcrypt, app
from flask import Blueprint, render_template, redirect, url_for, current_app,request, Response,send_file,make_response, send_from_directory, session
from flask import jsonify
import jsonpickle

user = Blueprint('User',__name__)


@user.route("/")
def login():
    return "Hello World"




@user.route('/user/track/bug', methods=['POST'])
def track_bug():
    data = request.json
    # print('Received data:', data)
    
    # Simulate saving the data to the database or any other processing
    # Here, we'll just return the received data as a response for testing
    
    # Return a Bug ID for the newly added bug
    
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    return jsonify({'status': True, 'data': data["bug_title"]}), 200




@user.route('/user/remove/bug', methods=['DELETE'])
def remove_bug_track():
    data = request.json

    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    return jsonify({'status': True, 'data': data}), 200
