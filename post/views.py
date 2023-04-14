from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages


def list_posts(request):
    posts = Post.objects.all().order_by('modified_date').reverse()
    context = {
        'posts': posts,
    }
    return render(request, 'post/list.html', context)


def create_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST, initial={
            'email': request.user.email})
        if post_form.is_valid():
            post_form.save()
            messages.success(request, f'New post created!')

            return redirect('/posts')
    else:
        post_form = PostForm(initial={
            'email': request.user.email})
    context = {'form': post_form}
    return render(request, 'post/create.html', context)


def edit_post(request, pk):
    return render(request, 'post/update.html', context)


def delete_post(request, pk):

    return render(request, 'post/delete.html', context)


def my_posts(request):
    posts = Post.objects.filter(email=request.user.email).order_by(
        'modified_date').reverse()
    context = {
        'posts': posts,
    }
    return render(request, 'post/list.html', context)
