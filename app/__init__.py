from flask import Flask
# from flask.ext.mysql import MySQL

application = Flask(__name__)

# mysql = MySQL()
# application.config['MYSQL_DATABASE_USER'] = 'root'
# application.config['MYSQL_DATABASE_PASSWORD'] = '12345'
# application.config['MYSQL_DATABASE_DB'] = 'os_database'
# application.config['MYSQL_DATABASE_HOST'] = 'localhost'
# mysql.init_app(application)
# con = mysql.connect()
from app import views


