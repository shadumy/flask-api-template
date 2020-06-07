FROM python:3.6.10-alpine
COPY requirements .

RUN apk update && apk add curl
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python get-pip.py

RUN pip install -r requirements
RUN rm requirements
RUN rm -f get-pip.py
RUN apk del curl
RUN mkdir app

EXPOSE 80