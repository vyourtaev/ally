from rest_framework import serializers
from api.models import Stack, Service, Port, STYLE_CHOICES, LANGUAGE_CHOICES


class PortSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Port


class ServiceSerializer(serializers.ModelSerializer):
    ports = serializers.StringRelatedField(many=True)

    class Meta:
        fields = '__all__'
        model = Service


class StackSerializer(serializers.ModelSerializer):
    services = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        fields = '__all__'
        model = Stack
