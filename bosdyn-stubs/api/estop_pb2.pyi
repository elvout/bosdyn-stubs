"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import bosdyn.api.header_pb2
import builtins
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _EstopStopLevel:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _EstopStopLevelEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_EstopStopLevel.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    ESTOP_LEVEL_UNKNOWN: _EstopStopLevel.ValueType  # 0
    """Invalid stop level."""

    ESTOP_LEVEL_CUT: _EstopStopLevel.ValueType  # 1
    """Immediately cut power to the actuators."""

    ESTOP_LEVEL_SETTLE_THEN_CUT: _EstopStopLevel.ValueType  # 2
    """Prepare for loss of actuator power, then cut power."""

    ESTOP_LEVEL_NONE: _EstopStopLevel.ValueType  # 4
    """No-stop level. The endpoint believes the robot is safe to operate."""

class EstopStopLevel(_EstopStopLevel, metaclass=_EstopStopLevelEnumTypeWrapper):
    """The state of the E-Stop system."""
    pass

ESTOP_LEVEL_UNKNOWN: EstopStopLevel.ValueType  # 0
"""Invalid stop level."""

ESTOP_LEVEL_CUT: EstopStopLevel.ValueType  # 1
"""Immediately cut power to the actuators."""

ESTOP_LEVEL_SETTLE_THEN_CUT: EstopStopLevel.ValueType  # 2
"""Prepare for loss of actuator power, then cut power."""

ESTOP_LEVEL_NONE: EstopStopLevel.ValueType  # 4
"""No-stop level. The endpoint believes the robot is safe to operate."""

global___EstopStopLevel = EstopStopLevel


class EstopEndpoint(google.protobuf.message.Message):
    """An  to the robot software-E-Stop system."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ROLE_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    UNIQUE_ID_FIELD_NUMBER: builtins.int
    TIMEOUT_FIELD_NUMBER: builtins.int
    CUT_POWER_TIMEOUT_FIELD_NUMBER: builtins.int
    role: typing.Text
    """Role of this endpoint. Should be a user-friendly string, e.g. "OCU"."""

    name: typing.Text
    """Name of this endpoint. Specifies a thing to fill the given role, e.g. "patrol-ocu01" """

    unique_id: typing.Text
    """Unique ID assigned by the server."""

    @property
    def timeout(self) -> google.protobuf.duration_pb2.Duration:
        """Maximum delay between challenge and response for this endpoint prior to soft power off
        handling. After timeout seconds has passed, the robot will try to get to a safe state prior
        to disabling motor power. The robot response is equivalent to an ESTOP_LEVEL_SETTLE_THEN_CUT
        which may involve the robot sitting down in order to prepare for disabling motor power.
        """
        pass
    @property
    def cut_power_timeout(self) -> google.protobuf.duration_pb2.Duration:
        """Optional maximum delay between challenge and response for this endpoint prior to disabling
        motor power. After cut_power_timeout seconds has passed, motor power will be disconnected
        immediately regardless of current robot state. If this value is not set robot will default
        to timeout plus a nominal expected duration to reach a safe state. In practice this
        is typically 3-4 seconds. The response is equivalent to an ESTOP_LEVEL_CUT.
        """
        pass
    def __init__(self,
        *,
        role: typing.Text = ...,
        name: typing.Text = ...,
        unique_id: typing.Text = ...,
        timeout: typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        cut_power_timeout: typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["cut_power_timeout",b"cut_power_timeout","timeout",b"timeout"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cut_power_timeout",b"cut_power_timeout","name",b"name","role",b"role","timeout",b"timeout","unique_id",b"unique_id"]) -> None: ...
global___EstopEndpoint = EstopEndpoint

class EstopConfig(google.protobuf.message.Message):
    """Configuration of a root / server."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ENDPOINTS_FIELD_NUMBER: builtins.int
    UNIQUE_ID_FIELD_NUMBER: builtins.int
    @property
    def endpoints(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___EstopEndpoint]:
        """EstopEndpoints that are part of this configuration.
        Unique IDs do not have to be filled out, but can be.
        """
        pass
    unique_id: typing.Text
    """Unique ID for this configuration."""

    def __init__(self,
        *,
        endpoints: typing.Optional[typing.Iterable[global___EstopEndpoint]] = ...,
        unique_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["endpoints",b"endpoints","unique_id",b"unique_id"]) -> None: ...
global___EstopConfig = EstopConfig

class EstopEndpointWithStatus(google.protobuf.message.Message):
    """EstopEndpoint with some extra status data."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ENDPOINT_FIELD_NUMBER: builtins.int
    STOP_LEVEL_FIELD_NUMBER: builtins.int
    TIME_SINCE_VALID_RESPONSE_FIELD_NUMBER: builtins.int
    @property
    def endpoint(self) -> global___EstopEndpoint:
        """The endpoint."""
        pass
    stop_level: global___EstopStopLevel.ValueType
    """Stop level most recently requested by the endpoint."""

    @property
    def time_since_valid_response(self) -> google.protobuf.duration_pb2.Duration:
        """Time since a valid response was provided by the endpoint."""
        pass
    def __init__(self,
        *,
        endpoint: typing.Optional[global___EstopEndpoint] = ...,
        stop_level: global___EstopStopLevel.ValueType = ...,
        time_since_valid_response: typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["endpoint",b"endpoint","time_since_valid_response",b"time_since_valid_response"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["endpoint",b"endpoint","stop_level",b"stop_level","time_since_valid_response",b"time_since_valid_response"]) -> None: ...
global___EstopEndpointWithStatus = EstopEndpointWithStatus

class EstopSystemStatus(google.protobuf.message.Message):
    """Status of Estop system."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ENDPOINTS_FIELD_NUMBER: builtins.int
    STOP_LEVEL_FIELD_NUMBER: builtins.int
    STOP_LEVEL_DETAILS_FIELD_NUMBER: builtins.int
    @property
    def endpoints(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___EstopEndpointWithStatus]:
        """Status for all available endpoints."""
        pass
    stop_level: global___EstopStopLevel.ValueType
    """Current stop level for the system.
    Will be the most-restrictive stop level specified by an endpoint, or a stop level
    asserted by the system as a whole (e.g. if an endpoint timed out).
    """

    stop_level_details: typing.Text
    """Human-readable information on the stop level."""

    def __init__(self,
        *,
        endpoints: typing.Optional[typing.Iterable[global___EstopEndpointWithStatus]] = ...,
        stop_level: global___EstopStopLevel.ValueType = ...,
        stop_level_details: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["endpoints",b"endpoints","stop_level",b"stop_level","stop_level_details",b"stop_level_details"]) -> None: ...
global___EstopSystemStatus = EstopSystemStatus

class EstopCheckInRequest(google.protobuf.message.Message):
    """Client request for setting/maintaining an E-Stop system level.
    After the first CheckIn, must include response to previous challenge.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    ENDPOINT_FIELD_NUMBER: builtins.int
    CHALLENGE_FIELD_NUMBER: builtins.int
    RESPONSE_FIELD_NUMBER: builtins.int
    STOP_LEVEL_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.RequestHeader:
        """Common request header."""
        pass
    @property
    def endpoint(self) -> global___EstopEndpoint:
        """The endpoint making the request."""
        pass
    challenge: builtins.int
    """Challenge being responded to.
    Don't set if this is the first EstopCheckInRequest.
    """

    response: builtins.int
    """Response to above challenge.
    Don't set if this is the first EstopCheckInRequest.
    """

    stop_level: global___EstopStopLevel.ValueType
    """Assert this stop level."""

    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.RequestHeader] = ...,
        endpoint: typing.Optional[global___EstopEndpoint] = ...,
        challenge: builtins.int = ...,
        response: builtins.int = ...,
        stop_level: global___EstopStopLevel.ValueType = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["endpoint",b"endpoint","header",b"header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["challenge",b"challenge","endpoint",b"endpoint","header",b"header","response",b"response","stop_level",b"stop_level"]) -> None: ...
global___EstopCheckInRequest = EstopCheckInRequest

class EstopCheckInResponse(google.protobuf.message.Message):
    """Server response to EstopCheckInRequest."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Status:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[EstopCheckInResponse._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNKNOWN: EstopCheckInResponse._Status.ValueType  # 0
        """Unknown error occurred."""

        STATUS_OK: EstopCheckInResponse._Status.ValueType  # 1
        """Valid challenge has been returned."""

        STATUS_ENDPOINT_UNKNOWN: EstopCheckInResponse._Status.ValueType  # 2
        """The endpoint specified in the request is not registered."""

        STATUS_INCORRECT_CHALLENGE_RESPONSE: EstopCheckInResponse._Status.ValueType  # 5
        """The challenge and/or response was incorrect."""

    class Status(_Status, metaclass=_StatusEnumTypeWrapper):
        pass

    STATUS_UNKNOWN: EstopCheckInResponse.Status.ValueType  # 0
    """Unknown error occurred."""

    STATUS_OK: EstopCheckInResponse.Status.ValueType  # 1
    """Valid challenge has been returned."""

    STATUS_ENDPOINT_UNKNOWN: EstopCheckInResponse.Status.ValueType  # 2
    """The endpoint specified in the request is not registered."""

    STATUS_INCORRECT_CHALLENGE_RESPONSE: EstopCheckInResponse.Status.ValueType  # 5
    """The challenge and/or response was incorrect."""


    HEADER_FIELD_NUMBER: builtins.int
    REQUEST_FIELD_NUMBER: builtins.int
    CHALLENGE_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.ResponseHeader:
        """Common response header."""
        pass
    @property
    def request(self) -> global___EstopCheckInRequest:
        """Copy of initial request."""
        pass
    challenge: builtins.int
    """Next challenge to answer."""

    status: global___EstopCheckInResponse.Status.ValueType
    """Status code for the response."""

    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.ResponseHeader] = ...,
        request: typing.Optional[global___EstopCheckInRequest] = ...,
        challenge: builtins.int = ...,
        status: global___EstopCheckInResponse.Status.ValueType = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header","request",b"request"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["challenge",b"challenge","header",b"header","request",b"request","status",b"status"]) -> None: ...
global___EstopCheckInResponse = EstopCheckInResponse

class RegisterEstopEndpointRequest(google.protobuf.message.Message):
    """Register an endpoint.
    EstopEndpoints must be registered before they can send commands or request challenges.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    TARGET_ENDPOINT_FIELD_NUMBER: builtins.int
    TARGET_CONFIG_ID_FIELD_NUMBER: builtins.int
    NEW_ENDPOINT_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.RequestHeader:
        """Common request header"""
        pass
    @property
    def target_endpoint(self) -> global___EstopEndpoint:
        """The endpoint to replace.
        Set the endpoint's unique ID if replacing an active endpoint.
        """
        pass
    target_config_id: typing.Text
    """ID of the configuration we are registering against."""

    @property
    def new_endpoint(self) -> global___EstopEndpoint:
        """The description of the new endpoint.
        Do not set the unique ID. It will be ignored.
        """
        pass
    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.RequestHeader] = ...,
        target_endpoint: typing.Optional[global___EstopEndpoint] = ...,
        target_config_id: typing.Text = ...,
        new_endpoint: typing.Optional[global___EstopEndpoint] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header","new_endpoint",b"new_endpoint","target_endpoint",b"target_endpoint"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header","new_endpoint",b"new_endpoint","target_config_id",b"target_config_id","target_endpoint",b"target_endpoint"]) -> None: ...
global___RegisterEstopEndpointRequest = RegisterEstopEndpointRequest

class RegisterEstopEndpointResponse(google.protobuf.message.Message):
    """Response to registration request."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Status:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[RegisterEstopEndpointResponse._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNKNOWN: RegisterEstopEndpointResponse._Status.ValueType  # 0
        """An unknown / unexpected error occurred."""

        STATUS_SUCCESS: RegisterEstopEndpointResponse._Status.ValueType  # 1
        """Request succeeded."""

        STATUS_ENDPOINT_MISMATCH: RegisterEstopEndpointResponse._Status.ValueType  # 2
        """Target endpoint did not match."""

        STATUS_CONFIG_MISMATCH: RegisterEstopEndpointResponse._Status.ValueType  # 3
        """Registered to wrong configuration."""

        STATUS_INVALID_ENDPOINT: RegisterEstopEndpointResponse._Status.ValueType  # 4
        """New endpoint was invalid."""

    class Status(_Status, metaclass=_StatusEnumTypeWrapper):
        pass

    STATUS_UNKNOWN: RegisterEstopEndpointResponse.Status.ValueType  # 0
    """An unknown / unexpected error occurred."""

    STATUS_SUCCESS: RegisterEstopEndpointResponse.Status.ValueType  # 1
    """Request succeeded."""

    STATUS_ENDPOINT_MISMATCH: RegisterEstopEndpointResponse.Status.ValueType  # 2
    """Target endpoint did not match."""

    STATUS_CONFIG_MISMATCH: RegisterEstopEndpointResponse.Status.ValueType  # 3
    """Registered to wrong configuration."""

    STATUS_INVALID_ENDPOINT: RegisterEstopEndpointResponse.Status.ValueType  # 4
    """New endpoint was invalid."""


    HEADER_FIELD_NUMBER: builtins.int
    REQUEST_FIELD_NUMBER: builtins.int
    NEW_ENDPOINT_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.ResponseHeader:
        """Common response header"""
        pass
    @property
    def request(self) -> global___RegisterEstopEndpointRequest:
        """Copy of the initial request."""
        pass
    @property
    def new_endpoint(self) -> global___EstopEndpoint:
        """The resulting endpoint on success."""
        pass
    status: global___RegisterEstopEndpointResponse.Status.ValueType
    """Status code for the response."""

    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.ResponseHeader] = ...,
        request: typing.Optional[global___RegisterEstopEndpointRequest] = ...,
        new_endpoint: typing.Optional[global___EstopEndpoint] = ...,
        status: global___RegisterEstopEndpointResponse.Status.ValueType = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header","new_endpoint",b"new_endpoint","request",b"request"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header","new_endpoint",b"new_endpoint","request",b"request","status",b"status"]) -> None: ...
global___RegisterEstopEndpointResponse = RegisterEstopEndpointResponse

class DeregisterEstopEndpointRequest(google.protobuf.message.Message):
    """Deregister the specified E-Stop endpoint registration."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    TARGET_ENDPOINT_FIELD_NUMBER: builtins.int
    TARGET_CONFIG_ID_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.RequestHeader:
        """Common request header"""
        pass
    @property
    def target_endpoint(self) -> global___EstopEndpoint:
        """The endpoint to deregister."""
        pass
    target_config_id: typing.Text
    """ID of the configuration we are registering against."""

    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.RequestHeader] = ...,
        target_endpoint: typing.Optional[global___EstopEndpoint] = ...,
        target_config_id: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header","target_endpoint",b"target_endpoint"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header","target_config_id",b"target_config_id","target_endpoint",b"target_endpoint"]) -> None: ...
global___DeregisterEstopEndpointRequest = DeregisterEstopEndpointRequest

class DeregisterEstopEndpointResponse(google.protobuf.message.Message):
    """Response to E-Stop endpoint  deregistration request."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Status:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[DeregisterEstopEndpointResponse._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNKNOWN: DeregisterEstopEndpointResponse._Status.ValueType  # 0
        """An unknown / unexpected error occurred."""

        STATUS_SUCCESS: DeregisterEstopEndpointResponse._Status.ValueType  # 1
        """Request succeeded."""

        STATUS_ENDPOINT_MISMATCH: DeregisterEstopEndpointResponse._Status.ValueType  # 2
        """Target endpoint did not match."""

        STATUS_CONFIG_MISMATCH: DeregisterEstopEndpointResponse._Status.ValueType  # 3
        """Registered to wrong configuration."""

        STATUS_MOTORS_ON: DeregisterEstopEndpointResponse._Status.ValueType  # 4
        """You cannot deregister an endpoint while the motors are on."""

    class Status(_Status, metaclass=_StatusEnumTypeWrapper):
        pass

    STATUS_UNKNOWN: DeregisterEstopEndpointResponse.Status.ValueType  # 0
    """An unknown / unexpected error occurred."""

    STATUS_SUCCESS: DeregisterEstopEndpointResponse.Status.ValueType  # 1
    """Request succeeded."""

    STATUS_ENDPOINT_MISMATCH: DeregisterEstopEndpointResponse.Status.ValueType  # 2
    """Target endpoint did not match."""

    STATUS_CONFIG_MISMATCH: DeregisterEstopEndpointResponse.Status.ValueType  # 3
    """Registered to wrong configuration."""

    STATUS_MOTORS_ON: DeregisterEstopEndpointResponse.Status.ValueType  # 4
    """You cannot deregister an endpoint while the motors are on."""


    HEADER_FIELD_NUMBER: builtins.int
    REQUEST_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.ResponseHeader:
        """Common resonse header."""
        pass
    @property
    def request(self) -> global___DeregisterEstopEndpointRequest:
        """Copy of the initial request."""
        pass
    status: global___DeregisterEstopEndpointResponse.Status.ValueType
    """Status code for the response."""

    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.ResponseHeader] = ...,
        request: typing.Optional[global___DeregisterEstopEndpointRequest] = ...,
        status: global___DeregisterEstopEndpointResponse.Status.ValueType = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header","request",b"request"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header","request",b"request","status",b"status"]) -> None: ...
global___DeregisterEstopEndpointResponse = DeregisterEstopEndpointResponse

class GetEstopConfigRequest(google.protobuf.message.Message):
    """Get the active EstopConfig."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    TARGET_CONFIG_ID_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.RequestHeader:
        """Common request header."""
        pass
    target_config_id: typing.Text
    """The 'unique_id' of EstopConfig to get."""

    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.RequestHeader] = ...,
        target_config_id: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header","target_config_id",b"target_config_id"]) -> None: ...
global___GetEstopConfigRequest = GetEstopConfigRequest

class GetEstopConfigResponse(google.protobuf.message.Message):
    """Response to EstopConfigRequest."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    REQUEST_FIELD_NUMBER: builtins.int
    ACTIVE_CONFIG_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.ResponseHeader:
        """Common response header."""
        pass
    @property
    def request(self) -> global___GetEstopConfigRequest:
        """Copy of the request."""
        pass
    @property
    def active_config(self) -> global___EstopConfig:
        """The currently active configuration."""
        pass
    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.ResponseHeader] = ...,
        request: typing.Optional[global___GetEstopConfigRequest] = ...,
        active_config: typing.Optional[global___EstopConfig] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["active_config",b"active_config","header",b"header","request",b"request"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["active_config",b"active_config","header",b"header","request",b"request"]) -> None: ...
global___GetEstopConfigResponse = GetEstopConfigResponse

class SetEstopConfigRequest(google.protobuf.message.Message):
    """Set a new active EstopConfig."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    CONFIG_FIELD_NUMBER: builtins.int
    TARGET_CONFIG_ID_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.RequestHeader:
        """Common request header."""
        pass
    @property
    def config(self) -> global___EstopConfig:
        """New configuration to set."""
        pass
    target_config_id: typing.Text
    """The 'unique_id' of EstopConfig to replace, if replacing one."""

    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.RequestHeader] = ...,
        config: typing.Optional[global___EstopConfig] = ...,
        target_config_id: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["config",b"config","header",b"header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["config",b"config","header",b"header","target_config_id",b"target_config_id"]) -> None: ...
global___SetEstopConfigRequest = SetEstopConfigRequest

class SetEstopConfigResponse(google.protobuf.message.Message):
    """Response to EstopConfigRequest."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Status:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[SetEstopConfigResponse._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNKNOWN: SetEstopConfigResponse._Status.ValueType  # 0
        """An unknown / unexpected error occurred."""

        STATUS_SUCCESS: SetEstopConfigResponse._Status.ValueType  # 1
        """Request succeeded."""

        STATUS_INVALID_ID: SetEstopConfigResponse._Status.ValueType  # 2
        """Tried to replace a EstopConfig, but provided bad ID."""

        STATUS_MOTORS_ON: SetEstopConfigResponse._Status.ValueType  # 4
        """You cannot set a configuration while the motors are on."""

    class Status(_Status, metaclass=_StatusEnumTypeWrapper):
        pass

    STATUS_UNKNOWN: SetEstopConfigResponse.Status.ValueType  # 0
    """An unknown / unexpected error occurred."""

    STATUS_SUCCESS: SetEstopConfigResponse.Status.ValueType  # 1
    """Request succeeded."""

    STATUS_INVALID_ID: SetEstopConfigResponse.Status.ValueType  # 2
    """Tried to replace a EstopConfig, but provided bad ID."""

    STATUS_MOTORS_ON: SetEstopConfigResponse.Status.ValueType  # 4
    """You cannot set a configuration while the motors are on."""


    HEADER_FIELD_NUMBER: builtins.int
    REQUEST_FIELD_NUMBER: builtins.int
    ACTIVE_CONFIG_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.ResponseHeader:
        """Common response header."""
        pass
    @property
    def request(self) -> global___SetEstopConfigRequest:
        """Copy of the request."""
        pass
    @property
    def active_config(self) -> global___EstopConfig:
        """The currently active configuration."""
        pass
    status: global___SetEstopConfigResponse.Status.ValueType
    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.ResponseHeader] = ...,
        request: typing.Optional[global___SetEstopConfigRequest] = ...,
        active_config: typing.Optional[global___EstopConfig] = ...,
        status: global___SetEstopConfigResponse.Status.ValueType = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["active_config",b"active_config","header",b"header","request",b"request"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["active_config",b"active_config","header",b"header","request",b"request","status",b"status"]) -> None: ...
global___SetEstopConfigResponse = SetEstopConfigResponse

class GetEstopSystemStatusRequest(google.protobuf.message.Message):
    """Ask for the current status of the Estop system."""
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
global___GetEstopSystemStatusRequest = GetEstopSystemStatusRequest

class GetEstopSystemStatusResponse(google.protobuf.message.Message):
    """Respond with the current Estop system status."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.ResponseHeader:
        """Common response header."""
        pass
    @property
    def status(self) -> global___EstopSystemStatus:
        """Status of the Estop system."""
        pass
    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.ResponseHeader] = ...,
        status: typing.Optional[global___EstopSystemStatus] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header","status",b"status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header","status",b"status"]) -> None: ...
global___GetEstopSystemStatusResponse = GetEstopSystemStatusResponse