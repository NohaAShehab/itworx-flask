from flask import Blueprint


employee_blueprint = Blueprint("employees", __name__, url_prefix='/employees')


from app.employees import  forms, views, api_views

