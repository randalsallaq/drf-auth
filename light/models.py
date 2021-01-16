from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class LightSample(models.Model):
    name = models.ForeignKey('auth.User', on_delete= models.CASCADE)
    light_type = models.CharField(max_length=64)
    price = models.TextField(max_length=600)

    def __str__(self):
        return str(self.name)