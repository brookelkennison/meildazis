# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from design.models import Design

# Create your views here.


def design_index(request):
    design = Design.objects.all()
    context1 = {
        'design': design
    }
    return render(request, 'design_index.html', context1)


def design_detail(request, design_id):
    design = get_object_or_404(Design, pk=design_id)
    return render(request, 'design_detail.html', {'design': design})

