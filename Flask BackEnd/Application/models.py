from datetime import datetime,date
from enum import Flag, unique
from Application import db
# from itsdangerous.url_safe import URLSafeTimedSerializer as Serializer
# from flask_security import UserMixin, RoleMixin
# from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Boolean, DateTime, Column, Integer, String, ForeignKey, Time, Float,Date

# Define models
roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    userID = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(100))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(100))
    current_login_ip = db.Column(db.String(100))
    login_count = db.Column(db.Integer)
    DateCreated = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)

    # Database relationships
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('roles', lazy='dynamic'))
