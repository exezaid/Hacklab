# *-* encoding:utf-8 *-*

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.csrf import csrf_protect

from models import Form
from forms import *


@csrf_protect
def form(request, success_url='sent', template_name='contact_form.html'):

    notify = True
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(request.POST, request.FILES)
        if contact_form.is_valid():
            new_form = {
                    'firstname': contact_form.cleaned_data['firstname'],
                    'lastname': contact_form.cleaned_data['lastname'],
                    'email': contact_form.cleaned_data['email'],
                    'pc': contact_form.cleaned_data['pc'],
                    'tipo': contact_form.cleaned_data['tipo'],
                    'caso': contact_form.cleaned_data['caso'],
                    }
            new_form = Form(**new_form)
            new_form.save(notify=notify)
            return HttpResponseRedirect(success_url)

    return render_to_response(template_name, RequestContext(request, {'form': contact_form}))

