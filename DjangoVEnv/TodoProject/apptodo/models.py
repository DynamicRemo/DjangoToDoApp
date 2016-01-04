from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class apptodo(models.Model):
    title = models.CharField(max_length=120)
    done = models.BooleanField(default=False)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.title