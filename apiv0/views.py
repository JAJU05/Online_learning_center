from home.models import Lesson,Teachers
from .serializers import LessonSerializer, TeachersSerializer

from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    pagination_class = PageNumberPagination

class LessonCreateAPIView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class LessonUpdateAPIView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class LessonRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class TeachersListAPIView(generics.ListAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializer
    pagination_class = PageNumberPagination

class TeachersCreateAPIView(generics.CreateAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializer

class TeachersUpdateAPIView(generics.UpdateAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializer


class TeachersDestroyAPIView(generics.DestroyAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializer

class TeachersRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializer