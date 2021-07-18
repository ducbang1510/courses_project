from django.contrib import admin
from .models import Lesson, Course, Category, Tag

# Register your models here.
admin.site.register(Lesson)
admin.site.register(Course)
admin.site.register(Category)
