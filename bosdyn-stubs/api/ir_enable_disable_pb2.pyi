"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import bosdyn.api.header_pb2
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class IREnableDisableRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Request:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _RequestEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[IREnableDisableRequest._Request.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        REQUEST_UNKNOWN: IREnableDisableRequest._Request.ValueType  # 0
        """Unspecified value -- should not be used."""

        REQUEST_OFF: IREnableDisableRequest._Request.ValueType  # 1
        """Disable emissions."""

        REQUEST_ON: IREnableDisableRequest._Request.ValueType  # 2
        """Enable emissions."""

    class Request(_Request, metaclass=_RequestEnumTypeWrapper):
        pass

    REQUEST_UNKNOWN: IREnableDisableRequest.Request.ValueType  # 0
    """Unspecified value -- should not be used."""

    REQUEST_OFF: IREnableDisableRequest.Request.ValueType  # 1
    """Disable emissions."""

    REQUEST_ON: IREnableDisableRequest.Request.ValueType  # 2
    """Enable emissions."""


    HEADER_FIELD_NUMBER: builtins.int
    REQUEST_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.RequestHeader:
        """/< Common request header."""
        pass
    request: global___IREnableDisableRequest.Request.ValueType
    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.RequestHeader] = ...,
        request: global___IREnableDisableRequest.Request.ValueType = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header","request",b"request"]) -> None: ...
global___IREnableDisableRequest = IREnableDisableRequest

class IREnableDisableResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.ResponseHeader:
        """/< Common response header."""
        pass
    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.ResponseHeader] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header"]) -> None: ...
global___IREnableDisableResponse = IREnableDisableResponse
