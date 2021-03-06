"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import bosdyn.api.full_body_command_pb2
import bosdyn.api.header_pb2
import bosdyn.api.lease_pb2
import bosdyn.api.mobility_command_pb2
import bosdyn.api.synchronized_command_pb2
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class RobotCommand(google.protobuf.message.Message):
    """A command for a robot to execute.
    The server decides if a set of commands is valid for a given robot and configuration.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FULL_BODY_COMMAND_FIELD_NUMBER: builtins.int
    SYNCHRONIZED_COMMAND_FIELD_NUMBER: builtins.int
    MOBILITY_COMMAND_FIELD_NUMBER: builtins.int
    @property
    def full_body_command(self) -> bosdyn.api.full_body_command_pb2.FullBodyCommand.Request:
        """Commands which require control of entire robot."""
        pass
    @property
    def synchronized_command(self) -> bosdyn.api.synchronized_command_pb2.SynchronizedCommand.Request:
        """A synchronized command, for partial or full control of robot."""
        pass
    @property
    def mobility_command(self) -> bosdyn.api.mobility_command_pb2.MobilityCommand.Request:
        """*** Deprecation Warning ***
        DEPRECATED as of 2.1.0: A mobility command for a robot to execute.
        The following fields will be deprecated and moved to 'reserved' in a future release.
        """
        pass
    def __init__(self,
        *,
        full_body_command: typing.Optional[bosdyn.api.full_body_command_pb2.FullBodyCommand.Request] = ...,
        synchronized_command: typing.Optional[bosdyn.api.synchronized_command_pb2.SynchronizedCommand.Request] = ...,
        mobility_command: typing.Optional[bosdyn.api.mobility_command_pb2.MobilityCommand.Request] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["command",b"command","full_body_command",b"full_body_command","mobility_command",b"mobility_command","synchronized_command",b"synchronized_command"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["command",b"command","full_body_command",b"full_body_command","mobility_command",b"mobility_command","synchronized_command",b"synchronized_command"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["command",b"command"]) -> typing.Optional[typing_extensions.Literal["full_body_command","synchronized_command","mobility_command"]]: ...
global___RobotCommand = RobotCommand

class RobotCommandFeedback(google.protobuf.message.Message):
    """Command specific feedback. Distance to goal, estimated time remaining, probability of
    success, etc. Note that the feedback should directly mirror the command request.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FULL_BODY_FEEDBACK_FIELD_NUMBER: builtins.int
    SYNCHRONIZED_FEEDBACK_FIELD_NUMBER: builtins.int
    MOBILITY_FEEDBACK_FIELD_NUMBER: builtins.int
    @property
    def full_body_feedback(self) -> bosdyn.api.full_body_command_pb2.FullBodyCommand.Feedback:
        """Commands which require control of entire robot."""
        pass
    @property
    def synchronized_feedback(self) -> bosdyn.api.synchronized_command_pb2.SynchronizedCommand.Feedback:
        """A synchronized command, for partial or full control of robot."""
        pass
    @property
    def mobility_feedback(self) -> bosdyn.api.mobility_command_pb2.MobilityCommand.Feedback:
        """*** Deprecation Warning ***
        DEPRECATED as of 2.1.0: Command to control mobility system of a robot.
        The following fields will be deprecated and moved to 'reserved' in a future release.
        """
        pass
    def __init__(self,
        *,
        full_body_feedback: typing.Optional[bosdyn.api.full_body_command_pb2.FullBodyCommand.Feedback] = ...,
        synchronized_feedback: typing.Optional[bosdyn.api.synchronized_command_pb2.SynchronizedCommand.Feedback] = ...,
        mobility_feedback: typing.Optional[bosdyn.api.mobility_command_pb2.MobilityCommand.Feedback] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["command",b"command","full_body_feedback",b"full_body_feedback","mobility_feedback",b"mobility_feedback","synchronized_feedback",b"synchronized_feedback"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["command",b"command","full_body_feedback",b"full_body_feedback","mobility_feedback",b"mobility_feedback","synchronized_feedback",b"synchronized_feedback"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["command",b"command"]) -> typing.Optional[typing_extensions.Literal["full_body_feedback","synchronized_feedback","mobility_feedback"]]: ...
global___RobotCommandFeedback = RobotCommandFeedback

class RobotCommandRequest(google.protobuf.message.Message):
    """A RobotCommand request message includes the lease and command as well as a clock
    identifier to ensure timesync when issuing commands with a fixed length.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    LEASE_FIELD_NUMBER: builtins.int
    COMMAND_FIELD_NUMBER: builtins.int
    CLOCK_IDENTIFIER_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.RequestHeader:
        """Common request header."""
        pass
    @property
    def lease(self) -> bosdyn.api.lease_pb2.Lease:
        """The Lease to show ownership of the robot."""
        pass
    @property
    def command(self) -> global___RobotCommand:
        """A command for a robot to execute. A command can be comprised of several subcommands."""
        pass
    clock_identifier: typing.Text
    """Identifier provided by the time sync service to verify time sync between robot and client."""

    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.RequestHeader] = ...,
        lease: typing.Optional[bosdyn.api.lease_pb2.Lease] = ...,
        command: typing.Optional[global___RobotCommand] = ...,
        clock_identifier: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["command",b"command","header",b"header","lease",b"lease"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["clock_identifier",b"clock_identifier","command",b"command","header",b"header","lease",b"lease"]) -> None: ...
global___RobotCommandRequest = RobotCommandRequest

class RobotCommandResponse(google.protobuf.message.Message):
    """The RobotCommand response message contains a robot command id that can be used to poll the
    robot command service for feedback on the state of the command.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Status:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[RobotCommandResponse._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNKNOWN: RobotCommandResponse._Status.ValueType  # 0
        """An unknown / unexpected error occurred."""

        STATUS_OK: RobotCommandResponse._Status.ValueType  # 1
        """Request was accepted."""

        STATUS_INVALID_REQUEST: RobotCommandResponse._Status.ValueType  # 2
        """[Programming Error] Request was invalid / malformed in some way."""

        STATUS_UNSUPPORTED: RobotCommandResponse._Status.ValueType  # 3
        """[Programming Error] The robot does not understand this command."""

        STATUS_NO_TIMESYNC: RobotCommandResponse._Status.ValueType  # 4
        """[Timesync Error] Client has not done timesync with robot."""

        STATUS_EXPIRED: RobotCommandResponse._Status.ValueType  # 5
        """[Timesync Error] The command was received after its end_time had already passed."""

        STATUS_TOO_DISTANT: RobotCommandResponse._Status.ValueType  # 6
        """[Timesync Error] The command end time was too far in the future."""

        STATUS_NOT_POWERED_ON: RobotCommandResponse._Status.ValueType  # 7
        """[Hardware Error] The robot must be powered on to accept a command."""

        STATUS_BEHAVIOR_FAULT: RobotCommandResponse._Status.ValueType  # 9
        """[Robot State Error] The robot must not have behavior faults."""

        STATUS_UNKNOWN_FRAME: RobotCommandResponse._Status.ValueType  # 8
        """[Frame Error] The frame_name for a command was not a known frame."""

    class Status(_Status, metaclass=_StatusEnumTypeWrapper):
        pass

    STATUS_UNKNOWN: RobotCommandResponse.Status.ValueType  # 0
    """An unknown / unexpected error occurred."""

    STATUS_OK: RobotCommandResponse.Status.ValueType  # 1
    """Request was accepted."""

    STATUS_INVALID_REQUEST: RobotCommandResponse.Status.ValueType  # 2
    """[Programming Error] Request was invalid / malformed in some way."""

    STATUS_UNSUPPORTED: RobotCommandResponse.Status.ValueType  # 3
    """[Programming Error] The robot does not understand this command."""

    STATUS_NO_TIMESYNC: RobotCommandResponse.Status.ValueType  # 4
    """[Timesync Error] Client has not done timesync with robot."""

    STATUS_EXPIRED: RobotCommandResponse.Status.ValueType  # 5
    """[Timesync Error] The command was received after its end_time had already passed."""

    STATUS_TOO_DISTANT: RobotCommandResponse.Status.ValueType  # 6
    """[Timesync Error] The command end time was too far in the future."""

    STATUS_NOT_POWERED_ON: RobotCommandResponse.Status.ValueType  # 7
    """[Hardware Error] The robot must be powered on to accept a command."""

    STATUS_BEHAVIOR_FAULT: RobotCommandResponse.Status.ValueType  # 9
    """[Robot State Error] The robot must not have behavior faults."""

    STATUS_UNKNOWN_FRAME: RobotCommandResponse.Status.ValueType  # 8
    """[Frame Error] The frame_name for a command was not a known frame."""


    HEADER_FIELD_NUMBER: builtins.int
    LEASE_USE_RESULT_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    ROBOT_COMMAND_ID_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.ResponseHeader:
        """Common response header."""
        pass
    @property
    def lease_use_result(self) -> bosdyn.api.lease_pb2.LeaseUseResult:
        """Details about how the lease was used."""
        pass
    status: global___RobotCommandResponse.Status.ValueType
    """Return status for a request."""

    message: typing.Text
    """Human-readable error description.  Not for programmatic analysis."""

    robot_command_id: builtins.int
    """Unique identifier for the command, If empty, command was not accepted."""

    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.ResponseHeader] = ...,
        lease_use_result: typing.Optional[bosdyn.api.lease_pb2.LeaseUseResult] = ...,
        status: global___RobotCommandResponse.Status.ValueType = ...,
        message: typing.Text = ...,
        robot_command_id: builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header","lease_use_result",b"lease_use_result"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header","lease_use_result",b"lease_use_result","message",b"message","robot_command_id",b"robot_command_id","status",b"status"]) -> None: ...
global___RobotCommandResponse = RobotCommandResponse

class RobotCommandFeedbackRequest(google.protobuf.message.Message):
    """The RobotCommandFeedback request message, which can get the feedback for a specific
    robot command id number.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    ROBOT_COMMAND_ID_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.RequestHeader:
        """Common request header."""
        pass
    robot_command_id: builtins.int
    """Unique identifier for the command, provided by StartRequest."""

    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.RequestHeader] = ...,
        robot_command_id: builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header","robot_command_id",b"robot_command_id"]) -> None: ...
global___RobotCommandFeedbackRequest = RobotCommandFeedbackRequest

class RobotCommandFeedbackResponse(google.protobuf.message.Message):
    """The RobotCommandFeedback response message, which contains the progress of the robot command."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Status:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[RobotCommandFeedbackResponse._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNKNOWN: RobotCommandFeedbackResponse._Status.ValueType  # 0
        """Status enum is DEPRECATED as of 2.1.0. Behavior execution is in an unknown / unexpected state."""

        STATUS_PROCESSING: RobotCommandFeedbackResponse._Status.ValueType  # 1
        """Status enum is DEPRECATED as of 2.1.0. The robot is actively working on the command"""

        STATUS_COMMAND_OVERRIDDEN: RobotCommandFeedbackResponse._Status.ValueType  # 2
        """Status enum is DEPRECATED as of 2.1.0. The command was replaced by a new command"""

        STATUS_COMMAND_TIMED_OUT: RobotCommandFeedbackResponse._Status.ValueType  # 3
        """Status enum is DEPRECATED as of 2.1.0. The command expired"""

        STATUS_ROBOT_FROZEN: RobotCommandFeedbackResponse._Status.ValueType  # 4
        """Status enum is DEPRECATED as of 2.1.0. The robot is in an unsafe state, and will only respond to known safe commands."""

    class Status(_Status, metaclass=_StatusEnumTypeWrapper):
        pass

    STATUS_UNKNOWN: RobotCommandFeedbackResponse.Status.ValueType  # 0
    """Status enum is DEPRECATED as of 2.1.0. Behavior execution is in an unknown / unexpected state."""

    STATUS_PROCESSING: RobotCommandFeedbackResponse.Status.ValueType  # 1
    """Status enum is DEPRECATED as of 2.1.0. The robot is actively working on the command"""

    STATUS_COMMAND_OVERRIDDEN: RobotCommandFeedbackResponse.Status.ValueType  # 2
    """Status enum is DEPRECATED as of 2.1.0. The command was replaced by a new command"""

    STATUS_COMMAND_TIMED_OUT: RobotCommandFeedbackResponse.Status.ValueType  # 3
    """Status enum is DEPRECATED as of 2.1.0. The command expired"""

    STATUS_ROBOT_FROZEN: RobotCommandFeedbackResponse.Status.ValueType  # 4
    """Status enum is DEPRECATED as of 2.1.0. The robot is in an unsafe state, and will only respond to known safe commands."""


    HEADER_FIELD_NUMBER: builtins.int
    LEASE_USE_RESULT_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    FEEDBACK_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.ResponseHeader:
        """Common response header."""
        pass
    @property
    def lease_use_result(self) -> bosdyn.api.lease_pb2.LeaseUseResult:
        """Details about how the lease was used."""
        pass
    status: global___RobotCommandFeedbackResponse.Status.ValueType
    """DEPRECATED as of 2.1.0: General status whether or not command is still processing."""

    message: typing.Text
    """DEPRECATED as of 2.1.0: Human-readable status message.  Not for programmatic analysis."""

    @property
    def feedback(self) -> global___RobotCommandFeedback:
        """Command specific feedback."""
        pass
    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.ResponseHeader] = ...,
        lease_use_result: typing.Optional[bosdyn.api.lease_pb2.LeaseUseResult] = ...,
        status: global___RobotCommandFeedbackResponse.Status.ValueType = ...,
        message: typing.Text = ...,
        feedback: typing.Optional[global___RobotCommandFeedback] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["feedback",b"feedback","header",b"header","lease_use_result",b"lease_use_result"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["feedback",b"feedback","header",b"header","lease_use_result",b"lease_use_result","message",b"message","status",b"status"]) -> None: ...
global___RobotCommandFeedbackResponse = RobotCommandFeedbackResponse

class ClearBehaviorFaultRequest(google.protobuf.message.Message):
    """A ClearBehaviorFault request message has the associated behavior fault id to be cleared."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    LEASE_FIELD_NUMBER: builtins.int
    BEHAVIOR_FAULT_ID_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.RequestHeader:
        """Common request header."""
        pass
    @property
    def lease(self) -> bosdyn.api.lease_pb2.Lease:
        """The Lease to show ownership of the robot."""
        pass
    behavior_fault_id: builtins.int
    """Unique identifier for the error"""

    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.RequestHeader] = ...,
        lease: typing.Optional[bosdyn.api.lease_pb2.Lease] = ...,
        behavior_fault_id: builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header","lease",b"lease"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["behavior_fault_id",b"behavior_fault_id","header",b"header","lease",b"lease"]) -> None: ...
global___ClearBehaviorFaultRequest = ClearBehaviorFaultRequest

class ClearBehaviorFaultResponse(google.protobuf.message.Message):
    """A ClearBehaviorFault response message has status indicating whether the service cleared
    the fault or not.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Status:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[ClearBehaviorFaultResponse._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNKNOWN: ClearBehaviorFaultResponse._Status.ValueType  # 0
        """An unknown / unexpected error occurred."""

        STATUS_CLEARED: ClearBehaviorFaultResponse._Status.ValueType  # 1
        """The BehaviorFault has been cleared."""

        STATUS_NOT_CLEARED: ClearBehaviorFaultResponse._Status.ValueType  # 2
        """The BehaviorFault could not be cleared."""

    class Status(_Status, metaclass=_StatusEnumTypeWrapper):
        pass

    STATUS_UNKNOWN: ClearBehaviorFaultResponse.Status.ValueType  # 0
    """An unknown / unexpected error occurred."""

    STATUS_CLEARED: ClearBehaviorFaultResponse.Status.ValueType  # 1
    """The BehaviorFault has been cleared."""

    STATUS_NOT_CLEARED: ClearBehaviorFaultResponse.Status.ValueType  # 2
    """The BehaviorFault could not be cleared."""


    HEADER_FIELD_NUMBER: builtins.int
    LEASE_USE_RESULT_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.ResponseHeader:
        """Common response header."""
        pass
    @property
    def lease_use_result(self) -> bosdyn.api.lease_pb2.LeaseUseResult:
        """Details about how the lease was used."""
        pass
    status: global___ClearBehaviorFaultResponse.Status.ValueType
    """Return status for a request."""

    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.ResponseHeader] = ...,
        lease_use_result: typing.Optional[bosdyn.api.lease_pb2.LeaseUseResult] = ...,
        status: global___ClearBehaviorFaultResponse.Status.ValueType = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header","lease_use_result",b"lease_use_result"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header","lease_use_result",b"lease_use_result","status",b"status"]) -> None: ...
global___ClearBehaviorFaultResponse = ClearBehaviorFaultResponse
