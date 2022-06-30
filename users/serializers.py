from asyncore import read, write
from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField()
    first_name = serializers.CharField(max_length=50)
    last_name =serializers.CharField(max_length=50)
    date_joined = serializers.DateField()
    updated_at = serializers.DateField(read_only=True)


    def vaidate_email(self, value):
        norm_email = value.lower()
        if User.objects.filter(email__iexact=norm_email).exists():
            raise serializers.ValidationError({"email":["email already exists"]})
        return norm_email

    def create(self, validated_data):
        user = User.objects.create_use(**validated_data)
        return user
