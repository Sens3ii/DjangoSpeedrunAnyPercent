from django.contrib import admin

# Register your models here.
from sso.models import User

admin.site.register(User)
