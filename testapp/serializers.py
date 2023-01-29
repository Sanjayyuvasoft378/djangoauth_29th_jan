from asyncore import write
from pyexpat import model
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_bytes,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from xml.dom import ValidationErr
from rest_framework import serializers
from .models import *
class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':"password"}
                                      ,write_only=True)
    class Meta:
        model = User
        fields = ['email','password','password2','name','tc']
        extra_kwargs = {
            "password":{"write_only":True}
        }
        
    def validate(self,attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("password and confirm_password doesn't match")
        return attrs

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)
            
            
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ['email','password']
        
        


class UserChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255,
                                     style={"input_type":"password"},write_only=True)
    password2 = serializers.CharField(max_length=255,
                                      style={"input_type":"password"},write_only=True)
    class Meta:
        model = User
        fields = ['password','password2']

    def validate(self,attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        user = self.context.get('user')
        if password != password2:
            raise serializers.ValidationError("password and confirm password doesn`t match")
        user.set_password(password)
        user.save()
        return attrs
