from datetime import datetime
import email
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Author
from .forms import AddPost, AddPostModelForm
from django.contrib.auth.decorators import permission_required

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
    return render(request, 'post.html', {'post':p})



def add_post(request):

    
    if request.method == "POST":
        form = AddPost(request.POST, request.FILES)

        if form.is_valid():
            post = Post()
            post.author = Author.objects.get(email=request.user.email)
            post.issued = datetime.now()
            post.title = form.cleaned_data['title']
            post.subtitle = form.cleaned_data['subtitle']
            post.content = form.cleaned_data['content']
            post.image = form.cleaned_data['image']
            post.post_type = form.cleaned_data['post_type']

            post.save()

            return redirect('posts')
    else:
        form = AddPost()  

    return render(request, "add_post.html", {'form':form})



@permission_required('app.add_post')
def add_post_model_form(request):
    if request.method == "POST":
        form = AddPostModelForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = Author.objects.get(email=request.user.email)
            post.issued = datetime.now()
            post.save()

            form.save_m2m()

            return redirect('posts')
    else:
        form = AddPostModelForm()  

    return render(request, "add_post.html", {'form':form})

