from flask.views import MethodView
from flask import render_template

class ErrorController(MethodView):
    def get(self,error): 
        return render_template("pages/errors/404.html")   