from django.urls import path

from . import views

urlpatterns = [

    path('posts', views.list_posts, name='list_posts'),

    path('post/create', views.create_post, name='create_post'),

    path('post/edit', views.edit_post, name='edit_post'),

    path('post/delete', views.delete_post, name='delete_post'),

    path('post/myposts', views.my_posts, name='my_posts'),

]
