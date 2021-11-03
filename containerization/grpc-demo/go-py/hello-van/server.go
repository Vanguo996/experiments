package main

import (
	"context"
	"fmt"
	pb "go-py/hello-van/pb"
)

const (
	port = ":52001"
)

type Van struct {
}

func (v *Van) HelloVan(ctx context.Context, request *pb.Request) (*pb.Response, error) {
	name := request.Name
	age := request.Age
	return &pb.Response{Result: fmt.Sprintf("name %s age %d", name, age)}, nil
}

// func startServe() {
// 	server := grpc.NewServer()
// 	pb.RegisterVanServer(server, &Van{}) // 传入一个pb.VanServer的接口 其中Van是HelloVan方法的接收者

// 	listen, err := net.Listen("tcp", port)
// 	fmt.Printf("listen in %s ...", port)
// 	if err != nil {
// 		fmt.Println(err)
// 		return
// 	}
// 	if err = server.Serve(listen); err != nil {
// 		fmt.Println(err)
// 		return
// 	}
// }
