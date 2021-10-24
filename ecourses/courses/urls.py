from django.contrib import admin
from django.urls import path, re_path, include
from . import views
from rest_framework import routers
# from .admin import admin_site

router = routers.DefaultRouter()
router.register('courses', views.CourseViewSet, basename='course')
router.register('lessons', views.LessonViewSet, basename='lesson')
router.register('users', views.UserViewSet, basename='user')
router.register('categories', views.CategoryViewSet, basename='category')
router.register('comments', views.CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('oauth2-info/', views.AuthInfo.as_view()),
    path('reset-password/verify-token/', views.CustomPasswordTokenVerificationView.as_view(), name='password_reset_verify_token'),
    path('reset-password/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    # path('', views.index, name="index"),
    # path('welcome/<int:year>/', views.welcome, name="welcome"),
    # path('test/', views.TestView.as_view()),
    # re_path(r'^welcome2/(?P<year_2>[0-9]{1,2})/$', views.welcome2, name="welcome2"),
    # path('admin/', admin_site.urls)
]
