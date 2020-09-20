from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages


def login_page(request):
    if request.user.is_authenticated:
        return redirect('main')
    if request.method == 'POST':
        print(request.POST)
        try:
            u = User.objects.get(email=request.POST.get('user_email'))
        except User.DoesNotExist:
            u = None
        print(u)
        user = authenticate(username=u.username,
                            password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            messages.add_message(request, messages.INFO,
                                 'Упс! Не подошло. Попробуй ещё!')
            return render(request, 'pages/login.html', {})
    else:
        return render(request, 'pages/login.html', {})


def user_logout(request):
    logout(request)
    return redirect('main')
