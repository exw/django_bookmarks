from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Link(models.Model):
    url = models.URLField(unique=True)
    def __unicode__(self):
        return self.url

class Bookmark(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User)
    link = models.ForeignKey(Link)
    def __unicode__(self):
        return u'%s, %s' % (self.user.username, self.link.url)

class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bookmarks = models.ManyToManyField(Bookmark)
    def __unicode__(self):
        return self.name

class SharedBookmark(models.Model):
    bookmark = models.OneToOneField(Bookmark)
    date = models.DateTimeField(auto_now_add=True)
    votes = models.IntegerField(default=1)
    users_voted = models.ManyToManyField(User)
    def __unicode__(self):
        return u'%s, %s' % (self.bookmark, self.votes)
