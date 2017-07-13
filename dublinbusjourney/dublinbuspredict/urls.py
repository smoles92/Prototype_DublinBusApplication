from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^map$', views.map, name='map'),
    url(r'^connections$', views.connections, name='connections'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^tickets_fares$', views.tickets_fares, name='tickets_fares'),
    url(r'^sampleQuery$', views.sampleQuery, name='sampleQuery'),
    url(r'^pilotRoutes', views.pilot_routes, name='pilot_routes'),
    url(r'^pilotDest$', views.pilot_dest, name='pilot_dest'),
    url(r'^runModel$', views.run_model, name='run_model'),
    ]
