
from django.db import models

# Create your models here.

class admin_post(models.Model):
    title = models.CharField(max_length= 50,default="")
    desc = models.CharField(max_length=50,default="")
    image = models.ImageField(upload_to = 'uplode_image')


class comments(models.Model):
    user = models.CharField(max_length=50)
    user_id = models.IntegerField()
    message =  models.CharField(max_length=200)

class Information(models.Model):
    title = models.CharField(max_length=100,null=True)
    date = models.CharField(max_length=100,null=True)