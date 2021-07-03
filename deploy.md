python manage.py check --deploy

secret key

debug

database pip install dj-database-url 
pip install psycopg2-binary

 import dj_database_url 
 dj_database_url.config(conn_max_age=500)

serving static files 
static root 
pip install whitenoise 
'whitenoise.middleware.WhiteNoiseMiddleware',

HTTP Server pip install gunicorn

export requirements

For Heroku procfile 
web: gunicorn projectName.wsgi --log-file -

Create Heroku app and Add Allowed hosts