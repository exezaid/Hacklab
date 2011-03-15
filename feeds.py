from django.contrib.syndication.views import Feed
from django.shortcuts import get_object_or_404
from django.contrib.syndication.views import FeedDoesNotExist

from apps.blog.models import Post

class LatestEntries(Feed):
    title = "Blog del grupo de usuarios de software libre de tucuman"
    link = "/"
    description = "Ultimos Posts"

    def items(self):
        return Post.objects.order_by('-created')[:5]


    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.category

