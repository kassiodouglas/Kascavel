from core.Environment import Environment

#---------------------------------------------
# Base de dados padrão da aplicação
# Sempre deve existir pois é utilizada em funções do nucleo
#---------------------------------------------

CONN = {
    'default': 'pygso',
    
    Environment.env('DB_CONN','pygso'): {
        'driver': Environment.env('DB_DRIVER','mysql'),
        'host': Environment.env('DB_HOST','localhost'),
        'port': int(Environment.env('DB_PORT',3306)),
        'database': Environment.env('DB_DATABASE','kascavel_db'),
        'user': Environment.env('DB_USER','root'),
        'password': Environment.env('DB_PASSWORD','')
    },
    
    #---------------------------------------------
    # Pode ser adicionado outras conexões abaixo
    # Descomente e edite as linhas abaixo ou crie mais
    # Aceito os drivers: sqlite, mysql, PostgreSQL
    #---------------------------------------------

    # Environment.env('KEY_DB_CONN',''): {
    #     'driver': Environment.env('KEY_DB_DRIVER',''),
    #     'host': Environment.env('KEY_DB_HOST',''),
    #     'port': int(Environment.env('KEY_DB_PORT',)),
    #     'database': Environment.env('KEY_DB_DATABASE',''),
    #     'user': Environment.env('KEY_DB_USER',''),
    #     'password': Environment.env('KEY_DB_PASSWORD','')
    # },
}


