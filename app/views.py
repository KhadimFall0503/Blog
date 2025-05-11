from django.shortcuts import render
from django.views import generic
from .models import Post

# Vue pour la liste des articles publiés
class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created')
    template_name = 'index.html'
    context_object_name = 'post'  # facultatif, pour un nom de contexte plus clair

# Vue pour le détail d’un article
class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post_details.html'
    context_object_name = 'post'  # facultatif, plus lisible dans le template
