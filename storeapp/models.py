from django.db import models
from django.contrib.auth.models import User

import datetime
import os
# Create your models here.

def get_file_path(request,filename):
    original_filename = filename
    nowTime=datetime.datetime.now().strftime('%Y%M%D%H:%M:%S')
    filename="%s%s" % (nowTime,original_filename)
    return os.path.join('uploads/',filename)

class Principal(models.Model):
    name=models.CharField(max_length=150, null=False, blank=False)
    principal_image=models.ImageField(upload_to=get_file_path, null=True,blank=True)    
    discription=models.TextField(null=False,blank=False)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    image=models.ImageField(upload_to=get_file_path,null=True, blank=True)
    name=models.CharField(max_length=150, null=False, blank=False)
    tittle=models.CharField(max_length=150, null=False, blank=False)
    des=models.CharField(max_length=50, null=False,blank=False)

    def __str__(self):
        return self.name

class Facility(models.Model):
    fac_image=models.ImageField(upload_to=get_file_path, null=True, blank=True)
    name= models.CharField(max_length=150, null=False, blank=False)
    desc=models.TextField(null=False,blank=False)

    def __str__(self):
        return self.name       

