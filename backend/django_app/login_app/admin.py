from django.contrib import admin
from user_app import models
from . import models
# Register your models here.

admin.site.register(models.User)
admin.site.register(models.LoginUser)
admin.site.register(models.UserLoginMap)