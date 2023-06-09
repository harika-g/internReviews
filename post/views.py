from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages
from .filters import PostFilter


def list_posts(request):
    posts = Post.objects.all().order_by('modified_date').reverse()
    filters = PostFilter(request.GET, queryset=posts)
    context = {
        'posts': posts,
        'filter': filters
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


def edit_post(request, id):

    selected_post = Post.objects.get(id=id)
    # if request.method == 'POST':
    post_form = PostForm(initial={
        'company': selected_post.company,
        'role': selected_post.role,
        'title': selected_post.title,
        'review': selected_post.review,
        'rating': selected_post.rating,
        'duration': selected_post.duration,
        'semester': selected_post.semester,
        'year': selected_post.year,
        'salary': selected_post.salary,
        'industry': selected_post.industry,
        'email': selected_post.email,
        'show_email': selected_post.show_email
    })
    print(selected_post.semester)
    if request.method == "POST":
        post_form = PostForm(request.POST, instance=selected_post)
        if post_form.is_valid():
            post_form.save()
            messages.success(request, f'Post updated')
            return redirect('/posts')
    # context =
    return render(request, 'post/update.html', {'form': post_form})


def delete_post(request, id):
    prev_url = request.META.get('HTTP_REFERER')
    post_to_del = Post.objects.get(id=id)
    post_to_del.delete()
    return redirect(prev_url)


def my_posts(request):
    posts = Post.objects.filter(email=request.user.email).order_by(
        'modified_date').reverse()
    filters = PostFilter(request.GET, queryset=posts)
    context = {
        'posts': posts,
        'filter': filters
    }
    return render(request, 'post/list.html', context)
