import grpc
import hello_pb2_grpc as pb2_grpc
import hello_pb2 as pb2
from concurrent import futures

class HelloServicer(pb2_grpc.Hello):

    """proto中创建的服务名称叫 Hello，继承这个服务。类名称可以自定义
    """

    def __init__(self, *args, **kwargs):
        pass

    def hello_grpc(self, request, context):
        """
        """

        # 来自proto文件的message
        name = request.name
        age = request.age

        res = f'hello first grpc service, {name} {age}'
        result = {'message': res, 'received': True}

        return pb2.hello_request(**result)

def serve():
    port = 520001
    # 传入一个线程池
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_HelloServicer_to_server(HelloServicer(), server)
    server.add_insecure_port("[::]:{0}".format(port))
    print("serving on port {0}".format(port))
    # 随着主线程结束，刚启动的服务就会立刻停止，调用 wait_for
    server.start()
    
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
    
    