from django.urls import path
from . import  views

urlpatterns = [
    path('', views.index, name='home'),
    path('like/', views.like_it, name="like-it"),
    path('new/join', views.new_github, name="new-github"),
]