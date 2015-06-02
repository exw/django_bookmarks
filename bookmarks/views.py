from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.models import User
from django.shortcuts import render_to_response

from django.http import HttpResponseRedirect
from django.contrib.auth import logout

# Create your views here.

def main_page(request):
    return render_to_response(
        'main_page.html',
        {'user': request.user}
    )

def user_page(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        raise Http404(u'Requested user not found.')

    bookmarks = user.bookmark_set.all()

    return render_to_response(
            'user_page.html',
            {'username': username,
            'bookmarks':bookmarks}
            )

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

