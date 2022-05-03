from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sso/', include('sso.urls', namespace='sso')),
    path('api/', include('api.urls', namespace='api')),
]
