import os
from Application import db,bcrypt, app
from flask import Blueprint, render_template, redirect, url_for, current_app,request, Response,send_file,make_response, send_from_directory, session
import jsonpickle

Tracking = Blueprint('Tracking',__name__)