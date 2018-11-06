import importlib
from rest_framework import viewsets
from rest_framework import permissions

from core import permissions as perms
from main_api import serializers as main_serializers
from alfheimproject.settings import CONFIG

models = importlib.import_module('core.{emu}.models'.format(emu=CONFIG['server']['conf']['emu_type']))


class CharactersRankingViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, perms.AllowHostOnly]
    serializer_class = main_serializers.RankingCharacterSerializer

    def get_queryset(self):
        queryset = models.Char.objects.all()
        rank_type = self.request.query_params.get('t', 'level')
        group = self.request.query_params.get('group', False)

        if rank_type == 'level':
            if group:
                queryset = models.Char.objects.raw('SELECT * FROM `char` GROUP BY `class`  ORDER BY `base_level` '
                                                   'DESC, `job_level` DESC, `base_exp` DESC, `job_exp` DESC')
                return queryset
            else:
                queryset = models.Char.objects.order_by('-base_level', '-job_level', '-base_exp', '-job_exp')
        elif rank_type == 'zeny':
            if group:
                queryset = models.Char.objects.raw('SELECT * FROM `char` GROUP BY `class`  ORDER BY `base_level` '
                                                   'DESC, `job_level` DESC, `zeny` DESC')
                return queryset
            else:
                queryset = models.Char.objects.order_by('-zeny', '-base_level', '-job_level')

        # Check for class and/or name filters
        class_id = self.request.query_params.get('class')
        name = self.request.query_params.get('name')

        # Apply filters if any exist
        if class_id:
            queryset = queryset.filter(class_field=class_id)
        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class GuildRankingViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, perms.AllowHostOnly]
    serializer_class = main_serializers.GameGuildSerializer
    queryset = models.Guild.objects.all()
    lookup_url_kwarg = 'pk'

    def get_queryset(self):
        queryset = models.Guild.objects.order_by('-guild_lv', '-exp')
        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(guild_name=name)
        return queryset
