from django.shortcuts import render

from .models import Notification

from twitteruser.models import CustomUser

def notification_view(request, id):
    html = 'notify.html'
    user = CustomUser.objects.get(id=id)
    notify = Notification.objects.filter(user=user)
    return render(request, html, {'notify': notify, 'users': user})
