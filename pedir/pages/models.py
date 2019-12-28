from django.conf import settings
from django.db import models

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(verbose_name="Post Writeup", max_length=300)
    date_posted = models.DateField(verbose_name="Date Posted",auto_now_add=True)
    likes = models.PositiveIntegerField(verbose_name="Total Likes", default=0)

    def __str__(self):
        return self.content


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def user_likes_post(id, user):
        """
        Checks if a user already likes post
        """
        qs = Like.objects.filter(post_id=id, user=user)
        if qs:
            return True
        return False
        