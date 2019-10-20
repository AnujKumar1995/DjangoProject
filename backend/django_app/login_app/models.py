from django.db import models
from user_app.models import User

# Create your models here.

#create Login class for separate user
class LoginUser(models.Model):
    loginUserId = models.IntegerField(primary_key=True)
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(max_length=50, null=False)
    
    def __str__(self):
        return self.email

#compare both user and login Db for unique user when user wants to login 
class UserLoginMap(models.Model):
    mappingID = models.IntegerField(primary_key=True)
    userId = models.ForeignKey(User , on_delete=models.CASCADE)
    loginId = models.ForeignKey(LoginUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.mappingID