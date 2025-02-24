from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.modles import Post,Comment
from blog.forms import PostForms,CommentForm
from django.views.generic import TemplateView,ListView,DeleteView,CreateView,UpdateView,DeleteView
# Create your views here.
class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__ite=timezone.now()).order_by('-published_date')

class PostDetailView(DeleteView):
    model = Post

class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForms
    model = Post

class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForms
    model = Post
class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post
    
    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')