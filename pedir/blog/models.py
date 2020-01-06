from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django.utils.html import mark_safe
from markdown import markdown


class Blog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Title", max_length=150, null=False, blank=False)
    slug = models.SlugField(verbose_name="Slug", max_length=100, unique=True)
    body = models.CharField(verbose_name="Blog Body", max_length=50000, null=False, blank=False)
    created = models.DateField(verbose_name="Date Created", auto_now_add=True)
    time = models.TimeField(verbose_name="Time",auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def get_avg_read_time(self):
        word_length = len(self.body)
        average_wpm = 200
        read_time = word_length / average_wpm
        if read_time < 1:
            return int(1)
        return int(read_time)

    def get_body_as_markdown(self):
        return mark_safe(markdown(self.body, safe_mode='escape'))

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.slug)])