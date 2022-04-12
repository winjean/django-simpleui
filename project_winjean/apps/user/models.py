from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserProfile(AbstractUser):
    first_name = None
    last_name = None
    telephone = models.CharField(max_length=11, verbose_name='电话号码')

    class Meta:
        db_table = "t_user"
        ordering = ['telephone']
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
