FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /twittertools
ENV DJANGO_ALLOWED_HOSTS='127.0.0.1'
COPY requirements.txt /twittertools/
RUN pip install -r requirements.txt
COPY ./twittertools/. /twittertools/
RUN pip install -r tweetfetch/neo4jintf/docker/features/requirements.txt
