# *-* coding=utf-8 *-*

from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.template import loader
from django.template import RequestContext
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _
from models import Form
import datetime

class ContactForm(forms.ModelForm):
    firstname = forms.CharField(max_length=140, widget=forms.TextInput(attrs={'class':'formTextFormulario'}), label=_(u'Nombre'))
    lastname = forms.CharField(max_length=140, widget=forms.TextInput(attrs={'class':'formTextFormulario'}), label=_(u'Apellido'))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'formTextFormulario'}), label=_(u'E-Mail'))
    pc = forms.CharField(widget=forms.RadioSelect)
    tipo = forms.CharField(widget=forms.RadioSelect)
    caso = forms.CharField(widget=forms.RadioSelect)


    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        super(ContactForm, self).save(*args, **kwargs)

    class Meta:
        model = Form

