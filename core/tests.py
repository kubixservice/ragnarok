import bcrypt
import hashlib

from django.test import TestCase

from .hashers import hasher


class TestModelsImport(TestCase):
    def setUp(self):
        self.password = 'password'
        self.bcrypt_password = self.bcrypt()
        self.md5_password = self.md5()

    def test_hasher(self):
        password = hasher.hash_password(self.password)
        self.assertEqual(password, self.bcrypt_password)
        self.assertEqual(password, self.md5_password)

    def bcrypt(self):
        salt = bcrypt.gensalt()
        password = bcrypt.hashpw(str(self.password).encode('utf-8'), salt)
        return password

    def md5(self):
        password = hashlib.md5(self.password.encode('utf-8')).hexdigest()
        return password
