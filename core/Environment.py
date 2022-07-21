from dotenv import dotenv_values

class Environment():
    
    def env(key, default = ''):
        """Retorna as chaves do arquvio .env"""
        env = {   
            **dotenv_values(".env.production"), 
            **dotenv_values(".env.development"),   
            **dotenv_values(".env"), 
        }       

        
        # return env[key] if hasattr(env,key) else default
        return env[key] if key in env else default
    
    
    def cache(key, default =''):
        pass
  