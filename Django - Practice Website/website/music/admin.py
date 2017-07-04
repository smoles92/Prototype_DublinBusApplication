from django.contrib import admin

from .models import Album, Song

admin.site.register(Album) # Register album
admin.site.register(Song) # Register song
