#urls.py for main app

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'main.views.home', name='home'),
)