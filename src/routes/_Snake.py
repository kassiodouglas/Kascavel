from src.core.router import add_route
from src.app.controllers._Snake.AdminController import AdminController


add_route("/admin", AdminController,'admin')