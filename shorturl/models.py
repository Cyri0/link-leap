from django.db import models
from django.contrib.auth.models import User


class MyShortURL(models.Model):
    longurl = models.URLField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    visible = models.BooleanField(default = True)
    creator = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + " id: " + str(self.id)
