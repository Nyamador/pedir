from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from .managers import SocialUserManager
from django.urls import reverse


class SocialUser(AbstractUser):
    gender_list = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'

    objects = SocialUserManager()

    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    username = models.CharField(verbose_name="Username", max_length=20, blank=False, null=False, unique=True)
    first_name = models.CharField(verbose_name="First Name", max_length=50, blank=False, null=False)
    last_name = models.CharField(verbose_name="Last Name", max_length=50, blank=False, null=False)
    slug = models.SlugField(verbose_name="Profile Slug", max_length=150, null=False, unique=True)
    bio = models.CharField(verbose_name="Bio", max_length=500, default="")
    country = models.CharField(verbose_name="Location", max_length=100)
    email = models.EmailField(verbose_name="Email", max_length=100)
    joined = models.DateField(verbose_name="Date Joined", auto_now_add=True)
    linkedIn = models.URLField(verbose_name="linkedIn Url", max_length=150, null=True, blank=True)
    twitter = models.URLField(verbose_name="Twitter Url", max_length=150, null=True, blank=True)
    ig = models.URLField(verbose_name="Ig Url", max_length=150, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def save(self,*args, **kwargs):
        self.slug = slugify(self.username)
        super(Profile, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('pages.views.profile_view', args=[str(self.username)])