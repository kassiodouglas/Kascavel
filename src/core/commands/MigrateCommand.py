from cleo.commands.command import Command
import os
# from src.app.configs.database import db_default

class MigrateCommand(Command):
    """
    Executas as migrações

    migrate      
        {--rollback : Volta os dados a ultima migração}       
        {--reset : Volta todas as migrações}
        {--status : Verifica o status das migrações}
        {--fresh : Roda do zero as migrações}
    """
    def handle(self):        
        command_orator = rf"orator migrate"
        config = " --config=src/app/configs/database.py --path=src/app/database/migrations"
        
        if self.option("rollback"):  
            command_orator_toexec = command_orator + rf":rollback"
        elif self.option("reset") or self.option("fresh"):  
            command_orator_toexec = command_orator + rf":reset {config}"
        elif self.option("status"):  
            command_orator_toexec = command_orator + rf":status {config}"
        else: 
            command_orator_toexec = command_orator + config        
      
        os.system(command_orator_toexec + " --force")
        
        if self.option("fresh"): 
             os.system(command_orator + config + " --force")
        
        