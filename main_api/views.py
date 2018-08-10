import datetime
import importlib

from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from . import serializers
from . import models as main_models
from . import permissions as perms

from core.core import server
from core.token import account_activation_token
from alfheimproject.settings import CONFIG

models = importlib.import_module('core.{emu}.models'.format(emu=CONFIG['server']['conf']['emu_type']))


class MainUserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated, perms.AllowHostOnly]

    def retrieve(self, request, *args, **kwargs):
        user = get_object_or_404(User.objects.all(), pk=request.user.id)
        serializer = serializers.UserSerializer(user)
        return Response(serializer.data)

    def perform_create(self, serializer):
        if CONFIG['security']['email_verification']:
            token = account_activation_token.make_token()
            expiration_date = datetime.date.today() + datetime.timedelta(
                days=CONFIG['security']['verification_key_expire'])
            instance = serializer.save(is_active=False)
            main_models.UserVerification.objects.create(
                user=instance,
                token=token,
                expiration_date=expiration_date
            )
        else:
            serializer.save(is_active=True)


class GameCharacterViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated, perms.AllowHostOnly, perms.IsMine]
    queryset = models.Char.objects.all()
    perm_type = 'Char'

    def retrieve(self, request, pk=None, *args, **kwargs):
        character = get_object_or_404(models.Char.objects.all(), pk=pk)

        action = request.query_params.get('action', False)
        if action == 'reset_position':
            character.reset_position()
        elif action == 'reset_look':
            character.reset_look()

        serializer = serializers.GameCharacterSerializer(character)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = models.Char.objects.filter(account_id__master_account=request.user.id)
        serializer = serializers.GameCharacterSerializer(queryset, many=True)
        return Response(serializer.data)


class GameAccountViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, perms.AllowHostOnly, perms.IsMine]
    serializer_class = serializers.GameAccountSerializer
    queryset = models.Login.objects.all()
    perm_type = 'Login'

    def retrieve(self, request, pk=None, *args, **kwargs):
        account = get_object_or_404(models.Login.objects.all(), pk=pk)
        serializer = serializers.GameAccountSerializer(account)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = models.Login.objects.filter(master_account=request.user.id)
        serializer = serializers.GameAccountSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(master_account=self.request.user, email=self.request.user.email)


class ServerRatesViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated, perms.AllowHostOnly]

    def retrieve(self, request):
        serializer = serializers.ServerRatesSerializer(CONFIG['server']['rates'])
        return Response(serializer.data)


class ServerStatusViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated, perms.AllowHostOnly]

    def retrieve(self, request):
        _status = server.get_server_status()
        _online = server.get_online_status()
        data = {**_status, **_online}
        serializer = serializers.ServerStatusSerializer(data)
        return Response(serializer.data)