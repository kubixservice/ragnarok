import importlib

from rest_framework import serializers
from django.contrib.auth.models import User

from core import fields
from alfheimproject.settings import CONFIG

models = importlib.import_module('core.{emu}.models'.format(emu=CONFIG['server']['conf']['emu_type']))


class GameGuildSerializer(serializers.ModelSerializer):
    emblem_url = fields.GuildEmblemField('emblem_url')
    members_count = serializers.IntegerField(source='get_members_count')

    class Meta:
        model = models.Guild
        fields = ('guild_id', 'guild_name', 'master', 'guild_lv', 'connect_member', 'max_member', 'average_lv',
                  'exp', 'emblem_url', 'members_count')


class RankingCharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Char
        fields = ('char_id', 'name', 'class_field', 'job_level', 'base_level', 'base_exp', 'job_exp',
                  'zeny', 'guild_id')


class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class GameCharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Char
        fields = ('char_id', 'account_id', 'name', 'class_field', 'job_level', 'base_level', 'base_exp', 'job_exp',
                  'zeny', 'str', 'agi', 'vit', 'int', 'dex', 'luk', 'max_hp', 'hp', 'max_sp', 'sp', 'status_point',
                  'skill_point', 'party_id', 'guild_id', 'pet_id', 'homun_id', 'last_map', 'last_x', 'last_y',
                  'save_map', 'save_x', 'save_y', 'partner_id', 'online', 'father', 'mother', 'child')


class GameAccountSerializer(serializers.ModelSerializer):
    userid = serializers.CharField(
        min_length=CONFIG['security']['min_username_length'],
        max_length=CONFIG['security']['max_username_length'],
        required=True,
        help_text='Min. length {min}, max. length {max}'.format(min=CONFIG['security']['min_username_length'],
                                                                max=CONFIG['security']['max_username_length']),
        label='Login'
    )

    user_pass = serializers.CharField(
        style={
            'input_type': 'password'
        },
        min_length=CONFIG['security']['min_password_length'],
        max_length=CONFIG['security']['max_password_length'],
        required=True,
        help_text='Min. length {min}, max. length {max}'.format(min=CONFIG['security']['min_password_length'],
                                                                max=CONFIG['security']['max_password_length']),
        label='Password',
        write_only=True
    )

    sex = serializers.ChoiceField(
        choices=['M', 'F'],
        required=True,
        help_text='Account gender',
        label='Gender',
    )

    class Meta:
        model = models.Login
        fields = ('account_id', 'userid', 'sex', 'email', 'group_id', 'state', 'unban_time', 'logincount', 'last_ip',
                  'birthdate', 'user_pass')
        read_only_fields = ('account_id', 'group_id', 'state', 'unban_time', 'logincount', 'last_ip',
                            'birthdate', 'email')
        extra_kwargs = {
            'user_pass': {
                'write_only': True
            },
        }

    def validate(self, attrs):
        if models.Login.objects.filter(userid=attrs['userid']).exists():
            raise serializers.ValidationError({'userid': 'User with this login already exists'}, 'user_already_exists')
        return attrs


class UserSerializer(serializers.ModelSerializer):
    game_accounts = GameAccountSerializer(many=True, read_only=True)
    password = serializers.CharField(
        style={
            'input_type': 'password'
        },
        min_length=CONFIG['security']['min_password_length'],
        max_length=CONFIG['security']['max_password_length'],
        required=True,
        help_text='Min. length {min}, max. length {max}'.format(min=CONFIG['security']['min_password_length'],
                                                                max=CONFIG['security']['max_password_length']),
        label='Password',
        write_only=True
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'is_active', 'game_accounts', 'password')
        read_only_fields = ('first_name', 'last_name', 'is_active', 'game_accounts')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }


class ServerRatesSerializer(serializers.Serializer):
    base_exp_rate = serializers.IntegerField()
    job_exp_rate = serializers.IntegerField()
    quest_exp_rate = serializers.IntegerField()
    mvp_exp_rate = serializers.IntegerField()
    common = serializers.IntegerField()
    common_boss = serializers.IntegerField()
    heal = serializers.IntegerField()
    heal_boss = serializers.IntegerField()
    useable = serializers.IntegerField()
    useable_boss = serializers.IntegerField()
    equip = serializers.IntegerField()
    equip_boss = serializers.IntegerField()
    card = serializers.IntegerField()
    card_boss = serializers.IntegerField()
    mvp_item = serializers.IntegerField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class ServerStatusSerializer(serializers.Serializer):
    map_server = serializers.IntegerField()
    char_server = serializers.IntegerField()
    login_server = serializers.IntegerField()
    discord_online = serializers.IntegerField()
    server_online = serializers.IntegerField()
    highest_peak = serializers.IntegerField()
    peak_date = serializers.DateField()
    discord_updated = serializers.DateTimeField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
