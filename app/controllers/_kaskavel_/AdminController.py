from flask.views import MethodView
from app.controllers.Controller import Controller
from flask import render_template

class AdminController(Controller,MethodView):
    def get(self):
        return render_template("_kaskavel_/admin.html") 