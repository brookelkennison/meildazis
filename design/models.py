# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Design(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    image = models.URLField()
