from django.shortcuts import render, get_object_or_404
from .models import Profile, Post

def home_page(request):
    posts = Post.objects.all().order_by('-id')
    profiles = Profile.objects.all()
    return render(request, 'home.html', {'posts': posts, 'profiles': profiles})

def profile_page(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    posts = profile.post_set.all().order_by('-id')
    return render(request, 'profile.html', {'profile': profile, 'posts': posts})

def search_page(request):
    query = request.GET.get('q', '')
    posts = Post.objects.filter(content__icontains=query)
    profiles = Profile.objects.filter(name__icontains=query)
    return render(request, 'search_results.html', {'query': query, 'posts': posts, 'profiles': profiles})
