"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import bosdyn.api.docking.docking_pb2
import bosdyn.api.geometry_pb2
import bosdyn.api.header_pb2
import bosdyn.api.image_pb2
import bosdyn.api.sparse_features_pb2
import builtins
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _WorldObjectType:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _WorldObjectTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_WorldObjectType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    WORLD_OBJECT_UNKNOWN: _WorldObjectType.ValueType  # 0
    WORLD_OBJECT_DRAWABLE: _WorldObjectType.ValueType  # 1
    WORLD_OBJECT_APRILTAG: _WorldObjectType.ValueType  # 2
    WORLD_OBJECT_IMAGE_COORDINATES: _WorldObjectType.ValueType  # 5
    WORLD_OBJECT_DOCK: _WorldObjectType.ValueType  # 6
class WorldObjectType(_WorldObjectType, metaclass=_WorldObjectTypeEnumTypeWrapper):
    """A type for the world object, which is associated with whatever properties the world object includes. This can
    be used to request specific kinds of objects; for example, a request for only fiducials.
    """
    pass

WORLD_OBJECT_UNKNOWN: WorldObjectType.ValueType  # 0
WORLD_OBJECT_DRAWABLE: WorldObjectType.ValueType  # 1
WORLD_OBJECT_APRILTAG: WorldObjectType.ValueType  # 2
WORLD_OBJECT_IMAGE_COORDINATES: WorldObjectType.ValueType  # 5
WORLD_OBJECT_DOCK: WorldObjectType.ValueType  # 6
global___WorldObjectType = WorldObjectType


class WorldObject(google.protobuf.message.Message):
    """The world object message is used to describe different objects seen by a robot. It contains information
    about the properties of the object in addition to a unique id and the transform snapshot.
    The world object uses "properties" to describe different traits about the object, such as image coordinates
    associated with the camera the object was detected in. A world object can have multiple different properties
    that are all associated with the single object.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    ACQUISITION_TIME_FIELD_NUMBER: builtins.int
    TRANSFORMS_SNAPSHOT_FIELD_NUMBER: builtins.int
    DRAWABLE_PROPERTIES_FIELD_NUMBER: builtins.int
    APRILTAG_PROPERTIES_FIELD_NUMBER: builtins.int
    IMAGE_PROPERTIES_FIELD_NUMBER: builtins.int
    DOCK_PROPERTIES_FIELD_NUMBER: builtins.int
    RAY_PROPERTIES_FIELD_NUMBER: builtins.int
    BOUNDING_BOX_PROPERTIES_FIELD_NUMBER: builtins.int
    ADDITIONAL_PROPERTIES_FIELD_NUMBER: builtins.int
    id: builtins.int
    """Unique integer identifier that will be consistent for the duration of a robot's battery life
    The id is set internally by the world object service.
    """

    name: typing.Text
    """A human readable name for the world object. Note that this differs from any frame_name's associated
    with the object (since there can be multiple frames describing a single object).
    """

    @property
    def acquisition_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time in robot time clock at which this object was most recently detected and valid."""
        pass
    @property
    def transforms_snapshot(self) -> bosdyn.api.geometry_pb2.FrameTreeSnapshot:
        """A tree-based collection of transformations, which will include the transformations to each
        of the returned world objects in addition to transformations to the common frames ("vision",
        "body", "odom"). All transforms within the snapshot are at the acquisition time of the world object.
        Note that each object's frame names are defined within the properties submessage. For example,
        the apriltag frame name is defined in the AprilTagProperties message as "frame_name_fiducial"
        """
        pass
    @property
    def drawable_properties(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DrawableProperties]:
        """The drawable properties describe geometric shapes associated with an object."""
        pass
    @property
    def apriltag_properties(self) -> global___AprilTagProperties:
        """The apriltag properties describe any fiducial identifying an object."""
        pass
    @property
    def image_properties(self) -> global___ImageProperties:
        """The image properties describe any camera and image coordinates associated with an object."""
        pass
    @property
    def dock_properties(self) -> global___DockProperties:
        """Properties describing a dock"""
        pass
    @property
    def ray_properties(self) -> global___RayProperties:
        """A ray pointing at the object.  Useful in cases where position is unknown but direction is
        known.
        """
        pass
    @property
    def bounding_box_properties(self) -> global___BoundingBoxProperties:
        """Bounding box in the world, oriented at the location provided in the transforms_snapshot."""
        pass
    @property
    def additional_properties(self) -> google.protobuf.any_pb2.Any:
        """An extra field for application-specific object properties."""
        pass
    def __init__(self,
        *,
        id: builtins.int = ...,
        name: typing.Text = ...,
        acquisition_time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        transforms_snapshot: typing.Optional[bosdyn.api.geometry_pb2.FrameTreeSnapshot] = ...,
        drawable_properties: typing.Optional[typing.Iterable[global___DrawableProperties]] = ...,
        apriltag_properties: typing.Optional[global___AprilTagProperties] = ...,
        image_properties: typing.Optional[global___ImageProperties] = ...,
        dock_properties: typing.Optional[global___DockProperties] = ...,
        ray_properties: typing.Optional[global___RayProperties] = ...,
        bounding_box_properties: typing.Optional[global___BoundingBoxProperties] = ...,
        additional_properties: typing.Optional[google.protobuf.any_pb2.Any] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["acquisition_time",b"acquisition_time","additional_properties",b"additional_properties","apriltag_properties",b"apriltag_properties","bounding_box_properties",b"bounding_box_properties","dock_properties",b"dock_properties","image_properties",b"image_properties","ray_properties",b"ray_properties","transforms_snapshot",b"transforms_snapshot"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["acquisition_time",b"acquisition_time","additional_properties",b"additional_properties","apriltag_properties",b"apriltag_properties","bounding_box_properties",b"bounding_box_properties","dock_properties",b"dock_properties","drawable_properties",b"drawable_properties","id",b"id","image_properties",b"image_properties","name",b"name","ray_properties",b"ray_properties","transforms_snapshot",b"transforms_snapshot"]) -> None: ...
global___WorldObject = WorldObject

class ListWorldObjectRequest(google.protobuf.message.Message):
    """The ListWorldObject request message, which can optionally include filters for the object type or timestamp."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    OBJECT_TYPE_FIELD_NUMBER: builtins.int
    TIMESTAMP_FILTER_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.RequestHeader:
        """Common request header"""
        pass
    @property
    def object_type(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[global___WorldObjectType.ValueType]:
        """Optional filters to apply to the world object request
        Specific type of object; can request multiple different properties
        """
        pass
    @property
    def timestamp_filter(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Timestamp to filter objects based on. The time should be in robot time
        All objects with header timestamps after (>) timestamp_filter will be returned
        """
        pass
    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.RequestHeader] = ...,
        object_type: typing.Optional[typing.Iterable[global___WorldObjectType.ValueType]] = ...,
        timestamp_filter: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header","timestamp_filter",b"timestamp_filter"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header","object_type",b"object_type","timestamp_filter",b"timestamp_filter"]) -> None: ...
global___ListWorldObjectRequest = ListWorldObjectRequest

class ListWorldObjectResponse(google.protobuf.message.Message):
    """The ListWorldObject response message, which contains all of the current world objects in the
    robot's perception scene.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    WORLD_OBJECTS_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.ResponseHeader:
        """Common response header"""
        pass
    @property
    def world_objects(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___WorldObject]:
        """The currently perceived world objects."""
        pass
    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.ResponseHeader] = ...,
        world_objects: typing.Optional[typing.Iterable[global___WorldObject]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header","world_objects",b"world_objects"]) -> None: ...
global___ListWorldObjectResponse = ListWorldObjectResponse

class MutateWorldObjectRequest(google.protobuf.message.Message):
    """The MutateWorldObject request message, which specifies the type of mutation and which object
    the mutation should be applied to.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Action:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _ActionEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[MutateWorldObjectRequest._Action.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        ACTION_UNKNOWN: MutateWorldObjectRequest._Action.ValueType  # 0
        """Invalid action."""

        ACTION_ADD: MutateWorldObjectRequest._Action.ValueType  # 1
        """Add a new object."""

        ACTION_CHANGE: MutateWorldObjectRequest._Action.ValueType  # 2
        """Change an existing objected (ID'd by integer ID number). This is
        only allowed to change objects added by the API-user, and not
        objects detected by Spot's perception system.
        """

        ACTION_DELETE: MutateWorldObjectRequest._Action.ValueType  # 3
        """Delete the object, ID'd by integer ID number. This is
        only allowed to change objects added by the API-user, and not
        objects detected by Spot's perception system.
        """

    class Action(_Action, metaclass=_ActionEnumTypeWrapper):
        pass

    ACTION_UNKNOWN: MutateWorldObjectRequest.Action.ValueType  # 0
    """Invalid action."""

    ACTION_ADD: MutateWorldObjectRequest.Action.ValueType  # 1
    """Add a new object."""

    ACTION_CHANGE: MutateWorldObjectRequest.Action.ValueType  # 2
    """Change an existing objected (ID'd by integer ID number). This is
    only allowed to change objects added by the API-user, and not
    objects detected by Spot's perception system.
    """

    ACTION_DELETE: MutateWorldObjectRequest.Action.ValueType  # 3
    """Delete the object, ID'd by integer ID number. This is
    only allowed to change objects added by the API-user, and not
    objects detected by Spot's perception system.
    """


    class Mutation(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        ACTION_FIELD_NUMBER: builtins.int
        OBJECT_FIELD_NUMBER: builtins.int
        action: global___MutateWorldObjectRequest.Action.ValueType
        """The action (add, change, or delete) to be applied to a world object."""

        @property
        def object(self) -> global___WorldObject:
            """World object to be mutated.
            If an object is being changed/deleted, then the world object id must match a world
            object id known by the service.
            """
            pass
        def __init__(self,
            *,
            action: global___MutateWorldObjectRequest.Action.ValueType = ...,
            object: typing.Optional[global___WorldObject] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["object",b"object"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["action",b"action","object",b"object"]) -> None: ...

    HEADER_FIELD_NUMBER: builtins.int
    MUTATION_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.RequestHeader:
        """Common request header"""
        pass
    @property
    def mutation(self) -> global___MutateWorldObjectRequest.Mutation:
        """The mutation for this request."""
        pass
    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.RequestHeader] = ...,
        mutation: typing.Optional[global___MutateWorldObjectRequest.Mutation] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header","mutation",b"mutation"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header","mutation",b"mutation"]) -> None: ...
global___MutateWorldObjectRequest = MutateWorldObjectRequest

class MutateWorldObjectResponse(google.protobuf.message.Message):
    """The MutateWorldObject response message, which includes the world object id for the object that
    the mutation was applied to if the request succeeds.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Status:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[MutateWorldObjectResponse._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNKNOWN: MutateWorldObjectResponse._Status.ValueType  # 0
        """Status of request is unknown. Check the status code of the response header."""

        STATUS_OK: MutateWorldObjectResponse._Status.ValueType  # 1
        """Request was accepted; GetObjectListResponse must still be checked to verify the changes."""

        STATUS_INVALID_MUTATION_ID: MutateWorldObjectResponse._Status.ValueType  # 2
        """The mutation object's ID is unknown such that the service could not recognize this object.
        This error applies to the CHANGE and DELETE actions, since it must identify the object by
        it's id number given by the service.
        """

        STATUS_NO_PERMISSION: MutateWorldObjectResponse._Status.ValueType  # 3
        """The mutation request is not allowed because it is attempting to change or delete an object
        detected by Spot's perception system.
        """

    class Status(_Status, metaclass=_StatusEnumTypeWrapper):
        pass

    STATUS_UNKNOWN: MutateWorldObjectResponse.Status.ValueType  # 0
    """Status of request is unknown. Check the status code of the response header."""

    STATUS_OK: MutateWorldObjectResponse.Status.ValueType  # 1
    """Request was accepted; GetObjectListResponse must still be checked to verify the changes."""

    STATUS_INVALID_MUTATION_ID: MutateWorldObjectResponse.Status.ValueType  # 2
    """The mutation object's ID is unknown such that the service could not recognize this object.
    This error applies to the CHANGE and DELETE actions, since it must identify the object by
    it's id number given by the service.
    """

    STATUS_NO_PERMISSION: MutateWorldObjectResponse.Status.ValueType  # 3
    """The mutation request is not allowed because it is attempting to change or delete an object
    detected by Spot's perception system.
    """


    HEADER_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    MUTATED_OBJECT_ID_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.ResponseHeader:
        """Common response header"""
        pass
    status: global___MutateWorldObjectResponse.Status.ValueType
    """Return status for the request."""

    mutated_object_id: builtins.int
    """ID set by the world object service for the mutated object"""

    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.ResponseHeader] = ...,
        status: global___MutateWorldObjectResponse.Status.ValueType = ...,
        mutated_object_id: builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header","mutated_object_id",b"mutated_object_id","status",b"status"]) -> None: ...
global___MutateWorldObjectResponse = MutateWorldObjectResponse

class ImageProperties(google.protobuf.message.Message):
    """ World object properties describing image coordinates associated with an object or scene."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CAMERA_SOURCE_FIELD_NUMBER: builtins.int
    COORDINATES_FIELD_NUMBER: builtins.int
    KEYPOINTS_FIELD_NUMBER: builtins.int
    IMAGE_SOURCE_FIELD_NUMBER: builtins.int
    IMAGE_CAPTURE_FIELD_NUMBER: builtins.int
    FRAME_NAME_IMAGE_COORDINATES_FIELD_NUMBER: builtins.int
    camera_source: typing.Text
    """Camera Source of such as "back", "frontleft", etc."""

    @property
    def coordinates(self) -> bosdyn.api.geometry_pb2.Polygon:
        """Image coordinates of the corners of a polygon (pixels of x[row], y[col]) in either
        clockwise/counter clockwise order
        """
        pass
    @property
    def keypoints(self) -> bosdyn.api.sparse_features_pb2.KeypointSet:
        """A set of keypoints and their associated metadata."""
        pass
    @property
    def image_source(self) -> bosdyn.api.image_pb2.ImageSource:
        """Camera parameters."""
        pass
    @property
    def image_capture(self) -> bosdyn.api.image_pb2.ImageCapture:
        """Image that produced the data."""
        pass
    frame_name_image_coordinates: typing.Text
    """Frame name for the object described by image coordinates."""

    def __init__(self,
        *,
        camera_source: typing.Text = ...,
        coordinates: typing.Optional[bosdyn.api.geometry_pb2.Polygon] = ...,
        keypoints: typing.Optional[bosdyn.api.sparse_features_pb2.KeypointSet] = ...,
        image_source: typing.Optional[bosdyn.api.image_pb2.ImageSource] = ...,
        image_capture: typing.Optional[bosdyn.api.image_pb2.ImageCapture] = ...,
        frame_name_image_coordinates: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["coordinates",b"coordinates","image_capture",b"image_capture","image_data",b"image_data","image_source",b"image_source","keypoints",b"keypoints"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["camera_source",b"camera_source","coordinates",b"coordinates","frame_name_image_coordinates",b"frame_name_image_coordinates","image_capture",b"image_capture","image_data",b"image_data","image_source",b"image_source","keypoints",b"keypoints"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["image_data",b"image_data"]) -> typing.Optional[typing_extensions.Literal["coordinates","keypoints"]]: ...
global___ImageProperties = ImageProperties

class DockProperties(google.protobuf.message.Message):
    """World object properties describing a dock"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DOCK_ID_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    FRAME_NAME_DOCK_FIELD_NUMBER: builtins.int
    UNAVAILABLE_FIELD_NUMBER: builtins.int
    dock_id: builtins.int
    """Consistent id associated with a given dock."""

    type: bosdyn.api.docking.docking_pb2.DockType.ValueType
    """Type of dock."""

    frame_name_dock: typing.Text
    """The frame name for the location of dock origin. This will be included in the transform snapshot."""

    unavailable: builtins.bool
    """Availability if the dock can be used"""

    def __init__(self,
        *,
        dock_id: builtins.int = ...,
        type: bosdyn.api.docking.docking_pb2.DockType.ValueType = ...,
        frame_name_dock: typing.Text = ...,
        unavailable: builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["dock_id",b"dock_id","frame_name_dock",b"frame_name_dock","type",b"type","unavailable",b"unavailable"]) -> None: ...
global___DockProperties = DockProperties

class AprilTagProperties(google.protobuf.message.Message):
    """ World object properties describing a fiducial object."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _AprilTagPoseStatus:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _AprilTagPoseStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[AprilTagProperties._AprilTagPoseStatus.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNKNOWN: AprilTagProperties._AprilTagPoseStatus.ValueType  # 0
        STATUS_OK: AprilTagProperties._AprilTagPoseStatus.ValueType  # 1
        """No known issues with the pose estimate."""

        STATUS_AMBIGUOUS: AprilTagProperties._AprilTagPoseStatus.ValueType  # 2
        """The orientation of the tag is ambiguous."""

        STATUS_HIGH_ERROR: AprilTagProperties._AprilTagPoseStatus.ValueType  # 3
        """The pose may be unreliable due to high reprojection error."""

    class AprilTagPoseStatus(_AprilTagPoseStatus, metaclass=_AprilTagPoseStatusEnumTypeWrapper):
        pass

    STATUS_UNKNOWN: AprilTagProperties.AprilTagPoseStatus.ValueType  # 0
    STATUS_OK: AprilTagProperties.AprilTagPoseStatus.ValueType  # 1
    """No known issues with the pose estimate."""

    STATUS_AMBIGUOUS: AprilTagProperties.AprilTagPoseStatus.ValueType  # 2
    """The orientation of the tag is ambiguous."""

    STATUS_HIGH_ERROR: AprilTagProperties.AprilTagPoseStatus.ValueType  # 3
    """The pose may be unreliable due to high reprojection error."""


    TAG_ID_FIELD_NUMBER: builtins.int
    DIMENSIONS_FIELD_NUMBER: builtins.int
    FRAME_NAME_FIDUCIAL_FIELD_NUMBER: builtins.int
    FIDUCIAL_POSE_STATUS_FIELD_NUMBER: builtins.int
    FRAME_NAME_FIDUCIAL_FILTERED_FIELD_NUMBER: builtins.int
    FIDUCIAL_FILTERED_POSE_STATUS_FIELD_NUMBER: builtins.int
    FRAME_NAME_CAMERA_FIELD_NUMBER: builtins.int
    DETECTION_COVARIANCE_FIELD_NUMBER: builtins.int
    DETECTION_COVARIANCE_REFERENCE_FRAME_FIELD_NUMBER: builtins.int
    tag_id: builtins.int
    """Consistent integer id associated with a given apriltag. April Tag detections will be from the
    tag family 36h11.
    """

    @property
    def dimensions(self) -> bosdyn.api.geometry_pb2.Vec2:
        """Apriltag size in meters, where x is the row/width length and y is the
        height/col length of the tag
        """
        pass
    frame_name_fiducial: typing.Text
    """The frame name for the raw version of this fiducial. This will be included in the transform snapshot."""

    fiducial_pose_status: global___AprilTagProperties.AprilTagPoseStatus.ValueType
    """Status of the pose estimation of the unfiltered fiducial frame."""

    frame_name_fiducial_filtered: typing.Text
    """The frame name for the filtered version of this fiducial. This will be included in the transform snapshot."""

    fiducial_filtered_pose_status: global___AprilTagProperties.AprilTagPoseStatus.ValueType
    """Status of the pose estimation of the filtered fiducial frame."""

    frame_name_camera: typing.Text
    """The frame name for the camera that detected this fiducial."""

    @property
    def detection_covariance(self) -> bosdyn.api.geometry_pb2.SE3Covariance:
        """A 6 x 6 Covariance matrix representing the marginal uncertainty of the last detection.
        The rows/columns are:
        rx, ry, rz, tx, ty, tz
        which represent incremental rotation and translation along the x, y, and z axes of the
        given frame, respectively.
        This is computed using the Jacobian of the pose estimation algorithm.
        """
        pass
    detection_covariance_reference_frame: typing.Text
    """The frame that the detection covariance is expressed in."""

    def __init__(self,
        *,
        tag_id: builtins.int = ...,
        dimensions: typing.Optional[bosdyn.api.geometry_pb2.Vec2] = ...,
        frame_name_fiducial: typing.Text = ...,
        fiducial_pose_status: global___AprilTagProperties.AprilTagPoseStatus.ValueType = ...,
        frame_name_fiducial_filtered: typing.Text = ...,
        fiducial_filtered_pose_status: global___AprilTagProperties.AprilTagPoseStatus.ValueType = ...,
        frame_name_camera: typing.Text = ...,
        detection_covariance: typing.Optional[bosdyn.api.geometry_pb2.SE3Covariance] = ...,
        detection_covariance_reference_frame: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["detection_covariance",b"detection_covariance","dimensions",b"dimensions"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["detection_covariance",b"detection_covariance","detection_covariance_reference_frame",b"detection_covariance_reference_frame","dimensions",b"dimensions","fiducial_filtered_pose_status",b"fiducial_filtered_pose_status","fiducial_pose_status",b"fiducial_pose_status","frame_name_camera",b"frame_name_camera","frame_name_fiducial",b"frame_name_fiducial","frame_name_fiducial_filtered",b"frame_name_fiducial_filtered","tag_id",b"tag_id"]) -> None: ...
global___AprilTagProperties = AprilTagProperties

class RayProperties(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RAY_FIELD_NUMBER: builtins.int
    FRAME_FIELD_NUMBER: builtins.int
    @property
    def ray(self) -> bosdyn.api.geometry_pb2.Ray:
        """Ray, usually pointing from the camera to the object."""
        pass
    frame: typing.Text
    """Frame the ray is expressed with respect to."""

    def __init__(self,
        *,
        ray: typing.Optional[bosdyn.api.geometry_pb2.Ray] = ...,
        frame: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["ray",b"ray"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["frame",b"frame","ray",b"ray"]) -> None: ...
global___RayProperties = RayProperties

class BoundingBoxProperties(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SIZE_EWRT_FRAME_FIELD_NUMBER: builtins.int
    FRAME_FIELD_NUMBER: builtins.int
    @property
    def size_ewrt_frame(self) -> bosdyn.api.geometry_pb2.Vec3:
        """An Oriented Bounding Box, with position and orientation at the frame provided in the
        transforms snapshot.

        The size of the box is expressed with respect to the frame.
        """
        pass
    frame: typing.Text
    """Frame the size is expressed with respect to."""

    def __init__(self,
        *,
        size_ewrt_frame: typing.Optional[bosdyn.api.geometry_pb2.Vec3] = ...,
        frame: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["size_ewrt_frame",b"size_ewrt_frame"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["frame",b"frame","size_ewrt_frame",b"size_ewrt_frame"]) -> None: ...
global___BoundingBoxProperties = BoundingBoxProperties

class DrawableProperties(google.protobuf.message.Message):
    """The drawing and visualization information for a world object."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class Color(google.protobuf.message.Message):
        """RGBA values for color ranging from [0,255] for R/G/B, and [0,1] for A."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        R_FIELD_NUMBER: builtins.int
        G_FIELD_NUMBER: builtins.int
        B_FIELD_NUMBER: builtins.int
        A_FIELD_NUMBER: builtins.int
        r: builtins.int
        """Red value ranging from [0,255]."""

        g: builtins.int
        """/ Green value ranging from [0,255]."""

        b: builtins.int
        """Blue value ranging from [0,255]."""

        a: builtins.float
        """Alpha (transparency) value ranging from [0,1]."""

        def __init__(self,
            *,
            r: builtins.int = ...,
            g: builtins.int = ...,
            b: builtins.int = ...,
            a: builtins.float = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["a",b"a","b",b"b","g",b"g","r",b"r"]) -> None: ...

    COLOR_FIELD_NUMBER: builtins.int
    LABEL_FIELD_NUMBER: builtins.int
    WIREFRAME_FIELD_NUMBER: builtins.int
    FRAME_FIELD_NUMBER: builtins.int
    SPHERE_FIELD_NUMBER: builtins.int
    BOX_FIELD_NUMBER: builtins.int
    ARROW_FIELD_NUMBER: builtins.int
    CAPSULE_FIELD_NUMBER: builtins.int
    CYLINDER_FIELD_NUMBER: builtins.int
    LINESTRIP_FIELD_NUMBER: builtins.int
    POINTS_FIELD_NUMBER: builtins.int
    FRAME_NAME_DRAWABLE_FIELD_NUMBER: builtins.int
    @property
    def color(self) -> global___DrawableProperties.Color:
        """Color of the object."""
        pass
    label: typing.Text
    """Label to be drawn at the origin of the object."""

    wireframe: builtins.bool
    """Drawn objects in wireframe."""

    @property
    def frame(self) -> global___DrawableFrame:
        """A drawable frame (oneof drawable field)."""
        pass
    @property
    def sphere(self) -> global___DrawableSphere:
        """A drawable sphere (oneof drawable field)."""
        pass
    @property
    def box(self) -> global___DrawableBox:
        """A drawable box (oneof drawable field)."""
        pass
    @property
    def arrow(self) -> global___DrawableArrow:
        """A drawable arrow (oneof drawable field)."""
        pass
    @property
    def capsule(self) -> global___DrawableCapsule:
        """A drawable capsule (oneof drawable field)."""
        pass
    @property
    def cylinder(self) -> global___DrawableCylinder:
        """A drawable cylinder (oneof drawable field)."""
        pass
    @property
    def linestrip(self) -> global___DrawableLineStrip:
        """A drawable linestrip (oneof drawable field)."""
        pass
    @property
    def points(self) -> global___DrawablePoints:
        """A drawable set of points (oneof drawable field)."""
        pass
    frame_name_drawable: typing.Text
    """The frame name for the drawable object. This will optionally be
    included in the frame tree snapshot.
    """

    def __init__(self,
        *,
        color: typing.Optional[global___DrawableProperties.Color] = ...,
        label: typing.Text = ...,
        wireframe: builtins.bool = ...,
        frame: typing.Optional[global___DrawableFrame] = ...,
        sphere: typing.Optional[global___DrawableSphere] = ...,
        box: typing.Optional[global___DrawableBox] = ...,
        arrow: typing.Optional[global___DrawableArrow] = ...,
        capsule: typing.Optional[global___DrawableCapsule] = ...,
        cylinder: typing.Optional[global___DrawableCylinder] = ...,
        linestrip: typing.Optional[global___DrawableLineStrip] = ...,
        points: typing.Optional[global___DrawablePoints] = ...,
        frame_name_drawable: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["arrow",b"arrow","box",b"box","capsule",b"capsule","color",b"color","cylinder",b"cylinder","drawable",b"drawable","frame",b"frame","linestrip",b"linestrip","points",b"points","sphere",b"sphere"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["arrow",b"arrow","box",b"box","capsule",b"capsule","color",b"color","cylinder",b"cylinder","drawable",b"drawable","frame",b"frame","frame_name_drawable",b"frame_name_drawable","label",b"label","linestrip",b"linestrip","points",b"points","sphere",b"sphere","wireframe",b"wireframe"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["drawable",b"drawable"]) -> typing.Optional[typing_extensions.Literal["frame","sphere","box","arrow","capsule","cylinder","linestrip","points"]]: ...
global___DrawableProperties = DrawableProperties

class DrawableFrame(google.protobuf.message.Message):
    """A coordinate frame drawing object, describing how large to render the arrows."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ARROW_LENGTH_FIELD_NUMBER: builtins.int
    ARROW_RADIUS_FIELD_NUMBER: builtins.int
    arrow_length: builtins.float
    arrow_radius: builtins.float
    def __init__(self,
        *,
        arrow_length: builtins.float = ...,
        arrow_radius: builtins.float = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["arrow_length",b"arrow_length","arrow_radius",b"arrow_radius"]) -> None: ...
global___DrawableFrame = DrawableFrame

class DrawableSphere(google.protobuf.message.Message):
    """A sphere drawing object."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RADIUS_FIELD_NUMBER: builtins.int
    radius: builtins.float
    def __init__(self,
        *,
        radius: builtins.float = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["radius",b"radius"]) -> None: ...
global___DrawableSphere = DrawableSphere

class DrawableBox(google.protobuf.message.Message):
    """A three dimensional box drawing object."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SIZE_FIELD_NUMBER: builtins.int
    @property
    def size(self) -> bosdyn.api.geometry_pb2.Vec3: ...
    def __init__(self,
        *,
        size: typing.Optional[bosdyn.api.geometry_pb2.Vec3] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["size",b"size"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["size",b"size"]) -> None: ...
global___DrawableBox = DrawableBox

class DrawableArrow(google.protobuf.message.Message):
    """A directed arrow drawing object."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DIRECTION_FIELD_NUMBER: builtins.int
    RADIUS_FIELD_NUMBER: builtins.int
    @property
    def direction(self) -> bosdyn.api.geometry_pb2.Vec3: ...
    radius: builtins.float
    def __init__(self,
        *,
        direction: typing.Optional[bosdyn.api.geometry_pb2.Vec3] = ...,
        radius: builtins.float = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["direction",b"direction"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["direction",b"direction","radius",b"radius"]) -> None: ...
global___DrawableArrow = DrawableArrow

class DrawableCapsule(google.protobuf.message.Message):
    """A oval-like capsule drawing object."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DIRECTION_FIELD_NUMBER: builtins.int
    RADIUS_FIELD_NUMBER: builtins.int
    @property
    def direction(self) -> bosdyn.api.geometry_pb2.Vec3: ...
    radius: builtins.float
    def __init__(self,
        *,
        direction: typing.Optional[bosdyn.api.geometry_pb2.Vec3] = ...,
        radius: builtins.float = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["direction",b"direction"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["direction",b"direction","radius",b"radius"]) -> None: ...
global___DrawableCapsule = DrawableCapsule

class DrawableCylinder(google.protobuf.message.Message):
    """A cylinder drawing object."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DIRECTION_FIELD_NUMBER: builtins.int
    RADIUS_FIELD_NUMBER: builtins.int
    @property
    def direction(self) -> bosdyn.api.geometry_pb2.Vec3: ...
    radius: builtins.float
    def __init__(self,
        *,
        direction: typing.Optional[bosdyn.api.geometry_pb2.Vec3] = ...,
        radius: builtins.float = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["direction",b"direction"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["direction",b"direction","radius",b"radius"]) -> None: ...
global___DrawableCylinder = DrawableCylinder

class DrawableLineStrip(google.protobuf.message.Message):
    """A line strip drawing object."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    POINTS_FIELD_NUMBER: builtins.int
    @property
    def points(self) -> bosdyn.api.geometry_pb2.Vec3: ...
    def __init__(self,
        *,
        points: typing.Optional[bosdyn.api.geometry_pb2.Vec3] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["points",b"points"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["points",b"points"]) -> None: ...
global___DrawableLineStrip = DrawableLineStrip

class DrawablePoints(google.protobuf.message.Message):
    """A set of points drawing object."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    POINTS_FIELD_NUMBER: builtins.int
    @property
    def points(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[bosdyn.api.geometry_pb2.Vec3]: ...
    def __init__(self,
        *,
        points: typing.Optional[typing.Iterable[bosdyn.api.geometry_pb2.Vec3]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["points",b"points"]) -> None: ...
global___DrawablePoints = DrawablePoints
