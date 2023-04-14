from django.contrib import admin

# Register your models here.
from .models import Post, Semester

admin.site.register(Post)
admin.site.register(Semester)
