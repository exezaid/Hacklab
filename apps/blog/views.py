from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.context_processors import csrf
from django.shortcuts import  render_to_response, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.views.generic import  list_detail
from django.template import RequestContext
from django.conf import settings
from django.http import Http404
import time

from apps.blog.models import Post

BLOG_PAGINATION = getattr(settings, 'BLOG_PAGINATION', 5)


def main(request):
      posts = Post.objects.all().order_by("-created")
    return list_detail.object_list(request, queryset=posts,
                    paginate_by=BLOG_PAGINATION, template_name='list.html')


@csrf_protect
def post(request, slug):
    post = get_object_or_404(Post.objects, slug=slug)
    return render_to_response("post.html", RequestContext(request, {'post': post}))



def category(request, object_pk=None):
    qs = Post.objects.all().filter(category=object_pk).order_by("-created")
    return list_detail.object_list(request, queryset=qs,
                        paginate_by=BLOG_PAGINATION,
                        template_name='category_list.html',)
