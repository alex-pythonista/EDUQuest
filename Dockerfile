# Using the official Python 3.8 runtime as a parent image
FROM python:3.8

# Install software needed in the container
# RUN apt-get install \
#         vim \
#         bash

# Python output is sent straight to the terminal without buffering it first
ENV PYTHONUNBUFFERED 1

# Set the working directory to /app
# This will be root directory for our project in the container
WORKDIR /app

# Install python dependencies before copying source code.
# This allows us to leverage the caching in docker.
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --cache-dir .pip-cache -r requirements.txt && \
    rm -rf .pip-cache

# Copy the current directory contents into the container at /app
ADD . /app

# Set entrypoint to the container
CMD ["python --version"]