FROM python
MAINTAINER Harpalsinh Gohil

ENV PYTHONUNBUFFERED 1

COPY ./requirement.txt /requirement.txt
RUN pip install -r /requirement.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

##RUN useradd -D user
#USER user
