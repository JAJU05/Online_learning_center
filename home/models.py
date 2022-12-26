
from django.db import models


# Create your models here.


class FirstView(models.Model):
    def __str__(self):
        return
        
class Lesson(models.Model):
    name = models.CharField(max_length=200)
    details = models.CharField(max_length=1000)
    teachers = models.ManyToManyField('Teachers')
    price = models.FloatField(default=0)
    duration = models.CharField(max_length=10)
    time_duration =models.FloatField(default=0)
    language = models.ManyToManyField('Language')
    lesson_image =models.ImageField(upload_to="lesson-img/", null=True)
    

    class Meta:
        ordering= ['name']

    def __str__(self) -> str:
        return f"{self.name} - {self.details}"

class Language(models.Model):
    language = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.language}"

class Teachers(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    about = models.CharField(max_length=200)
    email = models.EmailField()
    teacher_image = models.ImageField(upload_to="teacher-img/", null=True)
    phone = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return f"{self.last_name}  {self.first_name} - {self.about}"
 
class Student(models.Model):
    date_birth = models.DateTimeField(auto_now=True, null=True,)
    region = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.date_birth} {self.region} {self.city} {self.zip_code} {self.first_name} {self.last_name} {self.phone}"

class PaymentMethod(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Payment(models.Model):
    paymentDate = models.DateTimeField(auto_now=True, null=True,)
    paymentMethod = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    lessonBuy = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f"{self.paymentDate} {self.paymentMethod}"

class Class(models.Model):
    name = models.CharField(max_length=200)
    teacher = models.ManyToManyField('Teachers')
    lesson = models.ManyToManyField('Lesson')

    def __str__(self) -> str:
        return f"{self.name} {self.teacher} {self.lesson}"

class ClassStudent(models.Model):
    classStudent = models.ForeignKey(Class, on_delete=models.CASCADE, null=True)
    student = models.ManyToManyField('Student')

    def __str__(self) -> str:
        return f"{self.classStudent} {self.student}"

