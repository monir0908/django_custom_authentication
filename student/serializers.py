from rest_framework import serializers
from student.models import Student
from rest_framework.serializers import (
    ModelSerializer,
    Serializer,
    ValidationError,
    HyperlinkedModelSerializer,
)

from django.contrib.auth import authenticate

class StudentResigtrationSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = Student        
        fields = ['username','password']

    # def create(self, validated_data):        
    #     return Student.objects.create_user(**validated_data)



class StudentLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255, read_only=True)
    # mobile = serializers.CharField(max_length=255)

    #https://github.com/encode/django-rest-framework/blob/3.9.0/rest_framework/serializers.py#L86
    
    def validate(self, attrs):
        
        
        username = self.initial_data['username']
        password = self.initial_data['password']

        
        if username is None:
            raise serializers.ValidationError(
                'An username is required to log in.'
            )
     
        
        user = authenticate(username=username, password=password)

        print("-------------")
        print(user)
        
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )
        
        return {
            'password': user.password,
            'username': user.username
        }