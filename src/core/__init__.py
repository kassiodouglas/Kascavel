#core

#Lista de pacotes 
packages = [
    'Storage',
    'Environment',
    'Router',
]

#Faz o import dos pacotes
for pkg in packages: 
    exec( rf"from src.core.{pkg} import {pkg}") 


    





    


