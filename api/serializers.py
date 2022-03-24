from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from api.models import Phone
from django.contrib.auth.models import User

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ['id','phone_number', 'user', 'country' , 'city' , 'address', 'email']
        
class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = User 
        fields = ['email','username','password','password2']
        

