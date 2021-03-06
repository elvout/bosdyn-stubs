"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import bosdyn.api.geometry_pb2
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

class LocalGridType(google.protobuf.message.Message):
    """Representation of an available type of local grid."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text
    def __init__(self,
        *,
        name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___LocalGridType = LocalGridType

class LocalGridRequest(google.protobuf.message.Message):
    """LocalGrids are requested by LocalGridType string name."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LOCAL_GRID_TYPE_NAME_FIELD_NUMBER: builtins.int
    local_grid_type_name: typing.Text
    def __init__(self,
        *,
        local_grid_type_name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["local_grid_type_name",b"local_grid_type_name"]) -> None: ...
global___LocalGridRequest = LocalGridRequest

class LocalGridExtent(google.protobuf.message.Message):
    """Information about the dimensions of the local grid, including the number of grid cells and
    the size of each cell.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CELL_SIZE_FIELD_NUMBER: builtins.int
    NUM_CELLS_X_FIELD_NUMBER: builtins.int
    NUM_CELLS_Y_FIELD_NUMBER: builtins.int
    cell_size: builtins.float
    """Size of each side of the individual cells in the local grid (in meters).
    The area of a grid cell will be (cell_size x cell_size).
    """

    num_cells_x: builtins.int
    """Number of cells along x extent of local grid (number of columns in local grid/ the local
    grid width). Note, that the (num_cells_x)x(num_cells_y) represents the total number of grid
    cells in the local grid.
    """

    num_cells_y: builtins.int
    """Number of cells along y extent of local grid (number of rows in local grid).
    Note, that the (num_cells_x)x(num_cells_y) represents the totla number of grid
    cells in the local grid.
    """

    def __init__(self,
        *,
        cell_size: builtins.float = ...,
        num_cells_x: builtins.int = ...,
        num_cells_y: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cell_size",b"cell_size","num_cells_x",b"num_cells_x","num_cells_y",b"num_cells_y"]) -> None: ...
global___LocalGridExtent = LocalGridExtent

class LocalGrid(google.protobuf.message.Message):
    """A grid-based local grid structure, which can represent different kinds of data, such as terrain
    or obstacle data.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _CellFormat:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _CellFormatEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[LocalGrid._CellFormat.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        CELL_FORMAT_UNKNOWN: LocalGrid._CellFormat.ValueType  # 0
        """Not specified -- not a valid value."""

        CELL_FORMAT_FLOAT32: LocalGrid._CellFormat.ValueType  # 1
        """Each cell of the local grid is encoded as a little-endian 32-bit floating point number."""

        CELL_FORMAT_FLOAT64: LocalGrid._CellFormat.ValueType  # 2
        """Each cell of the local grid is encoded as a little-endian 64-bit floating point number."""

        CELL_FORMAT_INT8: LocalGrid._CellFormat.ValueType  # 3
        """Each cell of the local grid is encoded as a signed 8-bit integer."""

        CELL_FORMAT_UINT8: LocalGrid._CellFormat.ValueType  # 4
        """Each cell of the local grid is encoded as an unsigned 8-bit integer."""

        CELL_FORMAT_INT16: LocalGrid._CellFormat.ValueType  # 5
        """Each cell of the local grid is encoded as a little-endian signed 16-bit integer."""

        CELL_FORMAT_UINT16: LocalGrid._CellFormat.ValueType  # 6
        """Each cell of the local grid is encoded as a little-endian unsigned 16-bit integer."""

    class CellFormat(_CellFormat, metaclass=_CellFormatEnumTypeWrapper):
        """Describes the data type of a cell."""
        pass

    CELL_FORMAT_UNKNOWN: LocalGrid.CellFormat.ValueType  # 0
    """Not specified -- not a valid value."""

    CELL_FORMAT_FLOAT32: LocalGrid.CellFormat.ValueType  # 1
    """Each cell of the local grid is encoded as a little-endian 32-bit floating point number."""

    CELL_FORMAT_FLOAT64: LocalGrid.CellFormat.ValueType  # 2
    """Each cell of the local grid is encoded as a little-endian 64-bit floating point number."""

    CELL_FORMAT_INT8: LocalGrid.CellFormat.ValueType  # 3
    """Each cell of the local grid is encoded as a signed 8-bit integer."""

    CELL_FORMAT_UINT8: LocalGrid.CellFormat.ValueType  # 4
    """Each cell of the local grid is encoded as an unsigned 8-bit integer."""

    CELL_FORMAT_INT16: LocalGrid.CellFormat.ValueType  # 5
    """Each cell of the local grid is encoded as a little-endian signed 16-bit integer."""

    CELL_FORMAT_UINT16: LocalGrid.CellFormat.ValueType  # 6
    """Each cell of the local grid is encoded as a little-endian unsigned 16-bit integer."""


    class _Encoding:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _EncodingEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[LocalGrid._Encoding.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        ENCODING_UNKNOWN: LocalGrid._Encoding.ValueType  # 0
        """Not specified -- not a valid value."""

        ENCODING_RAW: LocalGrid._Encoding.ValueType  # 1
        """Cells are stored packed uncompressed."""

        ENCODING_RLE: LocalGrid._Encoding.ValueType  # 2
        """Run-length encoding: repeat counts stored in rle_counts."""

    class Encoding(_Encoding, metaclass=_EncodingEnumTypeWrapper):
        """Encoding used for storing the local grid."""
        pass

    ENCODING_UNKNOWN: LocalGrid.Encoding.ValueType  # 0
    """Not specified -- not a valid value."""

    ENCODING_RAW: LocalGrid.Encoding.ValueType  # 1
    """Cells are stored packed uncompressed."""

    ENCODING_RLE: LocalGrid.Encoding.ValueType  # 2
    """Run-length encoding: repeat counts stored in rle_counts."""


    LOCAL_GRID_TYPE_NAME_FIELD_NUMBER: builtins.int
    ACQUISITION_TIME_FIELD_NUMBER: builtins.int
    TRANSFORMS_SNAPSHOT_FIELD_NUMBER: builtins.int
    FRAME_NAME_LOCAL_GRID_DATA_FIELD_NUMBER: builtins.int
    EXTENT_FIELD_NUMBER: builtins.int
    CELL_FORMAT_FIELD_NUMBER: builtins.int
    ENCODING_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    RLE_COUNTS_FIELD_NUMBER: builtins.int
    CELL_VALUE_SCALE_FIELD_NUMBER: builtins.int
    CELL_VALUE_OFFSET_FIELD_NUMBER: builtins.int
    local_grid_type_name: typing.Text
    """The human readable string name that is used to identify the type of local grid data."""

    @property
    def acquisition_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The time at which the local grid data was computed and last valid at."""
        pass
    @property
    def transforms_snapshot(self) -> bosdyn.api.geometry_pb2.FrameTreeSnapshot:
        """A tree-based collection of transformations, which will include the transformations to each of
        the returned local grids in addition to transformations to the common frames ("vision", "body", "odom").
        All transforms within the snapshot are at the acquistion time of the local grid.
        """
        pass
    frame_name_local_grid_data: typing.Text
    """The frame name for the local grid data. This frame refers to the corner of cell (0, 0), such that
    the map data is in the +x, +y quadrant.
    The cell data is packed in x-y order, so the cell at:
      data[xi + extent.num_cells_x * yj]
    has its center at position:
      {(xi + 0.5) * extent.cell_size, (yj + 0.5) * extent.cell_size}.
    """

    @property
    def extent(self) -> global___LocalGridExtent:
        """Location, size and resolution of the local grid."""
        pass
    cell_format: global___LocalGrid.CellFormat.ValueType
    """The data type of all individual cells in the local grid."""

    encoding: global___LocalGrid.Encoding.ValueType
    """The encoding for the 'data' field of the local grid message."""

    data: builtins.bytes
    """The encoded local grid representation.
    Cells are encoded according to the encoding enum, and are stored in in row-major order (x-major).
    This means that the data field has data entered row by row. The grid cell located at (i, j) will be
    at the (index = i * num_cells_x + j) within the data array.
    """

    @property
    def rle_counts(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """RLE pixel repetition counts: use data[i] repeated rle_counts[i] times when decoding the
        bytes data field.
        """
        pass
    cell_value_scale: builtins.float
    """The scale for the cell value data; only valid if it is a non-zero number."""

    cell_value_offset: builtins.float
    """A fixed value offset that is applied to each value of the cell data.
    Actual values in local grid are: (({value from data} * cell_value_scale) + cell_value_offset).
    """

    def __init__(self,
        *,
        local_grid_type_name: typing.Text = ...,
        acquisition_time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        transforms_snapshot: typing.Optional[bosdyn.api.geometry_pb2.FrameTreeSnapshot] = ...,
        frame_name_local_grid_data: typing.Text = ...,
        extent: typing.Optional[global___LocalGridExtent] = ...,
        cell_format: global___LocalGrid.CellFormat.ValueType = ...,
        encoding: global___LocalGrid.Encoding.ValueType = ...,
        data: builtins.bytes = ...,
        rle_counts: typing.Optional[typing.Iterable[builtins.int]] = ...,
        cell_value_scale: builtins.float = ...,
        cell_value_offset: builtins.float = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["acquisition_time",b"acquisition_time","extent",b"extent","transforms_snapshot",b"transforms_snapshot"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["acquisition_time",b"acquisition_time","cell_format",b"cell_format","cell_value_offset",b"cell_value_offset","cell_value_scale",b"cell_value_scale","data",b"data","encoding",b"encoding","extent",b"extent","frame_name_local_grid_data",b"frame_name_local_grid_data","local_grid_type_name",b"local_grid_type_name","rle_counts",b"rle_counts","transforms_snapshot",b"transforms_snapshot"]) -> None: ...
global___LocalGrid = LocalGrid

class LocalGridResponse(google.protobuf.message.Message):
    """The local grid response message will contain either the local grid or an error status."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Status:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[LocalGridResponse._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNKNOWN: LocalGridResponse._Status.ValueType  # 0
        """Not specified -- not a valid value."""

        STATUS_OK: LocalGridResponse._Status.ValueType  # 1
        """LocalGrid was returned successfully."""

        STATUS_NO_SUCH_GRID: LocalGridResponse._Status.ValueType  # 2
        """The requested local grid-type is unknown."""

        STATUS_DATA_UNAVAILABLE: LocalGridResponse._Status.ValueType  # 3
        """The request local grid data is not available at this time."""

        STATUS_DATA_INVALID: LocalGridResponse._Status.ValueType  # 4
        """The local grid data was not valid for some reason."""

    class Status(_Status, metaclass=_StatusEnumTypeWrapper):
        pass

    STATUS_UNKNOWN: LocalGridResponse.Status.ValueType  # 0
    """Not specified -- not a valid value."""

    STATUS_OK: LocalGridResponse.Status.ValueType  # 1
    """LocalGrid was returned successfully."""

    STATUS_NO_SUCH_GRID: LocalGridResponse.Status.ValueType  # 2
    """The requested local grid-type is unknown."""

    STATUS_DATA_UNAVAILABLE: LocalGridResponse.Status.ValueType  # 3
    """The request local grid data is not available at this time."""

    STATUS_DATA_INVALID: LocalGridResponse.Status.ValueType  # 4
    """The local grid data was not valid for some reason."""


    LOCAL_GRID_TYPE_NAME_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    LOCAL_GRID_FIELD_NUMBER: builtins.int
    local_grid_type_name: typing.Text
    """The type name of the local grid included in this response."""

    status: global___LocalGridResponse.Status.ValueType
    """Status of the request for the individual local grid."""

    @property
    def local_grid(self) -> global___LocalGrid:
        """The requested local grid data."""
        pass
    def __init__(self,
        *,
        local_grid_type_name: typing.Text = ...,
        status: global___LocalGridResponse.Status.ValueType = ...,
        local_grid: typing.Optional[global___LocalGrid] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["local_grid",b"local_grid"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["local_grid",b"local_grid","local_grid_type_name",b"local_grid_type_name","status",b"status"]) -> None: ...
global___LocalGridResponse = LocalGridResponse

class GetLocalGridTypesRequest(google.protobuf.message.Message):
    """The GetLocalGridTypes request message asks to the local grid types."""
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
global___GetLocalGridTypesRequest = GetLocalGridTypesRequest

class GetLocalGridTypesResponse(google.protobuf.message.Message):
    """The GetLocalGridTypes response message returns to get all known string names for local grid types."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    LOCAL_GRID_TYPE_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.ResponseHeader:
        """Common response header."""
        pass
    @property
    def local_grid_type(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___LocalGridType]:
        """The list of available local grid types."""
        pass
    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.ResponseHeader] = ...,
        local_grid_type: typing.Optional[typing.Iterable[global___LocalGridType]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header","local_grid_type",b"local_grid_type"]) -> None: ...
global___GetLocalGridTypesResponse = GetLocalGridTypesResponse

class GetLocalGridsRequest(google.protobuf.message.Message):
    """The GetLocalGrid request message can request for multiple different types of local grids at one time."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    LOCAL_GRID_REQUESTS_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.RequestHeader:
        """Common request header."""
        pass
    @property
    def local_grid_requests(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___LocalGridRequest]:
        """Specifications of the requested local grids."""
        pass
    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.RequestHeader] = ...,
        local_grid_requests: typing.Optional[typing.Iterable[global___LocalGridRequest]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header","local_grid_requests",b"local_grid_requests"]) -> None: ...
global___GetLocalGridsRequest = GetLocalGridsRequest

class GetLocalGridsResponse(google.protobuf.message.Message):
    """The GetLocalGrid response message replies with all of the local grid data for the requested types, and
    a numerical count representing the amount of status errors that occurred when getting this data.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    LOCAL_GRID_RESPONSES_FIELD_NUMBER: builtins.int
    NUM_LOCAL_GRID_ERRORS_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.ResponseHeader:
        """Common response header."""
        pass
    @property
    def local_grid_responses(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___LocalGridResponse]:
        """Response of local grid or error status for each requested local grid."""
        pass
    num_local_grid_errors: builtins.int
    """The number of individual local grids requests which could not be satisfied."""

    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.ResponseHeader] = ...,
        local_grid_responses: typing.Optional[typing.Iterable[global___LocalGridResponse]] = ...,
        num_local_grid_errors: builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header","local_grid_responses",b"local_grid_responses","num_local_grid_errors",b"num_local_grid_errors"]) -> None: ...
global___GetLocalGridsResponse = GetLocalGridsResponse
