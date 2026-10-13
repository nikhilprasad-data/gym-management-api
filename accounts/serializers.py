from django.contrib.auth import authenticate
from dataclasses import field
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']


    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )

        return user

class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username','password']

    def validate(self,data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username,password=password)

            if not user:
                raise serializers.ValidationError("Invalid username or password.")
        else:
            raise serializers.ValidationError("Must include username and password.")

        data['user'] = user
        return data
