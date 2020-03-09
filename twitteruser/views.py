from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views import View

from .forms import create_account
from .models import CustomUser

from tweet.models import Tweet
from notification.models import Notification


# def create_account_view(request):
#     html = 'create_account.html'

#     if request.method == 'POST':
#         form = create_account(request.POST)

#         if form.is_valid():
#             data = form.cleaned_data
#             user = CustomUser.objects.create_user(
#                 username=data['username'],
#                 first_name=data['first_name'],
#                 email=data['email'],
#                 age=data['age'],
#                 password=data['password1']
#             )
#             login(request, user)
#             return render(request, 'user_page.html')
#     else:
#         form = create_account()
#     return render(request, html, {'accounts': form})

class CreateAccount(View):
    def get(self, request):
        html = 'create_account.html'
        form = create_account()
        return render(request, html, {'accounts': form})

    def post(self, request):
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
            return render(request, 'user_page.html')


@login_required()
def home_page(request):
    html = 'home.html'
    user = Tweet.objects.filter(created_by=request.user)
    following_user = Tweet.objects.filter(
        created_by__in=request.user.following_field.all())
    tweets = user | following_user
    notify = Notification.objects.filter(user=request.user)
    return render(request, html, {'tweets': tweets, 'notify': notify})


def user_page(request, id):
    html = 'user_page.html'
    user = CustomUser.objects.get(id=id)
    tweet = Tweet.objects.filter(created_by=user)
    return render(request, html, {'user': user, 'tweets': tweet})


def follow_view(request, id):
    follow = CustomUser.objects.get(id=id)
    request.user.following_field.add(follow)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def unfollow_view(request, id):
    unfollow = CustomUser.objects.get(id=id)
    request.user.following_field.remove(unfollow)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
