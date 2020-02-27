from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required

from .models import Notification

from twitteruser.models import CustomUser

@login_required()
def notification_view(request, id):
    html = 'notify.html'
    user = CustomUser.objects.get(id=id)
    notify = Notification.objects.filter(user=user)
    return render(request, html, {'notify': notify, 'users': user})

@login_required()
def clear_notify(request):
    clear_note = Notification.objects.all().delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))