from django.urls import path

from tweet import views

urlpatterns = [
    path('post_tweet/', views.post_tweet_view, name='post_tweet')
]