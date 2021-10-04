from django.db import models
from django.conf import settings

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100, default='누구신지?')
    pub_date = models.DateTimeField('date published')
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    hashtags = models.ManyToManyField('Hashtag', blank=True)
    likes_user = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='likes_user')

    def count_likes_user(self): # total likes_user
        return self.likes_user.count()

    def __str__(self):
        return self.title
        
#댓글
class Comment(models.Model):
    def __str__(self):
        return self.text

    post_id = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=50)

#해시태그
class Hashtag(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
