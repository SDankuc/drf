from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from . import views

urlpatterns = [
    path("auth/", obtain_auth_token),
    path("token/", TokenObtainPairView.as_view(), name = 'token_obtain_pair'), # api/token
    path("token/", TokenRefreshView.as_view(), name = "token_refresh"),
    path("token/", TokenVerifyView.as_view(), name = "token_verify"),
    path("",views.api_home)
]