import os
from dotenv import dotenv_values


def env(key):
    """_summary_

    Args:
        key (string): chave no arquivo .env

    Returns:
        _type_: string
    """
    env = {   
        **dotenv_values(".env.production"), 
        **dotenv_values(".env.development"),   
        **dotenv_values(".env"), 
    }
    return env[key]
    