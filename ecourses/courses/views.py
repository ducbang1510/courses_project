from django.shortcuts import render
from django.http import HttpResponse, request
from django.views import View
from drf_yasg.utils import swagger_auto_schema

from rest_framework import viewsets, permissions, status, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import renderers
from django.http import Http404
from django.conf import settings
from rest_framework.views import APIView

from .models import *
from .serializers import CourseSerializer, LessonSerializer, UserSerializer, CategorySerializer


class UserViewSet(viewsets.ViewSet,
                  generics.CreateAPIView,
                  generics.UpdateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, ]

    def get_permissions(self):
        if self.action == 'current_user':
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]

    @action(methods=['get'], detail=False, url_path='current-user')
    def current_user(self, request):
        return Response(self.serializer_class(request.user).data)

    # def get_permissions(self):
    #     if self.action == 'retrieve':
    #         return [permissions.IsAuthenticated()]
    #
    #     return [permissions.AllowAny()]


class CoursePagination(PageNumberPagination):
    page_size = 6


class CourseViewSet(viewsets.ViewSet, generics.ListAPIView):
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['subject']
    serializer_class = CourseSerializer
    pagination_class = CoursePagination

    def get_queryset(self):
        queryset = Course.objects.filter(active=True)
        category_id = self.request.query_params.get('category_id')
        q = self.request.query_params.get('q')

        if category_id is not None:
            queryset = queryset.filter(category_id=category_id)
        if q is not None:
            queryset = queryset.filter(subject__icontains=q)

        return queryset

    @action(methods=['get'], detail=True, url_path="lessons")
    def get_lessons(self, request, pk):
        lessons = Course.objects.get(pk=pk).lessons.filter(active=True)
        # lessons = self.get_object().lessons.filter(active=True)

        kw = request.query_params.get('kw')
        if kw is not None:
            lessons = lessons.filter(subject__icontains=kw)

        return Response(LessonSerializer(lessons, many=True).data,
                        status=status.HTTP_200_OK)


class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None     # Tắt phân trang cho category


class LessonPagination(PageNumberPagination):
    page_size = 3


class LessonViewSet(viewsets.ViewSet, generics.ListAPIView,
                    generics.RetrieveAPIView):
    queryset = Lesson.objects.filter(active=True)
    serializer_class = LessonSerializer
    pagination_class = LessonPagination

    @swagger_auto_schema(
        operation_description='This API for hide lesson from client',
        response={
            status.HTTP_200_OK: LessonSerializer()
        }
    )
    @action(methods=['post'], detail=True,
            url_path='hide-lesson',
            url_name='hide-lesson')
    def hide_lesson(self, request, pk=None):
        try:
            l = Lesson.objects.get(pk=pk)
            l.active = False
            l.save()
        except Lesson.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(data=LessonSerializer(l, context={'request': request}).data, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True,
            url_path='add-tag')
    def add_tag(self, request, pk):
        try:
            lesson = Lesson.objects.get(pk=pk)
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            tags = request.data.get("tags")
            if tags is not None:
                for tag in tags:
                    t, _ = Tag.objects.get_or_create(name=tag)
                    lesson.tags.add(t)

                lesson.save()

                return Response(self.serializer_class(lesson).data,
                                status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_404_NOT_FOUND)


class AuthInfo(APIView):
    def get(self, request):
        return Response(settings.OAUTH2_INFO, status=status.HTTP_200_OK)


def index(request):
    # return HttpResponse("e-Course App")
    return render(request, template_name='index.html', context={
        'name': 'Duc Bang'
    })


def welcome(request, year):
    return HttpResponse("Hello" + str(year))


def welcome2(request, year_2):
    return HttpResponse("Hello" + str(year_2))


class TestView(View):
    def get(self, request):
        return HttpResponse('TESTING')

    def post(self, request):
        pass
