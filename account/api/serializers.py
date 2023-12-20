from rest_framework import serializers
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


class ProfileSerializer(serializers.ModelSerializer):
    user = AccountSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['phone', 'bio', 'address', 'city', 'state', 'zipcode', 'photo_url']


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(many=True)
    class Meta:
        model = Account


