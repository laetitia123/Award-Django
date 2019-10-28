from django.test import TestCase

from django.test import TestCase


from django.test import TestCase
from .models import Project,User,Profile,Comment
import datetime as dt

class ImageTestClass(TestCase):
   
    def setUp(self):

        self.user1 = User(username='laetitia')
        self.user1.save()
        
        
        self.image=Project(name='amezing',description='django app',user=self.user1,likes="1",post="project")
        self.image.save_image()

 
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Project))

    def test_save_method(self):
        
        self.image.save_image()
        images=Image.objects.all()
        self.assertTrue(len(images)>0) 
   

    def test_delete_method(self):
        
       
        Project.objects.all().delete()

   
   
class CommentTestClass(TestCase):

    def setUp(self):
     
        self.user1 = User(username='LAETITIA')
        self.user1.save()
        self.nature=Profile(2,user=self.user1,bio='Nature')
        self.nature.save_prof()

        self.james=Project(2,name='PACY',description='thisis my website',user=self.user1,post="project")
        self.james.save_image()
      
        self.com=Comment(comment='amezing',comment_image=self.james,posted_by=self.nature,)
        self.com.save_com()

 
    def test_instance(self):

        self.assertTrue(isinstance(self.com,Comment))    
        
    def test_save_method(self):
        
        self.com.save_com()
        comm=Comment.objects.all()
        self.assertTrue(len(comm)>0) 
    def test_delete_method(self):
       
  
        Comment.objects.all().delete()
   
class ProfileTestClass(TestCase):
    
    def setUp(self):
        self.user1 = User(username='laetitia)
        self.user1.save()
        self.nature=Profile(2,user=self.user1,bio='hello wrold')
        self.nature.save_prof()

 
    def test_instance(self):
        self.assertTrue(isinstance(self.nature,Profile))

         
    def test_save_method(self):
      
      
        self.nature.save_prof()
        comm=Profile.objects.all()
        self.assertTrue(len(comm)>0) 

    def test_delete_method(self):
      
  
        Profile.objects.all().delete()