from rest_framework import viewsets
from rest_framework import permissions

from main_api import permissions as perms
from . import serializers
from . import models

from core.helpers.query_helper import QueryHelper


class CharBattlegroundsViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, perms.AllowHostOnly]
    serializer_class = serializers.CharBattlegroundsSerializer
    queryset = models.CharBg.objects.all()

    def get_queryset(self):
        # default queryset
        queryset = models.CharBg.objects.order_by('-score').all()
        guild = self.request.query_params.get('guild', None)
        if guild:
            queryset = queryset.filter(char_id__guild_id=guild)

        name = self.request.query_params.get('name', None)
        if name:
            queryset = queryset.filter(char_id__name=name)

        ordering = self.request.query_params.get('ordering', None)
        ordering = QueryHelper.validate_ordering(ordering, self.get_serializer().fields)
        if ordering:
            queryset = queryset.order_by(*ordering)
        return queryset


class CharWoeViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, perms.AllowHostOnly]
    serializer_class = serializers.CharWoeSerializer
    queryset = models.CharWstats.objects.order_by('-score').all()

    def get_queryset(self):
        # default queryset
        queryset = models.CharWstats.objects.order_by('-score').all()
        woe_date = self.request.query_params.get('woe_date', None)
        if woe_date:
            queryset = queryset.filter(woe_date=woe_date)

        guild = self.request.query_params.get('guild', None)
        if guild:
            queryset = queryset.filter(char_id__guild_id=guild)

        name = self.request.query_params.get('name', None)
        if name:
            queryset = queryset.filter(char_id__name=name)

        ordering = self.request.query_params.get('ordering', None)
        ordering = QueryHelper.validate_ordering(ordering, self.get_serializer().fields)
        if ordering:
            queryset = queryset.order_by(*ordering)
        return queryset


class CharWoeSkillCountViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.AllowAny, perms.AllowHostOnly]
    serializer_class = serializers.CharWoeSkillCountSerializer
    queryset = models.SkillCount.objects.all()
    lookup_url_kwarg = 'pk'

    def get_queryset(self):
        char_id = self.kwargs.get(self.lookup_url_kwarg)
        queryset = models.SkillCount.objects.filter(char_id=char_id).all()
        return queryset


class CharBattlegroundsSkillCountViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.AllowAny, perms.AllowHostOnly]
    serializer_class = serializers.CharBattlegroundsSkillCountSerializer
    queryset = models.BgSkillCount.objects.all()
    lookup_url_kwarg = 'pk'

    def get_queryset(self):
        char_id = self.kwargs.get(self.lookup_url_kwarg)
        queryset = models.BgSkillCount.objects.filter(char_id=char_id).all()
        return queryset
