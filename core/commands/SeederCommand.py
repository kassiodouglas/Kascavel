from cleo.commands.command import Command
import os

class SeederCommand(Command):
    """
    Cria um seeder

    seeder      
        {name : Nome do seeder}              
    """
    def handle(self):        
        name = self.argument("name")
        
        pathSeeders ='app/database/seeders'
        command_orator = rf"orator make:seed {name} -p {pathSeeders}"        
            
        os.system(command_orator)