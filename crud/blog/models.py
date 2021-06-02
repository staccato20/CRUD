from django.db import models
from django.conf import settings

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100, default='누구신지?')
    pub_date = models.DateTimeField('date published')
    content = models.TextField()

    def __str__(self):
        return self.title

#댓글
class Comment(models.Model):
    def __str__(self):
        return self.text

    post_id = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=50)