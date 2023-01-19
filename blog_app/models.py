from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    date_joined = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self. last_name}"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    title = models.CharField(max_length=150)
    rating = models.FloatField(max_length=20, null=True, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")

    def __str__(self):
        return f"{self.title}"

class Likes(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post_id = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now=True)


