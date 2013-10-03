from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Grupp(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    grupp = models.ForeignKey('self', blank=True, null=True, related_name='children')

class Sort(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    grupp = models.ForeignKey(Grupp)
    
class Plant(models.Model):
    sort = models.ForeignKey(Sort)
    user = models.ForeignKey(User)