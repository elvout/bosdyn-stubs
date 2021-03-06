"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import bosdyn.api.geometry_pb2
import bosdyn.api.graph_nav.map_pb2
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Route(google.protobuf.message.Message):
    """Route that the robot should follow or is currently following."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    WAYPOINT_ID_FIELD_NUMBER: builtins.int
    EDGE_ID_FIELD_NUMBER: builtins.int
    @property
    def waypoint_id(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Ordered list of waypoints to traverse, starting from index 0."""
        pass
    @property
    def edge_id(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[bosdyn.api.graph_nav.map_pb2.Edge.Id]:
        """Ordered list of edges to traverse between those waypoints."""
        pass
    def __init__(self,
        *,
        waypoint_id: typing.Optional[typing.Iterable[typing.Text]] = ...,
        edge_id: typing.Optional[typing.Iterable[bosdyn.api.graph_nav.map_pb2.Edge.Id]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["edge_id",b"edge_id","waypoint_id",b"waypoint_id"]) -> None: ...
global___Route = Route

class Localization(google.protobuf.message.Message):
    """The localization state of the robot. This reports the pose of the robot relative
    to a particular waypoint on the graph nav map.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    WAYPOINT_ID_FIELD_NUMBER: builtins.int
    WAYPOINT_TFORM_BODY_FIELD_NUMBER: builtins.int
    SEED_TFORM_BODY_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    waypoint_id: typing.Text
    """Waypoint this localization is relative to."""

    @property
    def waypoint_tform_body(self) -> bosdyn.api.geometry_pb2.SE3Pose:
        """Pose of body in waypoint frame."""
        pass
    @property
    def seed_tform_body(self) -> bosdyn.api.geometry_pb2.SE3Pose:
        """Pose of body in a common reference frame. The common reference frame defaults to the starting
        fiducial frame, but can be changed. See Anchoring for more info.
        """
        pass
    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time (in robot time basis) that this localization was valid."""
        pass
    def __init__(self,
        *,
        waypoint_id: typing.Text = ...,
        waypoint_tform_body: typing.Optional[bosdyn.api.geometry_pb2.SE3Pose] = ...,
        seed_tform_body: typing.Optional[bosdyn.api.geometry_pb2.SE3Pose] = ...,
        timestamp: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["seed_tform_body",b"seed_tform_body","timestamp",b"timestamp","waypoint_tform_body",b"waypoint_tform_body"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["seed_tform_body",b"seed_tform_body","timestamp",b"timestamp","waypoint_id",b"waypoint_id","waypoint_tform_body",b"waypoint_tform_body"]) -> None: ...
global___Localization = Localization
