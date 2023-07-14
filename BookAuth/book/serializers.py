from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Book
from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'author', 'price']

    def get_read_only_fields(self):
        read_only_fields = super().get_read_only_fields()
        read_only_fields.extend(['id', 'author'])

        return read_only_fields


User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'date_of_birth']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
