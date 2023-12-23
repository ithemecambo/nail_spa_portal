from rest_framework import serializers
from rest_framework.authtoken.models import Token

from account.models import *


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = '__all__'


class StaffSerializer(serializers.ModelSerializer):
    user = AccountSerializer(read_only=True)
    class Meta:
        model = StaffProfile
        fields = '__all__'


class ViewerProfileSerializer(serializers.ModelSerializer):
    user = AccountSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['phone', 'bio', 'address', 'city', 'state', 'zipcode', 'photo_url']


class UserSerializer(serializers.ModelSerializer):
    # profile = UserProfileSerializer(many=True)
    class Meta:
        model = Account
        fields = '__all__'


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        account = Account.objects.create(**validated_data)
        account.set_password(validated_data['password'])
        account.save()
        return account


class CreateUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        # fields = ['phone', 'bio', 'address', 'city', 'state', 'zipcode', 'photo_url', 'user']
        fields = '__all__'


class LoginUserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=50)
    class Meta:
        model = Account
        fields = ['email', 'password']


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'


