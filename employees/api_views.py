from flask_restful import Resource, marshal_with, fields, abort
from flask import  make_response

from app.models import EmployeeModel, DepartmentModel , db
from app.employees.parser import  employee_parser




#### define the request parser by the model



## generate api  for the EmployeeModel

dept_serializer = {
    "id": fields.Integer,
    "name": fields.String
}



employee_serilizer={
    "id": fields.Integer,
    "name": fields.String,
    "email": fields.String,
    "salary":fields.Integer,
    "age":fields.Integer,
    "dept_id":fields.Integer,
    "department":fields.Nested(dept_serializer)
}

class EmployeeList(Resource):
    @marshal_with(employee_serilizer)
    def get(self):
        employees = EmployeeModel.query.all()
        return employees, 200

    @marshal_with(employee_serilizer)
    def post(self):
        emp_args = employee_parser.parse_args()  # dict
        print(emp_args)
        employee= EmployeeModel(**emp_args)
        db.session.add(employee)
        db.session.commit()

        return employee, 201



class Employee(Resource):
    @marshal_with(employee_serilizer)
    def get(self, employee_id):
        employee = EmployeeModel.query.get(employee_id)
        if employee :
            return employee, 200
        else:
            abort(404, message="Employee not found ")
        pass


    @marshal_with(employee_serilizer)
    def put(self, employee_id):
        employee = EmployeeModel.query.get(employee_id)
        if employee:
            emp_args = employee_parser.parse_args()
            employee.name = emp_args["name"]
            employee.age = emp_args["age"]
            employee.dept_id = emp_args["dept_id"]
            employee.email = emp_args["email"]
            db.session.add(employee)
            db.session.commit()
            return employee, 200

        else:
            abort(404, message="Employee not found ")
        pass


    def delete(self, employee_id):
        employee = EmployeeModel.query.get(employee_id)
        if employee:
            db.session.delete(employee)
            db.session.commit()
            response = make_response("hiii", 204)
            return response
        else:
            abort(404, message="Employee not found ")
        pass

