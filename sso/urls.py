from django.urls import path, include
from rest_framework import routers

from sso.api import views

app_name = 'sso'

router = routers.DefaultRouter()

router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = router.urls
