from django.shortcuts import render
from .models import Post


def home(request):
    context = {'posts' : Post.objects.all() }

    return render(request, 'blog/home.html', context)

def about(req):
    return render(req, 'blog/about.html', {'title' : 'about'})