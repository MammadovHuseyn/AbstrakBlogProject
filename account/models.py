from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to ='avatar/' , default = 'default_userpp.jpg')
    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = 'Users'

