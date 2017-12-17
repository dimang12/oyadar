from django.shortcuts import render



def index(request, id):
    return render(
        request,
        "oyadar/profiles/profile.html"
    )