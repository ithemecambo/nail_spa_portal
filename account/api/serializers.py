from django.contrib.auth.password_validation import validate_password
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


class UpdateProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    class Meta:
        model = Profile
        fields = ['id', 'phone', 'bio', 'address', 'city', 'state', 'zipcode', 'photo_url', 'user']


# Check Password
class FindAccountEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Account
        fields = ['password', 'password2', 'old_password']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance


class ResetPasswordSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)

    class Meta:
        model = Account
        fields = '__all__'

    def save(self):
        email = self.validated_data['email']
        password = self.validated_data['password']
        if Account.objects.filter(email=email).exists():
            account = Account.objects.get(email=email)
            account.set_password(password)
            account.save()
            return account
        else:
            raise serializers.ValidationError({'message': 'Please enter valid credentials.'})
