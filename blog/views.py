from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView , DetailView , CreateView , UpdateView, DeleteView
from . import forms
from .models import Posts

from django.urls import reverse_lazy # new

class BlogListView(ListView):
    model = Posts
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Posts
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Posts
    fields = '__all__'
    template_name = 'post_new.html'
    
class BlogUpdateView(UpdateView):
    model = Posts
    fields = ['title', 'body']
    template_name = 'post_edit.html'

class BlogDeleteView(DeleteView):
    model = Posts
    template_name = 'post_delete.html'
    success_url = '/'  # Redirect to home after deletion or
    # success_url = reverse_lazy('home')  # Use reverse_lazy for class-based views

