#configs    

#Lista de pacotes
packages = [
    'app',
    'database', 
    'log',   
]

#Faz o import dos comandos
for pkg in packages: 
    exec( rf"from src.app.configs.{pkg} import *") 


