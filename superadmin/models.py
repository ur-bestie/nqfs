from django.db import models

# Create your models here.



class notifications(models.Model):
    notify = models.CharField(max_length=100)
    true = models.BooleanField(default=False)
