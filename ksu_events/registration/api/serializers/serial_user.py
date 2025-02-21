from rest_framework import serializers
from registration.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'date_joined')
        read_only_fields = fields


class UserSerializerLimited(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')
        read_only_fields = fields
