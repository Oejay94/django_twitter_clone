from django.urls import path

from tweet import views

urlpatterns = [
    path('post_tweet/', views.PostTweet.as_view(), name='post_tweet'),
    path('tweet_page/<int:id>/', views.TweetPage.as_view(), name='tweet_page'),
    path('delete_tweet/<int:id>/', views.DeleteTweet.as_view(), name='delete_tweet')
]