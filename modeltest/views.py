from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, "post_list.html", context)

def search(request):
    title = request.GET.get("title")
    print(title)
    
    titles = Post.objects.filter(name__contains=title)
    print(titles)
    return render(request, "search.html")