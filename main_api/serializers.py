import importlib

from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

from core import fields
from alfheimproject.settings import CONFIG

User = get_user_model()
models = importlib.import_module('core.{emu}.models'.format(emu=CONFIG['server']['conf']['emu_type']))

MIN_ULENGTH = CONFIG['security']['validation']['min_username_length']  # min username length
MAX_ULENGTH = CONFIG['security']['validation']['max_username_length']  # max username length
MIN_PLENGTH = CONFIG['security']['validation']['min_password_length']  # min password length
MAX_PLENGTH = CONFIG['security']['validation']['max_password_length']  # max password length


class GameGuildSerializer(serializers.ModelSerializer):
    emblem_url = fields.GuildEmblemField('emblem_url')
    members_count = serializers.IntegerField(source='get_members_count')

    class Meta:
        model = models.Guild
        fields = ('guild_id', 'guild_name', 'master', 'guild_lv', 'connect_member', 'max_member', 'average_lv',
                  'exp', 'emblem_url', 'members_count')


class RankingCharacterSerializer(serializers.ModelSerializer):
    class_name = fields.ClassNameField('class_name')

    class Meta:
        model = models.Char
        fields = ('char_id', 'name', 'class_field', 'job_level', 'base_level', 'base_exp', 'job_exp',
                  'zeny', 'guild_id', 'class_name')


class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    old_password = serializers.CharField(
        style={
            'input_type': 'password'
        },
        min_length=MIN_PLENGTH,
        max_length=MAX_PLENGTH,
        required=True,
        help_text='Min. length {min}, max. length {max}'.format(min=MIN_PLENGTH, max=MAX_PLENGTH),
        label='Password',
        write_only=True
    )
    new_password = serializers.CharField(
        style={
            'input_type': 'password'
        },
        validators=[validate_password],
        min_length=MIN_PLENGTH,
        max_length=MAX_PLENGTH,
        required=True,
        help_text='Min. length {min}, max. length {max}'.format(min=MIN_PLENGTH, max=MAX_PLENGTH),
        label='Password',
        write_only=True
    )
    email = serializers.EmailField(required=False)


class ChangeGamePasswordSerializer(serializers.Serializer):
    """
    Serializer for game account password change endpoint.
    """

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    old_password = serializers.CharField(
        required=True,
        style={
            'input_type': 'password'
        },
        min_length=MIN_PLENGTH,
        max_length=MAX_PLENGTH,
        help_text='Min. length {min}, max. length {max}'.format(min=MIN_PLENGTH, max=MAX_PLENGTH),
        label='Old Password',
        write_only=True
    )
    new_password = serializers.CharField(
        required=True,
        validators=[validate_password],
        style={
            'input_type': 'password'
        },
        min_length=MIN_PLENGTH,
        max_length=MAX_PLENGTH,
        help_text='Min. length {min}, max. length {max}'.format(min=MIN_PLENGTH, max=MAX_PLENGTH),
        label='New Password',
        write_only=True
    )
    account_id = serializers.IntegerField(required=True)


class GameCharacterSerializer(serializers.ModelSerializer):
    class_name = fields.ClassNameField('class_name')

    class Meta:
        model = models.Char
        fields = ('char_id', 'account_id', 'name', 'class_field', 'class_name', 'job_level', 'base_level', 'base_exp',
                  'job_exp', 'zeny', 'str', 'agi', 'vit', 'int', 'dex', 'luk', 'max_hp', 'hp', 'max_sp', 'sp',
                  'status_point', 'skill_point', 'party_id', 'guild_id', 'pet_id', 'homun_id', 'last_map', 'last_x',
                  'last_y', 'save_map', 'save_x', 'save_y', 'partner_id', 'online', 'father', 'mother', 'child')


class GameAccountSerializer(serializers.ModelSerializer):
    userid = serializers.CharField(
        min_length=MIN_ULENGTH,
        max_length=MAX_ULENGTH,
        required=True,
        help_text='Min. length {min}, max. length {max}'.format(min=MIN_ULENGTH, max=MAX_ULENGTH),
        label='Login'
    )

    user_pass = serializers.CharField(
        style={
            'input_type': 'password'
        },
        min_length=MIN_PLENGTH,
        max_length=MAX_PLENGTH,
        required=True,
        help_text='Min. length {min}, max. length {max}'.format(min=MIN_PLENGTH, max=MAX_PLENGTH),
        label='Password',
        write_only=True,
        validators=[validate_password]
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
        min_length=MIN_PLENGTH,
        max_length=MAX_PLENGTH,
        required=True,
        help_text='Min. length {min}, max. length {max}'.format(min=MIN_PLENGTH, max=MAX_PLENGTH),
        label='Password',
        write_only=True,
        validators=[validate_password]
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


class MediumPostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=300)
    img_url = serializers.URLField()
    summary = serializers.CharField(max_length=300)
    published = serializers.DateTimeField()
    link = serializers.URLField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class WoeScheduleSerializer(serializers.Serializer):
    start_day = fields.DayOfWeekField()
    start_time = serializers.TimeField()
    end_day = fields.DayOfWeekField()
    end_time = serializers.TimeField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

# class RSSFeedTagSerializer(serializers.Serializer):
#     term = serializers.CharField(max_length=100)
#
#     def update(self, instance, validated_data):
#         pass
#
#     def create(self, validated_data):
#         pass
#
#
# class RSSFeedSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     link = serializers.URLField()
#     tags = RSSFeedTagSerializer(many=True, read_only=True)
#     author = serializers.CharField(max_length=255)
#     published = serializers.DateTimeField()
#     summary = serializers.CharField(max_length=999)
#
#     def update(self, instance, validated_data):
#         pass
#
#     def create(self, validated_data):
#         pass
