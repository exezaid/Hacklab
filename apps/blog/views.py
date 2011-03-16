from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.context_processors import csrf
from django.shortcuts import  render_to_response, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.views.generic import  list_detail
import time

from apps.blog.models import Post

def main(request):
    """Main listing."""
    posts = Post.objects.all().order_by("-created")
    paginator = Paginator(posts, 5)
    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)

    return render_to_response("list.html", dict(posts=posts,
                                                post_list=posts.object_list))

@csrf_protect
def post(request, slug):
    post = Post.objects.get(slug=slug)
    d = dict(post=post, user=request.user)
    return render_to_response("post.html", d)



def category(request, object_pk=None):
    qs = Post.objects.all().filter(category=object_pk)
    return list_detail.object_list(request, template_name='category_list.html', queryset=qs)
