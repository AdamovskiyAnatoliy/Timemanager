from django.contrib import admin

from .models import Note, Dream, TopDream

admin.site.register(Note)
admin.site.register(Dream)
admin.site.register(TopDream)
