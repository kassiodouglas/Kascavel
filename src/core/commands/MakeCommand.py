from cleo.commands.command import Command
import os
from src.core.Storage import Storage

class MakeCommand(Command):
    """
    Criar um arquivo

    make
        {type : O que será criado} 
        {name : Nome do arquivo}       
    """
    def handle(self):
        type = self.argument("type")
        name = self.argument("name")

        run = getattr(self, type)  
        run(name)  
        
        
    def get_stub_content(self, type):
        stub_file = open(Storage.basePath(rf"src\\core\\stubs\\{type}.stub"), 'r+')
        stub_content = stub_file.read()
        stub_file.close()   
        
        return stub_content
    
    def create_file(self, name, stub_content):  
        controler_file = open(Storage.basePath(rf"src\\app\\controllers\\{name}.py"), 'w+')    
        controler_file.writelines(stub_content)   
        controler_file.close() 
        
        return True 
    
        
    def controller(self, name):        
        
        stub_content = self.get_stub_content('controller')
            
        dir_name = name
        
        if( "/" in dir_name):
            name_split = dir_name.split('/')
            dir_name = name_split[0] +"\\"+ name_split[1]        
            newdir = Storage.basePath(rf"src\\app\\controllers\\{name_split[0]}")
            
            if(os.path.isdir(newdir) == False): os.mkdir(newdir)
                
            stub_content = stub_content.replace("%NAMECLASS%", name_split[1])
            
        else:        
            stub_content = stub_content.replace("%NAMECLASS%",dir_name)
        

        self.create_file(name, stub_content)
        
        self.line(rf"Controller {name} criado")
        
    
    def model(self, name):
        self.line(rf"Model {name}")
        pass
    
    
    def config(self, name):
        self.line(rf"Config {name}")
        pass