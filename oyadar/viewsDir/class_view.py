from django.shortcuts import render


def index(request):
    return render(
        request,
        "oyadar/classes/index.html"
    )