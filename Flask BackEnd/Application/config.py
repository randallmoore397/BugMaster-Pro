import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'b081c94255edcd285425fe1bc513ebb217369ca21f369a9efa719737a55f11d968bdad56d8a7cc4751bdbd54f090a5669b305f98e8ac1224ed9857ae')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'mysql+mysqlconnector://username:password@localhost/dbname')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAX_CONTENT_LENGTH =  1024 * 1024  # 3 MB in bytes

