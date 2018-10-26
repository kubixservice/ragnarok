import importlib

from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from django.urls import reverse

from . import serializers
from core import permissions as perms
from alfheimproject.settings import CONFIG

models = importlib.import_module('core.{emu}.models'.format(emu=CONFIG['server']['conf']['emu_type']))


class ItemDBViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, perms.AllowHostOnly]
    serializer_class = serializers.ItemDBSerializer
    queryset = models.ItemDb.objects.all()


class VendingViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, perms.AllowHostOnly]
    serializer_class = serializers.VendingSerializer
    queryset = models.AutotradeData.objects.all()

    def get_queryset(self):
        queryset = models.AutotradeData.objects.all()
        return queryset
