from django.shortcuts import render
# from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
# from .models import UserCreationForm, CustomAuthenticationForm
# from django.contrib.auth import login as login
from .forms import StudentRegistrationForm
from .models import Student

def home(request):
    return render(request, 'home.html')
#
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('home')  # Điều hướng tới trang chính sau khi đăng kí
#     else:
#         form = UserCreationForm()
#     return render(request, 'register.html', {'form': form})
#
#
#
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             # Redirect to a success page.
#             return redirect('success_page_name')
#         else:
#             # Return an 'invalid login' error message.
#             return render(request, 'login.html', {'error_message': 'Invalid login credentials'})
#     else:
#         return render(request, 'login.html')
def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            student = Student(user=user, birthday=form.cleaned_data['birthday'])
            student.save()
            return redirect('home')  # Redirect to login page
    else:
        form = StudentRegistrationForm()
    return render(request, 'register.html', {'form': form})