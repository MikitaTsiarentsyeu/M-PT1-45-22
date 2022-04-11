from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.db.models import Q
# Create your views here.

def index(request):
    posts = Post.objects.order_by('-datetime')
    search_query = request.GET.get('search', '')
    if search_query:
        posts = Post.objects.filter(Q(title__icontains = search_query) | Q(content__icontains = search_query) | Q(preview__icontains = search_query)).order_by('-datetime') 
    else:
        posts = Post.objects.order_by('-datetime') 
    return render(request, 'main/index.html', {'title' : 'Главная страница', 'posts' : posts})

def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            preview = form.cleaned_data['preview']
            content = form.cleaned_data['content']
            image = form.cleaned_data['image']
            new_post_cleared= Post(title =title,
                                   preview=preview,
                                   content =content,
                                   image =image,)
            new_post_cleared.save()
            return redirect('home')
        else: 
            error = "Укажите корректные данные"
    context = {'form' : form, 'error' : error}
    return render(request, 'main/create.html', context)


def article(request, post_id):
    error = ''
    current_post = Post.objects.get(id = post_id)
    title = current_post.title
    latest_comments = Comment.objects.filter(post = post_id).order_by('-datetime')
    if request.method == 'POST':
        comment_form  = CommentForm(request.POST)
        if comment_form.is_valid():
            author_name = comment_form.cleaned_data['author_name']
            comment_text = comment_form.cleaned_data['comment_text']
            new_comment_cleared= Comment(post = current_post,
                                    author_name=author_name,
                                    comment_text =comment_text,)
            new_comment_cleared.save()
            return HttpResponseRedirect(f'/posts/{post_id}#comment')
        else: 
            error = "Укажите корректные данные"
    return render(request, 'main/article.html', {'title' : title, 'post': current_post,'latest_comments': latest_comments,'form':CommentForm,'error' : error, })