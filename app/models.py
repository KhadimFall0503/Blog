import os
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_delete

STATUS = ((0, "Draft"), (1, "Publish"))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    publish = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now=True)
    content = models.TextField()  # <-- Correction ici
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

@receiver(pre_delete, sender=Post)
def delete_post_image(sender, instance, **kwargs):
    if instance.image and os.path.isfile(instance.image.path):
        os.remove(instance.image.path)
