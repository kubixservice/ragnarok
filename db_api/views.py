import importlib

from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response

from . import serializers
from core import permissions as perms
from core.helpers.query_helper import QueryHelper

from alfheimproject.settings import CONFIG

models = importlib.import_module('core.{emu}.models'.format(emu=CONFIG['server']['conf']['emu_type']))


class ItemDBViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, perms.AllowHostOnly]
    serializer_class = serializers.ItemDBSerializer
    queryset = models.ItemDb.objects.all()


class VendingViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, perms.AllowHostOnly]
    serializer_class = serializers.VendingSerializer

    def get_queryset(self):
        queryset = models.AutotradeData.objects.all()
        ordering = self.request.query_params.get('order', '-price')

        ordering = QueryHelper().validate_ordering(ordering, self.get_serializer().fields)
        if ordering:
            queryset = queryset.order_by(*ordering)
        return queryset
