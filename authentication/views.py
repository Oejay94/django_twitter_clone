from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.views import View

from .forms import login_form

from twitteruser.models import CustomUser

# def login_view(request):
#     html = 'main.html'

#     if request.method == 'POST':
#         form = login_form(request.POST)

#         if form.is_valid():
#             data = form.cleaned_data
#             user = authenticate(
#                 username=data['username'],
#                 password=data['password']
#             )
#             if user is not None:
#                 login(request, user)
#                 return render(request, 'user_page.html')
#     else:
#         form = login_form()

#     return render(request, html, {'login': form})

class LoginView(View):
    def get(self, request):
        html = 'main.html'
        form = login_form()
        return render(request, html, {'login': form})

    def post(self, request):
        form = login_form(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )
            if user is not None:
                login(request, user)
                return render(request, 'user_page.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(request.GET.get('next', '/login/'))

