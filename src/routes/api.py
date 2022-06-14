from src.app.core.router import add_api
from src.app.controllers.HomeController import HomeController


add_api("/hoom", HomeController,'api.home')
