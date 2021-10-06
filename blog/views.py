from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
  CreateView,
  UpdateView, 
  DeleteView,
)
from django.urls import reverse_lazy
from .models import Post

class AdminBlogListView(ListView):
  model = Post
  template_name = "admin_home.html"
  context_object_name = "admin_all_posts_list"

class UserBlogListView(ListView):
  model = Post
  template_name = "user_home.html"
  context_object_name = "user_all_posts_list"

class UserBlogDetailView(DetailView):
  model= Post
  template_name = "user_post_detail.html"

class AdminBlogDetailView(DetailView):
  model= Post
  template_name = "post_detail.html"

class BlogCreateView(CreateView):
  model = Post
  template_name = "post_new.html"
  fields = ["title","author","body"]

class BlogUpdateView(UpdateView):
  model = Post
  template_name = "post_edit.html"
  fields = ["title", "body"]

class BlogDeleteView(DeleteView):
  model = Post
  template_name = "post_delete.html"
  success_url = reverse_lazy('home')