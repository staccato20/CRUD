from django.db import models
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog, Hashtag
from .forms import CreateForm, CommentForm, HashtagForm
import json
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# Create your views here.

def main(request):
    blogs = Blog.objects
    hashtags = Hashtag.objects
    return render(request, 'blog/main.html', {'blogs':blogs, 'hashtags':hashtags})

def write(request):
    return render(request, 'blog/write.html')

#왤까... 이게 된 이유가... 이게 원래꺼(m2m 안됐던거임)
# def create(request, blog=None):
#    if request.method == "POST":
#       form = CreateForm(request.POST, instance=blog)
#        if form.is_valid():
#            blog = form.save(commit=False)
#            form.save_m2m()
#            blog.pub_date = timezone.datetime.now()
#            blog.save()
#            return redirect('main')
#    else:
#        form = CreateForm(instance=blog)
#        return render(request, 'blog/write.html', {'form':form})

#def blogform(request, blog=None):
#    if request.method == 'POST':
#        form = CreateForm(request.POST, instance=blog)
#        if form.is_valid():
#            blog = form.save(commit=False)
#            blog.pub_date = timezone.datetime.now()
#            blog.save()
#            form.save_m2m()
#            return redirect('main')
#    else:
#        form = CreateForm(instance=blog)
#        return render(request, 'blog/write.html', {'form':form})

def create(request, blog=None):
    if request.method == "POST":
        form = CreateForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.pub_date = timezone.datetime.now()
            blog.save()
            form.save_m2m()
            return redirect('main')
    else:
        form = CreateForm(instance=blog)
        return render(request, 'blog/write.html', {'form':form})


def blogform(request, blog=None):
    if request.method == 'POST':
        form = CreateForm(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.pub_date = timezone.datetime.now()
            blog.save()
            form.save_m2m()
            return redirect('main')
    else:
        form = CreateForm(instance=blog)
        return render(request, 'blog/write.html', {'form':form})

def base(request):
    return render(request, 'blog/base.html')

def edit(request, id):
    blog = get_object_or_404(Blog, id = id)
    if request.method == "POST":
        form = CreateForm(request.POST, instance=blog)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('main')
    else:
        form = CreateForm(instance=blog)
    return render(request, 'blog/edit.html', {'form':form})

def delete(request, id):
    delete_blog = get_object_or_404(Blog, id = id)
    delete_blog.delete()
    return redirect ('main')

# 댓글 함수
def detail(request, id):
    blog = get_object_or_404(Blog, id = id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = blog
            comment.text = form.cleaned_data['text']
            comment.save()
            return redirect('detail', id)
    else:
        form=CommentForm()
        return render(request, 'blog/detail.html', {'blog':blog, 'form':form})

# 해시태그 함수
def hashtagform(request, hashtag=None):
    if request.method == 'POST':
        form = HashtagForm(request.POST, instance=hashtag)
        if form.is_valid():
            hashtag = form.save(commit=False)
            if Hashtag.objects.filter(name=form.cleaned_data['name']):
                form = HashtagForm()
                error_message = "이미 존재하는 해시태그 입니다."
                return render(request, 'blog/hashtag.html', {'form':form, "error_message": error_message})
            else:
                hashtag.name = form.cleaned_data['name']
                hashtag.save()
            return redirect('main')
    else:
        form = HashtagForm(instance=hashtag)
        return render(request, 'blog/hashtag.html', {'form':form})

def search(request, hashtag_id):
    hashtag = get_object_or_404(Hashtag, id=hashtag_id)
    return render(request, 'blog/search.html', {'hashtag':hashtag})

@login_required
@require_POST
def video_like(request):
    pk = request.POST.get('pk', None)
    video = get_object_or_404(Blog, pk=pk)
    user = request.user

    if video.likes_user.filter(id=user.id).exists():
        video.likes_user.remove(user)
        message = '좋아요 취소'
    else:
        video.likes_user.add(user)
        message = '좋아요'

    context = {'likes_count':video.count_likes_user(), 'message': message}
    return HttpResponse(json.dumps(context), content_type="application/json")
