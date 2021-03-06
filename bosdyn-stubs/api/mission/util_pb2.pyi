"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _Result:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _ResultEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Result.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    RESULT_UNKNOWN: _Result.ValueType  # 0
    """Invalid, should not be used."""

    RESULT_FAILURE: _Result.ValueType  # 1
    """The node completed running, but failed."""

    RESULT_RUNNING: _Result.ValueType  # 2
    """The node is still in process and has not completed."""

    RESULT_SUCCESS: _Result.ValueType  # 3
    """The node completed, and succeeded."""

    RESULT_ERROR: _Result.ValueType  # 4
    """The node encountered an operational error while trying to execute."""

class Result(_Result, metaclass=_ResultEnumTypeWrapper):
    """Results from executing / ticking / running a single node."""
    pass

RESULT_UNKNOWN: Result.ValueType  # 0
"""Invalid, should not be used."""

RESULT_FAILURE: Result.ValueType  # 1
"""The node completed running, but failed."""

RESULT_RUNNING: Result.ValueType  # 2
"""The node is still in process and has not completed."""

RESULT_SUCCESS: Result.ValueType  # 3
"""The node completed, and succeeded."""

RESULT_ERROR: Result.ValueType  # 4
"""The node encountered an operational error while trying to execute."""

global___Result = Result


class KeyValue(google.protobuf.message.Message):
    """Key/Value pair, used in other messages."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    key: typing.Text
    @property
    def value(self) -> global___Value: ...
    def __init__(self,
        *,
        key: typing.Text = ...,
        value: typing.Optional[global___Value] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...
global___KeyValue = KeyValue

class Value(google.protobuf.message.Message):
    """A value of a run-time or compile-time variable."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CONSTANT_FIELD_NUMBER: builtins.int
    RUNTIME_VAR_FIELD_NUMBER: builtins.int
    PARAMETER_FIELD_NUMBER: builtins.int
    @property
    def constant(self) -> global___ConstantValue:
        """A constant value."""
        pass
    @property
    def runtime_var(self) -> global___VariableDeclaration:
        """Look up a variable provided at run-time."""
        pass
    @property
    def parameter(self) -> global___VariableDeclaration:
        """Look up a Node Parameter."""
        pass
    def __init__(self,
        *,
        constant: typing.Optional[global___ConstantValue] = ...,
        runtime_var: typing.Optional[global___VariableDeclaration] = ...,
        parameter: typing.Optional[global___VariableDeclaration] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["constant",b"constant","parameter",b"parameter","runtime_var",b"runtime_var","source",b"source"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["constant",b"constant","parameter",b"parameter","runtime_var",b"runtime_var","source",b"source"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["source",b"source"]) -> typing.Optional[typing_extensions.Literal["constant","runtime_var","parameter"]]: ...
global___Value = Value

class VariableDeclaration(google.protobuf.message.Message):
    """Declaration of a run-time or compile-time variable."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Type:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[VariableDeclaration._Type.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        TYPE_UNKNOWN: VariableDeclaration._Type.ValueType  # 0
        TYPE_FLOAT: VariableDeclaration._Type.ValueType  # 1
        TYPE_STRING: VariableDeclaration._Type.ValueType  # 2
        TYPE_INT: VariableDeclaration._Type.ValueType  # 3
        TYPE_BOOL: VariableDeclaration._Type.ValueType  # 4
        TYPE_MESSAGE: VariableDeclaration._Type.ValueType  # 5
    class Type(_Type, metaclass=_TypeEnumTypeWrapper):
        """Supported types for blackboard or parameter values."""
        pass

    TYPE_UNKNOWN: VariableDeclaration.Type.ValueType  # 0
    TYPE_FLOAT: VariableDeclaration.Type.ValueType  # 1
    TYPE_STRING: VariableDeclaration.Type.ValueType  # 2
    TYPE_INT: VariableDeclaration.Type.ValueType  # 3
    TYPE_BOOL: VariableDeclaration.Type.ValueType  # 4
    TYPE_MESSAGE: VariableDeclaration.Type.ValueType  # 5

    NAME_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    name: typing.Text
    """Name of the variable, to be used as the key in KeyValue pairs."""

    type: global___VariableDeclaration.Type.ValueType
    """Type that this variable is expected to have. Used to verify assignments and comparisons."""

    def __init__(self,
        *,
        name: typing.Text = ...,
        type: global___VariableDeclaration.Type.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name","type",b"type"]) -> None: ...
global___VariableDeclaration = VariableDeclaration

class ConstantValue(google.protobuf.message.Message):
    """A constant value. Corresponds to the VariableDeclaration Type enum."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FLOAT_VALUE_FIELD_NUMBER: builtins.int
    STRING_VALUE_FIELD_NUMBER: builtins.int
    INT_VALUE_FIELD_NUMBER: builtins.int
    BOOL_VALUE_FIELD_NUMBER: builtins.int
    MSG_VALUE_FIELD_NUMBER: builtins.int
    float_value: builtins.float
    string_value: typing.Text
    int_value: builtins.int
    bool_value: builtins.bool
    @property
    def msg_value(self) -> google.protobuf.any_pb2.Any: ...
    def __init__(self,
        *,
        float_value: builtins.float = ...,
        string_value: typing.Text = ...,
        int_value: builtins.int = ...,
        bool_value: builtins.bool = ...,
        msg_value: typing.Optional[google.protobuf.any_pb2.Any] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["bool_value",b"bool_value","float_value",b"float_value","int_value",b"int_value","msg_value",b"msg_value","string_value",b"string_value","value",b"value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["bool_value",b"bool_value","float_value",b"float_value","int_value",b"int_value","msg_value",b"msg_value","string_value",b"string_value","value",b"value"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["value",b"value"]) -> typing.Optional[typing_extensions.Literal["float_value","string_value","int_value","bool_value","msg_value"]]: ...
global___ConstantValue = ConstantValue

class UserData(google.protobuf.message.Message):
    """Data a user can associate with a node."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    BYTESTRING_FIELD_NUMBER: builtins.int
    id: typing.Text
    """Identifier. Enables matching the Node uploaded to the MissionService with the NodeInfo
    downloaded from the MissionService.
    """

    bytestring: builtins.bytes
    """Arbitrary data. We recommend keeping it small, to avoid bloating the size of the mission."""

    def __init__(self,
        *,
        id: typing.Text = ...,
        bytestring: builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["bytestring",b"bytestring","id",b"id"]) -> None: ...
global___UserData = UserData
