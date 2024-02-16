from typing import Any
from django.core.management import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Deescrption of the command'


    def handle(self, *args: Any, **options: Any) -> str | None:
        self.stdout.write('This is my sample task')