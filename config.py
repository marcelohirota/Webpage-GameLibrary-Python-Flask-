import os

SECRET_KEY = 'hirota'
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "admin"
MYSQL_DB = "jogoteca"
MYSQL_PORT = 3306
UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'