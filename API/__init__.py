from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SECRET_KEY'] = '2018103006'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app,session_options={"autoflush":False})
serializer = Marshmallow(app)
try:
    from API import routes
except Exception as e:
    print(e)
