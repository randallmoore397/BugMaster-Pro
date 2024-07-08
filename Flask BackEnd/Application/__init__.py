from flask import Flask
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
from flask_mysql_connector import MySQL
from flask_bcrypt import Bcrypt
# from flask_security import Security, SQLAlchemyUserDatastore
# from flask_socketio import SocketIO
import os
# from flask_mail import Mail
# from flask_security import current_user

# from flask_wtf.csrf  import CsrfProtect
# from flask_wtf.csrf import CsrfProtect

# import msearch
# from flask_msearch import Search


# import pymysql
# pymysql.install_as_MySQLdb()





app = Flask(
            __name__,
            #? static_url_path='',
            #? static_folder='static/dist',
            template_folder='templates',
            )

#? 50 CHARACTER LONG SECRETE KEY
app.config['SECRET_KEY'] = 'b081c94255edcd285425fe1bc513ebb217369ca21f369a9efa719737a55f11d968bdad56d8a7cc4751bdbd54f090a5669b305f98e8ac1224ed9857ae'


#? 50 CHARACTER LONG WTFROMS SECRETE KEY
app.config['WTF_CSRF_SECRET_KEY'] = 'acf571632edb15df57a0b360ed6242f991a53756aea07f9f1ca4a90b0de0c1bf047069a15fcb01181a61f150233381483c4af887da58b15038ced2e1'

app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 3 MB in bytes

#********************** MySQL DATABASE CONFIG *******************#
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:@localhost:3306/studyliberia?charset=utf8"

# Configure the SQLAlchemy database URI
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://<DB_USERNAME>:<DB_PASSWORD>@<DB_ENDPOINT>/<DB_NAME>'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://<DB_USERNAME>:<DB_PASSWORD>@<DB_ENDPOINT>/<DB_NAME>'



# Flask Security Core  configurations
app.config["SECURITY_SEND_REGISTER_EMAIL"] = False
app.config["SECURITY_PASSWORD_SALT"] = "'585cc0e4317a663a2fb9a0dc3d2b3de2cfb6ea36a9089fa7a89b248edd404aad8906d4a30af9fa3ea14a55892e15a31511d5934a1e7c2e03cf7798ec'"
app.config["SECURITY_EMAIL_SENDER"] = "noreplySino@gmail.com"   # Specifies the email address to send emails as. Defaults to value set to MAIL_DEFAULT_SENDER if Flask-Mail is used 

app.config["SECURITY_TOKEN_MAX_AGE"] = 9000  # Specifies the number of seconds before an authentication token expires
app.config['TEMPLATES_AUTO_RELOAD'] = True


# URLs and Views configurations
# app.config["SECURITY_LOGIN_URL"] = "/account/login"                # Specifies the login URL. 

app.config["SECURITY_LOGIN_USER_TEMPLATE"] = "login.html"
# app.config["SECURITY_LOGOUT_URL"] = "/logout"              # Specifies the logout 
app.config['SECURITY_LOGIN_URL'] = '/login'


# app.config["SECURITY_RESET_PASSWORD_TEMPLATE"] = "templates/pasword_reset.html"         # Specifies the path to the template for the reset password page.
# app.config["SECURITY_CHANGE_PASSWORD_TEMPLATE"] = "templates/pasword_change.html"       # Specifies the path to the template for the change password page.

# Feature Flags configurations
app.config["SECURITY_CONFIRMABLE"] = False                      # Specifies if users are required to confirm their email address when registering a new account. 
# app.config["SECURITY_REGISTERABLE"] = True                      # Specifies if Flask-Security should create a user registration endpoint.
# app.config["SECURITY_RECOVERABLE"] = False                      # Specifies if Flask-Security should create a password reset/recover endpoint
app.config["SECURITY_TRACKABLE"] = True                         # Specifies if Flask-Security should track basic user login statistics. 

# Email configurations
# app.config["SECURITY_EMAIL_SUBJECT_REGISTER"] = " Welcome to "

app.config["MAIL_SERVER"] = 'smtp.gmail.com' 
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = 'noreplysanoe@gmail.com'
app.config["MAIL_PASSWORD"] = '&t&^&^^%^%)(&(&wer$@wQq8agdS*^DRE'



# app.config["SECURITY_USER_IDENTITY_ATTRIBUTES"] = ['schoolID']     # Specifies which attributes of the user object can be used for login.
app.config["SECURITY_REMEMBER_SALT"] = '3f1d92f5e2206f038d6b499d3dd36c355c1554adf2092a38357037fb479d5626d22e331846b5d47ea0517370e9a97125761beb39da8e2958402287ce'# Specifies the salt value when generating remember tokens.



db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
# socketio = SocketIO(app)

# init msearch to be use with your app
# search = Search(app)
# search.init_app(app)
# search.create_index(update=True)
# mail = Mail(app)





#? By default, msearch will index queries to make next queries faster
# This line specify the location where msearch index will be store
MSEARCH_INDEX_NAME =  os.path.join(app.root_path,'msearch')

#? simple,whoosh,elaticsearch, default is simple
MSEARCH_BACKEND = 'whoosh'
 
#?  Here we specify which column msearch will use as primary id in the  database, usually is the id column 
MSEARCH_PRIMARY_KEY = 'id'

#? auto create or update index
#? THis means msearch should auto index files
MSEARCH_ENABLE = True

#? SQLALCHEMY_TRACK_MODIFICATIONS must be set to True when msearch auto index is enabled
SQLALCHEMY_TRACK_MODIFICATIONS = True


from Application.models import User, Role
# #*IMPORTING MY CUSTOM LOGIN FORM HERE
# from studyliberia.main.forms import LoginForm

# user_datastore = SQLAlchemyUserDatastore(db, User, Role)

# #* For posterity, you can disable the default flask-security blueprint during the Security object init 
# security = Security(app, user_datastore) #register_blueprint=False


#*************** Import Blueprint **************
from Application.User.route import user
from Application.Tracking.route import Tracking



# from Application import db, security, user_datastore



#************ Register Blueprints *************#
app.register_blueprint(user)
app.register_blueprint(Tracking)






from Application import models








