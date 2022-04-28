"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import bosdyn.api.header_pb2
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GetLEDBrightnessRequest(google.protobuf.message.Message):
    """Request the current state of LEDs on the SpotCam."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.RequestHeader:
        """Common request header."""
        pass
    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.RequestHeader] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header"]) -> None: ...
global___GetLEDBrightnessRequest = GetLEDBrightnessRequest

class GetLEDBrightnessResponse(google.protobuf.message.Message):
    """Describes the current brightnesses of all LEDs."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    BRIGHTNESSES_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.ResponseHeader:
        """Common response header."""
        pass
    @property
    def brightnesses(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        """Brightness [0, 1] of the LED located at indices [0, 3]."""
        pass
    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.ResponseHeader] = ...,
        brightnesses: typing.Optional[typing.Iterable[builtins.float]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["brightnesses",b"brightnesses","header",b"header"]) -> None: ...
global___GetLEDBrightnessResponse = GetLEDBrightnessResponse

class SetLEDBrightnessRequest(google.protobuf.message.Message):
    """Set individual LED brightnesses."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class BrightnessesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int
        value: builtins.float
        def __init__(self,
            *,
            key: builtins.int = ...,
            value: builtins.float = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    HEADER_FIELD_NUMBER: builtins.int
    BRIGHTNESSES_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.RequestHeader:
        """Common request header."""
        pass
    @property
    def brightnesses(self) -> google.protobuf.internal.containers.ScalarMap[builtins.int, builtins.float]:
        """Brightness [0, 1] to assign to the LED located at indices [0, 3]."""
        pass
    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.RequestHeader] = ...,
        brightnesses: typing.Optional[typing.Mapping[builtins.int, builtins.float]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["brightnesses",b"brightnesses","header",b"header"]) -> None: ...
global___SetLEDBrightnessRequest = SetLEDBrightnessRequest

class SetLEDBrightnessResponse(google.protobuf.message.Message):
    """Response with any errors setting LED brightnesses."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.ResponseHeader:
        """Common response header."""
        pass
    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.ResponseHeader] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header"]) -> None: ...
global___SetLEDBrightnessResponse = SetLEDBrightnessResponse