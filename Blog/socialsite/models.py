from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils.translation import gettext_lazy as _
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True,blank=True)
    unique_user_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    
    def __str__(self):
        return self.user.username
    
    
class Post(models.Model):
    drafted = 1
    published = 2
    status_choices = [
        (drafted, _('drafted')),
        (published, _('published')),
    ]
    
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/',blank=True)
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=status_choices,default=drafted)
    likes = models.ManyToManyField(User,related_name = 'like_post',blank=True)
    
    
    def __str__(self):
        return self.title, self.author.username
    
    
    def like_count(self):
        return self.likes.count()
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    
    
    
    def __str__(self):
        return f'Comment by {self.author.first_name} on {self.post.title}'