FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python-pip python3-pip python3-dev

COPY ./ ./tracker
WORKDIR ./tracker
RUN pip3 install -r requirements.txt
RUN export FLASK_DEBUG=1
CMD uwsgi --socket 0.0.0.0:8080 --protocol=http --wsgi-file wsgi.py

