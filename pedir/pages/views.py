from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from users.models import Profile
from blog.models import Blog


def index(request):
    qs = Blog.objects.all()

    context = {
        'qs': qs
    }
    return render(request, 'pages/index.html', context)


def new(request):
    return render(request, 'pages/new-post.html')


def detail(request, slug):
    post = get_object_or_404(Blog, slug=slug)

    context = {
        'post': post
    }
    return render(request, 'pages/detail.html', context)


def create_profile(request):
    return render(request, 'pages/create_profile.html')

# @login_required
# def profile_view(request, slug):
#     profile = get_object_or_404(Profile, slug=slug)
#     context = {
#         'profile': profile
#     }
#     return render(request, 'pages/profile_view.html', context)
