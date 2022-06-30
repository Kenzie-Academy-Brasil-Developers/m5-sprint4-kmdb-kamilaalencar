from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(max_length=50)
    last_name =serializers.CharField(max_length=50)
    date_joined = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)


    def validate_email(self, value):
        norm_email = value.lower()
        if User.objects.filter(email__iexact=norm_email).exists():
            raise serializers.ValidationError({"email already exists"})
        return norm_email

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
