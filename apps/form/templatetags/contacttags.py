from django import template
from apps.form.forms import ContactForm
register = template.Library()

@register.inclusion_tag('form/contact_form.html')
def get_contact_form():
    return {'form': ContactForm()}

