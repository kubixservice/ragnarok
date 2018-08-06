from rest_framework import serializers

from django.contrib.auth.models import User

from core import models


class GameCharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Char
        fields = ('char_id', 'account_id', 'name', 'class_field', 'job_level', 'base_level', 'base_exp', 'job_exp',
                  'zeny', 'str', 'agi', 'vit', 'int', 'dex', 'luk', 'max_hp', 'hp', 'max_sp', 'sp', 'status_point',
                  'skill_point', 'party_id', 'guild_id', 'pet_id', 'homun_id', 'last_map', 'last_x', 'last_y',
                  'save_map', 'save_x', 'save_y', 'partner_id', 'online', 'father', 'mother', 'child')


class GameAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Login
        fields = ('account_id', 'userid', 'sex', 'email', 'group_id', 'state', 'unban_time', 'logincount', 'last_ip',
                  'birthdate', 'user_pass')
        read_only_fields = ('account_id', 'group_id', 'state', 'unban_time', 'logincount', 'last_ip',
                            'birthdate', 'email')
        extra_kwargs = {'user_pass': {'write_only': True}}


class UserSerializer(serializers.ModelSerializer):
    game_account = GameAccountSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'is_active', 'game_account')
