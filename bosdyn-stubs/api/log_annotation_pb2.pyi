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

class AddLogAnnotationRequest(google.protobuf.message.Message):
    """DEPRECATED as of 2.1.0: Please use the DataBufferService instead of the LogAnnotationService.
    The AddLogAnnotation request sends the information that should be added into the log.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    ANNOTATIONS_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.RequestHeader:
        """Common request/response header."""
        pass
    @property
    def annotations(self) -> global___LogAnnotations:
        """The annotations to be aded into the log (can be text messages, blobs or robot operator messages)."""
        pass
    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.RequestHeader] = ...,
        annotations: typing.Optional[global___LogAnnotations] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["annotations",b"annotations","header",b"header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["annotations",b"annotations","header",b"header"]) -> None: ...
global___AddLogAnnotationRequest = AddLogAnnotationRequest

class LogAnnotations(google.protobuf.message.Message):
    """DEPRECATED as of 2.1.0: Please use the DataBufferService instead of the LogAnnotationService.
    A container for elements to be added to the robot's logs.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TEXT_MESSAGES_FIELD_NUMBER: builtins.int
    OPERATOR_MESSAGES_FIELD_NUMBER: builtins.int
    BLOB_DATA_FIELD_NUMBER: builtins.int
    @property
    def text_messages(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___LogAnnotationTextMessage]:
        """Text messages to be added to the log."""
        pass
    @property
    def operator_messages(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___LogAnnotationOperatorMessage]:
        """Messages from the robot operator to be added to the log."""
        pass
    @property
    def blob_data(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___LogAnnotationLogBlob]:
        """One or more binary blobs to add to the log."""
        pass
    def __init__(self,
        *,
        text_messages: typing.Optional[typing.Iterable[global___LogAnnotationTextMessage]] = ...,
        operator_messages: typing.Optional[typing.Iterable[global___LogAnnotationOperatorMessage]] = ...,
        blob_data: typing.Optional[typing.Iterable[global___LogAnnotationLogBlob]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["blob_data",b"blob_data","operator_messages",b"operator_messages","text_messages",b"text_messages"]) -> None: ...
global___LogAnnotations = LogAnnotations

class LogAnnotationTextMessage(google.protobuf.message.Message):
    """DEPRECATED as of 2.1.0: Please use the DataBufferService instead of the LogAnnotationService.
    A text message to add to the robot's logs.
    These could be internal text-log messages from a client for use in debugging, for
    example.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Level:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _LevelEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[LogAnnotationTextMessage._Level.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        LEVEL_UNKNOWN: LogAnnotationTextMessage._Level.ValueType  # 0
        """Invalid, do not use."""

        LEVEL_DEBUG: LogAnnotationTextMessage._Level.ValueType  # 1
        """Events likely of interest only in a debugging context."""

        LEVEL_INFO: LogAnnotationTextMessage._Level.ValueType  # 2
        """Informational message during normal operation."""

        LEVEL_WARN: LogAnnotationTextMessage._Level.ValueType  # 3
        """Information about an unexpected but recoverable condition."""

        LEVEL_ERROR: LogAnnotationTextMessage._Level.ValueType  # 4
        """Information about an operation which did not succeed."""

    class Level(_Level, metaclass=_LevelEnumTypeWrapper):
        pass

    LEVEL_UNKNOWN: LogAnnotationTextMessage.Level.ValueType  # 0
    """Invalid, do not use."""

    LEVEL_DEBUG: LogAnnotationTextMessage.Level.ValueType  # 1
    """Events likely of interest only in a debugging context."""

    LEVEL_INFO: LogAnnotationTextMessage.Level.ValueType  # 2
    """Informational message during normal operation."""

    LEVEL_WARN: LogAnnotationTextMessage.Level.ValueType  # 3
    """Information about an unexpected but recoverable condition."""

    LEVEL_ERROR: LogAnnotationTextMessage.Level.ValueType  # 4
    """Information about an operation which did not succeed."""


    MESSAGE_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    SERVICE_FIELD_NUMBER: builtins.int
    LEVEL_FIELD_NUMBER: builtins.int
    TAG_FIELD_NUMBER: builtins.int
    FILENAME_FIELD_NUMBER: builtins.int
    LINE_NUMBER_FIELD_NUMBER: builtins.int
    TIMESTAMP_CLIENT_FIELD_NUMBER: builtins.int
    message: typing.Text
    """String annotation message to add to the log."""

    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Required timestamp of data in robot clock time."""
        pass
    service: typing.Text
    """The service responsible for the annotation. May be omitted."""

    level: global___LogAnnotationTextMessage.Level.ValueType
    """Level of significance of the text message."""

    tag: typing.Text
    """Optional tag to identify from what code/module this message originated from."""

    filename: typing.Text
    """Optional source file name originating the log message."""

    line_number: builtins.int
    """Optional source file line number originating the log message."""

    @property
    def timestamp_client(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Optional timestamp of data in client clock time."""
        pass
    def __init__(self,
        *,
        message: typing.Text = ...,
        timestamp: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        service: typing.Text = ...,
        level: global___LogAnnotationTextMessage.Level.ValueType = ...,
        tag: typing.Text = ...,
        filename: typing.Text = ...,
        line_number: builtins.int = ...,
        timestamp_client: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["timestamp",b"timestamp","timestamp_client",b"timestamp_client"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["filename",b"filename","level",b"level","line_number",b"line_number","message",b"message","service",b"service","tag",b"tag","timestamp",b"timestamp","timestamp_client",b"timestamp_client"]) -> None: ...
global___LogAnnotationTextMessage = LogAnnotationTextMessage

class LogAnnotationOperatorMessage(google.protobuf.message.Message):
    """DEPRECATED as of 2.1.0: Please use the DataBufferService instead of the LogAnnotationService.
    An operator message to be added to the robot's logs.
    These are notes especially intended to mark when logs should be preserved and reviewed
    to ensure that robot hardware and/or software is working as intended.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MESSAGE_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    TIMESTAMP_CLIENT_FIELD_NUMBER: builtins.int
    message: typing.Text
    """String annotation message to add to the log."""

    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Required timestamp of data in robot clock time."""
        pass
    @property
    def timestamp_client(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Optional timestamp of data in client clock time."""
        pass
    def __init__(self,
        *,
        message: typing.Text = ...,
        timestamp: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        timestamp_client: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["timestamp",b"timestamp","timestamp_client",b"timestamp_client"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["message",b"message","timestamp",b"timestamp","timestamp_client",b"timestamp_client"]) -> None: ...
global___LogAnnotationOperatorMessage = LogAnnotationOperatorMessage

class LogAnnotationLogBlob(google.protobuf.message.Message):
    """DEPRECATED as of 2.1.0: Please use the DataBufferService instead of the LogAnnotationService.
    A unit of binary data to be entered in a log.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TIMESTAMP_FIELD_NUMBER: builtins.int
    CHANNEL_FIELD_NUMBER: builtins.int
    TYPE_ID_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    TIMESTAMP_CLIENT_FIELD_NUMBER: builtins.int
    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Required timestamp of data in robot clock time."""
        pass
    channel: typing.Text
    """A general label for this blob.
    This is distinct from type_id, which identifies how the blob is to be parsed.
    """

    type_id: typing.Text
    """A description of the data's content and its encoding.
    This should be sufficient for deciding how to deserialize the data.
    For example, this could be the full name of a protobuf message type.
    """

    data: builtins.bytes
    """Raw data to be included as the blob log."""

    @property
    def timestamp_client(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Optional timestamp of data in client clock time."""
        pass
    def __init__(self,
        *,
        timestamp: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        channel: typing.Text = ...,
        type_id: typing.Text = ...,
        data: builtins.bytes = ...,
        timestamp_client: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["timestamp",b"timestamp","timestamp_client",b"timestamp_client"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["channel",b"channel","data",b"data","timestamp",b"timestamp","timestamp_client",b"timestamp_client","type_id",b"type_id"]) -> None: ...
global___LogAnnotationLogBlob = LogAnnotationLogBlob

class AddLogAnnotationResponse(google.protobuf.message.Message):
    """DEPRECATED as of 2.1.0: Please use the DataBufferService instead of the LogAnnotationService.
    The AddLogAnnotation response message, which is empty except for any potential header errors/warnings.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.ResponseHeader:
        """Common request/response header."""
        pass
    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.ResponseHeader] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header"]) -> None: ...
global___AddLogAnnotationResponse = AddLogAnnotationResponse