
FROM python:3.7

RUN apt-get update

RUN apt-get -y --no-install-recommends install nginx supervisor

RUN pip3 install uwsgi

COPY ./requirements.txt /urlhome/requirements.txt

RUN pip3 install -r /urlhome/requirements.txt

RUN useradd --no-create-home nginx

COPY nginx/nginx.conf /etc/nginx/
COPY nginx/flask_nginx.conf /etc/nginx/conf.d/
COPY nginx/uwsgi.ini /etc/uwsgi/
COPY nginx/supervisord.conf /etc/supervisor/



RUN rm /etc/nginx/sites-enabled/default
RUN rm -r /root/.cache
RUN mkdir -p /urlhome/data
COPY data/bad_urls.txt /data/bad_urls.txt
COPY urlapp /urlhome/urlapp

WORKDIR /urlhome

CMD ["/usr/bin/supervisord"]
