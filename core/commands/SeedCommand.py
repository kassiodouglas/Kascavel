from cleo.commands.command import Command
import os

class SeedCommand(Command):
    """
    Executa os seeders

    seed     
        {seeder?  : Nome do seeder}              
    """
    def handle(self):              
        
        pathSeeders ='app/database/seeders'
        config = rf" --config=core/commands/__migrate_db__.py --path={pathSeeders}"
        command_orator = rf"orator db:seed" 
        
      
        
        if self.argument("seeder"):     
            seeder = self.argument("seeder")        
            command_orator_toexec = command_orator + rf" --seeder {seeder} {config}" 
        else:
            command_orator_toexec = command_orator + config            

        os.system(command_orator_toexec + " --force")