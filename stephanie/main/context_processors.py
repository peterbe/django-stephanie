from django.core.urlresolvers import reverse
from django.conf import settings


def base(request):
    data = {
        'PROJECT_TITLE': settings.PROJECT_TITLE,
        'PROJECT_DESCRIPTION': settings.PROJECT_DESCRIPTION,
        'GOOGLE_ANALYTICS': getattr(settings, 'GOOGLE_ANALYTICS', not settings.DEBUG),
    }

    navs = [
        {'url': reverse('main:home'), 'title': 'Home'},
        #{'url': reverse('main:artgroup', args=('drawings',)), 'title': 'Drawings'},
        #{'url': reverse('main:artgroup', args=('photography',)), 'title': 'Photography'},
        #{'url': reverse('main:artgroup', args=('paintings',)), 'title': 'Paintings'},
        {'url': reverse('main:about'), 'title': 'About'},
        {'url': reverse('main:contact'), 'title': 'Contact'},
    ]
    for nav in navs:
        active = False
        if request.path == nav['url']:
            active = True
        nav['active'] = active

    data['navs'] = navs

    return data
