from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'circulante.views.home', name='home'),
<<<<<<< HEAD
    url(r'^', include('circulante.catalogo.urls')),
=======
    url(r'^cat/', include('circulante.catalogo.urls')),
>>>>>>> 76b4c88f288fe2dc8991da18df1ad30561d6c5aa

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
