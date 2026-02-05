from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=200, default="")
    iframe = models.CharField(max_length=600)

    class Meta:
        ordering = ['id']