# Create your models here.
from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class Post(models.Model):
    company = models.CharField(max_length=150)
    role = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    review = models.CharField(max_length=500)
    rating = models.IntegerField()
    duration = models.IntegerField()
    semester = models.CharField(max_length=15)
    year = models.PositiveIntegerField(default=current_year(), validators=[
                                       MinValueValidator(2013), max_value_current_year])
    salary = models.PositiveIntegerField(blank=True, null=True)
    industry = models.CharField(max_length=150, blank=True, null=True)
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
