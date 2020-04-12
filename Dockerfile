
FROM python:3.7

RUN apt-get update

RUN apt-get -y --no-install-recommends install nginx 

RUN pip3 install uwsgi

COPY ./requirements.txt /urlhome/requirements.txt

RUN pip3 install -r /urlhome/requirements.txt

COPY nginx/nginx.conf /etc/nginx/
COPY nginx/flask_nginx.conf /etc/nginx/conf.d/
COPY nginx/uwsgi.ini /etc/uwsgi/

RUN rm /etc/nginx/sites-enabled/default
RUN rm -r /root/.cache

WORKDIR /urlhome

