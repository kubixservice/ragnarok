import hashlib

import bcrypt

from .exceptions import RagnarokConfigError
from alfheimproject.settings import CONFIG


class PasswordHasher:

    @staticmethod
    def hash_password(password):
        _type = CONFIG['security']['password_hasher']
        if isinstance(_type, int):
            if _type == 1:  # BCrypt hashing
                password = PasswordHasher.bcrypt(password)
            elif _type == 2:  # MD5 hashing
                password = PasswordHasher.md5(password)
            return password
        else:
            raise RagnarokConfigError('{cls}:{method}: security > password_hasher must be integer'.format(
                cls=__class__.__name__,
                method=__class__.hash_password.__name__
            ))

    @staticmethod
    def bcrypt(password):
        salt = bcrypt.gensalt(rounds=CONFIG['security']['bcrypt']['rounds'])
        _hash = bcrypt.hashpw(str(password).encode('utf-8'), salt)
        return _hash.decode('utf-8')

    @staticmethod
    def md5(password):
        _hash = hashlib.md5(password.encode('utf-8')).hexdigest()
        return _hash


hasher = PasswordHasher()
