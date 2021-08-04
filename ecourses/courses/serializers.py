from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer, SerializerMethodField
from .models import Course, Lesson, Tag, User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password', 'avatar']
        extra_kwargs = {
            'password': {'write_only': 'true'}
        }

    def create(self, validated_data):
        user = User(**validated_data)
        # user.first_name = validated_data['first_name']
        # user.last_name = validated_data['last_name']
        user.set_password(validated_data['password'])
        user.save()

        return user


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
