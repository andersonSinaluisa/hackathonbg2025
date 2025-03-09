export PYTHONPATH=/code:$PYTHONPATH
# Esperar a que Celery esté listo antes de iniciar Gunicorn
cd /code
gunicorn evaluacion.wsgi:application --bind :8001 --workers 4 