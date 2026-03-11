from django.db import models
from django.db.models.fields import CharField


class Fields(models.Model):
    image = models.ImageField()
    text = models.TextField()

    def __str__(self):
        return self.text


class Forms(models.Model):
    name = models.CharField()
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
