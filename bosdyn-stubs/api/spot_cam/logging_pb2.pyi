"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import bosdyn.api.data_chunk_pb2
import bosdyn.api.geometry_pb2
import bosdyn.api.header_pb2
import bosdyn.api.image_pb2
import bosdyn.api.spot_cam.camera_pb2
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Logpoint(google.protobuf.message.Message):
    """A representation of a stored data acquisition."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _RecordType:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _RecordTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Logpoint._RecordType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STILLIMAGE: Logpoint._RecordType.ValueType  # 0
    class RecordType(_RecordType, metaclass=_RecordTypeEnumTypeWrapper):
        """Possible types of media that can be stored."""
        pass

    STILLIMAGE: Logpoint.RecordType.ValueType  # 0

    class _LogStatus:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _LogStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Logpoint._LogStatus.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        FAILED: Logpoint._LogStatus.ValueType  # 0
        QUEUED: Logpoint._LogStatus.ValueType  # 1
        """the logpoint has been queued to be downloaded from the renderer"""

        COMPLETE: Logpoint._LogStatus.ValueType  # 2
        """the logpoint is written to the disk"""

        UNKNOWN: Logpoint._LogStatus.ValueType  # -1
    class LogStatus(_LogStatus, metaclass=_LogStatusEnumTypeWrapper):
        """Possible stages of data acquisition."""
        pass

    FAILED: Logpoint.LogStatus.ValueType  # 0
    QUEUED: Logpoint.LogStatus.ValueType  # 1
    """the logpoint has been queued to be downloaded from the renderer"""

    COMPLETE: Logpoint.LogStatus.ValueType  # 2
    """the logpoint is written to the disk"""

    UNKNOWN: Logpoint.LogStatus.ValueType  # -1

    class _QueueStatus:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _QueueStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Logpoint._QueueStatus.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        QUEUED_UNKNOWN: Logpoint._QueueStatus.ValueType  # 0
        QUEUED_RENDER: Logpoint._QueueStatus.ValueType  # 1
        """The logpoint has been queued to be downloaded from the renderer"""

        QUEUED_DISK: Logpoint._QueueStatus.ValueType  # 2
        """The logpoint is in general ram, and will be written to the disk when resources allow"""

    class QueueStatus(_QueueStatus, metaclass=_QueueStatusEnumTypeWrapper):
        pass

    QUEUED_UNKNOWN: Logpoint.QueueStatus.ValueType  # 0
    QUEUED_RENDER: Logpoint.QueueStatus.ValueType  # 1
    """The logpoint has been queued to be downloaded from the renderer"""

    QUEUED_DISK: Logpoint.QueueStatus.ValueType  # 2
    """The logpoint is in general ram, and will be written to the disk when resources allow"""


    class ImageParams(google.protobuf.message.Message):
        """Description of image format."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        WIDTH_FIELD_NUMBER: builtins.int
        HEIGHT_FIELD_NUMBER: builtins.int
        FORMAT_FIELD_NUMBER: builtins.int
        width: builtins.int
        height: builtins.int
        format: bosdyn.api.image_pb2.Image.PixelFormat.ValueType
        def __init__(self,
            *,
            width: builtins.int = ...,
            height: builtins.int = ...,
            format: bosdyn.api.image_pb2.Image.PixelFormat.ValueType = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["format",b"format","height",b"height","width",b"width"]) -> None: ...

    class Calibration(google.protobuf.message.Message):
        """Data describing the camera intrinsics and extrinsics for a window of the image."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        XOFFSET_FIELD_NUMBER: builtins.int
        YOFFSET_FIELD_NUMBER: builtins.int
        WIDTH_FIELD_NUMBER: builtins.int
        HEIGHT_FIELD_NUMBER: builtins.int
        BASE_FRAME_NAME_FIELD_NUMBER: builtins.int
        BASE_TFROM_SENSOR_FIELD_NUMBER: builtins.int
        BASE_TFORM_SENSOR_FIELD_NUMBER: builtins.int
        INTRINSICS_FIELD_NUMBER: builtins.int
        xoffset: builtins.int
        yoffset: builtins.int
        width: builtins.int
        height: builtins.int
        base_frame_name: typing.Text
        @property
        def base_tfrom_sensor(self) -> bosdyn.api.geometry_pb2.SE3Pose:
            """'base_tfrom_sensor' defines the transform from the specific camera to the named base from.
            This is deprecated in favor of 'base_tform_sensor' which follows the intended naming convention
            and FrameTree directionality convention of the Spot system as defined in geometry.proto.
            """
            pass
        @property
        def base_tform_sensor(self) -> bosdyn.api.geometry_pb2.SE3Pose:
            """The transform from the named base frame to this specific camera"""
            pass
        @property
        def intrinsics(self) -> bosdyn.api.spot_cam.camera_pb2.Camera.PinholeIntrinsics: ...
        def __init__(self,
            *,
            xoffset: builtins.int = ...,
            yoffset: builtins.int = ...,
            width: builtins.int = ...,
            height: builtins.int = ...,
            base_frame_name: typing.Text = ...,
            base_tfrom_sensor: typing.Optional[bosdyn.api.geometry_pb2.SE3Pose] = ...,
            base_tform_sensor: typing.Optional[bosdyn.api.geometry_pb2.SE3Pose] = ...,
            intrinsics: typing.Optional[bosdyn.api.spot_cam.camera_pb2.Camera.PinholeIntrinsics] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["base_tform_sensor",b"base_tform_sensor","base_tfrom_sensor",b"base_tfrom_sensor","intrinsics",b"intrinsics"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["base_frame_name",b"base_frame_name","base_tform_sensor",b"base_tform_sensor","base_tfrom_sensor",b"base_tfrom_sensor","height",b"height","intrinsics",b"intrinsics","width",b"width","xoffset",b"xoffset","yoffset",b"yoffset"]) -> None: ...

    NAME_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    QUEUE_STATUS_FIELD_NUMBER: builtins.int
    TAG_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    IMAGE_PARAMS_FIELD_NUMBER: builtins.int
    CALIBRATION_FIELD_NUMBER: builtins.int
    name: typing.Text
    """Unique identifier for a data acquisition event."""

    type: global___Logpoint.RecordType.ValueType
    """Type of data held in this log point."""

    status: global___Logpoint.LogStatus.ValueType
    """Current stage of acquisition."""

    queue_status: global___Logpoint.QueueStatus.ValueType
    """Only filled out when status == QUEUED"""

    tag: typing.Text
    """An arbitrary string to be stored with the log data."""

    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time of acquisition."""
        pass
    @property
    def image_params(self) -> global___Logpoint.ImageParams:
        """Image format of the stored data."""
        pass
    @property
    def calibration(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Logpoint.Calibration]:
        """Camera data for all sub-images contained within the image data."""
        pass
    def __init__(self,
        *,
        name: typing.Text = ...,
        type: global___Logpoint.RecordType.ValueType = ...,
        status: global___Logpoint.LogStatus.ValueType = ...,
        queue_status: global___Logpoint.QueueStatus.ValueType = ...,
        tag: typing.Text = ...,
        timestamp: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        image_params: typing.Optional[global___Logpoint.ImageParams] = ...,
        calibration: typing.Optional[typing.Iterable[global___Logpoint.Calibration]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["image_params",b"image_params","timestamp",b"timestamp"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["calibration",b"calibration","image_params",b"image_params","name",b"name","queue_status",b"queue_status","status",b"status","tag",b"tag","timestamp",b"timestamp","type",b"type"]) -> None: ...
global___Logpoint = Logpoint

class DeleteRequest(google.protobuf.message.Message):
    """Delete a log point from the store."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    POINT_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.RequestHeader:
        """Common request header."""
        pass
    @property
    def point(self) -> global___Logpoint:
        """Log point to delete.  Only the name is used."""
        pass
    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.RequestHeader] = ...,
        point: typing.Optional[global___Logpoint] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header","point",b"point"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header","point",b"point"]) -> None: ...
global___DeleteRequest = DeleteRequest

class DeleteResponse(google.protobuf.message.Message):
    """Response to a deletion with any errors that occurred."""
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
global___DeleteResponse = DeleteResponse

class GetStatusRequest(google.protobuf.message.Message):
    """Request for status about the current stage of data acquisition."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    POINT_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.RequestHeader:
        """Common request header."""
        pass
    @property
    def point(self) -> global___Logpoint:
        """Log point to query.  Only the name is used."""
        pass
    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.RequestHeader] = ...,
        point: typing.Optional[global___Logpoint] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header","point",b"point"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header","point",b"point"]) -> None: ...
global___GetStatusRequest = GetStatusRequest

class GetStatusResponse(google.protobuf.message.Message):
    """Provide an update on the stage of data acquisition."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    POINT_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.ResponseHeader:
        """Common response header."""
        pass
    @property
    def point(self) -> global___Logpoint:
        """The logpoint returned here can be used to add a tag to the Logpoint later"""
        pass
    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.ResponseHeader] = ...,
        point: typing.Optional[global___Logpoint] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header","point",b"point"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header","point",b"point"]) -> None: ...
global___GetStatusResponse = GetStatusResponse

class RetrieveRequest(google.protobuf.message.Message):
    """Retrieve the binary data associated with a log point."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    POINT_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.RequestHeader:
        """Common request header."""
        pass
    @property
    def point(self) -> global___Logpoint:
        """Log point to retrieve.  Only the name is used."""
        pass
    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.RequestHeader] = ...,
        point: typing.Optional[global___Logpoint] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header","point",b"point"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header","point",b"point"]) -> None: ...
global___RetrieveRequest = RetrieveRequest

class RetrieveResponse(google.protobuf.message.Message):
    """Provide the data stored at a log point.
    Store() dictates what processing happens in this response.
    c0 -> c4 will return the raw (rgb24) fisheye image of the camera at that index.
    Storing a panorama will process the data into a stitched image.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    LOGPOINT_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.ResponseHeader:
        """Common response header."""
        pass
    @property
    def logpoint(self) -> global___Logpoint:
        """Log point retrieved."""
        pass
    @property
    def data(self) -> bosdyn.api.data_chunk_pb2.DataChunk:
        """Data chunk bytes field should be concatenated together to recover the binary data."""
        pass
    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.ResponseHeader] = ...,
        logpoint: typing.Optional[global___Logpoint] = ...,
        data: typing.Optional[bosdyn.api.data_chunk_pb2.DataChunk] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["data",b"data","header",b"header","logpoint",b"logpoint"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["data",b"data","header",b"header","logpoint",b"logpoint"]) -> None: ...
global___RetrieveResponse = RetrieveResponse

class RetrieveRawDataRequest(google.protobuf.message.Message):
    """Retrieve the binary data associated with a log point, with no processing applied.
    Storing a panorama will retrieve tiled individual images.
    For IR, the temperature at each pixel is 0.1 * the int value in Kelvin.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    POINT_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.RequestHeader:
        """Common request header."""
        pass
    @property
    def point(self) -> global___Logpoint:
        """Log point to retrieve.  Only the name is used."""
        pass
    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.RequestHeader] = ...,
        point: typing.Optional[global___Logpoint] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header","point",b"point"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header","point",b"point"]) -> None: ...
global___RetrieveRawDataRequest = RetrieveRawDataRequest

class RetrieveRawDataResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    LOGPOINT_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.ResponseHeader:
        """Common response header."""
        pass
    @property
    def logpoint(self) -> global___Logpoint:
        """Log point retrieved."""
        pass
    @property
    def data(self) -> bosdyn.api.data_chunk_pb2.DataChunk:
        """Data chunk bytes field should be concatenated together to recover the binary data."""
        pass
    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.ResponseHeader] = ...,
        logpoint: typing.Optional[global___Logpoint] = ...,
        data: typing.Optional[bosdyn.api.data_chunk_pb2.DataChunk] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["data",b"data","header",b"header","logpoint",b"logpoint"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["data",b"data","header",b"header","logpoint",b"logpoint"]) -> None: ...
global___RetrieveRawDataResponse = RetrieveRawDataResponse

class StoreRequest(google.protobuf.message.Message):
    """Trigger a data acquisition."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    CAMERA_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    TAG_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.RequestHeader:
        """Common request header."""
        pass
    @property
    def camera(self) -> bosdyn.api.spot_cam.camera_pb2.Camera:
        """Which camera to capture."""
        pass
    type: global___Logpoint.RecordType.ValueType
    """Type of data capture to perform."""

    tag: typing.Text
    """Metadata to associate with the store."""

    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.RequestHeader] = ...,
        camera: typing.Optional[bosdyn.api.spot_cam.camera_pb2.Camera] = ...,
        type: global___Logpoint.RecordType.ValueType = ...,
        tag: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["camera",b"camera","header",b"header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["camera",b"camera","header",b"header","tag",b"tag","type",b"type"]) -> None: ...
global___StoreRequest = StoreRequest

class StoreResponse(google.protobuf.message.Message):
    """Result of data acquisition trigger."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    POINT_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.ResponseHeader:
        """Common response header."""
        pass
    @property
    def point(self) -> global___Logpoint:
        """The log point returned here can be used to add a tag to the Logpoint later
        It will very likely be in th 'QUEUED' state.
        """
        pass
    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.ResponseHeader] = ...,
        point: typing.Optional[global___Logpoint] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header","point",b"point"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header","point",b"point"]) -> None: ...
global___StoreResponse = StoreResponse

class TagRequest(google.protobuf.message.Message):
    """Add tag metadata to an existing log point."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    POINT_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.RequestHeader:
        """Common request header."""
        pass
    @property
    def point(self) -> global___Logpoint:
        """Logpoint to add metadata to. Name and tag are used."""
        pass
    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.RequestHeader] = ...,
        point: typing.Optional[global___Logpoint] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header","point",b"point"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header","point",b"point"]) -> None: ...
global___TagRequest = TagRequest

class TagResponse(google.protobuf.message.Message):
    """Result of adding tag metadata to a log point."""
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
global___TagResponse = TagResponse

class ListCamerasRequest(google.protobuf.message.Message):
    """Request the available cameras."""
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
global___ListCamerasRequest = ListCamerasRequest

class ListCamerasResponse(google.protobuf.message.Message):
    """Provide the list of available cameras."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    CAMERAS_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.ResponseHeader:
        """Common response header."""
        pass
    @property
    def cameras(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[bosdyn.api.spot_cam.camera_pb2.Camera]:
        """List of all cameras which can be used in a StoreRequest."""
        pass
    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.ResponseHeader] = ...,
        cameras: typing.Optional[typing.Iterable[bosdyn.api.spot_cam.camera_pb2.Camera]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cameras",b"cameras","header",b"header"]) -> None: ...
global___ListCamerasResponse = ListCamerasResponse

class ListLogpointsRequest(google.protobuf.message.Message):
    """List all available log points, whether they have completed or not."""
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
global___ListLogpointsRequest = ListLogpointsRequest

class ListLogpointsResponse(google.protobuf.message.Message):
    """Provide all log points in the system."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    LOGPOINTS_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.ResponseHeader:
        """Common response header."""
        pass
    @property
    def logpoints(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Logpoint]:
        """List of all the individual log points concatenated into a list.
        This stream may take a long time to complete if there are a lot of stored images.
        """
        pass
    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.ResponseHeader] = ...,
        logpoints: typing.Optional[typing.Iterable[global___Logpoint]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header","logpoints",b"logpoints"]) -> None: ...
global___ListLogpointsResponse = ListLogpointsResponse

class SetPassphraseRequest(google.protobuf.message.Message):
    """Set encryption for the disk."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    PASSPHRASE_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.RequestHeader:
        """Common request header."""
        pass
    passphrase: typing.Text
    """A passphrase is a human-readable string used to generate
    an encryption key. An empty passphrase disables encryption.

    If the encryption key is set, everything new written to the drive gets encrypted. this includes

    1) the sql database
    2) logged data
    3) audio files uploaded with the Audio service
    4) probably other stuff that I haven't thought of

    If it's called repeatedly (with different keys), old data will
    still be on the disk, but unreadable, so new data will be
    written with the new key. the only exception is this; when
    encryption is off and a key is written, the sql database gets
    encrypted with the new key; old log and audio data remains
    unencrypted however.

    After setting the passphrase, please reboot the system to
    remount the encrypted filesystem layer.
    """

    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.RequestHeader] = ...,
        passphrase: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header","passphrase",b"passphrase"]) -> None: ...
global___SetPassphraseRequest = SetPassphraseRequest

class SetPassphraseResponse(google.protobuf.message.Message):
    """Response from setting the disk encryption.
    After setting the passphrase, please reboot the system to
    remount the encrypted filesystem layer.
    """
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
global___SetPassphraseResponse = SetPassphraseResponse

class DebugRequest(google.protobuf.message.Message):
    """Change debug logging settings on the SpotCam."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    ENABLE_TEMPERATURE_FIELD_NUMBER: builtins.int
    ENABLE_HUMIDITY_FIELD_NUMBER: builtins.int
    ENABLE_BIT_FIELD_NUMBER: builtins.int
    ENABLE_SHOCK_FIELD_NUMBER: builtins.int
    ENABLE_SYSTEM_STAT_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.RequestHeader:
        """Common request header."""
        pass
    enable_temperature: builtins.bool
    """Set true to enable logging of temperature data;"""

    enable_humidity: builtins.bool
    """Set true to enable logging of humidity data;"""

    enable_BIT: builtins.bool
    """Set true to enable logging of BIT events;
    BIT events are always recorded to volatile memory
    and can be viewed (and cleared) with the Health service,
    but this enables writing them to disk.
    """

    enable_shock: builtins.bool
    """Set true to enable logging of Shock data;
    this is on by default.
    """

    enable_system_stat: builtins.bool
    """Set to true to enable logging of system load stats
    cpu, gpu, memory, and network utilization
    Nowow a BIT, set true to enable logging of led driver status.
    bool enable_led_stat = 7;
    """

    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.RequestHeader] = ...,
        enable_temperature: builtins.bool = ...,
        enable_humidity: builtins.bool = ...,
        enable_BIT: builtins.bool = ...,
        enable_shock: builtins.bool = ...,
        enable_system_stat: builtins.bool = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["enable_BIT",b"enable_BIT","enable_humidity",b"enable_humidity","enable_shock",b"enable_shock","enable_system_stat",b"enable_system_stat","enable_temperature",b"enable_temperature","header",b"header"]) -> None: ...
global___DebugRequest = DebugRequest

class DebugResponse(google.protobuf.message.Message):
    """Response with any errors for debug setting changes."""
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
global___DebugResponse = DebugResponse
