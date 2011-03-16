import urllib, hashlib
from django import template
from apps.blog.models import Category

register = template.Library()


class CommonNode(template.Node):
    def __init__(self, obj=None, var=None):
        setattr(self, 'var', var)

@register.inclusion_tag('gravatar.html')
def show_gravatar(email, size=48):
    default = "/media/img/gravatar.jpg"

    url = "http://www.gravatar.com/avatar.php?"
    url += urllib.urlencode({'gravatar_id':hashlib.md5(email.lower()).hexdigest(), 'default':default, 'size':str(size)})

    return {'gravatar': {'url': url, 'size': size}}



class CategoryNode(CommonNode):
    def render(self, context):
        ret = Category.objects.all()
        if self.var:
            context[self.var] = ret
            return ''
        return ret

def get_category(parse, token):
    var = None
    try:
        tag, _as, var = token.split_contents()
    except ValueError:
        try:
            tag = token.split_contents()
        except ValueError:
            raise template.TemplateSyntaxError, "el formato del tag %r debe ser \
                    '{% get_category as category %}'" % token.split_contents()[0]

    return CategoryNode(var=var)

register.tag(get_category)
