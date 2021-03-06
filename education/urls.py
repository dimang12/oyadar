"""education URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from oyadar import views
from oyadar.viewsDir import assignmentView, class_view, profile_view


urlpatterns = [
    url(r'^$', login_required(views.index), name='index'),
    url(r'^assignment/', login_required(assignmentView.index), name='assignment'),
    url(r'^assignment-detail/(?P<id>\d+)/', login_required(assignmentView.detail), name='assignment-detail'),
    url(r'^answer/(?P<id>\d+)/', assignmentView.chooseAnswer, name='choose-answer'),
    url(r'^next-prev/(?P<id>\d+)/', assignmentView.nextPrev, name='next-prev'),

    url(r'^classes/$', login_required(class_view.index) ,name='classes'),
    url(r'^profile/(?P<id>\d+)/', profile_view.index, name='profile'),

    url(r'^register/', views.register, name="register"),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^accounts/', include('django.contrib.auth.urls')),

    url(r'^oyadar/', include('oyadar.urls')),
    url(r'^admin/', admin.site.urls),
]