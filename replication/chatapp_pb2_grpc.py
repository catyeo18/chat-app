# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import chatapp_pb2 as chatapp__pb2


class ChatStub(object):
    """The chat service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Send = channel.unary_unary(
                '/Chat/Send',
                request_serializer=chatapp__pb2.Data.SerializeToString,
                response_deserializer=chatapp__pb2.UserResponse.FromString,
                )
        self.Heartbeat = channel.unary_unary(
                '/Chat/Heartbeat',
                request_serializer=chatapp__pb2.HeartbeatRequest.SerializeToString,
                response_deserializer=chatapp__pb2.HeartbeatResponse.FromString,
                )
        self.ServerResponse = channel.unary_unary(
                '/Chat/ServerResponse',
                request_serializer=chatapp__pb2.Request.SerializeToString,
                response_deserializer=chatapp__pb2.Response.FromString,
                )
        self.ClientMessages = channel.unary_stream(
                '/Chat/ClientMessages',
                request_serializer=chatapp__pb2.Username.SerializeToString,
                response_deserializer=chatapp__pb2.Response.FromString,
                )
        self.Leader = channel.unary_unary(
                '/Chat/Leader',
                request_serializer=chatapp__pb2.LeaderRequest.SerializeToString,
                response_deserializer=chatapp__pb2.LeaderResponse.FromString,
                )


class ChatServicer(object):
    """The chat service definition.
    """

    def Send(self, request, context):
        """Updates the databases of the other servers
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Heartbeat(self, request, context):
        """Sends heartbeat check to other servers
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ServerResponse(self, request, context):
        """Client chat to server
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClientMessages(self, request, context):
        """Sends stream of client<>client messages to each client
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Leader(self, request, context):
        """Client asking whether server is leader
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ChatServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Send': grpc.unary_unary_rpc_method_handler(
                    servicer.Send,
                    request_deserializer=chatapp__pb2.Data.FromString,
                    response_serializer=chatapp__pb2.UserResponse.SerializeToString,
            ),
            'Heartbeat': grpc.unary_unary_rpc_method_handler(
                    servicer.Heartbeat,
                    request_deserializer=chatapp__pb2.HeartbeatRequest.FromString,
                    response_serializer=chatapp__pb2.HeartbeatResponse.SerializeToString,
            ),
            'ServerResponse': grpc.unary_unary_rpc_method_handler(
                    servicer.ServerResponse,
                    request_deserializer=chatapp__pb2.Request.FromString,
                    response_serializer=chatapp__pb2.Response.SerializeToString,
            ),
            'ClientMessages': grpc.unary_stream_rpc_method_handler(
                    servicer.ClientMessages,
                    request_deserializer=chatapp__pb2.Username.FromString,
                    response_serializer=chatapp__pb2.Response.SerializeToString,
            ),
            'Leader': grpc.unary_unary_rpc_method_handler(
                    servicer.Leader,
                    request_deserializer=chatapp__pb2.LeaderRequest.FromString,
                    response_serializer=chatapp__pb2.LeaderResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Chat', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Chat(object):
    """The chat service definition.
    """

    @staticmethod
    def Send(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Chat/Send',
            chatapp__pb2.Data.SerializeToString,
            chatapp__pb2.UserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Heartbeat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Chat/Heartbeat',
            chatapp__pb2.HeartbeatRequest.SerializeToString,
            chatapp__pb2.HeartbeatResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ServerResponse(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Chat/ServerResponse',
            chatapp__pb2.Request.SerializeToString,
            chatapp__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClientMessages(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Chat/ClientMessages',
            chatapp__pb2.Username.SerializeToString,
            chatapp__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Leader(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Chat/Leader',
            chatapp__pb2.LeaderRequest.SerializeToString,
            chatapp__pb2.LeaderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)