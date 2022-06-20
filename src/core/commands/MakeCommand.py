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
        controler_file = open(rf"{name}.py", 'w+')    
        controler_file.writelines(stub_content)   
        controler_file.close() 
        
        return True 
    
    
    def create_dirs(self, name, type, basepath):
        name_split = name.split('/')
        name_split.reverse()
        name = name_split[0]
        
        del name_split[0]

        newdir = ''
        for dir in name_split:               
            newdir = dir +  "\\" +newdir  
            
        newdir = rf"{basepath}\\{type}\\{newdir}"         
        if(os.path.isdir(newdir) == False): os.makedirs(newdir) 
        
        return [newdir, name]          
    
        
    def controller(self, name):               
        type = 'controllers'
        newdir = Storage.basePath(rf"src\\app\\{type}")
        
        if( "/" in name): 
            x = self.create_dirs(name, type, newdir)     
            newdir  = x[0]
            name    = x[1]      
       
        stub_content = self.get_stub_content('controller')      
        stub_content = stub_content.replace("%NAMECLASS%",name)        
        print(newdir +"\\"+ name)
        self.create_file( newdir +"\\"+ name, stub_content)
        
        self.line(rf"Controller {name} criado")
        
    
    def model(self, name):
        type = 'models'
        newdir = Storage.basePath(rf"src\\app\\{type}")
        
        if( "/" in name):
            x = self.create_dirs(name, type, newdir)     
            newdir  = x[0]
            name    = x[1]    
       
        stub_content = self.get_stub_content('model')              
        stub_content = stub_content.replace("%NAMECLASS%", name)       

        self.create_file( newdir +"\\"+ name, stub_content)
        
        self.line(rf"Model {name} criado")
            
    
    def config(self, name):
        type = 'configs'
        newdir = Storage.basePath(rf"src\\app\\{type}")
        
        if( "/" in name):
            x = self.create_dirs(name, type, newdir)     
            newdir  = x[0]
            name    = x[1]    
       
        stub_content = self.get_stub_content('config')              
        stub_content = stub_content.replace("%NAME%", name)       

        self.create_file( newdir +"\\"+ name, stub_content)
        
        self.line(rf"Config {name} criado")
        
        
    def command(self, name):
        type = 'commands'
        newdir = Storage.basePath(rf"src\\core\\{type}")
        
        if( "/" in name):
            x = self.create_dirs(name, type, newdir)      
            newdir  = x[0]
            name    = x[1]    
       
        command = name.replace('Command','')
        
        stub_content = self.get_stub_content('command')              
        stub_content = stub_content.replace("%NAMECLASS%", name)  
        stub_content = stub_content.replace("%COMMAND%", command)      

        self.create_file( newdir +"\\"+ name, stub_content)
        
        self.line(rf"Command {name} criado")