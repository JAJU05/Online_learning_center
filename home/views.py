from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from .models import *
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import LoginForm, RegisterForm

# Create your views here.

#teacher view
class FirstView(ListView):
    model = FirstView
    template_name = "index.html"

class TeachersListView(ListView):
    model = Teachers
    template_name = 'teachers.html'
    context_object_name = 'teachers'

    def get_queryset(self):
        return Teachers.objects.filter(**self.request.GET.dict())


class TeachersCreateView(CreateView):
    model = Teachers
    fields = '__all__'
    template_name = 'add-teachers.html'
    success_url = reverse_lazy('teachers')


class TeachersDetialView(DetailView):
    model = Teachers
    template_name = 'teachers-view.html'


class TeachersDeleteView(DeleteView):
    model = Teachers
    success_url = reverse_lazy('teachers')
    template_name = 'teachers_confirm_delete.html'

class TeachersUpdateView(UpdateView):
    model = Teachers
    template_name = 'teachers-update.html'
    fields = '__all__'
    success_url = reverse_lazy('teachers')


#lesson view

class LessonListView(ListView):
    model = Lesson
    template_name = 'lessons.html'
    context_object_name = 'lesson'

    def get_queryset(self):
        if len(self.request.GET.dict().items()) == 0:
            query = self.request.COOKIES.copy()
            if 'sessionid' in query:
                del query['sessionid']
            if 'csrftoken':
                del query['csrftoken']  
        else:
            query = self.request.GET.dict()
        return Lesson.objects.filter(**query)


class LessonCreateView(CreateView):
    model = Lesson 
    fields = '__all__'
    template_name = 'add-lesson.html'
    success_url = reverse_lazy('index')

 
class LessonDeleteView(DeleteView):
    model = Lesson
    success_url = reverse_lazy('index')
    template_name = 'lesson_confirm_delete.html'


class LessonUpdateView(UpdateView):
    model = Lesson
    template_name = 'view_lesson.html'
    fields = '__all__'
    success_url = reverse_lazy('index')




class BuyLessonListView(ListView):
    model = Payment
    template_name = 'buy.html'
    


def about(request):

    return render(request, "about.html" )

def blog(request):

    return render(request, "blog.html" )

def contact(request):

    return render(request, "contact.html" )

def course(request):

    return render(request, "course.html" )

def single(request):

    return render(request, "single.html" )

def index2(request):

    return render(request, "index2.html" )

def teacher(request):

    return render(request, "teacher.html" )

def search(request):

    return render(request, "search.html" )

#auth
def login_view(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, template_name='login.html', context={'form': form})
    else:
        from django.contrib.auth import login, authenticate
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect(reverse_lazy('index'))
        return render(request, template_name='login.html', context={'form': form, 'error_msg': 'Please, type correct user name and password'})

def logout_request(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect(reverse_lazy("index")) 

def register_view(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, template_name='register.html', context={'form': form})
    else:
        from django.contrib.auth import login, authenticate
        form = RegisterForm(data=request.POST)
        if form.is_valid():

            user = form.instance
            user.set_password(request.POST['password'])
            form.save()

            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if user:
                login(request, user)
                return redirect(reverse_lazy('index'))
            return render(request, template_name='register.html', context={'form': form, 'error_msg': 'Please, type correct user name and password'})
        
        return render(request, template_name='register.html', context={'form': form})

#buy
def buy(request):

    return render(request, "buy.html" )