FROM centos:centos7.9.2009

# FROM alpine/

WORKDIR /app

ADD ni-software-2020-20.1.0.49152-0+f0.el7.noarch.rpm .

RUN yum update && \
    yum install -y ni-software-2020-20.1.0.49152-0+f0.el7.noarch.rpm && \
    yum install -y ni-visa && \
    yum install -y python3 && \
    pip3 install pyvisa -i https://mirrors.aliyun.com/pypi/simple

ADD test.py .

# RUN ["python3", "test.py"]




