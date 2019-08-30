from django.urls import path
from . import views

app_name = 'eventos'
urlpatterns = [
    #path('', views.index, name='index'),
    path(r'eventos', views.CalendarView.as_view(), name='eventos'),
]