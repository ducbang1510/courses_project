from django.contrib import admin
from django.utils.html import mark_safe
from .models import Lesson, Course, Category, Tag


class LessonAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('/static/css/main.css', )
        }
    list_display = ['id', 'subject', 'created_date', 'active', 'course']
    search_fields = ['subject', 'created_date', 'course__subject']
    list_filter = ['subject', 'course__subject']
    readonly_fields = ['avatar']

    def avatar(self, lesson):
        return mark_safe("<img src='/static/{img_url}' alt='{alt}' width=120px />".format(img_url=lesson.image.name, alt=lesson.subject))


# Register your models here.
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Course)
admin.site.register(Category)
