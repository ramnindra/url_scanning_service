
FROM python:3.7

RUN apt-get update

RUN apt-get -y --no-install-recommends install nginx 

RUN pip3 install uwsgi

COPY ./requirements.txt /urlhome/requirements.txt

RUN pip3 install -r /urlhome/requirements.txt

WORKDIR /urlhome

