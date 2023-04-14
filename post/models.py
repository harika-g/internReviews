# Create your models here.
from django.db import models
from django import forms


class Post(models.Model):
    company = models.CharField(max_length=150)
    role = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    review = models.CharField(max_length=500)
    rating = models.IntegerField()
    duration = models.IntegerField()
    semester = models.CharField(max_length=15)
    year = models.IntegerField()
    salary = models.IntegerField()
    industry = models.CharField(max_length=150)
    email = models.EmailField(help_text='Enter your Texas A&M email')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    objects = models.Manager()


class Semester(models.Model):
    semester = models.CharField(max_length=15)

    def __str__(self):
        return self.semester

    objects = models.Manager()
