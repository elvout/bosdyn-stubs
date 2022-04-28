"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Association(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MAC_ADDRESS_FIELD_NUMBER: builtins.int
    CONNECTED_TIME_FIELD_NUMBER: builtins.int
    RX_SIGNAL_DBM_FIELD_NUMBER: builtins.int
    RX_SIGNAL_AVG_DBM_FIELD_NUMBER: builtins.int
    RX_BEACON_SIGNAL_AVG_DBM_FIELD_NUMBER: builtins.int
    EXPECTED_BITS_PER_SECOND_FIELD_NUMBER: builtins.int
    RX_BYTES_FIELD_NUMBER: builtins.int
    RX_PACKETS_FIELD_NUMBER: builtins.int
    RX_BITS_PER_SECOND_FIELD_NUMBER: builtins.int
    TX_BYTES_FIELD_NUMBER: builtins.int
    TX_PACKETS_FIELD_NUMBER: builtins.int
    TX_BITS_PER_SECOND_FIELD_NUMBER: builtins.int
    TX_RETRIES_FIELD_NUMBER: builtins.int
    TX_FAILED_FIELD_NUMBER: builtins.int
    BEACONS_RECEIVED_FIELD_NUMBER: builtins.int
    BEACON_LOSS_COUNT_FIELD_NUMBER: builtins.int
    mac_address: typing.Text
    """MAC address of the associated station"""

    @property
    def connected_time(self) -> google.protobuf.duration_pb2.Duration:
        """Time duration since the station last connected."""
        pass
    rx_signal_dbm: builtins.int
    """Signal strength of last received packet"""

    rx_signal_avg_dbm: builtins.int
    """Signal strength average"""

    rx_beacon_signal_avg_dbm: builtins.int
    """Signal strength average for beacons only."""

    expected_bits_per_second: builtins.int
    """Expected throughput"""

    rx_bytes: builtins.int
    """Total received bytes"""

    rx_packets: builtins.int
    """Total received packets from the associated station"""

    rx_bits_per_second: builtins.int
    """Last unicast receive rate"""

    tx_bytes: builtins.int
    """Total transmitted bytes"""

    tx_packets: builtins.int
    """Total transmitted packets to the associated station"""

    tx_bits_per_second: builtins.int
    """Current unicast transmit rate"""

    tx_retries: builtins.int
    """Cumulative retry count to this station, within connected time"""

    tx_failed: builtins.int
    """Cumulative failed tx packet count to this station, within connected time"""

    beacons_received: builtins.int
    """Number of beacons received from this peer"""

    beacon_loss_count: builtins.int
    """Number of times beacon loss was detected"""

    def __init__(self,
        *,
        mac_address: typing.Text = ...,
        connected_time: typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        rx_signal_dbm: builtins.int = ...,
        rx_signal_avg_dbm: builtins.int = ...,
        rx_beacon_signal_avg_dbm: builtins.int = ...,
        expected_bits_per_second: builtins.int = ...,
        rx_bytes: builtins.int = ...,
        rx_packets: builtins.int = ...,
        rx_bits_per_second: builtins.int = ...,
        tx_bytes: builtins.int = ...,
        tx_packets: builtins.int = ...,
        tx_bits_per_second: builtins.int = ...,
        tx_retries: builtins.int = ...,
        tx_failed: builtins.int = ...,
        beacons_received: builtins.int = ...,
        beacon_loss_count: builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["connected_time",b"connected_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["beacon_loss_count",b"beacon_loss_count","beacons_received",b"beacons_received","connected_time",b"connected_time","expected_bits_per_second",b"expected_bits_per_second","mac_address",b"mac_address","rx_beacon_signal_avg_dbm",b"rx_beacon_signal_avg_dbm","rx_bits_per_second",b"rx_bits_per_second","rx_bytes",b"rx_bytes","rx_packets",b"rx_packets","rx_signal_avg_dbm",b"rx_signal_avg_dbm","rx_signal_dbm",b"rx_signal_dbm","tx_bits_per_second",b"tx_bits_per_second","tx_bytes",b"tx_bytes","tx_failed",b"tx_failed","tx_packets",b"tx_packets","tx_retries",b"tx_retries"]) -> None: ...
global___Association = Association

class WifiDevice(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Type:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[WifiDevice._Type.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNKNOWN: WifiDevice._Type.ValueType  # 0
        AP: WifiDevice._Type.ValueType  # 1
        CLIENT: WifiDevice._Type.ValueType  # 2
    class Type(_Type, metaclass=_TypeEnumTypeWrapper):
        pass

    UNKNOWN: WifiDevice.Type.ValueType  # 0
    AP: WifiDevice.Type.ValueType  # 1
    CLIENT: WifiDevice.Type.ValueType  # 2

    TYPE_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    MAC_ADDRESS_FIELD_NUMBER: builtins.int
    SSID_FIELD_NUMBER: builtins.int
    TX_POWER_DBM_FIELD_NUMBER: builtins.int
    ASSOCIATIONS_FIELD_NUMBER: builtins.int
    type: global___WifiDevice.Type.ValueType
    name: typing.Text
    mac_address: typing.Text
    ssid: typing.Text
    tx_power_dbm: builtins.int
    @property
    def associations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Association]: ...
    def __init__(self,
        *,
        type: global___WifiDevice.Type.ValueType = ...,
        name: typing.Text = ...,
        mac_address: typing.Text = ...,
        ssid: typing.Text = ...,
        tx_power_dbm: builtins.int = ...,
        associations: typing.Optional[typing.Iterable[global___Association]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["associations",b"associations","mac_address",b"mac_address","name",b"name","ssid",b"ssid","tx_power_dbm",b"tx_power_dbm","type",b"type"]) -> None: ...
global___WifiDevice = WifiDevice

class WifiStats(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HOSTNAME_FIELD_NUMBER: builtins.int
    DEVICES_FIELD_NUMBER: builtins.int
    hostname: typing.Text
    @property
    def devices(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___WifiDevice]: ...
    def __init__(self,
        *,
        hostname: typing.Text = ...,
        devices: typing.Optional[typing.Iterable[global___WifiDevice]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["devices",b"devices","hostname",b"hostname"]) -> None: ...
global___WifiStats = WifiStats