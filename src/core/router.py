
class Router():  
    def router(self, app, web, api, error):    
        """Gera as rotas no Flask"""
        for item in web:   app.add_url_rule(item['route'], view_func=item['controller'])
        for item in api:   app.add_url_rule(item['route'], view_func=item['controller'])
        for item in error: app.register_error_handler(item['route'], item['controller'])    
        
    def add(route, controller, name):
        """Retorna um objeto da rota"""   
        return {"route":route,"controller": controller.as_view(name), "name": controller.__name__, "alias": name}

       
        

        