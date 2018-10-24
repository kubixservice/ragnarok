from django.core.exceptions import ValidationError
from django.core.validators import validate_ipv4_address, URLValidator
from alfheimproject.local_settings import logger


class ConfigValidator(object):
    """
    ConfigValidator provide validator for configuration file
    """
    domain_whitelist = ['localhost', 'http://localhost/']
    server_types = ['RE', 'Pre-RE']
    emu_types = ['hercules', 'rathena']
    fields = [
        # Field, expected type, min length, default value
        ('debug', bool, 0, False),
        ('server_name', str, 1, 'YourRO'),
        ('server_ip', str, 0, 'localhost'),
        ('server_domain', str, 0, 'http://localhost/'),
        ('map_port', int, 0, 5121),
        ('char_port', int, 0, 6121),
        ('login_port', int, 0, 6900),
        ('server_type', str, 2, 'RE'),
        ('emu_type', str, 7, 'hercules')
    ]
    message = '{field} is not valid, writing default [{default}]'

    def __init__(self, config):
        self.config = config
        self.errors = []
        self.validate()

    def validate(self):
        if not isinstance(self.config, dict):
            logger.error('unexcepted config format')
            raise TypeError('configuration type error. expected dict, got {err_}'.format(err_=type(self.config)))

        for field in self.fields:
            valid = True
            value = self.config['server']['conf'][field[0]]
            if value:
                if field[0] == 'server_ip' and value not in self.domain_whitelist:
                    try:
                        validate_ipv4_address(value)
                    except ValidationError:
                        valid = False
                elif field[0] == 'server_domain' and value not in self.domain_whitelist:
                    url_validator = URLValidator()
                    try:
                        url_validator(value)
                    except ValidationError:
                        valid = False
                elif (field[0] == 'server_type' and value not in self.server_types) or (
                        field[0] == 'emu_type' and value not in self.emu_types):
                    valid = False
                else:
                    if not isinstance(value, field[1]) or (field[2] > 0 and len(value) < field[2]):
                        valid = False

                if not valid:
                    self.config['server']['conf'][field[0]] = field[3]
                    logger.warn(self.message.format(field=field[0], default=field[3]))
                    self.errors.append(self.message.format(field=field[0], default=field[3]))

    def is_valid(self):
        return not len(self.errors)
