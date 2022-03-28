from dataclasses import fields
from rest_framework import serializers
from api.models import Phone , Email_log , Student
from django.contrib.auth.models import User



class StudentSerializer(serializers.ModelSerializer):
    class Meta :
        model = Student
        fields = ['id' , 'name' , 'roll' , 'city' , 'passby']


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ['id','phone_number', 'user', 'country' , 'city' , 'address', 'email']


class EmailSerializer(serializers.ModelSerializer):
    class Meta :
        model = Email_log
        fields = ['email', 'subject', 'body']
        
class UserSerializer(serializers.ModelSerializer):
    
    confirm_password = serializers.CharField(
            max_length=100,min_length=6,write_only=True)
    class Meta :
        model = User 
        fields = ['email','username','password','confirm_password']

    def create(self, validated_data):        
        if validated_data['password'] != validated_data['confirm_password'] :
            raise serializers.ValidationError({"password":"Password fields didn't match."})
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username' , 'password']
