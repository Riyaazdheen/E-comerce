from django.shortcuts import render, redirect
from .models import UserModel
from django.contrib.auth.models import User
from .forms import sign_in_form, sign_up_form
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def signin(request):
    user = User()
    if request.method == 'POST':
        form = sign_in_form(request.POST)
        print(request.POST, form.is_valid())
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home:home')
                
    else:
        form = sign_in_form()
    return render(request, 'Account/sign_in.html')

def signout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home:home')

def signup(request):
    context = {"valid":"is valid", "Error":''}
    if request.method == 'POST':
        form = sign_up_form(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            try:
                user = User.objects.get(username=username)
                context["Error"] = "User already Exists"
                context['valid'] = "is-invalid"
            except User.DoesNotExist:
                user = User.objects.create(username=username, password=password, email=email)
                UserModel.objects.create(user=user, phone=1234556)
                return redirect('account:signin')
    return render(request, 'Account/sign_up.html', context)