# Real-time-chat-application

## Introduction

[![Kafka](https://img.shields.io/badge/streaming_platform-kafka-black.svg?style=flat-square)](https://kafka.apache.org)
[![Docker Images](https://img.shields.io/badge/docker_images-wurstmeister-orange.svg?style=flat-square)](https://github.com/wurstmeister/kafka-docker)
[![Python](https://img.shields.io/badge/python-3.5+-blue.svg?style=flat-square)](https://www.python.org)

This is a simple chat application with Apache kafka, flask, socketio and NodeJS.

## How to run
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

* Prerequisites

    Make sure that you have Python 3.x, pip and git installed.

First, You have to clone this repository (or you can download zip file)

```bash
 git clone https://github.com/mansourehmotahari/Real-time-chat-application.git
```

You will need [Docker](https://docs.docker.com/install/) and [Docker Compose](https://docs.docker.com/compose/) to run it.Then you need kafka images.

You can install the images as usual with pip: 

```bash
 docker pull wurstmeister/kafka
```
And we also need:

```bash
 docker pull wurstmeister/zookeeper
```

Now you have to install all requirements:

```bash
 cd Real-time-chat-application
 pip install -r requirements.txt
```
Now run the following command to bring your containers up.

```bash
 docker-compose up 
```
After that, you should be able to start the app, in a new cmd window:

```bash
 cd Real-time-chat-application
 python app.py 
```
Finally, open two html file and , enjoy :) 

Hope it is helpful!




