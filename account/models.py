from django.db import models


# Create your models here.

class Profile(models.Model):
    user_name = models.CharField(max_length=200, unique=True)
    pasword = models.CharField(max_length=8, unique=True)

    def __str__(self):
        return self.user_name
