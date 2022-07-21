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
    'BundleAssets',   
]

#Faz o import dos comandos
for pkg in packages: 
    exec( rf"from core.{pkg} import {pkg}") 

