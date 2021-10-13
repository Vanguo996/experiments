

### 建立测量仪器的grpc流式传输服务


$ pip3 install grpcio grpcio-tools protobuf -i https://mirrors.aliyun.com/pypi/simple

python3 -m grpc_tools.protoc --python_out=. --grpc_python_out=. -I. matsuri.proto

--python_out 和 --grpc_python_out 表示输出路径，. 表示输出到当前路径；-I 表示从哪里寻找 protobuf 文件


├── grpc-server.py
├── matsuri_pb2_grpc.py   这里给grpc使用的
├── matsuri_pb2.py  这里是给protobuf使用的
└── matsuri.proto



grpc流模式

- 服务端数据流：

这种模式是客户端发起一次请求服务端返回一段连续的数据流。
典型的例子是客户端向服务端发送一个股票代码，服务端就把该股票的实时数据源源不断地返回给客户端。

- 客户端数据流：

与服务端数据流模式相反，这次是客户端不断地向服务端发送数据，
而在发送结束后，由服务端返回一个响应，典型的例子是物联网终端向服务器发送数据。比如大棚里面的温度传感器，显然要把里面的温度实时上报给服务器。

- 双向数据流：

顾名思义，这是客户端和服务端都可以向对方发送数据流，这个时候双方的数据可以同时互相发送，也就是实现实时交互，典型的例子是聊天机器人。 


