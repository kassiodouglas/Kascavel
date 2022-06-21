import os


class Storage():
    
    def basePath(path = ''):    
        return os.path.abspath(path)