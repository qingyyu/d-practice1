# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=240)
    def __str__(self):
        return self.username

class BaseFile(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=200)
    path = models.FileField(max_length=100)
    def __str__(self):
        return self.name
    
