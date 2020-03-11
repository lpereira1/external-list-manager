# Pull from python docker image, set a working directory add our environment
# variables then pip install requirements and finally copy our application over



FROM python:3.6.10-buster
LABEL maintainer="Lazaro Pereira <spmlaz@gmail.com>"

#set the working directory
WORKDIR /usr/src/external-list-manager

#set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#install requirements.txt dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/external-list-manager/requirements.txt
RUN pip install -r requirements.txt

#Copy the project into the image

COPY . /usr/src/external-list-manager
