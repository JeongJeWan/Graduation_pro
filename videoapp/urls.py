from django.urls import path
from . import views

app_name = 'videoapp'

urlpatterns = [
    path('', views.index, name='video_main'),
    path('list/', views.list_index, name='list'),
]
