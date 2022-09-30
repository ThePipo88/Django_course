from importlib.resources import contents
from django.shortcuts import render,HttpResponse
from .models import Post

# Create your views here.
def posts(request):
    posts = Post.objects.all()
    return HttpResponse(posts)

def post(request,id):
    blog = Post.objects.get(id=id)
    content = f'{blog.title} - {blog.desc}'
    return HttpResponse(content)
