package main

import (
	"context"
	"fmt"
	pb "grpc-client/hello_grpc/hello_pb"
	"net"

	"google.golang.org/grpc"
)

type Server struct {
}

func (s *Server) HelloGrpc(ctx context.Context, hello_request *pb.HelloRequest) (*pb.HelloResponse, error) {

	name := hello_request.Name
	age := hello_request.Age

	return &pb.HelloResponse{Message: fmt.Sprintf("name: %s, age: %d", name, age)}, nil
}

func main() {
	server := grpc.NewServer()
	// pb.RegisterHelloServer(server, &Server{})

	listener, err := net.Listen("tcp", ":52002")
	if err != nil {
		fmt.Println(err)
		return
	}
	// 开启服务，每来一个连接，内部会开一个协程去处理
	if err = server.Serve(listener); err != nil {
		fmt.Println(err)
		return
	}
}
