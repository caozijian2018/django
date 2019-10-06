#基本的django环境  来源  https://cloud.docker.com/repository/docker/caocaocao/django_1_11_22/builds/edit
#
FROM caocaocao/django_1_11_22
WORKDIR /app
# ensure local python is preferred over distribution python
ENV PATH /usr/local/bin:$PATH
COPY ./requirements.txt ./django/

# http://bugs.python.org/issue19846
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks Python 3*, and that's not OK.
ENV LANG C.UTF-8
# https://github.com/docker-library/python/issues/147
ENV PYTHONIOENCODING UTF-8


RUN pip3 install --no-cache-dir  -r /app/django/requirements.txt  \
  && mkdir -p /app/django/assets/img \
  && rm -rf /cache/* \
  && rm -rf /root/.cache/* \
  && python3 /app/django/src/manage.py collectstatic --noinput --settings=settings.local
  # && rm /site_api/requirements.txt
#CMD "python manage.py runserver 0.0.0.0:8000"
# CMD "python3 -V"