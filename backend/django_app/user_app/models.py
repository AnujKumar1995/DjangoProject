from django.db import models

# Create your models here.
class User(models.Model):
    userId = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(max_length =50, null=False)
    activate = models.BooleanField(default=False)
    created_on = models.DateTimeField()
    last_logged_in = models.DateTimeField()

    def __str__(self):
        return self.email

