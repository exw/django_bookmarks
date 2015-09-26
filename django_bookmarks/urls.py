"""django_bookmarks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from bookmarks import views as bookmarks

from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # Browsing
    url(r'^$', bookmarks.main_page, name='main_page'),
    url(r'^user/(\w+)/$', bookmarks.user_page, name='user_page'),
    url(r'^tag/([^\s]+)/$', bookmarks.tag_page, name='tag_page'),
    url(r'^tag/$', bookmarks.tag_cloud_page, name='tag_cloud_page'),
    url(r'^search/$', bookmarks.search_page, name='search_page'),

    # Session management
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', bookmarks.logout_page, name='logout_page'),
    url(r'^register/$', bookmarks.register_page, name='registration_page'),
    url(r'^register/success/$', TemplateView.as_view(template_name='registration/register_success.html')),

    # Account management
    url(r'^save/$', bookmarks.bookmark_save_page, name='bookmark_save_page'),

    # Ajax
    url(r'^ajax/tag/autocomplete/$', bookmarks.ajax_tag_autocomplete, 
        name ='ajax_tag_autocomplete'),

    # Static Files
    # url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': site_media}),
]
