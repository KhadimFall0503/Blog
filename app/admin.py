from django.contrib import admin
from .models import Post

# Configuration personnalisée de l'affichage du modèle dans l'admin
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created')
    list_filter = ('status',)
    search_fields = ('title', 'content')

# Enregistrement du modèle avec sa configuration admin
admin.site.register(Post, PostAdmin)
