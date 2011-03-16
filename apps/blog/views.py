from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.context_processors import csrf
from django.shortcuts import  render_to_response, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.views.generic import  list_detail
from django.conf import settings
import time

from apps.blog.models import Post

BLOG_PAGINATION = getattr(settings, 'BLOG_PAGINATION', 5)


def main(request):
    posts = Post.objects.all().order_by("-created")
    return list_detail.object_list(request, queryset=posts,
                    paginate_by=BLOG_PAGINATION, template_name="list.html")


@csrf_protect
def post(request, slug):
    post = Post.objects.get(slug=slug)
    d = dict(post=post, user=request.user)
    return render_to_response("post.html", d)



def category(request, object_pk=None):
    qs = Post.objects.all().filter(category=object_pk)
    return list_detail.object_list(request, template_name='category_list.html', queryset=qs)
