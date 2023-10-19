from django.db import models

# Create your models here.

class MyShortURL(models.Model):
    longurl = models.URLField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)