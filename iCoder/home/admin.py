import imp
from operator import contains
from django.contrib import admin
from .models import Contact

admin.site.register(Contact)