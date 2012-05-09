import os, sys

sys.path.append('/home/turma2/circulante/circulante')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "circulante.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
