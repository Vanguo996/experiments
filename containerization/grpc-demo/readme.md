
demo hello 来自github项目：

https://github.com/xinliangnote/Go/blob/master/02-Go%20gRPC/01-Go%20gRPC%20Hello%20World.md

go实现流式传输的服务端
go实现流式传输的客户端



// 服务端流模式，在返回值前面加上一个 stream
  rpc GetStream(StreamRequestData) returns (stream StreamResponseData){}
  // 客户端流模式，在参数前面加上一个 stream
  rpc PutStream(stream StreamRequestData) returns (StreamResponseData){}
  // 双向流模式
  rpc AllStream(stream StreamRequestData) returns (stream StreamResponseData){}


