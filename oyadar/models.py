# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    modified_date = models.DateTimeField(auto_now=True)
    expired_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title


class AssigmentQuestion(models.Model):
    assignment_id = models.ForeignKey(Assignment,on_delete=None)
    question_detail = models.TextField()
    question_note = models.TextField()
    question_type = models.IntegerField()
    answer_id = models.IntegerField(default=0)
    ordering = models.IntegerField(default=1)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_detail



class AssignmentAnswer(models.Model):
    question_id = models.ForeignKey(AssigmentQuestion, on_delete=models.CASCADE)
    answer_detail = models.TextField()
    ordering = models.IntegerField()
    create_date = models.DateField(default=timezone.now)
    modified_date = models.DateTimeField(auto_now=True)


class Class(models.Model):
    # user = models.ForeignKey(User)
    class_name = models.CharField(max_length=100)
    class_detail = models.TextField(default="")
    max_score = models.IntegerField(default=100)

    def __str__(self):
        return self.class_name


class Student(models.Model):
    student_first_name = models.CharField(max_length=150)
    student_last_name = models.CharField(max_length=150)
    student_email = models.CharField(max_length=100)
    student_password = models.CharField(max_length=64)


class StudentScore(models.Model):
    user = models.ForeignKey(User)
    class_id = models.ForeignKey(Class)
    total_score = models.FloatField(default=0.0)



class TestUser(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User)


