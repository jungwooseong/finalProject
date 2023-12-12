from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse
from django.utils import timezone
from rest_framework import viewsets
from .serializers import PostSerializer

from .models import Post
# Create your views here.

def download_list(request):
    
    user_id = request.session.get('user')
    return render(request, 'blog/download.html', {'username':user_id})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, "blog/login.html", {'posts': posts})


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    serializer_class = PostSerializer



def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        
        password = request.POST.get('password', None)
        me = UserModel.objects.get(username=username)
        
        if me.password == password:
            request.session['user'] = me.username
            posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
            return render(request, 'blog/index.html',{'username':username, 'posts':posts})
        else:
            return redirect('/sign-in')
    elif request.method == 'GET':
        return render(request, 'blog/login.html', {})

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/sign-in')



class IntruderImage(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer