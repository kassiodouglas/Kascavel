from cleo.commands.command import Command
from flask import Flask
from src.core import Router, BundleAssets
from src.core.Storage import Storage
from src.routes import web, api, error
from flask_assets import Environment, Bundle

class ServerCommand(Command):
    """
    Inicia o servidor

    server
        {--host=localhost : Host do servidor} 
        {--p|port=9000 : Porta do servidor}   
        {--d|debug : Modo de debug}       
    """
    def handle(self):
        app = Flask(__name__, 
            static_folder=Storage().basePath('src/resources/assets'),
            template_folder=Storage().basePath('src/resources/views')
        )     
        
        Router().router(app, web.routes, api.routes, error.routes)
        
        BundleAssets(app)      
        
        app.run(
            host='localhost' if self.option('host') else self.option('host'),
            port=9000 if self.option('port') else self.option('port'),
            debug=True if self.option('debug') else False
        )
        