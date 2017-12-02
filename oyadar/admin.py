# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from django.contrib import admin
from .models import Assignment,AssigmentQuestion, AssignmentAnswer, TestUser, Class
from .models import StudentScore


# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "expired_date"]

class QuesitonAdmin(admin.ModelAdmin):
    list_display = ["get_assignment_title","question_detail", "question_note", "question_type"]
    #
    # fields = ["assignment_id","question_detail","question_note","question_type","answer_id", "ordering"]

    def get_assignment_title(self, obj):
        return obj.assignment_id.title

class AnswerAdmin(admin.ModelAdmin):
    list_display = ["question_id","answer_detail"]


class ClassAdmin(admin.ModelAdmin):
    list_display = ["class_name","class_detail"]

    #
    # get_assignment_title.admin_order_field = 'asignment_id__tittle'
    # get_assignment_title.short_description = 'asignment_id__tittle'

class TestUserAdmin(admin.ModelAdmin):
    list_display = ["user","title"]


class StudentScoreAdmin(admin.ModelAdmin):
    list_display = ["user","class_id", "total_score"]




admin.site.register(Assignment, ItemAdmin)
admin.site.register(AssigmentQuestion, QuesitonAdmin)
admin.site.register(AssignmentAnswer, AnswerAdmin)
admin.site.register(TestUser, TestUserAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(StudentScore, StudentScoreAdmin)