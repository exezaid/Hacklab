from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name_category = models.CharField(max_length=15)
    slug = models.SlugField(max_length=30, unique=True)

    def __unicode__(self):
      return self.name_category

    @models.permalink
    def get_absolute_url(self):
        return ('apps.blog.views.category', (), {'object_pk':self.pk})



class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=30, unique=True)
    body = models.TextField()
    category = models.ForeignKey(Category)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


    @models.permalink
    def get_absolute_url(self):
        return ('apps.blog.views.post', (), {'slug':self.slug})





