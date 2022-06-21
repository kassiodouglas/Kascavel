from dotenv import dotenv_values

class Environment():
    
    def env(key, default = ''):
        """Retorna as chaves do arquvio .env"""
        env = {   
            **dotenv_values(".env.production"), 
            **dotenv_values(".env.development"),   
            **dotenv_values(".env"), 
        }
        
        value = default  if hasattr(env,key)  else env[key]    
        return value
   