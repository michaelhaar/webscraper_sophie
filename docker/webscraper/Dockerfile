# Start a new Python 3.8 parent image (see https://hub.docker.com/r/library/python)
FROM python:3.8

# Avoid .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# Ensure that Python output is sent straight to terminal and that we can see the output of our application
ENV PYTHONUNBUFFERED 1

#install system dependencies
RUN apt-get update \
	&& apt-get install -y python3 python3-dev python3-pip libxml2-dev \
	libxslt1-dev zlib1g-dev libffi-dev libssl-dev

# install the required python packages
COPY requirements/requirements.txt /tmp/requirements.txt

RUN set -ex \
	&& pip install --upgrade pip \
	&& pip install pip-tools \
	&& pip install -r /tmp/requirements.txt \
	&& rm -rf /root/.cache/

# copy in the rest of your app’s source code from your host to your image filesystem.
COPY . /src/

WORKDIR /src/