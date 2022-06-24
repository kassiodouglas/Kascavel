from src.core.Environment import Environment

#---------------------------------------------
# Base de dados padrão da aplicação
# Sempre deve existir pois é utilizada em funções do nucleo
#---------------------------------------------

CONN_DEFAULT = {
    Environment.env('DB_DRIVER','mysql'): {
        'driver': Environment.env('DB_DRIVER','mysql'),
        'host': Environment.env('DB_HOST','localhost'),
        'database': Environment.env('DB_DATABASE','kascavel_db'),
        'user': Environment.env('DB_USER','root'),
        'password': Environment.env('DB_PASSWORD','')
    },
}

#---------------------------------------------
# Pode ser adicionado outras conexões abaixo
# Descomente e edite as linhas abaixo ou crie mais
# Aceito os drivers: sqlite, mysql, PostgreSQL
#---------------------------------------------

# db = {
#     'sqlite': {
#         'driver': 'sqlite',
#         'host': '',
#         'database': '',
#         'user': '',
#         'password': ''   
#     },
# }
