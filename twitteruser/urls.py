from django.urls import path

from twitteruser import views

urlpatterns = [
    path('create_account/', views.CreateAccount.as_view(), name='create_account'),
    path('', views.home_page, name='home'),
    path('user_page/<int:id>/', views.user_page, name='user_page'),
    path('follow/<int:id>/', views.follow_view, name='follow'),
    path('unfollow/<int:id>/', views.unfollow_view, name='unfollow')
]