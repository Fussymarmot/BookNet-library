from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .forms import RegisterForm, ProfileForm


def register(request):
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # сразу входим после регистрации
            return redirect('profile')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


@login_required
def profile(request):
    """Страница профиля текущего пользователя с возможностью редактирования."""
    profile_obj = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile_obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль обновлён.')
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile_obj)

    books = request.user.books.all()
    return render(request, 'accounts/profile.html', {
        'profile_user': request.user,
        'form': form,
        'books': books,
    })


def user_profile(request, username):
    """Публичная страница профиля другого пользователя (только просмотр)."""
    user_obj = get_object_or_404(User, username=username)
    books = user_obj.books.all()
    return render(request, 'accounts/public_profile.html', {
        'profile_user': user_obj,
        'books': books,
    })
