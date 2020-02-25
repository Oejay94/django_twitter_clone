from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login

from .forms import create_account
from .models import CustomUser
from tweet.models import Tweet

def create_account_view(request):
    html = 'create_account.html'

    if request.method == 'POST':
        form = create_account(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = CustomUser.objects.create_user(
                username=data['username'], 
                first_name=data['first_name'],
                email=data['email'],
                age=data['age'],
                password=data['password1']
            )
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
    else:
        form = create_account()
    return render(request, html, {'accounts': form})


def home_page(request):
    html = 'home.html'
    tweet = Tweet.objects.all()
    return render(request, html, {'tweets': tweet})


def user_page(request, id):
    html = 'user_page.html'
    user = CustomUser.objects.get(id=id)
    tweet = Tweet.objects.filter(created_by=user)
    return render(request, html, {'user': user, 'tweets': tweet})


def follow_view(request, id):
    follow = CustomUser.objects.get(id=id)
    request.user.username.followers.add(follow)
    return HttpResponseRedirect(reverse('user_page'))