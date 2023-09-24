from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# class UserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('username', 'password1', 'password2')
# class CustomAuthenticationForm(AuthenticationForm):
#     class Meta:
#         model = User
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/')
    bio = models.TextField()
    birthday = models.DateField()

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='courses/', null=True, blank=True)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title

class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.lesson.title}"

