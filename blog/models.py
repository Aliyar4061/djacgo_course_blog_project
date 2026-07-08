from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (
        ('drf', 'Draft'),
        ('pub', 'Published'),
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICES, max_length=3)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
