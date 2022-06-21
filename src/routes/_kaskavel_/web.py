from src.core.Router import Router
from src.app.controllers._kaskavel_.AdminController import AdminController


routes = [    
    Router.add("/admin", AdminController,'admin')  
]
    