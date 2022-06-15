from src.core.Router import Router
from src.app.controllers.ErrorController import ErrorController


routes = [
    Router.create_route(404, ErrorController,'error404'),    
]
    