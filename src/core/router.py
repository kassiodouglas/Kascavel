
class Router():  
    def router(self, app, web, api, error):    
        """Gera as rotas no Flask"""
        for item in web:   app.add_url_rule(item['route'], view_func=item['controller'])
        for item in api:   app.add_url_rule(item['route'], view_func=item['controller'])
        for item in error: app.register_error_handler(item['route'], item['controller'])    
        
    def create_route(route, controller, name):
        """Retorna um objeto da rota"""   
        return {"route":route,"controller": controller.as_view(name), "name": controller.__name__, "alias": name}

        
    # def add_route(self, route, controller, name):    
    #     """Acumula as rotas WEB"""   
    #     obj = {"route":route,"controller": controller.as_view(name), "name": controller.__name__, "alias": name}
    #     self.global_web.append(obj)   
    #     print(self.global_web)
        
        
    # def add_api(self, route, controller, name):  
    #     """Acumulas as rotas API"""  
    #     obj = {"route":"/api/" + route,"controller": controller.as_view(name), "name": controller.__name__, "alias": name}
    #     self.global_api.append(obj)    
        
        
    # def add_error(self, route, controller, name):    
    #     """Acumular as rotas ERROR"""
    #     obj = {"route":route,"controller": controller.as_view(name), "name": controller.__name__, "alias": name}
    #     self.global_error.append(obj)     


    # def list(self):
        # print('\nRotas WEB------------------------------------------------------------')
        # for item in self.global_web:          
        #     print(rf"Route: {item['route']} | Controller: {item['name']} | Name: {item['alias']}")
    
        
        # print('\nRotas API------------------------------------------------------------')
        # for item in self.global_api:   
        #     print(rf"Route: {item['route']} | Controller: {item['name']} | Name: {item['alias']}")
        
        # print('\nRotas ERROR------------------------------------------------------------')
        # for item in self.global_error:   
        #     print(rf"Route: {item['route']} | Controller: {item['name']} | Name: {item['alias']}")
        

        