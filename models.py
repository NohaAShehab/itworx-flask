"""
    Any operation related to the database will be done in the model

"""
from flask_sqlalchemy import  SQLAlchemy

db = SQLAlchemy()

class DepartmentModel(db.Model):
    __tablename__  = 'departments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    ######################### classname  ### will use it while using the objects
    employees = db.relationship('EmployeeModel', backref='department', lazy=True)
    #
class EmployeeModel(db.Model):
    __tablename__ = "employees"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    salary = db.Column(db.Integer, default=1000)
    email = db.Column(db.String(100), unique=True, nullable=True)
    age =db.Column(db.Integer, default=25)
    dept_id= db.Column(db.Integer, db.ForeignKey('departments.id'),
        nullable=False)