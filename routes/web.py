from ..core.Router import Router
from src.app.controllers.InitialController import InitialController



routes = [
    Router.add("/", InitialController,'initial'),  
]

#Extender rota de outro arquivo
# from ..routes._kaskavel_.web import routes as routes_admin
# routes.extend(routes_admin)
    