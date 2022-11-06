#  ## here I will initilize the app
from flask import Flask
from app.models import db
from app.config import config as AppConfig
from flask_migrate import Migrate




def create_app(config_name):
    app = Flask(__name__)
    current_config = AppConfig[config_name]
    # app.config["SQLALCHEMY_DATABASE_URI"] = AppConfig[config_name].SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_DATABASE_URI"] = current_config
    app.config.from_object(current_config)
    # get the configuration of the database
    db.init_app(app)

    migrate = Migrate(app, db)
    ### register the student application to the project
    from app.students import students_blueprint
    app.register_blueprint(students_blueprint)



    #########################################

    return app
