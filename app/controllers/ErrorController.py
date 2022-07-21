from flask.views import MethodView
from app.controllers.Controller import Controller
from flask import render_template

class ErrorController(Controller,MethodView):
    def get(self,error): 
        return render_template("pages/errors/404.html", error=error)   