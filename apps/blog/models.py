from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField('E-Mail', blank=True)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    class Admin:
        pass


class Category(models.Model):
    name_category = models.CharField(max_length=15)

    def __unicode__(self):
      return self.name_category


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





