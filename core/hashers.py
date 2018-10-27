import bcrypt
import hashlib

from alfheimproject.settings import CONFIG


class PasswordHasher:
    """PasswordHasher provide methods to encrypt game account passwords"""
    def __init__(self, hash_type):
        self.hash_type = hash_type

    """Main method"""
    def hash_password(self, password):
        if self.hash_type == 'bcrypt':  # BCrypt hashing
            password = self.bcrypt(password)
        elif self.hash_type == 'md5':  # MD5 hashing
            password = self.md5(password)
        return password

    """BCrypt hashing"""
    def bcrypt(self, password):
        salt = bcrypt.gensalt(rounds=CONFIG['security']['bcrypt']['rounds'],
                              prefix=CONFIG['security']['bcrypt']['prefix'])

        hashed = bcrypt.hashpw(str(password).encode('utf-8'), salt)
        return hashed.decode('utf-8')

    """md5 no-salt hashing"""
    def md5(self, password):
        hashed = hashlib.md5(password.encode('utf-8')).hexdigest()
        return hashed


hasher = PasswordHasher(CONFIG['security']['game_account']['password_hasher'])
