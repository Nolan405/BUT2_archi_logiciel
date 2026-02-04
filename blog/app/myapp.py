from flask import Flask
from .extensions import api, db
from .views import ns
import os

basedir = os.path.abspath(os.path.dirname(__file__))
new_instance_path = os.path.join(basedir, '..', 'instance')

app = Flask(__name__, instance_path=new_instance_path)

# Ensuite, vous configurez votre base de données pour qu'elle soit dedans
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

# initialisation de restx
api.init_app(app)
db.init_app(app)

# ajout du namespace defini dans views
api.add_namespace(ns)