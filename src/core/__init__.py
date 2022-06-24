#core    

#Lista de pacotes
packages = [
    'Storage',
    'Environment',
    'Router',
    'Email',
    'IA',
    'Log',
    'Queue',
    'Rpa',
    'Session',    
]

#Faz o import dos comandos
for pkg in packages: 
    exec( rf"from src.core.{pkg} import {pkg}") 

