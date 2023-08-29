FROM python:3.7-slim

# Set up a safe working directory to put the code in
WORKDIR /root/work

# Do not copy anything other than reqs because this is a dev container and so we are using Docker volumes instead.
COPY requirements-dev.txt .
COPY requirements.txt .
# NOTE: this is a dev container so we should use a docker volume mount instead of copying in files

RUN apt-get update && \
    apt-get install -y gcc git libc-dev libpq-dev
# Install python deps, both dev and regular
RUN pip install -r requirements-dev.txt

ENV DOCKERIZE_VERSION v0.7.0

RUN apt-get install -y wget openssl \
    && wget -O - https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz | tar xzf - -C /usr/local/bin

COPY ./dev/db/custom-entrypoint.sh /usr/local/bin/custom-entrypoint.sh
RUN chmod u+x /usr/local/bin/custom-entrypoint.sh
ENTRYPOINT ["custom-entrypoint.sh"]

EXPOSE 8000

CMD ["gunicorn", "--worker-tmp-dir", "/dev/shm", "--reload", "-w", "2", "--worker-class=gthread", "--log-file=-", "-b", ":8000", "django_to_do_api.wsgi"]