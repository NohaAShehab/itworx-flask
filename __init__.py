#  ## here I will initilize the app
from flask import Flask
from flask_restful import Api


from app.models import db
from app.config import config as AppConfig
from flask_migrate import Migrate
from app.employees.api_views import EmployeeList,Employee




def create_app(config_name):
    app = Flask(__name__)
    current_config = AppConfig[config_name]
    app.config["SQLALCHEMY_DATABASE_URI"] = current_config
    app.config.from_object(current_config)
    app.config['SECRET_KEY'] = current_config.SECRET_KEY
    db.init_app(app)

    migrate = Migrate(app, db)
    ###### add the api interface to the application
    api = Api(app)
    api.add_resource(EmployeeList, '/api/employees')
    api.add_resource(Employee, "/api/employees/<int:employee_id>")


    # ######################## Blueprints and resources ##################3
    from app.students import students_blueprint
    app.register_blueprint(students_blueprint)

    from app.employees import employee_blueprint
    app.register_blueprint(employee_blueprint)



    #########################################

    return app
