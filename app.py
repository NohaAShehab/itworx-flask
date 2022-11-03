from flask import Flask
from flask import render_template, make_response
from flask import request
from flask_sqlalchemy import  SQLAlchemy
# 1- create the application
app = Flask(__name__)
print(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///db.sqlite"
db = SQLAlchemy(app)

"""

    to start the application from the terminal
    export FLASK_APP=app
    export FLASK_DEBUG=1
    flask run
    
    pip install flask-shell-ipython
"""
if __name__ == '__main__':
    app.run(debug=True)


############################################
@app.route("/", endpoint='landing')
def intery():
    return "<h1>Welcome to your first flask app </h1>"


@app.route("/index")
def index():
    return "<h1> Hello World </h1>"

#################################

def testurl():
    l = ["python","django", "flask", "odoo"]
    # return "hi"
    return l
app.add_url_rule("/test", view_func=testurl, endpoint="test")


# ############### accept parameter from the url
@app.route("/sayhello/<name>/<int:id>", endpoint="helloname")
def sayHello(name, id):
    m = "iti"
    print(m, name)
    return f"Hello {name} {id}"


### customize page_not_found

@app.errorhandler(404)
def page_not_found(error):
    # return "<h1> Sorry the request page not found </h1>"
    return render_template("page_not_found.html")

@app.route("/home/<user>", endpoint="homeuser")
def user_home(user):
    courses = ["python", "django", "flask"]
    info = {
        "name":user,
        "courses": courses
    }

    # print(request.args.get("track"))
    print("-------------------------- ")
    print(request)
    ### get the request paramenters
    print(request.args.to_dict())
    print(request.args.get("track"))
    return render_template("userprofile.html", username=user, courses=courses, info=info)


@app.route("/profile/<user>", endpoint="profileuser")
def user_profile(user):

    return render_template("profile.html", user=user)



@app.route("/response", endpoint="response")
def response():
    info = {
        "name":"noha",
        "track": "python"
    }

    # r = make_response(info)
    # r.status_code = 300
    # return r

    return info, 201

# ##################### connect to the database ######
class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), unique=True)
    age = db.Column(db.Integer, default = 10)

    def __str__(self):
        return self.name



@app.route("/students", endpoint='students')
def get_all_students():
    students = Student.query.all()
    return render_template("students.html", students=students)



@app.route("/students/<int:student_id>", endpoint='studentinfo')
def get_student(student_id):
    student = Student.query.get_or_404(student_id)
    return render_template("studentprofile.html", student=student)


@app.route("/listitems", endpoint="listitems")
def list_items():
    courses = ["Flask", "Django", "Odoo", "python"]
    names = ["Ahmed", "Shehab", "Carol", "Shrouk"]
    return render_template("lists.html", courses=courses, names=names)

