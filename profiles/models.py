from django.db import models

# Create your models here.

from django.contrib.auth.models import User,AbstractUser

from django.utils.timezone import now

from django.core.exceptions import ValidationError

import re

import uuid

def VALID(value):

  x=re.match('^09\d{9}$',value)

  if x :
    return value
  else:
     raise ValidationError('the phone number is incorrect')

class User(AbstractUser):

    avatar=models.ImageField(upload_to='files/avatars',null=True,blank=True)

    phone=models.CharField(max_length=11,null=True,blank=True,validators=[VALID],help_text='example:09121112020')

    g=[('m','Male'),('f','Female'),('c','Costum'),('p','Prefer Not To Say')]

    gender=models.CharField(max_length=10,choices=g,default='m')

    birthday=models.DateField(null=True,blank=True,default=now)

    def __str__(self):
        
        return self.username



class ads(models.Model):

    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)

    user=models.ForeignKey(User, on_delete=models.CASCADE)

    image=models.ImageField(upload_to='files/images',null=False,blank=False)

    title=models.CharField(max_length=150,null=False,blank=False)

    available=models.BooleanField(default=False)

    c=[('electronics','Electronics'),('restaurants','Restaurants')]

    category=models.CharField(max_length=100,choices=c,default='electronics')

    location=models.CharField(max_length=50)

    created_at=models.DateTimeField(auto_now=False, auto_now_add=True)

    updatted_at=models.DateTimeField(auto_now=True, auto_now_add=False)




    
