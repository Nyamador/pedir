from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('new/', views.new, name='create-post'),
    path('b/<slug:slug>', views.detail, name='post-detail'),
    path('view/', views.profile_view, name='view-profile'),
    # path('like', views.like_it, name="like-it"),
]