FROM python:3.5-jessie
# Base packages
RUN apt-get update && \
    apt-get install -y git software-properties-common zip unzip rsync wget

RUN apt-get -y update && \
    apt-get -y install google-chrome-stable

RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install selenium
RUN pip3 install requests
RUN pip3 install urllib3
RUN pip3 install Appium-Python-Client


WORKDIR /var/www/uat
ADD . .