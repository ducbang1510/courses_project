from django.contrib import admin
from django.urls import path, re_path, include
from . import views
from rest_framework import routers
# from .admin import admin_site

router = routers.DefaultRouter()
router.register('courses', views.CourseViewSet)
router.register('lessons', views.LessonViewSet)
router.register('users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('', views.index, name="index"),
    # path('welcome/<int:year>/', views.welcome, name="welcome"),
    # path('test/', views.TestView.as_view()),
    # re_path(r'^welcome2/(?P<year_2>[0-9]{1,2})/$', views.welcome2, name="welcome2"),
    # path('admin/', admin_site.urls)
]