from src.core import Environment
from orator import DatabaseManager 
from src.app.configs.database import *

#---------------------------------------------
# Configuração de logs
# Configure por aqui o que precisar, posteriormente poderá cachear as informações
#---------------------------------------------

log = {
    "conn": DatabaseManager( globals()[Environment.env('LOG_CONN','CONN_DEFAULT')]),
    'table':Environment.env('LOG_TABLE','logs'),
    "driver":Environment.env('LOG_DRIVER','csv'),
    "logoff":Environment.env('LOG_OFF','FALSE'), 
}