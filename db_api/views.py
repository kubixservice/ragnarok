import importlib
from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response

from django.urls import reverse

from . import serializers

from alfheimproject.settings import CONFIG

models = importlib.import_module('core.{emu}.models'.format(emu=CONFIG['server']['conf']['emu_type']))


class ItemDBViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = None
