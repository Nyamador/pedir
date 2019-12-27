from django.contrib.auth.models import AbstractUser 
from django.db import models
from django.utils.translation import ugettext_lazy as _
from . managers import SocialUserManager


class SocialUser(AbstractUser):

    gender_list = (
        ('M', 'Male'),
        ('F','Female'),
    )

    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'

    objects = SocialUserManager()

    REQUIRED_FIELDS = []


    class Meta:
        verbose_name = _('user')