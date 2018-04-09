# vim: syntax=dockerfile
FROM alpine
MAINTAINER Tim Heap <tim@timheap.me>

RUN mkdir /app
WORKDIR /app/

RUN apk add --no-cache \
        tini \
        uwsgi uwsgi-python3 \
        python3 python3-dev py3-pillow postgresql-dev gcc musl-dev

RUN pip3 install --no-cache-dir --upgrade pip setuptools wheel

COPY requirements.in requirements.txt /app/
RUN pip3 install --no-cache-dir pyinotify -r requirements.txt

COPY ./authorsanonymous /app/authorsanonymous
COPY ./deploy /app/deploy
COPY ./manage.py /app/manage.py
RUN ln -fs /app/deploy/settings.py /app/settings.py

ENV PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=UTF-8 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app/ \
    DJANGO_SETTINGS_MODULE=settings \
    LC_ALL=C.UTF-8 \
    LANG=C.UTF-8

EXPOSE 80
ENTRYPOINT ["/sbin/tini", "--"]
CMD ["/app/deploy/run.sh"]
