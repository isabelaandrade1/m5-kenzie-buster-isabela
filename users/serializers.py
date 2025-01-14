from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'birthdate',
            'first_name', 'last_name', 'password',
            'is_employee', 'is_superuser'
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'is_superuser': {'read_only': True},
            'is_employee': {'read_only': True},
        }

    def create(self, validated_data):
        if User.objects.filter(email=validated_data.get('email')).exists():
            raise serializers.ValidationError({"email": "email already registered."})
        if User.objects.filter(username=validated_data.get('username')).exists():
            raise serializers.ValidationError({"username": "username already taken."})

        is_employee = validated_data.pop('is_employee', False)
        user = User(**validated_data)
        user.is_employee = is_employee
        user.is_superuser = is_employee
        user.password = make_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        # Verifica se a senha está sendo atualizada
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        
        # Atualiza os campos válidos
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance
