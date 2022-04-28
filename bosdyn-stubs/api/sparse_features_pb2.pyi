"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import bosdyn.api.geometry_pb2
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Keypoint(google.protobuf.message.Message):
    """A point of interest in an image expressed as a pixel coordinate with associated metadata."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    COORDINATES_FIELD_NUMBER: builtins.int
    BINARY_DESCRIPTOR_FIELD_NUMBER: builtins.int
    SCORE_FIELD_NUMBER: builtins.int
    SIZE_FIELD_NUMBER: builtins.int
    ANGLE_FIELD_NUMBER: builtins.int
    @property
    def coordinates(self) -> bosdyn.api.geometry_pb2.Vec2:
        """The image pixel coordinates of the keypoint."""
        pass
    binary_descriptor: builtins.bytes
    """A binary descriptor representing the keypoint."""

    score: builtins.float
    """The score of this keypoint from the underlying keypoint detector, if applicable."""

    size: builtins.float
    """The diameter in pixels of the local neighborhood used to construct the descriptor."""

    angle: builtins.float
    """The orientation of the keypoint, if applicable."""

    def __init__(self,
        *,
        coordinates: typing.Optional[bosdyn.api.geometry_pb2.Vec2] = ...,
        binary_descriptor: builtins.bytes = ...,
        score: builtins.float = ...,
        size: builtins.float = ...,
        angle: builtins.float = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["coordinates",b"coordinates"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["angle",b"angle","binary_descriptor",b"binary_descriptor","coordinates",b"coordinates","score",b"score","size",b"size"]) -> None: ...
global___Keypoint = Keypoint

class KeypointSet(google.protobuf.message.Message):
    """A set of keypoints detected in a single image."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _KeypointType:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _KeypointTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[KeypointSet._KeypointType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        KEYPOINT_UNKNOWN: KeypointSet._KeypointType.ValueType  # 0
        KEYPOINT_SIMPLE: KeypointSet._KeypointType.ValueType  # 1
        """Keypoints that consist only of image coordinates. Simple keypoints do not have
        descriptors.
        """

        KEYPOINT_ORB: KeypointSet._KeypointType.ValueType  # 2
        """Keypoints detected by the ORB feature extraction algorithm (Oriented FAST and Rotated
        BRIEF.)
        """

    class KeypointType(_KeypointType, metaclass=_KeypointTypeEnumTypeWrapper):
        pass

    KEYPOINT_UNKNOWN: KeypointSet.KeypointType.ValueType  # 0
    KEYPOINT_SIMPLE: KeypointSet.KeypointType.ValueType  # 1
    """Keypoints that consist only of image coordinates. Simple keypoints do not have
    descriptors.
    """

    KEYPOINT_ORB: KeypointSet.KeypointType.ValueType  # 2
    """Keypoints detected by the ORB feature extraction algorithm (Oriented FAST and Rotated
    BRIEF.)
    """


    KEYPOINTS_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    @property
    def keypoints(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Keypoint]:
        """A set of detected keypoints and associated metadata."""
        pass
    type: global___KeypointSet.KeypointType.ValueType
    """The algorithm used to compute this keypoint and its descriptor."""

    def __init__(self,
        *,
        keypoints: typing.Optional[typing.Iterable[global___Keypoint]] = ...,
        type: global___KeypointSet.KeypointType.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["keypoints",b"keypoints","type",b"type"]) -> None: ...
global___KeypointSet = KeypointSet

class Match(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    REFERENCE_INDEX_FIELD_NUMBER: builtins.int
    LIVE_INDEX_FIELD_NUMBER: builtins.int
    DISTANCE_FIELD_NUMBER: builtins.int
    reference_index: builtins.int
    """The index in the reference KeypointSet of the keypoint in the matching pair."""

    live_index: builtins.int
    """The index in the live KeypointSet of the keypoint in the matching pair."""

    distance: builtins.float
    """The distance in descriptor space between the two keypoints."""

    def __init__(self,
        *,
        reference_index: builtins.int = ...,
        live_index: builtins.int = ...,
        distance: builtins.float = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["distance",b"distance","live_index",b"live_index","reference_index",b"reference_index"]) -> None: ...
global___Match = Match

class KeypointMatches(google.protobuf.message.Message):
    """A pair of keypoint sets containing only features in common that have been matched."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    REFERENCE_KEYPOINTS_FIELD_NUMBER: builtins.int
    LIVE_KEYPOINTS_FIELD_NUMBER: builtins.int
    MATCHES_FIELD_NUMBER: builtins.int
    @property
    def reference_keypoints(self) -> global___KeypointSet:
        """The set of common keypoints in a first ("reference") image."""
        pass
    @property
    def live_keypoints(self) -> global___KeypointSet:
        """The set of common keypoints in a second ("live") image."""
        pass
    @property
    def matches(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Match]:
        """Indices of pairs of matches in the two KeypointSets and their distance measure."""
        pass
    def __init__(self,
        *,
        reference_keypoints: typing.Optional[global___KeypointSet] = ...,
        live_keypoints: typing.Optional[global___KeypointSet] = ...,
        matches: typing.Optional[typing.Iterable[global___Match]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["live_keypoints",b"live_keypoints","reference_keypoints",b"reference_keypoints"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["live_keypoints",b"live_keypoints","matches",b"matches","reference_keypoints",b"reference_keypoints"]) -> None: ...
global___KeypointMatches = KeypointMatches