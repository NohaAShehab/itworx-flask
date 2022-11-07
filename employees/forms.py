from flask_wtf import FlaskForm

from wtforms import StringField, IntegerField, \
    TimeField, EmailField, FileField
from wtforms.validators import DataRequired



class EmployeeForm(FlaskForm):
    name = StringField('Name',validators=[DataRequired()])
    salary = IntegerField('Salary')
    email = EmailField('Email')
    age = IntegerField('Age')




