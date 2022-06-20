from src.core import Environment

conn_db_mysql = {
    'mysql': {
        'driver': 'mysql',
        'host': 'localhost',
        'database': 'ssnake',
        'user': 'root',
        'password': '',
        'prefix': ''
    },
}


conn_db_log = { 
    'sqlite': {
        'driver': 'sqlite',        
        'database': 'src/app/database/log.sqlite3',        
        'prefix': ''
    }
}