from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class News(models.Model):
    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=200)
    full_description = models.TextField()
    type = models.ForeignKey(
        'Type',
        on_delete=models.SET_NULL,
        null=True,
        related_name='type'
    )

    def __str__(self) -> str:
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name
