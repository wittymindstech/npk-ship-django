from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from knotend.forms import SignUpForm, LoginForm
from knotend.models import Courses, Blog


def index(request):
    npkc = Courses.objects.all()
    npkb = Blog.objects.all()
    context = {"courses": npkc, "blogs": npkb}
    return render(request, "index.html", context)


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, "register.html", {'form': form})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                if request.user.is_superuser:
                    return redirect('/')
                return redirect("/")

            else:
                msg = "Username or Password Doesn't match"

        else:
            msg = 'Error validating the form'
    return render(request, "login.html", {"form": form, "msg": msg})


def profile(request, username):
    user = get_object_or_404(User, username=username)
    us = User.objects.filter(username=user)
    return render(request, 'profile.html', {'profile': us})
