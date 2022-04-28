"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import bosdyn.api.header_pb2
import bosdyn.api.lease_pb2
import builtins
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Params(google.protobuf.message.Message):
    """Parameters to AutoReturn actions."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MOBILITY_PARAMS_FIELD_NUMBER: builtins.int
    MAX_DISPLACEMENT_FIELD_NUMBER: builtins.int
    MAX_DURATION_FIELD_NUMBER: builtins.int
    @property
    def mobility_params(self) -> google.protobuf.any_pb2.Any:
        """Robot-specific mobility parameters to use.
        For example, see bosdyn.api.spot.MobilityParams.
        """
        pass
    max_displacement: builtins.float
    """Allow AutoReturn to move the robot this far in the XY plane from the location where
    AutoReturn started. Travel along the Z axis (which is gravity-aligned) does not count.
    Must be > 0.
    meters
    """

    @property
    def max_duration(self) -> google.protobuf.duration_pb2.Duration:
        """Optionally specify the maximum amount of time AutoReturn can take.
        If this duration is exceeded, AutoReturn will stop trying to move the robot.
        Omit to try indefinitely. Robot may become stuck and never take other comms loss actions!
        """
        pass
    def __init__(self,
        *,
        mobility_params: typing.Optional[google.protobuf.any_pb2.Any] = ...,
        max_displacement: builtins.float = ...,
        max_duration: typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["max_duration",b"max_duration","mobility_params",b"mobility_params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["max_displacement",b"max_displacement","max_duration",b"max_duration","mobility_params",b"mobility_params"]) -> None: ...
global___Params = Params

class ConfigureRequest(google.protobuf.message.Message):
    """Configure the AutoReturn system."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    LEASES_FIELD_NUMBER: builtins.int
    PARAMS_FIELD_NUMBER: builtins.int
    CLEAR_BUFFER_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.RequestHeader:
        """Common request header."""
        pass
    @property
    def leases(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[bosdyn.api.lease_pb2.Lease]:
        """Leases that AutoReturn may use to accomplish its goals when AutoReturn automatically
        triggers. If left empty, AutoReturn will not automatically trigger.
        """
        pass
    @property
    def params(self) -> global___Params:
        """Parameters to use when AutoReturn automatically triggers."""
        pass
    clear_buffer: builtins.bool
    """Forget any buffered locations the robot may be remembering. Defaults to false.
    Set to true if the robot has just crossed an area it should not traverse in AutoReturn.
    """

    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.RequestHeader] = ...,
        leases: typing.Optional[typing.Iterable[bosdyn.api.lease_pb2.Lease]] = ...,
        params: typing.Optional[global___Params] = ...,
        clear_buffer: builtins.bool = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header","params",b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["clear_buffer",b"clear_buffer","header",b"header","leases",b"leases","params",b"params"]) -> None: ...
global___ConfigureRequest = ConfigureRequest

class ConfigureResponse(google.protobuf.message.Message):
    """Response to a configuration request."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Status:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[ConfigureResponse._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNKNOWN: ConfigureResponse._Status.ValueType  # 0
        STATUS_OK: ConfigureResponse._Status.ValueType  # 1
        STATUS_INVALID_PARAMS: ConfigureResponse._Status.ValueType  # 2
    class Status(_Status, metaclass=_StatusEnumTypeWrapper):
        pass

    STATUS_UNKNOWN: ConfigureResponse.Status.ValueType  # 0
    STATUS_OK: ConfigureResponse.Status.ValueType  # 1
    STATUS_INVALID_PARAMS: ConfigureResponse.Status.ValueType  # 2

    HEADER_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    INVALID_PARAMS_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.ResponseHeader:
        """Common response header."""
        pass
    status: global___ConfigureResponse.Status.ValueType
    """Return status for the request."""

    @property
    def invalid_params(self) -> global___Params:
        """If status is STATUS_INVALID_PARAMS, this contains the settings that were invalid."""
        pass
    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.ResponseHeader] = ...,
        status: global___ConfigureResponse.Status.ValueType = ...,
        invalid_params: typing.Optional[global___Params] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header","invalid_params",b"invalid_params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header","invalid_params",b"invalid_params","status",b"status"]) -> None: ...
global___ConfigureResponse = ConfigureResponse

class GetConfigurationRequest(google.protobuf.message.Message):
    """Ask for the current configuration."""
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
global___GetConfigurationRequest = GetConfigurationRequest

class GetConfigurationResponse(google.protobuf.message.Message):
    """Response to a "get configuration" request."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    ENABLED_FIELD_NUMBER: builtins.int
    REQUEST_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.ResponseHeader:
        """Common response header."""
        pass
    enabled: builtins.bool
    """A simple yes/no, will AutoReturn automatically trigger."""

    @property
    def request(self) -> global___ConfigureRequest:
        """The most recent successful ConfigureRequest.
        Will be empty if service has not successfully been configured.
        """
        pass
    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.ResponseHeader] = ...,
        enabled: builtins.bool = ...,
        request: typing.Optional[global___ConfigureRequest] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header","request",b"request"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["enabled",b"enabled","header",b"header","request",b"request"]) -> None: ...
global___GetConfigurationResponse = GetConfigurationResponse

class StartRequest(google.protobuf.message.Message):
    """Start AutoReturn behavior now."""
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
global___StartRequest = StartRequest

class StartResponse(google.protobuf.message.Message):
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
global___StartResponse = StartResponse
