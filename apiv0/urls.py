"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *

urlpatterns = [
    path('lessons/', LessonListAPIView.as_view(), name='get_lessons'),
    path('lessons/create/', LessonCreateAPIView.as_view(), name='create_lessons'),
    path('lessons/update/<int:pk>', LessonUpdateAPIView.as_view(), name='update_lessons'),
    path('lessons/delete/<int:pk>', LessonDestroyAPIView.as_view(), name='delete_lessons'),
    path('lessons/view/<int:pk>', LessonRetrieveAPIView.as_view(), name='view_lesson'),

    path('teacher/', TeachersListAPIView.as_view(), name='get_teachers'),
    path('teacher/create/', TeachersCreateAPIView.as_view(), name='create_teacher'),
    path('teacher/update/<int:pk>', TeachersUpdateAPIView.as_view(), name='update_teacher'),
    path('teacher/delete/<int:pk>', TeachersDestroyAPIView.as_view(), name='delete_teacher'),
    path('teacher/view/<int:pk>', TeachersRetrieveAPIView.as_view(), name='view_teacher'),
]
