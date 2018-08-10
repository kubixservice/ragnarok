import uuid


class AccountActivationTokenGenerator(object):
    @staticmethod
    def make_token():
        _token = uuid.uuid4()
        return str(_token)


account_activation_token = AccountActivationTokenGenerator()
