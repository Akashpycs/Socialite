from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Storie(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    img = models.ImageField(upload_to = "Stories")
    time = models.DateTimeField(auto_now_add = True)
    dead = models.BooleanField(default = False)

    def __str__(self):
        return str(self.user) + " - " + str(self.time)


    # P _ { : ; p [ "
