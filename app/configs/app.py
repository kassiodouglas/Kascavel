from core import Environment

#---------------------------------------------
# Configurações da aplicação
# Configure por aqui o que precisar, posteriormente poderá cachear as informações
# Outras chaves podem ser adicionadas dentro da chave 'app'
#---------------------------------------------

app = {
    'name':     Environment.env('APP_NAME','KascavelFramework'),
    'debug':    Environment.env('APP_DEBUG','True'),
    'ambient':  Environment.env('APP_AMBIENT','local'),  
    'key':      Environment.env('APP_KEY',''),   
}