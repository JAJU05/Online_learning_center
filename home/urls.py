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
    path('', FirstView.as_view(), name='index'),
    
    path('course/', LessonListView.as_view(), name='view-lesson'),
    path('lesson/create/', LessonCreateView.as_view(), name='add-lesson'),
    path('lesson/view/<int:pk>/', LessonUpdateView.as_view(), name='update-lesson'),
    path('lesson/delete/<int:pk>/', LessonDeleteView.as_view(), name='delete-lesson'),

    path('teachers/', TeachersListView.as_view(), name='teachers'),
    path('teachers/create/', TeachersCreateView.as_view(), name='add-teachers'),
    path('teachers/view-publisher/<int:pk>/', TeachersDetialView.as_view(), name='detial-teachers'),
    path('teachers/update-teachers/<int:pk>/', TeachersUpdateView.as_view(), name='update-teachers'),
    path('teachers/delete-teachers/<int:pk>/', TeachersDeleteView.as_view(), name='delete-teachers'),

    #auth
    path('login/', login_view, name='login'),
    path('logout/', logout_request, name='logout'),
    path('register/', register_view, name='register'),

    #temlate
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
    path('course/', course, name='course'),
    path('single/', single, name='single'),
    path('teacher/', teacher, name='teacher'),
    path('index2/', index2, name='index2'),
    path('search/', search, name='search'),
    
    #buying
    path('buy/',buy ,name='buy'),



]   

    