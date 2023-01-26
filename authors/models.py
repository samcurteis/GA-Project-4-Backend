from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=1000, unique=True)
    favorites = models.ManyToManyField(
        "jwt_auth.User", related_name='favorite_authors', blank=True)

    def __str__(self):
        return f"{self.name}"
