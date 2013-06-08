from django.core.urlresolvers import reverse
from django.conf import settings


def base(request):
    data = {
        'PROJECT_TITLE': settings.PROJECT_TITLE,
        'PROJECT_DESCRIPTION': settings.PROJECT_DESCRIPTION,
    }

    navs = [
        {'url': reverse('main:home'), 'title': 'Home'},
        {'url': '/artwork', 'title': 'Artwork'},
        {'url': '/photography', 'title': 'Photography'},
        {'url': '/about', 'title': 'About'},
        {'url': reverse('main:contact'), 'title': 'Contact'},
    ]
    for nav in navs:
        active = False
#        print "COMPARE", (request.path, nav['url'])
        if request.path == nav['url']:
            active = True
        nav['active'] = active

    data['navs'] = navs

    return data
