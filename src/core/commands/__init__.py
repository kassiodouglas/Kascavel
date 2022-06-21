#core/commands    

#Lista de pacotes
packages = [
    'HelloCommand',
    'ServerCommand',
    'MakeCommand',
    'MigrateCommand',
    'MigrationCommand',
]

#Faz o import dos comandos
for pkg in packages: 
    exec( rf"from src.core.commands.{pkg} import {pkg}") 
    
