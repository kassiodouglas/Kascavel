# from src.core.Environment import Environment

# db_default = {
#     'mysql': {
#         'driver': Environment.env('DB_DRIVER','mysql'),
#         'host': Environment.env('DB_HOST','localhost'),
#         'database': Environment.env('DB_DATABASE','kascavel_db'),
#         'user': Environment.env('DB_USER','root'),
#         'password': Environment.env('DB_PASSWORD',''),
#         'prefix': Environment.env('DB_PREFIX',''),
#     },
# }

DATABASES = {
    'mysql': {
        'driver': 'mysql',
        'host': 'localhost',
        'database': 'kascavel_db',
        'user': 'root',
        'password': '',
        'prefix': '',
    },
}

