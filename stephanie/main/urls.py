from django.conf.urls import patterns, url, include

from . import views

urlpatterns = patterns(
    '',
    url('^robots\.txt$',
        views.robots_txt,
        name='robots_txt'),
    url(r'^$', views.home,
        name='home'),
    url(r'^contact/$', views.contact,
        name='contact'),
    url(r'^artwork/(?P<slug>[-\w]+)$', views.artwork,
        name='artwork'),
)
