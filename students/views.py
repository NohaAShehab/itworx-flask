from app.students import students_blueprint


@students_blueprint.route("/")
def index():
    return "<h1> Hello from views </h1>"
