from django.shortcuts import render
from oyadar.models import Class, StudentScore


def index(request):
    classes = StudentScore.objects.filter(user_id=request.user.id)

    return render(
        request,
        "oyadar/classes/index.html",
        {
            "classes": classes
        }
    )