from flask_assets import Environment, Bundle
from src.core.Storage import Storage
import os

class BundleAssets():
    
    def __init__(self, app) -> None:        
    
        self.assets = Environment(app)
        self.js()
        self.css()
        
        
        
    def listFiles(self, dir):
        list = []
        pasta = Storage().basePath(rf'src/resources/assets/{dir}')
        for diretorio, subpastas, arquivos in os.walk(pasta):
            for arquivo in arquivos:
                list.append(os.path.join(os.path.realpath(diretorio), arquivo))
                
        print(list)                
        return list
               

    def js(self):
        js = Bundle('js/*.js', filters='jsmin', output='public/js/app.js')        
        self.assets.register('js_all', js)
        
    
    def css(self):
        
        
        
        
                
                
                
                
        listsCss = self.listFiles('scss') #['scss/*.scss','scss/navbar/*.scss']
        allsCss = []
        for file in listsCss:
            bundle = Bundle(file, filters='pyscss', output='public/css/file.css')  
            allsCss.append(bundle)   


        listCss = self.listFiles('css') #['css/fonts/*.css','css/*.css']
        allCss = []            
        for file in listCss:
            bundle = Bundle(file, filters='cssmin', output='public/css/file.css')  
            allCss.append(bundle)               

        all_css = allsCss + allCss           
        css = Bundle( all_css, filters='cssmin', output='public/css/app.css')        
        self.assets.register('css_all', css)