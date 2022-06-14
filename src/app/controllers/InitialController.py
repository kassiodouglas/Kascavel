from flask.views import MethodView
from src.app.controllers.Controller import Controller
from flask import render_template

class InitialController(Controller,MethodView):
    def get(self):
        return render_template("pages/_initial/index.html") 