from rest_framework import routers

from sso.api import views

app_name = 'sso'

router = routers.DefaultRouter()

router.register(r'users', views.UserViewSet)

urlpatterns = router.urls
