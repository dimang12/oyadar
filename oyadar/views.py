# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import StudentScore

# Create your viewsDir here.
def index(request):

    scores = StudentScore.objects.filter(user_id=request.user.id)

    return render(
        request,
        "oyadar/index.html",
        {
            "scores": scores
        }
    )

def homework(request, id):
    return render(
        request,
        "oyadar/homework.html"
    )

def register(request):
    return render(
        request,
        "oyadar/users/register.html"
    )

def login(request):

    return render(
        request,
        "oyadar/users/login.html"
    )