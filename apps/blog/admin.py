from django.contrib import admin
from apps.blog.models import Post, Category

class PostAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    display_fields = ["title", "created"]

class CategoryAdmin(admin.ModelAdmin):
    display_fields = ["category"]

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
