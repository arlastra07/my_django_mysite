from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 127.0.0.1:8000 --> local
    # mydjangosite.com --> online
    path('', views.post_list, name='post_list'),

    #127.0.0.1:8000/post/2 --> local
    # mydjangosite.com/post/2 --> online
    path('post/<int:pk>', views.post_detail, name='post_detail'),

    #127.0.0.1:8000/post/new --> local
    # mydjangosite.com/post/new --> online
    path('post/new/', views.post_new, name='post_new'),
    #127.0.0.1:8000/post/2/edit --> local
    # mydjangosite.com/post/2/edit --> online
    path('post/<int:pk>/edit', views.post_edit, name='post_edit'),
] 
