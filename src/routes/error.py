from src.app.controllers.ErrorController import ErrorController
from src.core.router import add_error


add_error(404, ErrorController,'error.404')
