FROM python:3.6.10-alpine
COPY requirements .

RUN apt-get -y update && apt-get install curl -y
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python get-pip.py

RUN pip install -r requirements
RUN rm requirements
RUN rm -f get-pip.py
RUN apt-get -y remove --purge curl
RUN mkdir app

EXPOSE 80