package main

import (
	"fmt"

	"google.golang.org/grpc"

	pb "grpc-client/hello_van/go_client"
)

func main() {
	// 连接 22222 端口，这是 Python 服务
	conn, err := grpc.Dial("127.0.0.1:22222", grpc.WithInsecure())
	if err != nil {
		fmt.Println(err)
		return
	}
	defer func() { _ = conn.Close() }()
	client := pb.NewVanClient(conn)
	// response, _ := client.HelloMea(
	// 	context.Background(),
	// 	&pb.Request{Name: "神乐 mea", Age: 38},
	// )
	fmt.Println(response.Result) // name is 神乐 mea, 38 years old
}
