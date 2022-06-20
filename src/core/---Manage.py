# from src.app.configs import console
# from flask import Flask
# from src.routes import web, api, error
# from src.core.Router import Router
# from src.core.Storage import Storage
# import os

# class Manage():      
    
#     def __init__(self):
#         self.routes = [web.routes, api.routes, error.routes]


#     def exec_terminal_line(self, args):
#         """Executa o comando do terminal"""
#         method = args[1]  if len(args) > 1 else None    
#         params = args[2:]   
        
        
#         if(method in console['commands_admin']):   
#             run = getattr(self, method)  
#             run(params)   
#             return            
#         else:
#             print('Comando não reconhecido. Comandos aceitos:\n')
#             print(' - migrate [fresh] :: Rodas as migrações - [fresh]:roda novamente todas as migrações')
#             print(' - server :: Inicia o servidor de desenvolvimento')
#             print(' - make [elemento] [name] :: cria um elemento')
#             return
            
    
#     def server(self, params):
#         """Inicia o servidor"""      

#         app = Flask(__name__, 
#                     static_folder=Storage.basePath('src/resources/assets'),
#                     template_folder=Storage.basePath('src/resources/views')
#         )                

#         Router().router(app, web.routes, api.routes, error.routes)
        
#         app.run(
#             host='localhost',
#             port=9000,
#             debug=True
#         )
        
        
#     def help(self, params):
#         print('Ajuda!!!')
        
        
#     def migrate(self, params): 
#         """Faz a migração do banco de dados"""
#         print(rf'Migrando banco de dados')
            
            
#     def make(self, params):  
#         """Criar elementos"""   
        
        
#         if(params[0] == 'controller'):  
#             self.make_controller(params[1])  
            
#         elif(params[0] == 'model'):  
#             self.make_model(params) 
            
                
#         elif(params[0] == 'migration'):  
#             self.make_migration(params)   
            
                
#         elif(params[0] == 'seeder'):  
#             self.make_seeder(params[1])   
            
#         elif(params[0] == 'config'):  
#             self.make_config(params[1])   
            
                
#         else:  
#             print('Comando não reconhecido. Comandos aceitos:\n')
#             print(' - controller [name]')
#             print(' - model [name]')
#             print(' - migration [name]')
#             print(' - seeder [name]')
        
        
#     def make_controller(self, params): 
#         """Cria um controller"""
#         print(rf'Criando Controller: {params[0]}')     
        
#         basepath = "D:\\ServerLocal\\Python\\sSnake"
        
#         stub_file = open(rf"{basepath}\\src\\core\\stubs\\controller.stub", 'r+')    
#         stub_content = stub_file.read()
#         stub_file.close()
            
#         dir_name = params[0]
        
#         if( "/" in params[0]):
#             name_split = params[0].split('/')
#             dir_name = name_split[0] +"\\"+ name_split[1]        
#             newdir = rf"{basepath}\\src\\app\\controllers\\{name_split[0]}"
            
#             if(os.path.isdir(newdir) == False):
#                 os.mkdir(newdir)
                
#             stub_content = stub_content.replace("%NAMECLASS%", name_split[1])
            
#         else:        
#             stub_content = stub_content.replace("%NAMECLASS%", params[0])
        

#         controler_file = open(rf"{basepath}\\src\\app\\controllers\\{dir_name}.py", 'w+')    
#         controler_file.writelines(stub_content)   
#         controler_file.close()
        
        
#     def make_model(self, params): 
#         """Cria um model"""      
#         print(rf'Criando model: {params[1]}')
        
        
#         basepath = "D:\\ServerLocal\\Python\\sSnake"
        
#         stub_file = open(rf"{basepath}\\src\\core\\stubs\\model.stub", 'r+')    
#         stub_content = stub_file.read()
#         stub_file.close()
            
#         dir_name = params[1]
        
#         if( "/" in params[1]):
#             name_split = params[1].split('/')
#             dir_name = name_split[0] +"\\"+ name_split[1]        
#             newdir = rf"{basepath}\\src\\app\\models\\{name_split[0]}"
            
#             if(os.path.isdir(newdir) == False):
#                 os.mkdir(newdir)
                
#             stub_content = stub_content.replace("%MODELNAME%", name_split[1])
#             stub_content = stub_content.replace("%CONN%", params[2])
           
            
#         else:        
#             stub_content = stub_content.replace("%MODELNAME%", params[1])
#             stub_content = stub_content.replace("%CONN%", params[2])
        

#         controler_file = open(rf"{basepath}\\src\\app\\models\\{dir_name}.py", 'w+')    
#         controler_file.writelines(stub_content)   
#         controler_file.close()
        
        
#     def make_migration(self, params): 
#         """Cria uma migration"""
#         print(rf'Criando migration: {params}')
        
        
#     def make_seeder(self, params): 
#         """Cria um seeder"""
#         print(rf'Criando seeder: {name}')
        
        
#     def make_config(self, params):
#         """Cria um arquivo de configuração"""
#         print(rf'Criando Config: {name}')  
        
#         basepath = "D:\\ServerLocal\\Python\\PyKassFramework\\"
        
#         stub_file = open(rf"{basepath}\\src\\core\\stubs\\config.stub", 'r+')    
#         stub_content = stub_file.read()
#         stub_file.close()
            
#         dir_name = name
        
#         if( "/" in name):
#             name_split = name.split('/')
#             dir_name = name_split[0] +"\\"+ name_split[1]        
#             newdir = rf"{basepath}\\src\\app\\controllers\\{name_split[0]}"
            
#             if(os.path.isdir(newdir) == False):
#                 os.mkdir(newdir)
                
#             stub_content = stub_content.replace("%NAME%", name_split[1])
            
#         else:        
#             stub_content = stub_content.replace("%NAME%", name)
        

#         controler_file = open(rf"{basepath}\\src\\app\\config\\{dir_name}.py", 'w+')    
#         controler_file.writelines(stub_content)   
#         controler_file.close()
           
            
#     def list(self, params): 
#         """Lista um conjunto de elementos"""
#         if(params[0] == 'routes'):
#             self.list_routes(params)
                
#         else:  
#             print('Comando não reconhecido. Comandos aceitos:\n')
#             print(' - routes')


#     def list_routes(self, params):
#         """Retorna a listagem de rotas criadas"""
#         print(self.routes)

    
#     def list_config(self, params):
#         print('Pegando todas as configurações')
        
        
#     def cache(self, params):
#         print('Cachedo!') 

    
        
        
            
            
            
            
            