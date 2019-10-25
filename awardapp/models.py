from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.dispatch import receiver
from django.db.models.signals import post_save

class Project(models.Model):
    title = models.CharField(max_length =60)
    description=models.CharField(max_length =360)
    profile = models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'projectes/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projectes')
    link=models.CharField(max_length =60)


    def save_image(self):
        
        self.save()

    
    def delete_image(self):
       
        self.delete()

    
    def update_caption(self):
       
        pass

    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        images = cls.objects.filter(pub_date__date = today)
        return images

    @classmethod
    def days_news(cls,date):
        news = cls.objects.filter(pub_date__date = date)
        return news
  

    @classmethod
    def get_comments(self):
        images=cls.objects.all().prefetch_related("comment_set")
        return self.comments.all()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True)
    Name = models.TextField(default="Any")
    contact= models.TextField(default="Any")
    profile_picture = models.ImageField(
        upload_to='users/', default='users/user.png')
    bio = models.TextField(default="Welcome !")

    

    @classmethod
    def search(cls,username):
        profiles=cls.objects.filter(user__username__icontains=username)
        return profiles

class Comment(models.Model):
    comment= models.TextField()
    photo = models.ForeignKey(Project, on_delete=models.CASCADE,null=True)
    posted_by=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.posted_by
    

    def get_comment(self,id):
        comments=Comment.objects.filter(image_id=id)
        return comments