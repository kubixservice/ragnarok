import os
import commentjson

from django.core.management.base import BaseCommand, CommandError

from ._config import ConfigValidator
from alfheimproject.settings import BASE_DIR


class Command(BaseCommand):
    help = 'This command will validate setup'

    def handle(self, *args, **options):

        try:
            with open(os.path.join(BASE_DIR, 'alfheimproject/conf/config.json')) as config:
                config_json = commentjson.load(config)
        except FileNotFoundError:
            raise CommandError('config.json not found. Did you forgot to add it?')

        validator = ConfigValidator(config_json)

        if validator.is_valid():
            self.stdout.write('Configuration file is valid, now you can enable your site.')
        else:
            self.stdout.write('Configuration is not valid, please check main.log')
            self.stdout.write('We created a config.test.json file with valid configuration for you.')
            with open('config.test.json', 'w+') as file:
                json = commentjson.dumps(validator.config)
                file.write(json)
