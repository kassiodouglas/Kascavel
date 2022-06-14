from src.app.core.router import add_route
from src.app.controllers.HomeController import HomeController


add_route("/", HomeController,'home')
add_route("/sobre", HomeController,'about')