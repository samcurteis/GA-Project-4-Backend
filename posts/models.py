from django.db import models

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(
        "jwt_auth.User", related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post_likes = models.ManyToManyField(
        "jwt_auth.User", related_name='post_likes', blank=True)
    post_favorites = models.ManyToManyField(
        "jwt_auth.User", related_name='post_favorites', blank=True)

    def __str__(self):
        return f"{self.title} - {self.author}"
