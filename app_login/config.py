import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://admin:rS5mQ5CTc22MD02F@localhost/applogin')
    SQLALCHEMY_TRACK_MODIFICATIONS = False