
global_web = [] 
global_api = []  
global_error = []  

def router(app):    
    for item in global_web:   app.add_url_rule(item['route'], view_func=item['controller'])
    for item in global_api:   app.add_url_rule(item['route'], view_func=item['controller'])
    for item in global_error: app.register_error_handler(item['route'], item['controller'])    

    
def add_route(route, controller, name):    
    obj = {"route":route,"controller": controller.as_view(name)}
    global_web.append(obj)   
    
    
def add_api(route, controller, name):    
    obj = {"route":"/api/" + route,"controller": controller.as_view(name)}
    global_api.append(obj)    
    
    
def add_error(route, controller, name):    
    obj = {"route":route,"controller": controller.as_view(name)}
    global_error.append(obj)     



    
        