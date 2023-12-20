import secrets
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from rest_framework.authtoken.views import obtain_auth_token


from .views import (
    AccountViewSet,
    StaffViewSet,
    ProfileViewSet,
)

app_name = 'account'

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('login/', obtain_auth_token, name=None),
    path('register/', obtain_auth_token, name=None),

    path('accounts/', AccountViewSet.as_view(), name=None),
    path('account-detail/<email>'+f"{secrets.token_hex(6)}"+'<int:pk>/',
         AccountViewSet.as_view(), name='account-detail'),

    path('getUsers/', StaffViewSet.as_view(), name='getUsers'),
    path('profile/<int:id>/', ProfileViewSet.as_view(), name='profile'),


]
