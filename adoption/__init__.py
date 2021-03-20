import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SJFkfjasokfjSJFOKS2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

from adoption.puppies.views import puppies_blueprint
from adoption.owners.views import owners_blueprint

app.register_blueprint(puppies_blueprint, url_prefix='/puppies')
app.register_blueprint(owners_blueprint, url_prefix='/owners')