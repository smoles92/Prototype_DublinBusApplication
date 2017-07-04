from django.conf.urls import url
from . import views # from current directory import Python file/module called views

app_name = 'music' # Set this to your app name

urlpatterns = [
    # /music/
    url(r'^$', views.index, name= 'index'),
    
    # /music/<album_id>/
    # Look for pattern with the number, and forward slash, pull out no and treat as album id
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'), 
    
    # /music/<album_id>/favorite
    # Look for pattern with the number, and forward slash, pull out no and treat as album id
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'), 
    ]