from src.core import Environment

app = {
    'name':     Environment.env('APP_NAME','sSnake'),
    'debug':    Environment.env('APP_DEBUG','True'),
    'ambient':  Environment.env('APP_AMBIENT','local'),  
    'key':      Environment.env('APP_KEY',''),   
}