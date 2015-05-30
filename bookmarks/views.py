from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.models import User

# Create your views here.

def main_page(request):
    template = loader.get_template('main_page.html')
    variables = RequestContext(request, {
        'head_title': u'Django Bookmarks',
        'page_title': u'Welcome to Django Bookmarks',
        'page_body': u'Where you can store and share bookmarks!'
        })
    output = template.render(variables)
    return HttpResponse(output)

def user_page(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        raise Http404(u'Requested user not found.')

    bookmarks = user.bookmark_set.all()

    template = loader.get_template('user_page.html')
    variables = RequestContext(request, {
        'username': username,
        'bookmarks': bookmarks
        })
    output = template.render(variables)
    return HttpResponse(output)
