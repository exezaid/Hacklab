from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.core.mail import send_mail
import urllib, hashlib


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
    author = models.ForeignKey(Author)
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=30, unique=True)
    body = models.TextField()
    category = models.ForeignKey(Category)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


    @models.permalink
    def get_absolute_url(self):
        return ('main', ())


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=60)
    email = models.EmailField('e-mail', blank=True)
    body = models.TextField()
    post = models.ForeignKey(Post)

    def __unicode__(self):
        return unicode("%s: %s" % (self.post, self.body[:60]))

    def save(self, *args, **kwargs):
        """Email when a comment is added."""
        if "notify" in kwargs and kwargs["notify"] == True:
            message = "Comment was was added to '%s' by '%s': \n\n%s" % (self.post, self.author,
                                                                         self.body)
            from_addr = "no-reply@lugtucuman.org.ar"
            recipient_list = ["admin@lugtucuman.org.ar"]
            send_mail("New comment added", message, from_addr, recipient_list)

        if "notify" in kwargs: del kwargs["notify"]
        super(Comment, self).save(*args, **kwargs)


### Admin


class PostAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    display_fields = ["title", "created"]


class CommentAdmin(admin.ModelAdmin):
    display_fields = ["post", "author", "created"]


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')

class CategoryAdmin(admin.ModelAdmin):
    display_fields = ["category"]

