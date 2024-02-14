from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    img_url = models.URLField()
    group_url = models.URLField()
    description = models.TextField()
    likes = models.IntegerField(default=0)
    saved_by = models.ManyToManyField(User, related_name="saved_posts")

    def __str__(self):
        return self.title
