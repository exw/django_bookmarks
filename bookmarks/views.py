from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

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
