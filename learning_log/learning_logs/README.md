Whenever I change something in the models.py I have to run
1. python manage.py makemigrations "appname" (learning_logs)
2. python manage.py migrate
3. register models with the admin site (admin.site.register(ClassName))
To query the db use the django shell:
python manage.py shell

In settings.py register your app under INSTALLED_APPS

Making web pages with Django
1. defining urls in the app (learning_logs)
2. writing views
3. writing templates

Run the server:
python manage.py runserver

Create super user:
python manage.py createsuperuser

Creating a virtual environment with venv:
python -m venv "venv_name"
source "venv_name"/bin/activate
deactivate
