# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import rawdata_pb2 as rawdata__pb2


class RawDataStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Transform = channel.unary_unary(
                '/pb.RawData/Transform',
                request_serializer=rawdata__pb2.TransformRequest.SerializeToString,
                response_deserializer=rawdata__pb2.TransformResponse.FromString,
                )


class RawDataServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Transform(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RawDataServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Transform': grpc.unary_unary_rpc_method_handler(
                    servicer.Transform,
                    request_deserializer=rawdata__pb2.TransformRequest.FromString,
                    response_serializer=rawdata__pb2.TransformResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pb.RawData', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RawData(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Transform(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.RawData/Transform',
            rawdata__pb2.TransformRequest.SerializeToString,
            rawdata__pb2.TransformResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
