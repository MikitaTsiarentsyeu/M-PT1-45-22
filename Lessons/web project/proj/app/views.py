from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Author

def home(request):
    return render(request, 'home.html', {"test": 1234})

# def posts(request):
#     posts = Post.objects.all()
#     post_list=''

#     for post in posts:
#         post_list += f"<li><h3>{post.title}</h3><p>by {post.author.name}</p></li>"

#     resp = f"<h1>All posts:</h1><ul>{post_list}</ul>"
#     return HttpResponse(resp)

def posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts':posts})

# def post(request, post_id):
#     p = Post.objects.get(id=post_id)
#     resp = f"<h1>{p.title}</h1><p>{p.content}</p>"
#     return HttpResponse(resp)

def post(request, post_id):
    p = Post.objects.get(id=post_id)
    return render(request, 'post.html', {'post': p})
