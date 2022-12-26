from django.contrib import admin
from .models import *

admin.site.register(Lesson)
admin.site.register(Teachers)
admin.site.register(Language)
admin.site.register(Student)
admin.site.register(PaymentMethod)
admin.site.register(Payment)
admin.site.register(Class)
admin.site.register(ClassStudent)