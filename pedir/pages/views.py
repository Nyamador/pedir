from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from users.models import Profile
from blog.models import Blog
from blog.forms import BlogCreationForm


def index(request):
    qs = Blog.objects.all()

    context = {
        'qs': qs
    }
    return render(request, 'pages/index.html', context)


def new(request):
    if request.method == 'POST':
            user = request.user
            title = request.POST.get('title')
            body = request.POST.get('body')
            new_blog = Blog(user=user, title=title, body=body)
            new_blog.save()
            return redirect('home')

    return render(request, 'pages/new-post.html')


def detail(request, slug):
    post = get_object_or_404(Blog, slug=slug)

    context = {
        'post': post
    }
    return render(request, 'pages/detail.html', context)


def create_profile(request):
    return render(request, 'pages/create_profile.html')


def profile_view(request):
    # profile = get_object_or_404(Profile, slug=slug)
    # context = {
    #     'profile': profile
    # }
    return render(request, 'pages/profile_view.html')
