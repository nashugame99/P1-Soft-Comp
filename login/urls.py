from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^professional-login/$', auth_views.login, {'template_name': 'professional.html'}, name='professional'),
    url(r'^amateur-login/$', auth_views.login, {'template_name': 'amateur.html'}, name='amateur'),
    url(r'^professional-logout/$', auth_views.logout, {'template_name': 'professional-logout.html'}, name='professional-logout'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'amateur-logout.html'}, name='amateur-logout'),
]
