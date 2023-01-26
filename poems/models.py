from django.db import models

# Create your models here.


class Poem(models.Model):
    author = models.ForeignKey(
        "authors.Author", related_name='poems', on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    content = models.TextField()
    poem_likes = models.ManyToManyField(
        "jwt_auth.User", related_name='poem_likes', blank=True)
    poem_favorites = models.ManyToManyField(
        "jwt_auth.User", related_name='poem_favorites', blank=True)

    def __str__(self):
        return f"{self.title} - {self.author}"
