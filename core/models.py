from django.db import models

# Create your models here.

class Game(models.Model):
    iframe = models.CharField(max_length=600)

    class Meta:
        ordering = ['id']