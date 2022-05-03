from django.urls import path
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from sso.api.views import RegistrationAPIView, my_profile

app_name = 'sso'

router = routers.DefaultRouter()

urlpatterns = [
    path(r'users/', RegistrationAPIView.as_view()),
    path(r'profile/my', my_profile),
    path(r'login/', obtain_jwt_token),
    path(r'token-refresh/', refresh_jwt_token)
]

urlpatterns += router.urls
