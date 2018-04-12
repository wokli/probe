FROM python:3.6.5-alpine


RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN apk add --no-cache --virtual .build-dependencies alpine-sdk && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del .build-dependencies

COPY . /usr/src/app
CMD ["python"]