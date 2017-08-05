from django.db import models
from django.utils import timezone

emailLength = 30

class User(models.Model):
    USER_ID = models.CharField(max_length = 30, primary_key = True)
    USER_PW = models.CharField(max_length = 30)

class UserFriend(models.Model):            
    USER_ID = models.CharField(max_length = 30)
    FRIEND_ID = models.CharField(max_length = 30)    
    USER_FRIEND = models.TextField(primary_key = True, default = '')

class UserMusic(models.Model):
    USER_ID = models.CharField(max_length = 30)
    DATE = models.DateTimeField(default = timezone.now)
    YTB_LINK = models.TextField()

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title 