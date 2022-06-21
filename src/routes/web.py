from ..core.Router import Router
from ..app.controllers.InitialController import InitialController
from ..routes._kaskavel_.web import routes as routes_admin


routes = [
    Router.add("/", InitialController,'initial'),  
]

#Rotas administrativas do framework
routes.extend(routes_admin)
    