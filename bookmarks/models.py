from django.db import models

# Create your models here.
from django.db import models

class Link(models.Model):
    url = models.URLField(unique=True)
