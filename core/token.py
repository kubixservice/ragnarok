import uuid


class AccountActivationTokenGenerator:
    @staticmethod
    def make_token():
        token = uuid.uuid4()
        return str(token)


account_activation_token = AccountActivationTokenGenerator()
