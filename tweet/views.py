from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Tweet
from .forms import post_tweet

def post_tweet_view(request):
    html = 'post_tweet.html'

    if request.method == 'POST':
        form = post_tweet(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Tweet.objects.create(
                body=data['body'],
                created_by=request.user
            )
            return HttpResponseRedirect(reverse('home'))
    else:
        form = post_tweet()
    
    return render(request, html, {'post': form})