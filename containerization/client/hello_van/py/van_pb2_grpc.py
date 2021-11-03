# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import van_pb2 as van__pb2


class VanStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.HelloVan = channel.unary_unary(
                '/Van/HelloVan',
                request_serializer=van__pb2.request.SerializeToString,
                response_deserializer=van__pb2.response.FromString,
                )


class VanServicer(object):
    """Missing associated documentation comment in .proto file."""

    def HelloVan(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_VanServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'HelloVan': grpc.unary_unary_rpc_method_handler(
                    servicer.HelloVan,
                    request_deserializer=van__pb2.request.FromString,
                    response_serializer=van__pb2.response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Van', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Van(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def HelloVan(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Van/HelloVan',
            van__pb2.request.SerializeToString,
            van__pb2.response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
