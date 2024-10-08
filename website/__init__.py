import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .views import views
from .auth import auth

db = SQLAlchemy()
DB_NAME = "database.db"
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ajkbdasbf'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + DB_NAME
    db.init_app(app)

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note
    create_db(app)

    return app

def create_db(app):
    if not os.path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created database!', DB_NAME)