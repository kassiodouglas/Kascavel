

global_web = [] 
global_api = []  
global_error = []  



def router(app):    
    """Gera as rotas no Flask"""
    for item in global_web:   app.add_url_rule(item['route'], view_func=item['controller'])
    for item in global_api:   app.add_url_rule(item['route'], view_func=item['controller'])
    for item in global_error: app.register_error_handler(item['route'], item['controller'])    

    
def add_route(route, controller, name):    
    """Acumula as rotas WEB"""   
    obj = {"route":route,"controller": controller.as_view(name), "name": controller.__name__, "alias": name}
    global_web.append(obj)   
    
    
def add_api(route, controller, name):  
    """Acumulas as rotas API"""  
    obj = {"route":"/api/" + route,"controller": controller.as_view(name), "name": controller.__name__, "alias": name}
    global_api.append(obj)    
    
    
def add_error(route, controller, name):    
    """Acumular as rotas ERROR"""
    obj = {"route":route,"controller": controller.as_view(name), "name": controller.__name__, "alias": name}
    global_error.append(obj)     


def list():
    print('\nRotas WEB------------------------------------------------------------')
    for item in global_web:          
        print(rf"Route: {item['route']} | Controller: {item['name']} | Name: {item['alias']}")
   
    
    print('\nRotas API------------------------------------------------------------')
    for item in global_api:   
        print(rf"Route: {item['route']} | Controller: {item['name']} | Name: {item['alias']}")
    
    print('\nRotas ERROR------------------------------------------------------------')
    for item in global_error:   
        print(rf"Route: {item['route']} | Controller: {item['name']} | Name: {item['alias']}")
    

    
        