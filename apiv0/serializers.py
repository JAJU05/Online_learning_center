from rest_framework import serializers
from home.models import Lesson, Teachers


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'

class TeachersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teachers
        fields = '__all__'