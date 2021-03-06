import os
from flask import Flask
from flask.globals import session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from datetime import timedelta

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()


def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # specify the path of the image storage directory
    app.config['UPLOAD_FOLDER'] = './static/img'
    # Limiting the size of uploaded images
    app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
    # Validating file extensions
    app.config['UPLOAD_EXTENSIONS'] = ['.jpg']

    db.init_app(app)
    """
    we need to specify our user loader. 
    A user loader tells Flask-Login how to find a specific user 
    from the ID that is stored in their session cookie. 
    We can add this in our create_app function along with init code for Flask-Login
    """
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # set timeout (10 mins) for login
    @app.before_request
    def make_session_permanent():
        session.permanent = True
        app.permanent_session_lifetime = timedelta(minutes=10)

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # blueprint for manage parts of app
    from .mana import mana as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
