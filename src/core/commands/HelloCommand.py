from cleo.commands.command import Command

class HelloCommand(Command):
    """
    Hello

    hello
        {name? : Who do you want to say hello?} 
        {--u|upper : upper the text}       
    """
    def handle(self):
        name = self.argument("name")

        if name:
            text = f"Hello {name}"
        else:
            text = "-.-!"       

        if self.option("upper"):
            text = text.upper() 

        self.line(rf"<info>{text}</info>")