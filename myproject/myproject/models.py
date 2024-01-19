from django.contrib.auth.models import AbstractUser
from djongo import models
from .models import Blog

class User(AbstractUser):
    # additional fields in here
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_deleted = models.DateTimeField(null=True)
    

def create_blog(request):
    blog = Blog(title='My first blog', content='This is my first blog post.')
    blog.save()

def get_all_blogs(request):
        blogs = Blog.objects.all()  # retrieves all blogs

def get_single_blog(request, blog_id):
        blog = Blog.objects.get(id=blog_id)  # retrieves a single blog by its id

def update_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.title = 'Updated title'
    blog.content = 'Updated content'
    blog.save()

def delete_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()    
