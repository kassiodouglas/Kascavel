from flask.views import MethodView
from flask import render_template

class InitialController(MethodView):
    def get(self):
        return render_template("pages/_initial/index.html") 