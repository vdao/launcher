FROM alpine:3.6

EXPOSE 3031
VOLUME /usr/src/app/public
VOLUME /usr/src/app/conf
WORKDIR /usr/src/app

RUN apk add --no-cache \
        uwsgi \
        uwsgi-python3 \
        python3

COPY . .
RUN rm -rf public/*
RUN rm -rf conf/*

RUN pip3 install --no-cache-dir -r requirements.txt

CMD [ "uwsgi", "conf/uwsgi.ini"]