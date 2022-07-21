from orator.migrations import Migration


class CreateTbLogs(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('logs') as table:
            table.increments('id')
            table.timestamps()
            table.string('namelog')
            table.string('text')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('logs')
