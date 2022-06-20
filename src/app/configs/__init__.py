#app/configs

#Lista de pacotes
packages = [
    'app',
    'database',
]

#Faz o import dos pacotes
for pkg in packages: 
    exec( rf"from ..configs.{pkg} import *") 