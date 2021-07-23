from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer, SerializerMethodField
from .models import Course, Lesson, Tag


class CourseSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'subject', 'image', 'created_date', 'category_id']


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class LessonSerializer(ModelSerializer):
    tags = TagSerializer(many=True)
    tag_links = SerializerMethodField(source='tags')

    def get_tag_links(self, lesson):
        return "ABC_" + lesson.subject

    class Meta:
        model = Lesson
        fields = ["id", "subject", "content", "created_date", "image", "tags", "tag_links"]
