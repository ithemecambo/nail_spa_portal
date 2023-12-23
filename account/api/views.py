from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import update_last_login
from rest_framework import permissions, status, generics
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import *

from account.models import *
from . import serializers


class AccountViewSet(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser, FileUploadParser]

    def get_object(self, pk):
        try:
            return Account.objects.get(pk=pk)
        except Account.DoesNotExist:
            return None

    def get(self, request, *args, **kwargs):
        accounts = Account.objects.filter(is_staff=True)
        serializer = serializers.AccountSerializer(accounts, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
            'sex': request.data.get('sex'),
            'email': request.data.get('email'),
            'password': request.data.get('password'),
            'phone': request.data.get('phone'),
            'fax': request.data.get('fax'),
            'address': request.data.get('address'),
            'photo_url': request.data.get('photo_url'),
        }
        serializer = serializers.AccountSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        instance = self.get_object(pk)
        if not instance:
            return Response({'data': 'Account does not existing.'},
                            status=status.HTTP_400_BAD_REQUEST)

        data = {
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
            'sex': request.data.get('sex'),
            'email': request.data.get('email'),
            'password': request.data.get('password'),
            'phone': request.data.get('phone'),
            'fax': request.data.get('fax'),
            'address': request.data.get('address'),
            'photo_url': request.data.get('photo_url'),
        }
        serializer = serializers.AccountSerializer(instance=instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        instance = self.get_object(pk)
        if not instance:
            return Response({'data': 'Account does not existing.'},
                            status=status.HTTP_400_BAD_REQUEST)

        instance.delete()
        return Response({'data': 'Account was deleted from system.'},
                        status=status.HTTP_200_OK)


class StaffViewSet(generics.ListAPIView):
    serializer_class = serializers.StaffSerializer
    queryset = StaffProfile.objects.all()


class ProfileViewSet(APIView):
    def get(self, request, *args, **kwargs):
        profile = Profile.objects.filter(user=kwargs.get('id'))
        if profile.exists():
            serializer = serializers.ProfileSerializer(profile, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data={'message': 'Profile search not found! Please try to find another profiles.'},
                        status=status.HTTP_200_OK)


class CreateAccountViewSet(APIView):
    def get(self, request, *args, **kwargs):
        accounts = Account.objects.filter(pk=kwargs.get('pk'))
        serializer = serializers.AccountSerializer(accounts, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = serializers.CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateUserProfileViewSet(APIView):
    parser_classes = [MultiPartParser, FormParser, FileUploadParser]

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = serializers.CreateUserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ViewerUserProfileViewSet(APIView):
    # permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        profiles = Profile.objects.filter(user__id=kwargs.get('pk', None))
        serializer = serializers.ViewerProfileSerializer(profiles, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CustomLoginAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        # serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.pk,
                'email': user.email
            })
        return Response({
            'message': 'Invalid email and/or password. Please try again!'
        }, status=status.HTTP_400_BAD_REQUEST)


class UpdateProfileViewSet(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.UpdateProfileSerializer
    queryset = Profile.objects.all()


class UpdateProfileDetailAPIView(APIView):
    parser_classes = [MultiPartParser, FormParser, FileUploadParser]

    def put(self, request, id, *args, **kwargs):
        if Profile.objects.filter(id=id).exists():
            profile = Profile.objects.get(id=id)
            data = {
                'phone': request.data.get('phone'),
                'bio': request.data.get('bio'),
                'address': request.data.get('address'),
                'city': request.data.get('city'),
                'state': request.data.get('state'),
                'zipcode': request.data.get('zipcode'),
                'photo_url': request.data.get('photo_url')
            }
            serializer = serializers.UpdateProfileSerializer(instance=profile,
                                                             data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Profile doesn't exists in our database."}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id, *args, **kwargs):
        if Profile.objects.filter(id=id).exists():
            profile = Profile.objects.get(id=id)
            data = {
                'phone': request.data.get('phone'),
                'bio': request.data.get('bio'),
                'address': request.data.get('address'),
                'city': request.data.get('city'),
                'state': request.data.get('state'),
                'zipcode': request.data.get('zipcode'),
                'photo_url': request.data.get('photo_url')
            }
            serializer = serializers.UpdateProfileSerializer(instance=profile,
                                                             data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Profile doesn't exists in our database."}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, *args, **kwargs):
        if Profile.objects.filter(id=id).exists():
            profile = Profile.objects.get(id=id)
            profile.delete()
            return Response({"message": "Profile user was deleted from database."}, status=status.HTTP_200_OK)
        return Response({"message": "Profile doesn't exists in our database."}, status=status.HTTP_400_BAD_REQUEST)


class FindAccountEmailViewSet(APIView):
    def get(self, request, *args, **kwargs):
        if Account.objects.filter(email=kwargs['email']).exists():
            print(kwargs['email'])
            account = Account.objects.filter(email=kwargs['email'])
            serializer = serializers.FindAccountEmailSerializer(account, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response({'message': 'Your account does not exist. Please try an other emails.'},
                        status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordViewSet(generics.UpdateAPIView):
    queryset = Account.objects.all()
    permission_classes = [IsAuthenticated, ]
    serializer_class = serializers.ChangePasswordSerializer


class ResetPasswordViewSet(APIView):
    def get_object(self, pk):
        try:
            return Account.objects.get(pk=pk)
        except Account.DoesNotExist:
            return None

    def put(self, request, pk, *args, **kwargs):
        instance = self.get_object(pk)
        if not instance:
            return Response({'message': 'Account does not existing.'},
                            status=status.HTTP_400_BAD_REQUEST)

        data = {
            'email': request.data.get('email'),
            'password': request.data.get('password')
        }
        serializer = serializers.ResetPasswordSerializer(instance=instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutApiView(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        auth.logout(request)
        return Response({'message': 'successfully deleted'})
