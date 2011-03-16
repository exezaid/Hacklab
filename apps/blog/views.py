from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.context_processors import csrf
from django.shortcuts import  render_to_response
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

    return render_to_response("list.html", dict(posts=posts, user=request.user,
                                                post_list=posts.object_list))


def post(request, slug):
    post = Post.objects.get(slug=slug)
    d = dict(post=post, user=request.user)
    d.update(csrf(request))
    return render_to_response("post.html", d)
