from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class newmodel(models.Model):
    name=models.CharField(max_length=20);
    another_name=CharField(max_length=20);
    