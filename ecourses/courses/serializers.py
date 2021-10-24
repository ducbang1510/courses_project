from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer, SerializerMethodField, Serializer, \
    CharField
from .models import Course, Lesson, Tag, User, Category, Comment


class CustomTokenSerializer(Serializer):
    token = CharField()


class UserSerializer(ModelSerializer):
    avatar_url = SerializerMethodField()

    def get_avatar_url(self, user):
        request = self.context.get('request')
        if user.avatar and hasattr(user.avatar, 'name'):
            avatar_url = user.avatar.name
            if avatar_url.startswith('static/'):
                avatar_url = '/%s' % avatar_url
            else:
                avatar_url = '/static/%s' % avatar_url

            return request.build_absolute_uri(avatar_url)
        else:
            return None

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password',
                  'date_joined', 'avatar_url']
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
    image = SerializerMethodField()

    def get_image(self, course):
        request = self.context['request']
        name = course.image.name
        if name.startswith('static/'):
            path = '/%s' % name
        else:
            path = '/static/%s' % name

        return request.build_absolute_uri(path)

    class Meta:
        model = Course
        fields = ['id', 'subject', 'image', 'created_date', 'category_id']


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


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
        fields = ["id", "subject", "content", "created_date", "image", "tags", "tag_links", "course_id"]


# class LessonDetailSerializer():
#     tags = TagSerializer(many=True)
#
#     class Meta:
#         model = Ls

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
