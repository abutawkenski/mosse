from django.shortcuts import render, redirect
from .models import Blog, About, Tag
from .forms import SubForm, CommentsForm, Comments
# Create your views here.


def index(request):
    return render(request, 'index.html')


def blog(request):
    blog = Blog.objects.all()
    sub = SubForm(request.POST or None)
    if sub.is_valid():
        sub.save()

    ctx = {
        'blogs': blog,
        'sub': sub
    }
    return render(request, 'blog.html', ctx)

def detail(request, pk):
    blog = Blog.objects.get(id=pk)
    comments = CommentsForm(request.POST or None)
    if comments.is_valid():
        com = comments.save(commit=False)
        com.blog = blog
        com.save()
        return redirect('.')
    ctx = {
        'blog': blog,
        'comments': comments,
    }
    return render(request, 'blog-single.html', ctx)


def about(request):
    about = About.objects.all()
    ctx = {
        'about': about
    }
    return render(request, 'about.html', ctx)

def contact(request):
    return render(request, 'contact.html')