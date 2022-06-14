from src.resources.app import app
  
def server(app):
    """Inicia o servidor de testes"""    
    app.run(
        host='localhost',
        port=9000,
        debug=True
        )
    

def migrate(migration, fresh=False): 
    """Faz a migração do banco de dados"""
    print(rf'Migrando banco de dados')
    
    
def make(elemento, name):  
    """Criar elementos"""
    
    if(elemento == 'controller'):  
        make_controller(name)  
        
    elif(elemento == 'model'):  
        make_model(name) 
        
             
    elif(elemento == 'migration'):  
        make_migration(name)   
        
             
    elif(elemento == 'seeder'):  
        make_seeder(name)   
        
             
    else:  
        print('Comando não reconhecido. Comandos aceitos:\n')
        print(' - controller [name]')
        print(' - model [name]')
        print(' - migration [name]')
        print(' - seeder [name]')
      


def make_controller(name): 
    """Cria um controller"""
    print(rf'Criando Controller: {name}')    
    
def make_model(name): 
    """Cria um model"""
    print(rf'Criando model: {name}')
    
def make_migration(name): 
    """Cria uma migration"""
    print(rf'Criando migration: {name}')
    
def make_seeder(name): 
    """Cria um seeder"""
    print(rf'Criando seeder: {name}')
    
  


def exec_terminal_line(args):
    """Executa o comando do terminal"""
    method = args[1]  if len(args) > 1 else None
    args_1 = args[2]  if len(args) > 2 else None
    args_2 = args[3]  if len(args) > 3 else None    

    
    if(method == 'migrate'):
        migrate(args_1, args_2)
        
    elif(method == 'server'):
        server(app)
        
    elif(method == 'make'):
        make(args_1, args_2)
        
    else:
        print('Comando não reconhecido. Comandos aceitos:\n')
        print(' - migrate [fresh] :: Rodas as migrações - [fresh]:roda novamente todas as migrações')
        print(' - server :: Inicia o servidor de desenvolvimento')
        print(' - make [elemento] [name] :: cria um elemento')
        
        
