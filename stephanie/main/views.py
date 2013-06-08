from django.utils.timezone import utc
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.core.urlresolvers import reverse

from sorl.thumbnail import get_thumbnail

from .models import Category, Artwork
from . import forms


def robots_txt(request):
    return http.HttpResponse(
        'User-agent: *\n'
        '%s: /' % ('Allow' if settings.ENGAGE_ROBOTS else 'Disallow'),
        mimetype='text/plain',
    )


def home(request):
    data = {}
    data['artworks'] = Artwork.objects.all()
    return render(request, 'main/home.html', data)


def contact(request):
    data = {}
    if request.POST:
        form = forms.Contact(request.POST)
        if form.is_valid():
            contact_item = form.save()
            tos = [x[1] for x in settings.MANAGERS]
            body = contact_item.message.strip()
            body += '\n\n--\nSent from %s' % request.build_absolute_uri()
            result = send_mail(
                "Email from Contact page",
                body,
                contact_item.email,
                tos
            )
            if result:
                contact_item.sent = True
                contact_item.save()
            url = reverse('main:contact')
            url += '?sent=1'
            return redirect(url)
    else:
        form = forms.Contact()
    data['form'] = form
    data['sent'] = request.GET.get('sent')
    return render(request, 'main/contact.html', data)
