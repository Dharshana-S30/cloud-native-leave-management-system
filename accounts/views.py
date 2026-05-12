from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from .models import UserProfile
from .forms import SignupForm
from .models import UserProfile


def login_view(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                profile = UserProfile.objects.get(user=user)

                if profile.role == 'employee':
                    return redirect('employee_dashboard')

                elif profile.role == 'manager':
                    return redirect('manager_dashboard')

                else:
                    return redirect('login')

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')

def signup_view(request):
    form = SignupForm()

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Create UserProfile
            role = form.cleaned_data['role']
            UserProfile.objects.create(user=user, role=role)

            return redirect('login')

    return render(request, 'signup.html', {'form': form})