from cleo.commands.command import Command
import os
from src.core.Storage import Storage

class MigrationCommand(Command):
    """
    Criar um arquivo de migração

    migration      
        {name : Nome da migração}       
        {--table= : Nome da tabela a usar}
        {--create : Adicionando o comando de criação}
    """
    def handle(self):        
        name = self.argument("name")
        
        pathMigrations ='src/app/database/migrations'
        command_orator = rf"orator make:migration {name} -p {pathMigrations}"
        
        if self.option("table"):  command_orator = command_orator + rf" --table={self.option('table')}"
        if self.option("create"): command_orator = command_orator + " --create"       
      
            
        os.system(command_orator)
        
        
        