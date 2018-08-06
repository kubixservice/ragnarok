from rest_framework import permissions

from core import models

from alfheimproject.settings import ALLOWED_HOSTS


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
            try:
                account = models.Login.objects.get(account_id=pk)
            except models.Login.DoesNotExist:
                return False

            return account.master_account_id == request.user.id

        return True
