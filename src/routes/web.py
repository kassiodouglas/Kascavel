from src.core.router import add_route
from src.app.controllers.InitialController import InitialController


add_route("/", InitialController,'initial')
