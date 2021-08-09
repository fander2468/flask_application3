from flask import Flask
from config import Config
# Import flask wrappers
from flask_login import LoginManager # for logging users in and maintaining a sesion
from flask_sqlalchemy import SQLAlchemy # This is used to talk to our database
from flask_migrate import Migrate # Makes altering the Database a lot easier


# init Login Manager
login = LoginManager() # used to login users and create a session
login.login_view = 'auth.login' # Used to redirect users if they enter wrong credentials or they are an invalid user
login.login_message = "You must be logged in to view this page." 
login.login_message_category = "warning" 

# init the database from_object
db = SQLAlchemy() # create a variable to talk to db and pass in the flask app 

# init Migrate
migrate = Migrate()

def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(config_class)
    login.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    from .blueprints.main import bp as main_bp
    app.register_blueprint(main_bp)

    from .blueprints.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from .blueprints.social import bp as social_bp
    app.register_blueprint(social_bp)
    
    return app
