#-*- coding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

from_addr = settings.DEFAULT_FROM_EMAIL
recipient_list = [mail_tuple[1] for mail_tuple in settings.MANAGERS]

PC_CHOICES = (
    ('S', 'Si'),
    ('N', 'No'),
)

TIPO_CHOICES = (
    ('NOT', 'Es una Portatil'),
    ('DES', 'Es una PC de escritorio'),
    ('MAC', 'Es una Mac u otra'),
    ('PEN', 'Llevare un Pentdrive (debe ser de 512 Mb o más)'),
)

CASO_CHOICES = (
    ('PARTI', 'Llevare mi Computadora con las particiones listas(*)'),
    ('DESFR', 'Llevare mi Computadora defragmentada'),
    ('BORRA', 'Se puede borrar el disco entero'),
)


class Form(models.Model):
    firstname = models.CharField(max_length=140, verbose_name=(u'Nombre'))
    lastname = models.CharField(max_length=140, verbose_name=(u'Apellido'))
    email = models.EmailField(verbose_name=(u'E-Mail'))
    pc = models.CharField(max_length=1, choices=PC_CHOICES,  verbose_name=(u'PC?'))
    tipo = models.CharField(blank=True, max_length=3, choices=TIPO_CHOICES,  verbose_name=(u'Tipo'))
    caso = models.CharField(blank=True, max_length=5, choices=CASO_CHOICES, verbose_name=(u'¿Cual es tu caso?'))


    def __unicode__(self):
        return u'%s %s' % (self.firstname, self.lastname)

    def save(self, *args, **kwargs):
        if "notify" in kwargs and kwargs["notify"] == True:
            message = "Nombre y Apellido: %s, %s\nEmail: %s " % (self.firstname, self.lastname, self.email)
            send_mail( "Nuevo registro FLISOL", message, from_addr, recipient_list)

        if "notify" in kwargs: del kwargs["notify"]

        super(Form, self).save(*args, ** kwargs)


    class Meta:
        verbose_name = u'Flisol'
        verbose_name_plural = u'Flisol'

