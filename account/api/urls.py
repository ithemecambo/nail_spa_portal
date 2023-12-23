import secrets
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from rest_framework.authtoken.views import obtain_auth_token


from .views import (
    AccountViewSet,
    StaffViewSet,
    CustomLoginAuthToken,
    CreateAccountViewSet,
    ViewerUserProfileViewSet,
    CreateUserProfileViewSet,
    UpdateProfileViewSet,
    UpdateProfileDetailAPIView,
    FindAccountEmailViewSet,
    ChangePasswordViewSet,
    ResetPasswordViewSet,
)

app_name = 'account'

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('login-user/', obtain_auth_token, name=None),
    path('register/', obtain_auth_token, name=None),

    path('accounts/', AccountViewSet.as_view(), name=None),
    path('account-detail/<email>'+f"{secrets.token_hex(6)}"+'<int:pk>/',
         AccountViewSet.as_view(), name='account-detail'),

    path('getUsers/', StaffViewSet.as_view(), name='getUsers'),

    # Account
    path('account/<int:pk>/', CreateAccountViewSet.as_view(), name='account'),
    path('create-account/', CreateAccountViewSet.as_view(), name='create-account'),

    # Profile
    path('profile/<int:pk>/', ViewerUserProfileViewSet.as_view(), name='profile'),
    path('create-profile/', CreateUserProfileViewSet.as_view(), name='create-profile'),

    # Staff members
    path('login/', CustomLoginAuthToken.as_view(), name='login'),

    path('update-profile/<int:id>/', UpdateProfileDetailAPIView.as_view(), name='update-profile'),
    path('update/<int:pk>/', UpdateProfileViewSet.as_view(), name='update'),

    path('looking-profile/<str:email>/', FindAccountEmailViewSet.as_view(), name='looking-profile'),
    path('change-password/<int:pk>/', ChangePasswordViewSet.as_view(), name='change-password'),
    path('reset-password/<int:pk>/', ResetPasswordViewSet.as_view(), name='reset-password'),




]
