# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from design.models import Design

# Register your models here.


class DesignAdmin(admin.ModelAdmin):
    pass

admin.site.register(Design, DesignAdmin)