from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from . import serializers
from . import permissions as perms
from core import models


class MainUserViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated, perms.AllowHostOnly]

    def retrieve(self, request, *args, **kwargs):
        user = get_object_or_404(User.objects.all(), pk=request.user.id)
        serializer = serializers.UserSerializer(user)
        return Response(serializer.data)


class GameCharacterViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated, perms.AllowHostOnly]
    queryset = models.Char.objects.all()

    def retrieve(self, request, pk=None, *args, **kwargs):
        character = get_object_or_404(models.Char.objects.all(), pk=pk)
        serializer = serializers.GameCharacterSerializer(character)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        game_account_id = request.query_params.get('ga_id')
        if game_account_id:
            queryset = models.Char.objects.filter(account_id=game_account_id)
        else:
            queryset = models.Char.objects.filter(account_id__master_account=request.user.id)
        serializer = serializers.GameCharacterSerializer(queryset, many=True)
        return Response(serializer.data)


class GameAccountViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, perms.AllowHostOnly, perms.IsMine]
    serializer_class = serializers.GameAccountSerializer
    queryset = models.Login.objects.all()

    def retrieve(self, request, pk=None, *args, **kwargs):
        account = get_object_or_404(models.Login.objects.all(), pk=pk)
        serializer = serializers.GameAccountSerializer(account)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = models.Login.objects.filter(master_account=request.user.id)
        serializer = serializers.GameAccountSerializer(queryset, many=True)
        return Response(serializer.data)
