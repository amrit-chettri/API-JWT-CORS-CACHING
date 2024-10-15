from django.db import models
from django.contrib.auth.models import User



class Lead(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    message = models.TextField()
    photo = models.ImageField(upload_to='test/images', blank=True, null=True)

    def __str__(self):
        return self.name


