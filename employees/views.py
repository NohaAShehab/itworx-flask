from flask import request, render_template
from app.employees import employee_blueprint
from app.employees.forms import EmployeeForm
from app.models import EmployeeModel, db


def validateinputs(request):
    errors = {}
    if not request['name']:
        errors["name"]= "name required"
    emp = EmployeeModel.query.filter_by(email=request["email"]).first()
    if emp:
        errors["email"] = "email exists"

    return errors



@employee_blueprint.route("/", endpoint="employees",methods= ["GET", "POST"])
def employees():
    form = EmployeeForm()
    if request.method=="GET":
        return render_template("employees/create.html", form=form, name='noha')
    elif request.method=="POST":

        requestform = dict(request.form)
        # print(requestform)
        # emp = EmployeeModel.query.filter_by(email=requestform["email"]).first()
        # if emp:
        #     # return  "Email already exists"
        #     return render_template("employees/create.html", form=form, name='noha',
        #                            errors="Email already exists")

        errors = validateinputs(requestform)
        if errors:
            return render_template("employees/create.html", form=form, name='noha',
                                       errors=errors)

        del requestform['csrf_token']
        employee = EmployeeModel(
            **requestform)

        db.session.add(employee)
        db.session.commit()

        return "POST ADDED "

