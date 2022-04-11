from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from ckeditor.fields import RichTextField

User = get_user_model()

# Create your models here.
class ABS(models.Model):
    create_data = models.DateTimeField(auto_now_add=True)
    update_data = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    subject = models.CharField(max_length=30, choices=(('1', 'Sayt islemir'), ('2', 'Sikayet')))
    message = models.TextField()

    def __str__(self) -> str:
        return self.name
    
class Categories(ABS):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to = 'image/categories')
    
    def __str__(self) -> str:
        return self.title

class Tag(ABS):
    title = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.title

class Stories(ABS):
    slug = models.SlugField(null = True, blank=True, editable=False)
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, related_name='stories', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True) # thought
    image = models.ImageField(upload_to = 'image/story_images')
    cover_image = models.ImageField(upload_to = 'image/story_cover_image')
    desc = RichTextField()
    # desc = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title


class Images(ABS):
    image = models.ImageField(upload_to='image/desc')
    stories = models.ForeignKey(Stories, related_name='images', on_delete=models.CASCADE)
