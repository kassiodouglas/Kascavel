from flask.views import MethodView
from flask import render_template

class AdminController(MethodView):
    def get(self):
        return render_template("_Snake/admin.html") 