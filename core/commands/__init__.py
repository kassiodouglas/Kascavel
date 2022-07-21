#core/commands    

#Lista de pacotes
packages = [
    'HelloCommand',
    'ServerCommand',
    'MakeCommand',
    'MigrateCommand',
    'MigrationCommand',
    'SeederCommand',
    'SeedCommand',
]

#Faz o import dos comandos
for pkg in packages: 
    exec( rf"from core.commands.{pkg} import {pkg}") 
    
