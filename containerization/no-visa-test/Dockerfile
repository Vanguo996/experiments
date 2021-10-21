FROM centos:centos7.9.2009

WORKDIR /app

COPY /server .

RUN yum install -y python3 python3-devel && \
    pip3 install --upgrade setuptools -i https://mirrors.aliyun.com/pypi/simple && \
    pip3 install --upgrade pip -i https://mirrors.aliyun.com/pypi/simple && \
    pip3 install pyvisa -i https://mirrors.aliyun.com/pypi/simple && \
    pip3 install grpcio grpcio-tools protobuf -i https://mirrors.aliyun.com/pypi/simple

# 用于保持容器稳定在运行状态
ENTRYPOINT ["/bin/bash", "-ce", "tail -f /dev/null"]

# CMD [ "python3", "websocket-server.py"]

