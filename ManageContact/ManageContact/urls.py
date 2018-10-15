"""
Definition of urls for ManageContact.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views
import MainModule.forms
import MainModule.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^$', MainModule.views.home, name='home'),
    url(r'^ViewFullContact/(?P<pk>\d+)/$', MainModule.views.ViewFullContact, name='ViewFullContact'),
    url(r'^New$', MainModule.views.CreateContact, name='NewContact'),
    url(r'^DeleteContact/(?P<pk>\d+)/$', MainModule.views.DeleteContact, name='DeleteContact'),
  
    url(r'^UpdatePhone/(?P<pk>\d+)/$', MainModule.views.UpdatePhone, name='UpdatePhone'),
    url(r'^DeletePhone/(?P<pk>\d+)/(?P<ContactId>\d+)$', MainModule.views.DeletePhone, name='DeletePhone'),
    url(r'^NewPhone/(?P<ContactId>\d+)$', MainModule.views.NewPhone, name='NewPhone'),

    url(r'^UpdateAddress/(?P<pk>\d+)/$', MainModule.views.UpdateAddress, name='UpdateAddress'),
    url(r'^DeleteAddress/(?P<pk>\d+)/(?P<ContactId>\d+)$', MainModule.views.DeleteAddress, name='DeleteAddress'),
    url(r'^NewAddress/(?P<ContactId>\d+)$', MainModule.views.NewAddress, name='NewAddress'),

    url(r'^UpdateDate/(?P<pk>\d+)/$', MainModule.views.UpdateDate, name='UpdateDate'),
    url(r'^Delete/(?P<pk>\d+)/(?P<ContactId>\d+)$', MainModule.views.DeleteDate, name='DeleteDate'),
    url(r'^NewDate/(?P<ContactId>\d+)$', MainModule.views.NewDate, name='NewDate'),

    url(r'^contact$', MainModule.views.contact, name='contact'),
    url(r'^about$', MainModule.views.about, name='about'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'MainModule/login.html',
            'authentication_form': MainModule.forms.BootstrapAuthenticationForm,
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
