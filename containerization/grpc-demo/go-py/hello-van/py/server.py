import grpc
import logging
# import van_pb2_grpc as pb2_grpc
from van_pb2 import response
from van_pb2_grpc import VanServicer, add_VanServicer_to_server
from concurrent.futures import ThreadPoolExecutor

from random import randint
import time

class Van(VanServicer):

    def HelloVan(self, request, context):
        name = request.name
        age = request.age
        logging.info(f"{name}, {age}")
        return response(result=f"name is {name}, age {age}")

    def HelloStreamVan(self, request, context):
        """返回stream数据流
        """
        name = request.name
        age = request.age
        logging.info(name)
        # for index, i in enumerate(name):
        #     logging.info(f"{index}, {i}")
        #     yield response(result=f"{index}, {i}")
        
        i = 9999
        value1 = 100
        value2 = 50
        t = 0
        while i:
            value1 += randint(0, 10)
            value2 += randint(0, 10)

            data = '{},{},{}\n'.format(t, value1, value2)
            i -= 1
            t += 1
            time.sleep(1)
            yield response(result=data)

    # def get_hash(self, data):
    #     """
    #     """






if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO, 
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    port = 52002
    grpc_server = grpc.server(ThreadPoolExecutor())
    
    add_VanServicer_to_server(Van(), grpc_server)

    grpc_server.add_insecure_port(f"127.0.0.1:{port}")
    grpc_server.start()
    logging.info("server ready on port {0}".format(port))

    grpc_server.wait_for_termination()
    