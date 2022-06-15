from src.core.Router import Router
from src.app.controllers.InitialController import InitialController
from src.app.controllers._Snake.AdminController import AdminController


routes = [
    Router.create_route("/", InitialController,'initial'),       
    Router.create_route("/admin", AdminController,'admin')  
]
    