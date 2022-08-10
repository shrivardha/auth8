from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Info(models.Model):
    #user=models.ForeignKey(User, on_delete=models.CASCADE,related_name="info", null=True)
    name=models.CharField(max_length=200,default='default')
    def __str__(self) :
        return self.name
class Item(models.Model):
    info=models.ForeignKey(Info,on_delete=models.CASCADE)
    text=models.CharField(max_length=300,default='default')
    def __str__(self) :
        return self.text