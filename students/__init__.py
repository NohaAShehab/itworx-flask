from flask import Blueprint

students_blueprint = Blueprint("students", __name__)

from app.students import views


