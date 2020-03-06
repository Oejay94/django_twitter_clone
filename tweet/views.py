from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views import View
import re

from .models import Tweet
from .forms import post_tweet

from notification.models import Notification
from twitteruser.models import CustomUser


# def post_tweet_view(request):
#     html = 'post_tweet.html'

#     if request.method == 'POST':
#         form = post_tweet(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             add_tweet = Tweet.objects.create(
#                 body=data['body'],
#                 created_by=request.user
#             )
#             # Peter Marsh helped with mentioning users in a tweet

#             # Check if @ sign is inside tweet
#             if '@' in data['body']:
#                 # If it is then grab username that follows @ character
#                 find_user = re.findall(r'@(\w+)', data['body'])
#                 target_username = find_user[0]
#                 # Get the instance of the twitter user based off of username
#                 target_user = CustomUser.objects.get(username=target_username)

#                 Notification.objects.create(
#                     user=target_user,
#                     tweet=add_tweet
#                 )
#             return HttpResponseRedirect(reverse('home'))
#     else:
#         form = post_tweet()

#     return render(request, html, {'post': form})


class PostTweet(View):

    def get(self, request):
        html = 'post_tweet.html'
        form = post_tweet()
        return render(request, html, {'post': form})

    def post(self, request):
        form = post_tweet(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            add_tweet = Tweet.objects.create(
                body=data['body'],
                created_by=request.user
            )
            # Peter Marsh helped with mentioning users in a tweet

            # Check if @ sign is inside tweet
            if '@' in data['body']:
                # If it is then grab username that follows @ character
                find_user = re.findall(r'@(\w+)', data['body'])
                target_username = find_user[0]
                # Get the instance of the twitter user based off of username
                target_user = CustomUser.objects.get(username=target_username)

                Notification.objects.create(
                    user=target_user,
                    tweet=add_tweet
                )
            return HttpResponseRedirect(reverse('home'))


# def tweet_page(request, id):
#     html = 'tweet_page.html'
#     tweets = Tweet.objects.get(id=id)
#     return render(request, html, {'tweets': tweets})


class TweetPage(View):

    def get(self, request, id):
        html = 'tweet_page.html'
        tweets = Tweet.objects.get(id=id)
        return render(request, html, {'tweets': tweets})
