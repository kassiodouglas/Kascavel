from flask.views import MethodView
from flask import request, render_template

class HomeController(MethodView):
    def get(self):
        return render_template("pages/home/index.html") 