import os

class Storage():
    
    def basePath(self, path = ''):    
        """Caminho base da aplicação"""
        return os.path.abspath(path)
    
    def pathStorage(self, dir = ''):
        """Caminho ate pasta storage"""
        return self.basePath('resources\\assets\\storage\\' + dir)
    
    def pathRpaDownloads(self, dir = ''):
        """Caminho ate pasta de downloads do RPA"""
        return self.basePath('core\\chromedriver\\downloads\\' + dir)
    
    def file_exists(self, filepath):
        """Verifica se um arquivo existe"""
        if(os.path.isfile(filepath)): return True
        return False
    
    def dir_exists(self, pathdir):
        """Verifica se um diretorio existe"""
        if(os.path.isdir(pathdir)): return True
        return False