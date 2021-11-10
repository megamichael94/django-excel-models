from django.core.management.base import BaseCommand, CommandError
from polls.models import Question as Poll


class Command(BaseCommand):
    """
    Class that handles the command itself, parses the excel file and creates a
    model to later handle the
    """

    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        #todo: check nargs params
        parser.add_argument('file_path', nargs='+', type=str)

    def handle(self, *args, **options):
        """
        Function called once the command has been called.
        #todo: finish docstring and add to help
        """

        self.stdout.write(
            self.style.SUCCESS('Successfully imported excel files'))
