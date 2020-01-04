from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('new/', views.new, name='create-post'),
    # path('like', views.like_it, name="like-it"),
]

#Routes
# Home
# Blog Detail
# Profile