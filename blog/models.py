from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        # related_name='posts'
    )
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('post_detail', kwargs={'pk': self.pk})
    
