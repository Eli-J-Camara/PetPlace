from django.db import models
from django.utils import timezone
from user_profile.models import CustomUser
from tagulous.models import TagField

class Post(models.Model):
    display_name = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post_pic= models.ImageField(upload_to='post_img/', null=True)
    caption = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    tags = TagField()

    def __str__(self):
        return f'{self.display_name} | {self.caption}'

class Comment(models.Model):
    comment = models.TextField(max_length=300)
    created_at = models.created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(CustomUser, related_name='commenter', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment