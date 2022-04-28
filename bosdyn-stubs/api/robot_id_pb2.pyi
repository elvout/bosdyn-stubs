"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import bosdyn.api.header_pb2
import bosdyn.api.parameter_pb2
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class RobotId(google.protobuf.message.Message):
    """Robot identity information, which should be static while robot is powered-on."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SERIAL_NUMBER_FIELD_NUMBER: builtins.int
    SPECIES_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    SOFTWARE_RELEASE_FIELD_NUMBER: builtins.int
    NICKNAME_FIELD_NUMBER: builtins.int
    COMPUTER_SERIAL_NUMBER_FIELD_NUMBER: builtins.int
    serial_number: typing.Text
    """A unique string identifier for the particular robot."""

    species: typing.Text
    """Type of robot.  E.g., 'spot'."""

    version: typing.Text
    """Robot version/platform."""

    @property
    def software_release(self) -> global___RobotSoftwareRelease:
        """Version information about software running on the robot."""
        pass
    nickname: typing.Text
    """Optional, customer-supplied nickname."""

    computer_serial_number: typing.Text
    """Computer Serial Number. Unlike serial_number, which identifies a complete robot,
    the computer_serial_number identifies the computer hardware used in the robot.
    """

    def __init__(self,
        *,
        serial_number: typing.Text = ...,
        species: typing.Text = ...,
        version: typing.Text = ...,
        software_release: typing.Optional[global___RobotSoftwareRelease] = ...,
        nickname: typing.Text = ...,
        computer_serial_number: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["software_release",b"software_release"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["computer_serial_number",b"computer_serial_number","nickname",b"nickname","serial_number",b"serial_number","software_release",b"software_release","species",b"species","version",b"version"]) -> None: ...
global___RobotId = RobotId

class SoftwareVersion(google.protobuf.message.Message):
    """The software versioning number for a release."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MAJOR_VERSION_FIELD_NUMBER: builtins.int
    MINOR_VERSION_FIELD_NUMBER: builtins.int
    PATCH_LEVEL_FIELD_NUMBER: builtins.int
    major_version: builtins.int
    """Signficant changes to software."""

    minor_version: builtins.int
    """Normal changes to software."""

    patch_level: builtins.int
    """Fixes which should not change intended capabilities or affect compatibility."""

    def __init__(self,
        *,
        major_version: builtins.int = ...,
        minor_version: builtins.int = ...,
        patch_level: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["major_version",b"major_version","minor_version",b"minor_version","patch_level",b"patch_level"]) -> None: ...
global___SoftwareVersion = SoftwareVersion

class RobotSoftwareRelease(google.protobuf.message.Message):
    """Description of the software release currently running on the robot."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VERSION_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    CHANGESET_DATE_FIELD_NUMBER: builtins.int
    CHANGESET_FIELD_NUMBER: builtins.int
    API_VERSION_FIELD_NUMBER: builtins.int
    BUILD_INFORMATION_FIELD_NUMBER: builtins.int
    INSTALL_DATE_FIELD_NUMBER: builtins.int
    PARAMETERS_FIELD_NUMBER: builtins.int
    @property
    def version(self) -> global___SoftwareVersion:
        """The software version, e.g., 2.0.1"""
        pass
    name: typing.Text
    """The name of the robot, e.g., '20190601'"""

    type: typing.Text
    """Kind of software release."""

    @property
    def changeset_date(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Timestamp of the changeset."""
        pass
    changeset: typing.Text
    """Changeset hash."""

    api_version: typing.Text
    """API version.  E.g., 2.14.5."""

    build_information: typing.Text
    """Extra information associated with the build."""

    @property
    def install_date(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Date/time when release was installed."""
        pass
    @property
    def parameters(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[bosdyn.api.parameter_pb2.Parameter]:
        """Other information about the build."""
        pass
    def __init__(self,
        *,
        version: typing.Optional[global___SoftwareVersion] = ...,
        name: typing.Text = ...,
        type: typing.Text = ...,
        changeset_date: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        changeset: typing.Text = ...,
        api_version: typing.Text = ...,
        build_information: typing.Text = ...,
        install_date: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        parameters: typing.Optional[typing.Iterable[bosdyn.api.parameter_pb2.Parameter]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["changeset_date",b"changeset_date","install_date",b"install_date","version",b"version"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["api_version",b"api_version","build_information",b"build_information","changeset",b"changeset","changeset_date",b"changeset_date","install_date",b"install_date","name",b"name","parameters",b"parameters","type",b"type","version",b"version"]) -> None: ...
global___RobotSoftwareRelease = RobotSoftwareRelease

class RobotIdRequest(google.protobuf.message.Message):
    """The RobotId request message sent to a robot to learn it's basic identification information."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.RequestHeader:
        """Common request/response header."""
        pass
    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.RequestHeader] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header"]) -> None: ...
global___RobotIdRequest = RobotIdRequest

class RobotIdResponse(google.protobuf.message.Message):
    """The RobotId response message, including the ID information for a robot."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    ROBOT_ID_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.ResponseHeader:
        """Common request/response header."""
        pass
    @property
    def robot_id(self) -> global___RobotId:
        """The requested RobotId information."""
        pass
    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.ResponseHeader] = ...,
        robot_id: typing.Optional[global___RobotId] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header","robot_id",b"robot_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header","robot_id",b"robot_id"]) -> None: ...
global___RobotIdResponse = RobotIdResponse