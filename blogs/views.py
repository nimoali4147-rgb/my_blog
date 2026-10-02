from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post


# Create your views here.
def hello(request):
    return HttpResponse('Hello world!')

def home(request):
    return render(request, 'index.html')

def  about(request):
    return render(request, "about.html")

def  contact(request):
    contact = {
        "email": "nimo@gmail.com"
    }
    return render(request, "contact.html", contact)


def blogs(request):
    posts = Post.objects.all()
    return render(request, "blogs.html", {"posts": posts})

def blog_detail(request, slug):
    # post = Post.objects.get(id=post_id)
    post = get_object_or_404(Post, slug=slug) # get_object_or_404 - which id you search if not an existing id it retutn page not found 404
    return render(request, "blog_detail.html",{"post": post})

# try:
#     post = Post.objects.get(id=post_id)
# except Post.DoesNotExist:
#     raise Http404