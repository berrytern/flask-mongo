FROM ubuntu:18.04
MAINTAINER berrytern@gmail.com
RUN apt-get update
RUN apt-get install -y python3 python3-pip git
RUN mkdir flask && cd flask && git init && git remote add origin https://github.com/berrytern/flask-mongo.git
RUN cd flask && git fetch origin && git checkout -B master --track origin/master
CMD cd flask && git fetch origin && git checkout -B master --track origin/master && ls && pip3 install -r requirements.txt && python3 src/server.py

EXPOSE 3000
EXPOSE 3001