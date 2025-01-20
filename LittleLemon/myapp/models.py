from django.db import models

# Create your models here.
class Menu(models.Model):
    item_name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
