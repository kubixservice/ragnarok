import importlib
from rest_framework import permissions
from alfheimproject.settings import CONFIG, ALLOWED_HOSTS

models = importlib.import_module('core.{emu}.models'.format(emu=CONFIG['server']['conf']['emu_type']))


class AllowHostOnly(permissions.BasePermission):
    ALLOW_LIST = [] + ALLOWED_HOSTS

    def has_permission(self, request, view):
        ip_addr = request.META['REMOTE_ADDR']
        if '*' in self.ALLOW_LIST:
            return True

        return ip_addr in self.ALLOW_LIST


class IsMine(permissions.BasePermission):

    def has_permission(self, request, view):
        pk = view.kwargs.get('pk')
        if pk:
            if view.perm_type == 'Login':
                try:
                    account = models.Login.objects.get(account_id=pk)
                except models.Login.DoesNotExist:
                    return False
                return account.master_account_id == request.user.id
            elif view.perm_type == 'Char':
                try:
                    char = models.Char.objects.get(char_id=pk)
                except models.Char.DoesNotExist:
                    return False
                return char.account_id.master_account_id == request.user.id
        return True
