import datetime
import importlib

from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from . import serializers
from . import models as main_models
from core import permissions as perms

from core.core import server
from core.token import account_activation_token
from core.medium import get_medium_posts
from alfheimproject.settings import CONFIG

User = get_user_model()
models = importlib.import_module('core.{emu}.models'.format(emu=CONFIG['server']['conf']['emu_type']))


class UserVerificationViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, *args, **kwargs):
        token = self.request.query_params.get('token', None)
        response = {
            'message': '',
            'code': 0
        }

        if not token:
            response['message'] = 'Bad request'
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        try:
            verification = main_models.UserVerification.objects.get(token=token)
        except main_models.UserVerification.DoesNotExist:
            response['message'] = 'Token not found, request new'
            response['code'] = 1
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        if not verification.is_available:
            response['message'] = 'Token not available'
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        if verification.user.is_active:
            response['message'] = 'User already active'
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        current_date = datetime.date.today()
        if current_date > verification.expiration_date:
            response['message'] = 'Token not found, request new'
            response['code'] = 1
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        verification.is_available = False
        verification.user.is_active = True
        verification.save()
        verification.user.save()
        response['message'] = 'User activated'
        return Response(response, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        data = self.request.data

        try:
            user = User.objects.get(email=data['email'])
        except User.DoesNotExist:
            return Response({'message': 'User with this email does not exist'}, status=status.HTTP_404_NOT_FOUND)

        if user.is_active:
            return Response({'message': 'User already active'}, status=status.HTTP_400_BAD_REQUEST)

        token = account_activation_token.make_token()
        expiration_date = datetime.date.today() + datetime.timedelta(days=CONFIG['security']['verification_key_expire'])
        user.verification.create(
            token=token,
            expiration_date=expiration_date,
            created_date=datetime.date.today()
        )
        return Response({'message': 'Verification was sent'}, status=status.HTTP_200_OK)


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


class PasswordUpdateViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ChangePasswordSerializer
    permission_classes = [permissions.AllowAny, perms.AllowHostOnly]

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            user = self.request.user
            if not user:
                try:
                    user = User.objects.get(email=data.get('email'))
                except User.DoesNotExist:
                    return Response('User not found', status=status.HTTP_404_NOT_FOUND)

            if not user.check_password(data.get('old_password')):
                return Response({'old_password': 'Incorrect old password'}, status=status.HTTP_400_BAD_REQUEST)
            user.set_password(data.get('new_password'))
            user.save()
            return Response('Password has been updated', status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GamePasswordUpdateViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ChangeGamePasswordSerializer
    permission_classes = [permissions.AllowAny, perms.AllowHostOnly]

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            account_id = data.get('account_id')
            if account_id:
                try:
                    account = models.Login.objects.get(account_id=account_id)
                except models.Login.DoesNotExist:
                    return Response('Account not found', status=status.HTTP_404_NOT_FOUND)

                if not account.check_password(data.get('old_password')):
                    return Response({'old_password': 'Incorrect old password'}, status=status.HTTP_400_BAD_REQUEST)
                account.set_password(data.get('new_password'))
                account.save()
                return Response('Password has been updated', status=status.HTTP_200_OK)
            else:
                return Response('account_id not found', status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


class MediumViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request):
        data = get_medium_posts()
        serializer = serializers.MediumPostSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class WoeScheduleViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        woe = []
        for schedule in CONFIG['woe']:
            woe.append({
                'start_day': schedule[0],
                'start_time': schedule[1],
                'end_day': schedule[2],
                'end_time': schedule[3]
            })
        serializer = serializers.WoeScheduleSerializer(woe, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# class RSSFeedViewSet(viewsets.ViewSet):
#     permission_classes = [permissions.AllowAny]
#
#     def list(self, request):
#         rss = feed()
#         serializer = serializers.RSSFeedSerializer(rss, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
