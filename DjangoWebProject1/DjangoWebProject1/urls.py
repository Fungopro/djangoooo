"""
Definition of urls for DjangoWebProject1.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views
from django.conf.urls.static import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^quests/$', app.views.about, name='about'),
    url(r'^SelectAnswer/$', app.views.answer, name='answer'),
    url(r'^admin/', admin.site.urls),
    url(r'^$', app.views.home, name='home'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
                {
                    'title': 'Log in',
                    'year': datetime.now().year,
                }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
if settings.DEBUG:

    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

# Эта строка опциональна и будет добавлять url'ы только при DEBUG = True

urlpatterns += staticfiles_urlpatterns()
