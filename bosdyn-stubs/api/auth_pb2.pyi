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

class GetAuthTokenRequest(google.protobuf.message.Message):
    """The GetAuthToken request message includes login information for the robot."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    USERNAME_FIELD_NUMBER: builtins.int
    PASSWORD_FIELD_NUMBER: builtins.int
    TOKEN_FIELD_NUMBER: builtins.int
    APPLICATION_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.RequestHeader:
        """Common request header."""
        pass
    username: typing.Text
    """Username to authenticate with. Must be set if password is set."""

    password: typing.Text
    """Password to authenticate with. Not neccessary if token is set."""

    token: typing.Text
    """Token to authenticate with. Can be used in place of the password, to re-mint a token."""

    application_token: typing.Text
    """Deprecated as of 2.0.1. Application Token for authenticating with robots on older releases."""

    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.RequestHeader] = ...,
        username: typing.Text = ...,
        password: typing.Text = ...,
        token: typing.Text = ...,
        application_token: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["application_token",b"application_token","header",b"header","password",b"password","token",b"token","username",b"username"]) -> None: ...
global___GetAuthTokenRequest = GetAuthTokenRequest

class GetAuthTokenResponse(google.protobuf.message.Message):
    """The GetAuthToken response message includes an authentication token if the login information
    is correct and succeeds.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Status:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[GetAuthTokenResponse._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNKNOWN: GetAuthTokenResponse._Status.ValueType  # 0
        """STATUS_UNKNOWN should never be used. If used, an internal error has happend."""

        STATUS_OK: GetAuthTokenResponse._Status.ValueType  # 1
        """STATUS_OK indicates that authentication has succeeded. The 'token' field field will
        be populated with a session token that can be used to authenticate the user.
        """

        STATUS_INVALID_LOGIN: GetAuthTokenResponse._Status.ValueType  # 2
        """STATUS_INVALID_LOGIN indicates that authentication has failed since an invalid
        username and/or password were provided.
        """

        STATUS_INVALID_TOKEN: GetAuthTokenResponse._Status.ValueType  # 3
        """STATUS_INVALID_TOKEN indicates that authentication has failed since the 'token'
        provided in the request is invalid. Reasons for the token being invalid could be
        because it has expired, because it is improperly formed, for the wrong robot, the
        user that the token is for has changed a password, or many other reasons. Clients
        should use username/password-based authentication when refreshing the token fails.
        """

        STATUS_TEMPORARILY_LOCKED_OUT: GetAuthTokenResponse._Status.ValueType  # 4
        """STATUS_TEMPORARILY_LOCKED_OUT indicates that authentication has failed since
        authentication for the user is temporarily locked out due to too many unsuccessful
        attempts. Any new authentication attempts should be delayed so they may happen after
        the lock out period ends.
        """

        STATUS_INVALID_APPLICATION_TOKEN: GetAuthTokenResponse._Status.ValueType  # 5
        """STATUS_INVALID_APPLICATION_TOKEN indicates that the 'application_token' field in the
        request was invalid.
        """

        STATUS_EXPIRED_APPLICATION_TOKEN: GetAuthTokenResponse._Status.ValueType  # 6
        """STATUS_EXPIRED_APPLICATION_TOKEN indicates that the 'application_token' field in the
        request was valid, but has expired.
        """

    class Status(_Status, metaclass=_StatusEnumTypeWrapper):
        pass

    STATUS_UNKNOWN: GetAuthTokenResponse.Status.ValueType  # 0
    """STATUS_UNKNOWN should never be used. If used, an internal error has happend."""

    STATUS_OK: GetAuthTokenResponse.Status.ValueType  # 1
    """STATUS_OK indicates that authentication has succeeded. The 'token' field field will
    be populated with a session token that can be used to authenticate the user.
    """

    STATUS_INVALID_LOGIN: GetAuthTokenResponse.Status.ValueType  # 2
    """STATUS_INVALID_LOGIN indicates that authentication has failed since an invalid
    username and/or password were provided.
    """

    STATUS_INVALID_TOKEN: GetAuthTokenResponse.Status.ValueType  # 3
    """STATUS_INVALID_TOKEN indicates that authentication has failed since the 'token'
    provided in the request is invalid. Reasons for the token being invalid could be
    because it has expired, because it is improperly formed, for the wrong robot, the
    user that the token is for has changed a password, or many other reasons. Clients
    should use username/password-based authentication when refreshing the token fails.
    """

    STATUS_TEMPORARILY_LOCKED_OUT: GetAuthTokenResponse.Status.ValueType  # 4
    """STATUS_TEMPORARILY_LOCKED_OUT indicates that authentication has failed since
    authentication for the user is temporarily locked out due to too many unsuccessful
    attempts. Any new authentication attempts should be delayed so they may happen after
    the lock out period ends.
    """

    STATUS_INVALID_APPLICATION_TOKEN: GetAuthTokenResponse.Status.ValueType  # 5
    """STATUS_INVALID_APPLICATION_TOKEN indicates that the 'application_token' field in the
    request was invalid.
    """

    STATUS_EXPIRED_APPLICATION_TOKEN: GetAuthTokenResponse.Status.ValueType  # 6
    """STATUS_EXPIRED_APPLICATION_TOKEN indicates that the 'application_token' field in the
    request was valid, but has expired.
    """


    HEADER_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    TOKEN_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.ResponseHeader: ...
    status: global___GetAuthTokenResponse.Status.ValueType
    """The status of the grpc GetAuthToken request."""

    token: typing.Text
    """Token data. Only specified if status == STATUS_OK."""

    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.ResponseHeader] = ...,
        status: global___GetAuthTokenResponse.Status.ValueType = ...,
        token: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header","status",b"status","token",b"token"]) -> None: ...
global___GetAuthTokenResponse = GetAuthTokenResponse
