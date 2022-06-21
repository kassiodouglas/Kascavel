from orator.migrations import Migration


class UpdateLogs(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('logs') as table:
            pass

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('logs') as table:
            pass
