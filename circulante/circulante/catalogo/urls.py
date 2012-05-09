from django.conf.urls import patterns, include, url

from .views import busca, catalogar, editar

urlpatterns = patterns('',
<<<<<<< HEAD
    url(r'catalogar', catalogar, name='catalogar'),
    url(r'editar/(\d+)', editar, name='editar'),
    url(r'', busca, name='busca'),    
=======
    url(r'busca', busca, name='busca'),
    url(r'catalogar', catalogar, name='catalogar'),
    url(r'editar/(\d+)', editar, name='editar'),
>>>>>>> 76b4c88f288fe2dc8991da18df1ad30561d6c5aa
)
