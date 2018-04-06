FROM python:3.6-alpine3.7
MAINTAINER ilanyu <lanyu19950316@gmail.com>

RUN apk add --update --no-cache chromium chromium-chromedriver zlib-dev xvfb wait4ports xorg-server dbus ttf-freefont mesa-dri-swrast grep udev

RUN pip install -U selenium xlwt

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

VOLUME ["/usr/src/app/"]

COPY docker-entrypoint.sh /entrypoint.sh

RUN chmod a+x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

CMD ["python", "/usr/src/app/main.py"]
