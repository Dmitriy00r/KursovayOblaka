from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm


# Create your views here.
def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # получаем имя пользователя и пароль из формы
            username = form.cleaned_data.get('username')
            messages.success(request, f'Создан аккаунт {username}!')
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/regist.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'registration/profile.html')

