from django.urls import path

from authentication import views

urlpatterns = [
    path('login/', views.login_view, name='main'),
    path('logout/', views.logout_view, name='logout')
]