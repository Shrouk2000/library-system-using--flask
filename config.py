
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'mysecretkey')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://library:123@localhost/library_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
