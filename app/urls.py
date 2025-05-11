from django.urls import path
from .views import PostListView, PostDetailView  # Assure-toi que le nom de la classe est PostDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', PostListView.as_view(), name='home'),  # Liste des articles
    path('<slug:slug>/', PostDetailView.as_view(), name='detail'),  # Détail d’un article via slug
]

# Pour servir les fichiers médias en mode développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
