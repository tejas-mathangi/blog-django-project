from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView , DetailView , CreateView
from . import forms
from .models import Posts

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
    


