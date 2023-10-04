# base image  
FROM python:3.10.6
# setup environment variable
ENV DockerHOME=/home/app/webapp

# set work directory
RUN mkdir -p $DockerHOME

# where your code lives  
WORKDIR $DockerHOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip

# copy whole project to your docker home directory.
COPY . $DockerHOME

# run this command to install all dependencies
RUN pip install -r requirements.txt

RUN python manage.py migrate --noinput

ENV DJANGO_DB_NAME=default
ENV DJANGO_SU_NAME=pahpa
ENV DJANGO_SU_EMAIL=pahpa@pahpa.dev
ENV DJANGO_SU_PASSWORD=pahpa1234
ENV DJANGO_SETTINGS_MODULE=django_study.settings

RUN python -c "import django; django.setup(); \
   from django.contrib.auth.management.commands.createsuperuser import get_user_model; \
   get_user_model()._default_manager.db_manager('$DJANGO_DB_NAME').create_superuser( \
   username='$DJANGO_SU_NAME', \
   email='$DJANGO_SU_EMAIL', \
   password='$DJANGO_SU_PASSWORD')"

# port where the Django app runs
EXPOSE 8000

# start server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
