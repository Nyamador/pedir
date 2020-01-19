from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.shortcuts import render, get_object_or_404, redirect
from users.models import Profile
from blog.models import Post
from blog.forms import BlogCreationForm
from users.forms import ProfileForm


def index(request):
    qs = Post.objects.all()
    trends = "sih"
    context = {
        'qs': qs
    }
    return render(request, 'pages/index.html', context)


class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'pages/post_update_view.html'


def new(request):
    if request.method == 'POST':
            user = request.user
            title = request.POST.get('title')
            body = request.POST.get('body')
            new_post = Post(user=user, title=title, body=body)
            new_post.save()
            return redirect('home')

    return render(request, 'pages/new-post.html')


def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

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

def edit(request):
    context = {
        'form' : ProfileForm
    }
    return render(request, 'pages/edit_profile.html', context )

    