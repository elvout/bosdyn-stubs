"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import bosdyn.api.header_pb2
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class LicenseInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Status:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[LicenseInfo._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNKNOWN: LicenseInfo._Status.ValueType  # 0
        STATUS_VALID: LicenseInfo._Status.ValueType  # 1
        STATUS_EXPIRED: LicenseInfo._Status.ValueType  # 2
        STATUS_NOT_YET_VALID: LicenseInfo._Status.ValueType  # 3
        STATUS_MALFORMED: LicenseInfo._Status.ValueType  # 4
        STATUS_SERIAL_MISMATCH: LicenseInfo._Status.ValueType  # 5
        STATUS_NO_LICENSE: LicenseInfo._Status.ValueType  # 6
    class Status(_Status, metaclass=_StatusEnumTypeWrapper):
        pass

    STATUS_UNKNOWN: LicenseInfo.Status.ValueType  # 0
    STATUS_VALID: LicenseInfo.Status.ValueType  # 1
    STATUS_EXPIRED: LicenseInfo.Status.ValueType  # 2
    STATUS_NOT_YET_VALID: LicenseInfo.Status.ValueType  # 3
    STATUS_MALFORMED: LicenseInfo.Status.ValueType  # 4
    STATUS_SERIAL_MISMATCH: LicenseInfo.Status.ValueType  # 5
    STATUS_NO_LICENSE: LicenseInfo.Status.ValueType  # 6

    STATUS_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    ROBOT_SERIAL_FIELD_NUMBER: builtins.int
    NOT_VALID_BEFORE_FIELD_NUMBER: builtins.int
    NOT_VALID_AFTER_FIELD_NUMBER: builtins.int
    LICENSED_FEATURES_FIELD_NUMBER: builtins.int
    status: global___LicenseInfo.Status.ValueType
    """The status of the uploaded license for this robot."""

    id: typing.Text
    """Unique license number."""

    robot_serial: typing.Text
    """Serial number of the robot this license covers."""

    @property
    def not_valid_before(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The license is not valid for use for any dates before this timestamp."""
        pass
    @property
    def not_valid_after(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The license is not valid for use for any dates after this timestamp."""
        pass
    @property
    def licensed_features(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """/ Human readable list of licensed features included for this license."""
        pass
    def __init__(self,
        *,
        status: global___LicenseInfo.Status.ValueType = ...,
        id: typing.Text = ...,
        robot_serial: typing.Text = ...,
        not_valid_before: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        not_valid_after: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        licensed_features: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["not_valid_after",b"not_valid_after","not_valid_before",b"not_valid_before"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["id",b"id","licensed_features",b"licensed_features","not_valid_after",b"not_valid_after","not_valid_before",b"not_valid_before","robot_serial",b"robot_serial","status",b"status"]) -> None: ...
global___LicenseInfo = LicenseInfo

class GetLicenseInfoRequest(google.protobuf.message.Message):
    """"""
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
global___GetLicenseInfoRequest = GetLicenseInfoRequest

class GetLicenseInfoResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    LICENSE_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.ResponseHeader:
        """Common response header"""
        pass
    @property
    def license(self) -> global___LicenseInfo:
        """The details about the current license that is uploaded to the robot."""
        pass
    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.ResponseHeader] = ...,
        license: typing.Optional[global___LicenseInfo] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header","license",b"license"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header","license",b"license"]) -> None: ...
global___GetLicenseInfoResponse = GetLicenseInfoResponse

class GetFeatureEnabledRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    FEATURE_CODES_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.RequestHeader:
        """Common request header."""
        pass
    @property
    def feature_codes(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Check if specific named features are enabled on the robot under the currently
        loaded license.
        """
        pass
    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.RequestHeader] = ...,
        feature_codes: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["feature_codes",b"feature_codes","header",b"header"]) -> None: ...
global___GetFeatureEnabledRequest = GetFeatureEnabledRequest

class GetFeatureEnabledResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class FeatureEnabledEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text
        value: builtins.bool
        def __init__(self,
            *,
            key: typing.Text = ...,
            value: builtins.bool = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    HEADER_FIELD_NUMBER: builtins.int
    FEATURE_ENABLED_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.ResponseHeader:
        """Common response header."""
        pass
    @property
    def feature_enabled(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, builtins.bool]:
        """The resulting map showing the feature name (as the map key) and a boolean indicating
        if the feature is enabled with this license (as the map value).
        """
        pass
    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.ResponseHeader] = ...,
        feature_enabled: typing.Optional[typing.Mapping[typing.Text, builtins.bool]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["feature_enabled",b"feature_enabled","header",b"header"]) -> None: ...
global___GetFeatureEnabledResponse = GetFeatureEnabledResponse
