from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
import datetime

from django.contrib.auth.models import User

class Category(models.Model):
  category_name=models.CharField(max_length=40, null=False)
  category_description=models.TextField(blank=True,null=False)
  category_photo=models.FileField(upload_to='media/', null=False)
  def __str__(self):
     return self.category_name


class Location(models.Model):
  County_name=models.CharField(max_length=40 , null=False)
  Postal_Adress=models.CharField(max_length=40 , null=False)
  postal_Code=models.CharField(max_length=40 , null=False)
  
  def __str__(self):
     return self.County_name


class Evidence(models.Model):
  reporter=models.ForeignKey(User, on_delete=models.CASCADE,default=15)
  evidence=models.FileField(upload_to='media/')
  location=models.ForeignKey(Location, on_delete=models.CASCADE,default=1)
  category=models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
  description=models.TextField(max_length=60)
  happened_on = models.DateTimeField(default=datetime.datetime.now())
  
  def __str__(self):
     return self.description 





