package main

import (
	"context"
	"log"
	"time"

	"google.golang.org/grpc"

	pb "go-py/hello-van/pb"
)

func main() {
	addr := "127.0.0.1:52002"
	// conn, err := grpc.Dial(addr, grpc.WithInsecure(), grpc.WithBlock())
	conn, err := grpc.Dial(addr, grpc.WithInsecure())
	if err != nil {
		log.Fatal(err)
	}
	defer conn.Close()

	client := pb.NewVanClient(conn)
	// req := &pb.Request{}
	log.Printf("calling %s", addr)
	response, err := client.HelloVan(
		context.Background(),
		&pb.Request{Name: "van", Age: 1},
	)

	log.Println(response.Result)

	req := &pb.Request{Name: "sakdfjhceq", Age: 1000}

	res, err := client.HelloStreamVan(
		context.Background(),
		req,
	)
	// for i in range res {
	// res.RecvMsg()
	for {
		word, err := res.Recv()
		if err != nil {
			log.Fatal(err)
			break
		}

		log.Println(word)
		time.Sleep(10 * time.Millisecond)
	}
	log.Println(res.Recv())
	// }

}
