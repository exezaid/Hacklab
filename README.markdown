======================================
Como usar Django con Apache y mod_wsgi
======================================

Implementación de Django con Apache_ y `mod_wsgi`_ es la forma recomendada 
para poner Django en producción.

.. _Apache: http://httpd.apache.org/
.. _mod_wsgi: http://code.google.com/p/modwsgi/

mod_wsgi es un módulo Apache que puede ser utilizado para alojar cualquier
aplicación Python que soporta la `interfaz de Python WSGI`_, incluyendo Django.
Django funciona con cualquier versión de Apache que soporta mod_wsgi.

.. _interfaz de Python WSGI: http://www.python.org/dev/peps/pep-0333/

La `documentación oficial mod_wsgi`_ es fantástica, es una fuente con todos
los detalles acerca de cómo utilizar mod_wsgi. Usted probablemente querrá
comenzar con la `instalación y la documentación de configuración`_.

.. _documentación oficial mod_wsgi: http://code.google.com/p/modwsgi/
.. _instalación y la documentación de configuración: http://code.google.com/p/modwsgi/wiki/InstallationInstructions

Configuracion basica
====================

Una vez que tenga mod_wsgi instalado y activado, editar el archivo ``httpd.conf``
y añade::

    WSGIScriptAlias / /ruta/a/app/apache/django.wsgi

El primer bit de arriba en la URL es donde desea que se sirva su aplicación en (``/``
indica la URL raíz), y el segundo es la ubicación de un "archivo WSGI" -- ver
más abajo -- en el sistema, por lo general dentro de su proyecto. Esto le dice a Apache
para servir a todas las solicitudes por debajo de la URL dada con el WSGI definido por ese archivo.

A continuación tendremos que crear esta aplicación WSGI, por lo que se crear el archivo
mencionados en la segunda parte de ``WSGIScriptAlias`` y añade::

    import os
    import sys

    os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

    import django.core.handlers.wsgi
    application = django.core.handlers.wsgi.WSGIHandler()

Si el proyecto no está en su ``PYTHONPATH`` por defecto, puede agregar::

    path = '/path/to/mysite'
    if path not in sys.path:
        sys.path.append(path)

just below the ``import sys`` line to place your project on the path. Remember to
replace 'mysite.settings' with your correct settings file, and '/path/to/mysite'
with your own project's location.
justo debajo de ``import sys`` para colocar el proyecto en el path. Recuerde
se sustituirá 'mysite.settings' con el archivo de configuración correcta, y
'/ruta/a/app' con la ubicación de su propio proyecto.

.. _serving-media-files:

Sirviendo archivos estaticos
============================

Django no sirve los archivos de medios en sí, deja ese trabajo a cualquier
servidor Web que elija.

Sin embargo, si usted no tiene más remedio que servir a los archivos multimedia 
en el mismo Apache ``VirtualHost`` con Django, puede configurar Apache para servir 
a algunas URL como medios estáticos, y otros que utilizan la interfaz mod_wsgi con Django.

En este ejemplo se configura Django en la raíz del sitio, pero explícitamente sirve ``robots.txt``,
``favicon.ico``, cualquier archivo CSS, y algo en el espacio de la URL 
``/media/`` como un archivo statico. Todas las otras direcciones URL se sirve con mod_wsgi::

    Alias /robots.txt /usr/local/wsgi/static/robots.txt
    Alias /favicon.ico /usr/local/wsgi/static/favicon.ico

    AliasMatch ^/([^/]*\.css) /usr/local/wsgi/static/styles/$1

    Alias /media/ /usr/local/wsgi/static/media/

    <Directory /usr/local/wsgi/static>
    Order deny,allow
    Allow from all
    </Directory>

    WSGIScriptAlias / /usr/local/wsgi/scripts/django.wsgi

    <Directory /usr/local/wsgi/scripts>
    Order allow,deny
    Allow from all
    </Directory>


Más detalles sobre la configuración de un sitio con mod_wsgi, para servir archivos estáticos se pueden encontrar
en la documentación mod_wsgi en `hosting static files`_.

.. _hosting static files: http://code.google.com/p/modwsgi/wiki/ConfigurationGuidelines#Hosting_Of_Static_Files

.. _serving-the-admin-files:

Sirviendo a los archivos de admin
=================================

Tenga en cuenta que el servidor de desarrollo de Django sirve automágicamente 
los ficheros de administración, pero este no es el caso cuando se utiliza cualquier
otro servidor. Ud. es responsable de la creación de la configuracion de Apache,
o cualquier servidor de medios que está utilizando, para servir a los archivos 
de administración.

Los archivos de administrador estan en (:file:`django/contrib/admin/media`) de
la aplicacion de Django.

Aquí hay dos opciones recomendadas:

    1. Crear un vínculo simbólico a la carpeta media desde su
       documento raíz. De esta manera, todos los archivos relacionados con
       Django -- código **y** plantillas - permanecer en un solo lugar, y aún
       así ser capaz de  hacer ``svn update`` para actualizar el código y obtener
       las últimas plantillas de administración, si cambian.

    2. O bien, copia los archivos multimedia de administración para que esten dentro 
       de su documento raíz de Apache .

Base de datos
=============

La configuración de la Base de datos se realiza en el archivo ``settings.py`` 
se puede optar por diferentes tipos de motores

    * Postgresql
    * mysql
    * sqlite3
    * oracle

la sección de configuración se ve de la siguiente forma

    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
    }

luego de configurar la base de datos se debe realizar la sincronización con el siguiente comando.

    python manage.py syncdb

Esto crea las tablas correspondientes y le preguntara si quiere crear un súper usuario.

Detalles
========

Para obtener más información, consulte la `documentación mod_wsgi integración con Django`_,
lo que explica lo anterior con más detalle, y camina a través de todos los diversos
opciones que tienes para implementar mod_wsgi.

.. _documentación mod_wsgi integración con Django: http://code.google.com/p/modwsgi/wiki/IntegrationWithDjango
