

import os
from Application import db,bcrypt, app
from flask import Blueprint, render_template, redirect, url_for, current_app,request, Response,send_file,make_response, send_from_directory, session
import jsonpickle
from flask import jsonify


project = Blueprint('project',__name__)


@project.route("/user/create/new/project",methods=['POST'])
def createProject():
    data = request.json

    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    return jsonify({'status': True, 'data': data}), 200




@project.route("/user/create/delete/project",methods=['DELETE'])
def deleteProject():
    data = request.json

    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    return jsonify({'status': True, 'data': data}), 200



@project.route("/user/get/project/details",methods=['GET'])
def projectDetails():
    data = request.json

    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    return jsonify({'status': True, 'data': data}), 200



@project.route("/user/update/project",methods=['POST'])
def editProject():
    data = request.json

    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    return jsonify({'status': True, 'data': data}), 200
