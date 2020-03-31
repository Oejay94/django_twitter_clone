from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required

from .models import Notification

from twitteruser.models import TwitterUser

@login_required()
def notification_view(request, id):
    html = 'notify.html'
    user = TwitterUser.objects.get(id=id)
    notify = Notification.objects.filter(user=user, viewed=False)
    for i in notify:
        i.viewed = True
        i.save()
    return render(request, html, {'notify': notify, 'users': user})
