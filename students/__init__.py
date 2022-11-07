from flask import Blueprint

students_blueprint = Blueprint("students", __name__, url_prefix="/students")

from app.students import views


