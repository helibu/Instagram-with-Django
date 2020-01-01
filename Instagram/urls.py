from django.urls import path
from . import views 

urlpatterns = [
    path('', views.HelloWorld.as_view(), name='helloworld'),
    path('posts/', views.PostsView.as_view(), name= 'posts'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name= 'post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name= 'make_post'),
    path('post/update/<int:pk>/', views.PostUpdateView.as_view(), name= 'update_post'),
    path('post/delete/<int:pk>/', views.PostDeleteView.as_view(), name= 'delete_post'),

]
