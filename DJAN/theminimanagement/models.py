from django.db import models

# Create your models here.

class job(models.Model):
    id = models.IntegerField()
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
