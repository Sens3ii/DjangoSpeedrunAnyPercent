from rest_framework import viewsets
from rest_framework import permissions

from sso.api.serializers import UserSerializer
from sso.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
