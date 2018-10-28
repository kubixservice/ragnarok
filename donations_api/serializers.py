from rest_framework import serializers


class DonationSerializer(serializers.Serializer):
    amount = serializers.IntegerField(min_value=1)
    points = serializers.IntegerField(min_value=1)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
