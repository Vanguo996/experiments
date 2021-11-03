import grpc
import van_pb2 as pb2
import van_pb2_grpc as pb2_grpc


class Van(pb2_grpc.VanServicer):

    def HelloVan(self, request, context):
        name = request.name
        age = request.age
        return pb2.response(result=f"name is {name}, {age} years old")

if __name__ == '__main__':
    from concurrent.futures import ThreadPoolExecutor
    grpc_server = grpc.server(ThreadPoolExecutor(max_workers=4))
    pb2_grpc.add_VanServicer_to_server(Van(), grpc_server)
    grpc_server.add_insecure_port("127.0.0.1:22222")
    grpc_server.start()
    grpc_server.wait_for_termination()