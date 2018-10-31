import importlib
from rest_framework import serializers

from core import fields
from alfheimproject.settings import CONFIG

models = importlib.import_module('core.{emu}.models'.format(emu=CONFIG['server']['conf']['emu_type']))


class ItemDBSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ItemDb
        fields = '__all__'


class MerchantSerializer(serializers.ModelSerializer):
    class_name = fields.ClassNameField('class_name')

    class Meta:
        model = models.Char
        fields = ('name', 'class_field', 'class_name', 'last_map', 'last_x', 'last_y')


class CartInventorySerializer(serializers.ModelSerializer):
    nameid = ItemDBSerializer(many=False, read_only=True)
    card0 = ItemDBSerializer(many=False, read_only=True)
    card1 = ItemDBSerializer(many=False, read_only=True)
    card2 = ItemDBSerializer(many=False, read_only=True)
    card3 = ItemDBSerializer(many=False, read_only=True)

    class Meta:
        model = models.CartInventory
        fields = ('nameid', 'refine', 'attribute', 'card0', 'card1', 'card2', 'card3')


class VendingSerializer(serializers.ModelSerializer):
    character = MerchantSerializer(many=False, read_only=True)
    item = CartInventorySerializer(many=False, read_only=True)
    title = serializers.CharField(max_length=255, source='vending_title')
    map_image = fields.GatField(source='current_map')

    class Meta:
        model = models.AutotradeData
        fields = ('character', 'item', 'amount', 'price', 'title', 'map_image')
