from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'eventos'
urlpatterns = [
    #path('', views.index, name='index'),
    path(r'eventos', views.CalendarView.as_view(), name='calendar'),
    path(r'eventos/new/', views.event, name='event_new'),
    path(r'eventos/edit/(?P<event_id>\d+)/', views.event, name='event_edit'),
]