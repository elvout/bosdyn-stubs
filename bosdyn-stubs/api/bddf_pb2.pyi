"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _PodTypeEnum:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _PodTypeEnumEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_PodTypeEnum.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    TYPE_UNSPECIFIED: _PodTypeEnum.ValueType  # 0
    TYPE_INT8: _PodTypeEnum.ValueType  # 1
    TYPE_INT16: _PodTypeEnum.ValueType  # 2
    TYPE_INT32: _PodTypeEnum.ValueType  # 3
    TYPE_INT64: _PodTypeEnum.ValueType  # 4
    TYPE_UINT8: _PodTypeEnum.ValueType  # 5
    TYPE_UINT16: _PodTypeEnum.ValueType  # 6
    TYPE_UINT32: _PodTypeEnum.ValueType  # 7
    TYPE_UINT64: _PodTypeEnum.ValueType  # 8
    TYPE_FLOAT32: _PodTypeEnum.ValueType  # 9
    TYPE_FLOAT64: _PodTypeEnum.ValueType  # 10
class PodTypeEnum(_PodTypeEnum, metaclass=_PodTypeEnumEnumTypeWrapper):
    """"Plain old data" types which may be stored within POD data blocks."""
    pass

TYPE_UNSPECIFIED: PodTypeEnum.ValueType  # 0
TYPE_INT8: PodTypeEnum.ValueType  # 1
TYPE_INT16: PodTypeEnum.ValueType  # 2
TYPE_INT32: PodTypeEnum.ValueType  # 3
TYPE_INT64: PodTypeEnum.ValueType  # 4
TYPE_UINT8: PodTypeEnum.ValueType  # 5
TYPE_UINT16: PodTypeEnum.ValueType  # 6
TYPE_UINT32: PodTypeEnum.ValueType  # 7
TYPE_UINT64: PodTypeEnum.ValueType  # 8
TYPE_FLOAT32: PodTypeEnum.ValueType  # 9
TYPE_FLOAT64: PodTypeEnum.ValueType  # 10
global___PodTypeEnum = PodTypeEnum


class DescriptorBlock(google.protobuf.message.Message):
    """The file format consists of 3 kinds of blocks with simple framing:
     - Serialized DescriptorBlock protos, describing either the main file,
        a defining a series of data blocks, or a file index,
     - Serialized DataDescriptorBlock protos, describing a single data block, and
     - Binary data.

    A Descriptor block typically describes a series of messages, but the descriptor at the
     start of the file describes the contents of the file as a whole, and the descriptor
     at the end of the file is an index structure to allow efficient access to the contents
     of the file.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FILE_DESCRIPTOR_FIELD_NUMBER: builtins.int
    SERIES_DESCRIPTOR_FIELD_NUMBER: builtins.int
    SERIES_BLOCK_INDEX_FIELD_NUMBER: builtins.int
    FILE_INDEX_FIELD_NUMBER: builtins.int
    @property
    def file_descriptor(self) -> global___FileFormatDescriptor: ...
    @property
    def series_descriptor(self) -> global___SeriesDescriptor: ...
    @property
    def series_block_index(self) -> global___SeriesBlockIndex: ...
    @property
    def file_index(self) -> global___FileIndex: ...
    def __init__(self,
        *,
        file_descriptor: typing.Optional[global___FileFormatDescriptor] = ...,
        series_descriptor: typing.Optional[global___SeriesDescriptor] = ...,
        series_block_index: typing.Optional[global___SeriesBlockIndex] = ...,
        file_index: typing.Optional[global___FileIndex] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["DescriptorType",b"DescriptorType","file_descriptor",b"file_descriptor","file_index",b"file_index","series_block_index",b"series_block_index","series_descriptor",b"series_descriptor"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["DescriptorType",b"DescriptorType","file_descriptor",b"file_descriptor","file_index",b"file_index","series_block_index",b"series_block_index","series_descriptor",b"series_descriptor"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["DescriptorType",b"DescriptorType"]) -> typing.Optional[typing_extensions.Literal["file_descriptor","series_descriptor","series_block_index","file_index"]]: ...
global___DescriptorBlock = DescriptorBlock

class DataDescriptor(google.protobuf.message.Message):
    """A DataDescriptor describes a data block which immediately follows it in the file.
    A corresponding SeriesDescriptor with a matching series_index must precede this in the file.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SERIES_INDEX_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    ADDITIONAL_INDEXES_FIELD_NUMBER: builtins.int
    series_index: builtins.int
    """The series_index references the SeriesDescriptor to which the data following is associated."""

    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The time at which the data is considered to be captured/sampled.
        E.g., the shutter-close time of a captured image.
        """
        pass
    @property
    def additional_indexes(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """Sometimes a visualizer will want to organize message by data timestamp, sometimes by
         the time messages were published or logged.
        The additional_indexes field allows extra indexes or timestamps to be associated with
         each data block for this purpose.
        Other identifying information may also be used here, such as the PID of the process which
         originated the data (e.g., for detecting if and when that process restarted).
        The values in this field should correspond to the labels defined in "additional_index_names"
         in the corresponding SeriesDescriptor.
        """
        pass
    def __init__(self,
        *,
        series_index: builtins.int = ...,
        timestamp: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        additional_indexes: typing.Optional[typing.Iterable[builtins.int]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["timestamp",b"timestamp"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["additional_indexes",b"additional_indexes","series_index",b"series_index","timestamp",b"timestamp"]) -> None: ...
global___DataDescriptor = DataDescriptor

class FileFormatDescriptor(google.protobuf.message.Message):
    """The first block in the file should be a DescriptorBlock containing a FileFormatDescriptor.
    FileFormatDescriptor indicates the file format version and annotations.
    Annotations describe things like the robot from which the log was taken and the release id.
    The format of annotation keys should be
      {project-or-organization}/{annotation-name}
    For example, 'bosdyn/robot-serial-number'.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _CheckSumType:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _CheckSumTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[FileFormatDescriptor._CheckSumType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        CHECKSUM_TYPE_UNKNOWN: FileFormatDescriptor._CheckSumType.ValueType  # 0
        """Checksum type is unspecified.  Should not be used."""

        CHECKSUM_TYPE_NONE: FileFormatDescriptor._CheckSumType.ValueType  # 1
        """The writer of this stream is not computing a checksum.
        The stream checksum at the end of the file will be 160 bits all set to 0.
        """

        CHECKSUM_TYPE_SHA1: FileFormatDescriptor._CheckSumType.ValueType  # 2
        """A 160 bit SHA1 checksum will be included at the end of the stream.
        This checksum will be computed over all data before digest itself at the
         end of the stream, and can be used to verify the stream was received uncorrupted.
        """

    class CheckSumType(_CheckSumType, metaclass=_CheckSumTypeEnumTypeWrapper):
        pass

    CHECKSUM_TYPE_UNKNOWN: FileFormatDescriptor.CheckSumType.ValueType  # 0
    """Checksum type is unspecified.  Should not be used."""

    CHECKSUM_TYPE_NONE: FileFormatDescriptor.CheckSumType.ValueType  # 1
    """The writer of this stream is not computing a checksum.
    The stream checksum at the end of the file will be 160 bits all set to 0.
    """

    CHECKSUM_TYPE_SHA1: FileFormatDescriptor.CheckSumType.ValueType  # 2
    """A 160 bit SHA1 checksum will be included at the end of the stream.
    This checksum will be computed over all data before digest itself at the
     end of the stream, and can be used to verify the stream was received uncorrupted.
    """


    class AnnotationsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text
        value: typing.Text
        def __init__(self,
            *,
            key: typing.Text = ...,
            value: typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    VERSION_FIELD_NUMBER: builtins.int
    ANNOTATIONS_FIELD_NUMBER: builtins.int
    CHECKSUM_TYPE_FIELD_NUMBER: builtins.int
    CHECKSUM_NUM_BYTES_FIELD_NUMBER: builtins.int
    @property
    def version(self) -> global___FileFormatVersion:
        """The version number of the BDDF file."""
        pass
    @property
    def annotations(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """File/stream-wide annotations to describe the content of the file."""
        pass
    checksum_type: global___FileFormatDescriptor.CheckSumType.ValueType
    """The type of checksum supported by this stream.
    For BDDF version 1.0.0 this should be SHA1.
    """

    checksum_num_bytes: builtins.int
    """The number of bytes used for the BDDF checksum.
    For BDDF version 1.0.0 this should always be 20, even if CHECKSUM_NONE is used.
    """

    def __init__(self,
        *,
        version: typing.Optional[global___FileFormatVersion] = ...,
        annotations: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        checksum_type: global___FileFormatDescriptor.CheckSumType.ValueType = ...,
        checksum_num_bytes: builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["version",b"version"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["annotations",b"annotations","checksum_num_bytes",b"checksum_num_bytes","checksum_type",b"checksum_type","version",b"version"]) -> None: ...
global___FileFormatDescriptor = FileFormatDescriptor

class FileFormatVersion(google.protobuf.message.Message):
    """The current data file format is 1.0.0."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MAJOR_VERSION_FIELD_NUMBER: builtins.int
    MINOR_VERSION_FIELD_NUMBER: builtins.int
    PATCH_LEVEL_FIELD_NUMBER: builtins.int
    major_version: builtins.int
    minor_version: builtins.int
    patch_level: builtins.int
    def __init__(self,
        *,
        major_version: builtins.int = ...,
        minor_version: builtins.int = ...,
        patch_level: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["major_version",b"major_version","minor_version",b"minor_version","patch_level",b"patch_level"]) -> None: ...
global___FileFormatVersion = FileFormatVersion

class SeriesDescriptor(google.protobuf.message.Message):
    """A description of a series of data blocks.
    These data blocks may either represent binary messages of a variable size, or they may
     represent a sequence of samples of POD data samples: single/vector/matrix/... of integer
     or floating-point values.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class AnnotationsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text
        value: typing.Text
        def __init__(self,
            *,
            key: typing.Text = ...,
            value: typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    SERIES_INDEX_FIELD_NUMBER: builtins.int
    SERIES_IDENTIFIER_FIELD_NUMBER: builtins.int
    IDENTIFIER_HASH_FIELD_NUMBER: builtins.int
    MESSAGE_TYPE_FIELD_NUMBER: builtins.int
    POD_TYPE_FIELD_NUMBER: builtins.int
    STRUCT_TYPE_FIELD_NUMBER: builtins.int
    ANNOTATIONS_FIELD_NUMBER: builtins.int
    ADDITIONAL_INDEX_NAMES_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    series_index: builtins.int
    """This index for the series is unique within the data file."""

    @property
    def series_identifier(self) -> global___SeriesIdentifier:
        """This is the globally unique {key -> value} mapping to identify the series."""
        pass
    identifier_hash: builtins.int
    """This is a hash of the series_identifier.
    The hash is the first 64 bits (read as a big-endian encoded uint64_t) of
     SHA1(S K1 V1 K2 V2 ...) where,
      - S is series identifier text,
      - K1 and V1 are the key and value of the first key and value of the `spec`,
      - K2 and V2 are the second key and value of the spec, etc...
    Here, all strings are encoded as utf-8, and keys are sorted lexicographically using this
     encoding (K1 < K2 < ...).
    """

    @property
    def message_type(self) -> global___MessageTypeDescriptor: ...
    @property
    def pod_type(self) -> global___PodTypeDescriptor: ...
    @property
    def struct_type(self) -> global___StructTypeDescriptor: ...
    @property
    def annotations(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Annotations are a {key -> value} mapping for associating additional information with
         the series.
        The format of annotation keys should be
          {project-or-organization}/{annotation-name}
        For example, 'bosdyn/channel-name', 'bosdyn/protobuf-type'.
        Annotation keys without a '/' are reserved.
        The only current key in the reserved namespace is 'units': e.g., {'units': 'm/s2'}.
        """
        pass
    @property
    def additional_index_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Labels for additional index values which should be attached to each DataDescriptor
         in the series.
        See the description of "additional_indexes" in DataDescriptor.
        """
        pass
    description: typing.Text
    def __init__(self,
        *,
        series_index: builtins.int = ...,
        series_identifier: typing.Optional[global___SeriesIdentifier] = ...,
        identifier_hash: builtins.int = ...,
        message_type: typing.Optional[global___MessageTypeDescriptor] = ...,
        pod_type: typing.Optional[global___PodTypeDescriptor] = ...,
        struct_type: typing.Optional[global___StructTypeDescriptor] = ...,
        annotations: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        additional_index_names: typing.Optional[typing.Iterable[typing.Text]] = ...,
        description: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["DataType",b"DataType","message_type",b"message_type","pod_type",b"pod_type","series_identifier",b"series_identifier","struct_type",b"struct_type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["DataType",b"DataType","additional_index_names",b"additional_index_names","annotations",b"annotations","description",b"description","identifier_hash",b"identifier_hash","message_type",b"message_type","pod_type",b"pod_type","series_identifier",b"series_identifier","series_index",b"series_index","struct_type",b"struct_type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["DataType",b"DataType"]) -> typing.Optional[typing_extensions.Literal["message_type","pod_type","struct_type"]]: ...
global___SeriesDescriptor = SeriesDescriptor

class MessageTypeDescriptor(google.protobuf.message.Message):
    """If a data series contains a sequence of binary messages, the encoding and format of these
     messages is described by a MesssageTypeDescriptor.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CONTENT_TYPE_FIELD_NUMBER: builtins.int
    TYPE_NAME_FIELD_NUMBER: builtins.int
    IS_METADATA_FIELD_NUMBER: builtins.int
    content_type: typing.Text
    """Description of the content type.
    E.g., "application/protobuf", "image/jpeg", "text/csv", ...
    """

    type_name: typing.Text
    """If content_type is "application/protobuf", this is the full-name of the protobuf type."""

    is_metadata: builtins.bool
    """If true, message contents are necessary for interpreting other messages.
    If the content of this file is split into multiple output files, these messages should be
     copied into each.
    """

    def __init__(self,
        *,
        content_type: typing.Text = ...,
        type_name: typing.Text = ...,
        is_metadata: builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["content_type",b"content_type","is_metadata",b"is_metadata","type_name",b"type_name"]) -> None: ...
global___MessageTypeDescriptor = MessageTypeDescriptor

class PodTypeDescriptor(google.protobuf.message.Message):
    """If a data series contains signals-style data of time-sampled "plain old datatypes", this
     describes the content of the series.
    All POD data stored in data blocks is stored in little-endian byte order.
    Any number of samples may be stored within a given data block.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    POD_TYPE_FIELD_NUMBER: builtins.int
    DIMENSION_FIELD_NUMBER: builtins.int
    pod_type: global___PodTypeEnum.ValueType
    """The type of machine-readable values stored."""

    @property
    def dimension(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """If empty, indicates a single POD per sample.
        If one-element, indicates a vector of the given size per sample.
        If two-elements, indicates a matrix of the given size, and so on.
        An M x N x .. x P array of data is traversed from innermost (P) to outermost (M) dimension.
        """
        pass
    def __init__(self,
        *,
        pod_type: global___PodTypeEnum.ValueType = ...,
        dimension: typing.Optional[typing.Iterable[builtins.int]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["dimension",b"dimension","pod_type",b"pod_type"]) -> None: ...
global___PodTypeDescriptor = PodTypeDescriptor

class StructTypeDescriptor(google.protobuf.message.Message):
    """A struct series is a composite formed by a set of other series whose messages or signals-ticks
     are sampled at the same time.
    For example, all there may be a struct series for a set of signals variables, all from a
     process with an 'update()' function within which all all variables are sampled with the
     same timestamp.
    DataBlocks will not directly reference this series, but only child series of this series.
    Struct series may reference other struct series, but the series structure must be a directed
     acyclic graph (DAG): no circular reference structures.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class KeyToSeriesIdentifierHashEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text
        value: builtins.int
        def __init__(self,
            *,
            key: typing.Text = ...,
            value: builtins.int = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    KEY_TO_SERIES_IDENTIFIER_HASH_FIELD_NUMBER: builtins.int
    @property
    def key_to_series_identifier_hash(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, builtins.int]:
        """A map of a name-reference to a series, identified by its series_identifer_hash."""
        pass
    def __init__(self,
        *,
        key_to_series_identifier_hash: typing.Optional[typing.Mapping[typing.Text, builtins.int]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["key_to_series_identifier_hash",b"key_to_series_identifier_hash"]) -> None: ...
global___StructTypeDescriptor = StructTypeDescriptor

class FileIndex(google.protobuf.message.Message):
    """As a file is closed, a DescriptorBlock containing a FileIndex should be written.
    The FileIndex summarizes the data series stored in the file and the location of the
     block-indexes for each type in the file.
    Each series is assigned a "series_index" within the file, and this index may be used to
     index into the repeated fields in this message.
    E.g., for the series with series_index N, you can access its SeriesIdentifier by accessing
     element N the of the series_identifiers repeated field.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SERIES_IDENTIFIERS_FIELD_NUMBER: builtins.int
    SERIES_BLOCK_INDEX_OFFSETS_FIELD_NUMBER: builtins.int
    SERIES_IDENTIFIER_HASHES_FIELD_NUMBER: builtins.int
    @property
    def series_identifiers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___SeriesIdentifier]:
        """SeriesIdentifer for each series in this file."""
        pass
    @property
    def series_block_index_offsets(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """The offset from the start of the file of the SeriesBlockIndex block for each series."""
        pass
    @property
    def series_identifier_hashes(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """The hash of the series_identifier for each series."""
        pass
    def __init__(self,
        *,
        series_identifiers: typing.Optional[typing.Iterable[global___SeriesIdentifier]] = ...,
        series_block_index_offsets: typing.Optional[typing.Iterable[builtins.int]] = ...,
        series_identifier_hashes: typing.Optional[typing.Iterable[builtins.int]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["series_block_index_offsets",b"series_block_index_offsets","series_identifier_hashes",b"series_identifier_hashes","series_identifiers",b"series_identifiers"]) -> None: ...
global___FileIndex = FileIndex

class SeriesBlockIndex(google.protobuf.message.Message):
    """This describes the location of the SeriesDescriptor DescriptorBlock for the series, and
     the timestamp and location in the file of every data block in the series.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class BlockEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        TIMESTAMP_FIELD_NUMBER: builtins.int
        FILE_OFFSET_FIELD_NUMBER: builtins.int
        ADDITIONAL_INDEXES_FIELD_NUMBER: builtins.int
        @property
        def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp:
            """The timestamp of data in this block."""
            pass
        file_offset: builtins.int
        """The offset of the data block from the start of the file."""

        @property
        def additional_indexes(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
            """Values of the additional indexes for describing this block."""
            pass
        def __init__(self,
            *,
            timestamp: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
            file_offset: builtins.int = ...,
            additional_indexes: typing.Optional[typing.Iterable[builtins.int]] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["timestamp",b"timestamp"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["additional_indexes",b"additional_indexes","file_offset",b"file_offset","timestamp",b"timestamp"]) -> None: ...

    SERIES_INDEX_FIELD_NUMBER: builtins.int
    DESCRIPTOR_FILE_OFFSET_FIELD_NUMBER: builtins.int
    BLOCK_ENTRIES_FIELD_NUMBER: builtins.int
    TOTAL_BYTES_FIELD_NUMBER: builtins.int
    series_index: builtins.int
    """The series_index for the series described by this index block."""

    descriptor_file_offset: builtins.int
    """Offset of type descriptor block from start of file."""

    @property
    def block_entries(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___SeriesBlockIndex.BlockEntry]:
        """The timestamp and location of each data block for this series."""
        pass
    total_bytes: builtins.int
    """The total size of the data stored in the data blocks of this series."""

    def __init__(self,
        *,
        series_index: builtins.int = ...,
        descriptor_file_offset: builtins.int = ...,
        block_entries: typing.Optional[typing.Iterable[global___SeriesBlockIndex.BlockEntry]] = ...,
        total_bytes: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["block_entries",b"block_entries","descriptor_file_offset",b"descriptor_file_offset","series_index",b"series_index","total_bytes",b"total_bytes"]) -> None: ...
global___SeriesBlockIndex = SeriesBlockIndex

class SeriesIdentifier(google.protobuf.message.Message):
    """A key or description for selecting a message series.
    Because there may be multiple ways of describing a message series, we identify
     them by a unique mapping of {key -> value}.
    A series_type corresponds to a set of keys which are expected in the mapping.
    A 'bosdyn:grpc:requests' series_type, containing GRPC robot-id request messages, might
     thus be specified as:
      {'service': 'robot_id', 'message': 'bosdyn.api.RobotIdRequest'}
    A 'bosdyn:logtick' series_type, containing a signals data variable from LogTick
      annotations might be specified as:
      {'varname': 'tablet.wifi.rssi', 'schema': 'tablet-comms', 'client': 'bd-tablet'}
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class SpecEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text
        value: typing.Text
        def __init__(self,
            *,
            key: typing.Text = ...,
            value: typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    SERIES_TYPE_FIELD_NUMBER: builtins.int
    SPEC_FIELD_NUMBER: builtins.int
    series_type: typing.Text
    """This is the kind of spec, which should correspond to a set of keys which are expected
     in the spec.
    """

    @property
    def spec(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """This is the "key" for naming the series within the file.
        A key->value description which should be unique for this series within the file
         with this series_type.
        """
        pass
    def __init__(self,
        *,
        series_type: typing.Text = ...,
        spec: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["series_type",b"series_type","spec",b"spec"]) -> None: ...
global___SeriesIdentifier = SeriesIdentifier
