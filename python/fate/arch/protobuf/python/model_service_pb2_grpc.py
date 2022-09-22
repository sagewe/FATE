# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import model_service_pb2 as model__service__pb2


class ModelServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.publishLoad = channel.unary_unary(
            "/com.webank.ai.fate.api.mlmodel.manager.ModelService/publishLoad",
            request_serializer=model__service__pb2.PublishRequest.SerializeToString,
            response_deserializer=model__service__pb2.PublishResponse.FromString,
        )
        self.publishBind = channel.unary_unary(
            "/com.webank.ai.fate.api.mlmodel.manager.ModelService/publishBind",
            request_serializer=model__service__pb2.PublishRequest.SerializeToString,
            response_deserializer=model__service__pb2.PublishResponse.FromString,
        )
        self.publishOnline = channel.unary_unary(
            "/com.webank.ai.fate.api.mlmodel.manager.ModelService/publishOnline",
            request_serializer=model__service__pb2.PublishRequest.SerializeToString,
            response_deserializer=model__service__pb2.PublishResponse.FromString,
        )
        self.queryModel = channel.unary_unary(
            "/com.webank.ai.fate.api.mlmodel.manager.ModelService/queryModel",
            request_serializer=model__service__pb2.QueryModelRequest.SerializeToString,
            response_deserializer=model__service__pb2.QueryModelResponse.FromString,
        )
        self.unload = channel.unary_unary(
            "/com.webank.ai.fate.api.mlmodel.manager.ModelService/unload",
            request_serializer=model__service__pb2.UnloadRequest.SerializeToString,
            response_deserializer=model__service__pb2.UnloadResponse.FromString,
        )
        self.unbind = channel.unary_unary(
            "/com.webank.ai.fate.api.mlmodel.manager.ModelService/unbind",
            request_serializer=model__service__pb2.UnbindRequest.SerializeToString,
            response_deserializer=model__service__pb2.UnbindResponse.FromString,
        )


class ModelServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def publishLoad(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def publishBind(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def publishOnline(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def queryModel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def unload(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def unbind(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ModelServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "publishLoad": grpc.unary_unary_rpc_method_handler(
            servicer.publishLoad,
            request_deserializer=model__service__pb2.PublishRequest.FromString,
            response_serializer=model__service__pb2.PublishResponse.SerializeToString,
        ),
        "publishBind": grpc.unary_unary_rpc_method_handler(
            servicer.publishBind,
            request_deserializer=model__service__pb2.PublishRequest.FromString,
            response_serializer=model__service__pb2.PublishResponse.SerializeToString,
        ),
        "publishOnline": grpc.unary_unary_rpc_method_handler(
            servicer.publishOnline,
            request_deserializer=model__service__pb2.PublishRequest.FromString,
            response_serializer=model__service__pb2.PublishResponse.SerializeToString,
        ),
        "queryModel": grpc.unary_unary_rpc_method_handler(
            servicer.queryModel,
            request_deserializer=model__service__pb2.QueryModelRequest.FromString,
            response_serializer=model__service__pb2.QueryModelResponse.SerializeToString,
        ),
        "unload": grpc.unary_unary_rpc_method_handler(
            servicer.unload,
            request_deserializer=model__service__pb2.UnloadRequest.FromString,
            response_serializer=model__service__pb2.UnloadResponse.SerializeToString,
        ),
        "unbind": grpc.unary_unary_rpc_method_handler(
            servicer.unbind,
            request_deserializer=model__service__pb2.UnbindRequest.FromString,
            response_serializer=model__service__pb2.UnbindResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "com.webank.ai.fate.api.mlmodel.manager.ModelService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class ModelService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def publishLoad(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/com.webank.ai.fate.api.mlmodel.manager.ModelService/publishLoad",
            model__service__pb2.PublishRequest.SerializeToString,
            model__service__pb2.PublishResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def publishBind(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/com.webank.ai.fate.api.mlmodel.manager.ModelService/publishBind",
            model__service__pb2.PublishRequest.SerializeToString,
            model__service__pb2.PublishResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def publishOnline(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/com.webank.ai.fate.api.mlmodel.manager.ModelService/publishOnline",
            model__service__pb2.PublishRequest.SerializeToString,
            model__service__pb2.PublishResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def queryModel(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/com.webank.ai.fate.api.mlmodel.manager.ModelService/queryModel",
            model__service__pb2.QueryModelRequest.SerializeToString,
            model__service__pb2.QueryModelResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def unload(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/com.webank.ai.fate.api.mlmodel.manager.ModelService/unload",
            model__service__pb2.UnloadRequest.SerializeToString,
            model__service__pb2.UnloadResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def unbind(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/com.webank.ai.fate.api.mlmodel.manager.ModelService/unbind",
            model__service__pb2.UnbindRequest.SerializeToString,
            model__service__pb2.UnbindResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
