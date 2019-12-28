from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Post, Like
from django.db.models import F, Count


def index(request):
    feeds = Post.objects.all()
    context ={
        'feeds': feeds
    }

    return render(request, 'pages/index.html', context)

def like_it(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('objectid')
        response_data = {}
        like_object = Like.objects.filter(post=post_id, user=user).exists()
        if not like_object:
            response_data = {}
            post = Post.objects.get(id=post_id)
            post.likes = F('likes') + 1
            post.save()
            post = Post.objects.get(id=post_id)
            post.refresh_from_db() #get the fresh value from the database
            user_like = Like.objects.create(user=user, post_id=post_id)
            user_like.save()
            response_data['result'] = 'Like Successful'
            response_data['likes'] = post.likes

            return JsonResponse(response_data)     
        else:
            response_data = {}
            user_like = Like.objects.get(user=user, post_id=post_id)
            user_like.delete()
            post = Post.objects.get(id=post_id)
            post.likes = F('likes') - 1
            post.save()
            post = Post.objects.get(id=post_id)
            post.refresh_from_db() #get the fresh value from the database
            response_data['result'] = 'Unlike Successful'
            response_data['likes'] = post.likes

            return JsonResponse(response_data)                   
