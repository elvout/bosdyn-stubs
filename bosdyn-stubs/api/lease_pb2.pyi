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
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Lease(google.protobuf.message.Message):
    """Leases are used to verify that a client has exclusive access to a shared
    resources. Examples of shared resources are the motors for a robot, or
    indicator lights on a robot.
    Leases are initially obtained by clients from the LeaseService. Clients
    then attach Leases to Commands which require them. Clients may also
    generate sub-Leases to delegate out control of the resource to other
    services.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RESOURCE_FIELD_NUMBER: builtins.int
    EPOCH_FIELD_NUMBER: builtins.int
    SEQUENCE_FIELD_NUMBER: builtins.int
    CLIENT_NAMES_FIELD_NUMBER: builtins.int
    resource: typing.Text
    """The resource that the Lease is for."""

    epoch: typing.Text
    """The epoch for the Lease. The sequences field are scoped to a particular epoch.
    One example of where this can be used is to generate a random epoch
    at LeaseService startup.
    """

    @property
    def sequence(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """Logical vector clock indicating when the Lease was generated."""
        pass
    @property
    def client_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """The set of different clients which have sent/receieved the lease."""
        pass
    def __init__(self,
        *,
        resource: typing.Text = ...,
        epoch: typing.Text = ...,
        sequence: typing.Optional[typing.Iterable[builtins.int]] = ...,
        client_names: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["client_names",b"client_names","epoch",b"epoch","resource",b"resource","sequence",b"sequence"]) -> None: ...
global___Lease = Lease

class ResourceTree(google.protobuf.message.Message):
    """Lease resources can be divided into a hierarchy of sub-resources that can
    be commanded together. This message describes the hierarchy of a resource.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RESOURCE_FIELD_NUMBER: builtins.int
    SUB_RESOURCES_FIELD_NUMBER: builtins.int
    resource: typing.Text
    """The name of this resource."""

    @property
    def sub_resources(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ResourceTree]:
        """Sub-resources that make up this resource."""
        pass
    def __init__(self,
        *,
        resource: typing.Text = ...,
        sub_resources: typing.Optional[typing.Iterable[global___ResourceTree]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource",b"resource","sub_resources",b"sub_resources"]) -> None: ...
global___ResourceTree = ResourceTree

class LeaseOwner(google.protobuf.message.Message):
    """Details about who currently owns the Lease for a resource."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLIENT_NAME_FIELD_NUMBER: builtins.int
    USER_NAME_FIELD_NUMBER: builtins.int
    client_name: typing.Text
    """The name of the client application."""

    user_name: typing.Text
    """The name of the user."""

    def __init__(self,
        *,
        client_name: typing.Text = ...,
        user_name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["client_name",b"client_name","user_name",b"user_name"]) -> None: ...
global___LeaseOwner = LeaseOwner

class LeaseUseResult(google.protobuf.message.Message):
    """Result for when a Lease is used - for example, in a LeaseRetainer, or
    associated with a command.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Status:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[LeaseUseResult._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNKNOWN: LeaseUseResult._Status.ValueType  # 0
        """An internal issue occurred."""

        STATUS_OK: LeaseUseResult._Status.ValueType  # 1
        """The Lease was accepted."""

        STATUS_INVALID_LEASE: LeaseUseResult._Status.ValueType  # 2
        """The Lease is invalid."""

        STATUS_OLDER: LeaseUseResult._Status.ValueType  # 3
        """The Lease is older than the current lease, and rejected."""

        STATUS_REVOKED: LeaseUseResult._Status.ValueType  # 4
        """The Lease holder did not check in regularly enough, and the Lease is stale."""

        STATUS_UNMANAGED: LeaseUseResult._Status.ValueType  # 5
        """The Lease was for an unmanaged resource."""

        STATUS_WRONG_EPOCH: LeaseUseResult._Status.ValueType  # 6
        """The Lease was for the wrong epoch."""

    class Status(_Status, metaclass=_StatusEnumTypeWrapper):
        pass

    STATUS_UNKNOWN: LeaseUseResult.Status.ValueType  # 0
    """An internal issue occurred."""

    STATUS_OK: LeaseUseResult.Status.ValueType  # 1
    """The Lease was accepted."""

    STATUS_INVALID_LEASE: LeaseUseResult.Status.ValueType  # 2
    """The Lease is invalid."""

    STATUS_OLDER: LeaseUseResult.Status.ValueType  # 3
    """The Lease is older than the current lease, and rejected."""

    STATUS_REVOKED: LeaseUseResult.Status.ValueType  # 4
    """The Lease holder did not check in regularly enough, and the Lease is stale."""

    STATUS_UNMANAGED: LeaseUseResult.Status.ValueType  # 5
    """The Lease was for an unmanaged resource."""

    STATUS_WRONG_EPOCH: LeaseUseResult.Status.ValueType  # 6
    """The Lease was for the wrong epoch."""


    STATUS_FIELD_NUMBER: builtins.int
    OWNER_FIELD_NUMBER: builtins.int
    ATTEMPTED_LEASE_FIELD_NUMBER: builtins.int
    PREVIOUS_LEASE_FIELD_NUMBER: builtins.int
    LATEST_KNOWN_LEASE_FIELD_NUMBER: builtins.int
    LATEST_RESOURCES_FIELD_NUMBER: builtins.int
    status: global___LeaseUseResult.Status.ValueType
    @property
    def owner(self) -> global___LeaseOwner:
        """The current lease owner."""
        pass
    @property
    def attempted_lease(self) -> global___Lease:
        """The lease which was attempted for use."""
        pass
    @property
    def previous_lease(self) -> global___Lease:
        """The previous lease, if any, which was used."""
        pass
    @property
    def latest_known_lease(self) -> global___Lease:
        """The "latest"/"most recent" lease known to the system."""
        pass
    @property
    def latest_resources(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Lease]:
        """Represents the latest "leaf" resources of the hierarchy."""
        pass
    def __init__(self,
        *,
        status: global___LeaseUseResult.Status.ValueType = ...,
        owner: typing.Optional[global___LeaseOwner] = ...,
        attempted_lease: typing.Optional[global___Lease] = ...,
        previous_lease: typing.Optional[global___Lease] = ...,
        latest_known_lease: typing.Optional[global___Lease] = ...,
        latest_resources: typing.Optional[typing.Iterable[global___Lease]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["attempted_lease",b"attempted_lease","latest_known_lease",b"latest_known_lease","owner",b"owner","previous_lease",b"previous_lease"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["attempted_lease",b"attempted_lease","latest_known_lease",b"latest_known_lease","latest_resources",b"latest_resources","owner",b"owner","previous_lease",b"previous_lease","status",b"status"]) -> None: ...
global___LeaseUseResult = LeaseUseResult

class AcquireLeaseRequest(google.protobuf.message.Message):
    """The AcquireLease request message which sends which resource the lease should be for."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    RESOURCE_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.RequestHeader:
        """Common request header."""
        pass
    resource: typing.Text
    """The resource to obtain a Lease for."""

    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.RequestHeader] = ...,
        resource: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header","resource",b"resource"]) -> None: ...
global___AcquireLeaseRequest = AcquireLeaseRequest

class AcquireLeaseResponse(google.protobuf.message.Message):
    """The AcquireLease response returns the lease for the desired resource if it could be obtained.
    If a client is returned a new lease, the client should initiate a
    RetainLease bidirectional streaming request immediately after completion
    of AcquireLease.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Status:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[AcquireLeaseResponse._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNKNOWN: AcquireLeaseResponse._Status.ValueType  # 0
        """UNKNOWN should never be used. An internal LeaseService issue has happened
        if UNKNOWN is set.
        """

        STATUS_OK: AcquireLeaseResponse._Status.ValueType  # 1
        """AcquireLease was successful.The lease field will be populated with the new
        lease for the resource. The client is expected to call the RetainLease method
        immediately after.
        """

        STATUS_RESOURCE_ALREADY_CLAIMED: AcquireLeaseResponse._Status.ValueType  # 2
        """AcquireLease failed since the resource has already been claimed.
        The TakeLease method may be used to forcefully grab the lease.
        """

        STATUS_INVALID_RESOURCE: AcquireLeaseResponse._Status.ValueType  # 3
        """AcquireLease failed since the resource is not known to LeaseService.
        The ListLeaseResources method may be used to list all known
        resources.
        """

        STATUS_NOT_AUTHORITATIVE_SERVICE: AcquireLeaseResponse._Status.ValueType  # 4
        """The LeaseService is not authoritative - so Acquire should not work."""

    class Status(_Status, metaclass=_StatusEnumTypeWrapper):
        pass

    STATUS_UNKNOWN: AcquireLeaseResponse.Status.ValueType  # 0
    """UNKNOWN should never be used. An internal LeaseService issue has happened
    if UNKNOWN is set.
    """

    STATUS_OK: AcquireLeaseResponse.Status.ValueType  # 1
    """AcquireLease was successful.The lease field will be populated with the new
    lease for the resource. The client is expected to call the RetainLease method
    immediately after.
    """

    STATUS_RESOURCE_ALREADY_CLAIMED: AcquireLeaseResponse.Status.ValueType  # 2
    """AcquireLease failed since the resource has already been claimed.
    The TakeLease method may be used to forcefully grab the lease.
    """

    STATUS_INVALID_RESOURCE: AcquireLeaseResponse.Status.ValueType  # 3
    """AcquireLease failed since the resource is not known to LeaseService.
    The ListLeaseResources method may be used to list all known
    resources.
    """

    STATUS_NOT_AUTHORITATIVE_SERVICE: AcquireLeaseResponse.Status.ValueType  # 4
    """The LeaseService is not authoritative - so Acquire should not work."""


    HEADER_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    LEASE_FIELD_NUMBER: builtins.int
    LEASE_OWNER_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.ResponseHeader:
        """Common response Header."""
        pass
    status: global___AcquireLeaseResponse.Status.ValueType
    """Return status for the request."""

    @property
    def lease(self) -> global___Lease:
        """The lease for the resource. Only set if status field == STATUS_OK."""
        pass
    @property
    def lease_owner(self) -> global___LeaseOwner:
        """The owner for the lease. Set if status field == OK or status field == RESOURCE_ALREADY_CLAIMED."""
        pass
    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.ResponseHeader] = ...,
        status: global___AcquireLeaseResponse.Status.ValueType = ...,
        lease: typing.Optional[global___Lease] = ...,
        lease_owner: typing.Optional[global___LeaseOwner] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header","lease",b"lease","lease_owner",b"lease_owner"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header","lease",b"lease","lease_owner",b"lease_owner","status",b"status"]) -> None: ...
global___AcquireLeaseResponse = AcquireLeaseResponse

class TakeLeaseRequest(google.protobuf.message.Message):
    """The TakeLease request message which sends which resource the lease should be for."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    RESOURCE_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.RequestHeader:
        """Common request header."""
        pass
    resource: typing.Text
    """The resource to obtain a Lease for."""

    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.RequestHeader] = ...,
        resource: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header","resource",b"resource"]) -> None: ...
global___TakeLeaseRequest = TakeLeaseRequest

class TakeLeaseResponse(google.protobuf.message.Message):
    """The TakeLease response returns the lease for the desired resource if it could be obtained.
    In most cases if the resource is managed by the LeaseService, TakeLease
    will succeed. However, in the future policies may be introduced which will prevent
    TakeLease from succeeding and clients should be prepared to handle that
    case.
    If a client obtains a new lease, the client should initiate a
    RetainLease bidirectional streaming request immediately after completion
    of TakeLease.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Status:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[TakeLeaseResponse._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNKNOWN: TakeLeaseResponse._Status.ValueType  # 0
        """UNKNOWN should never be used. An internal LeaseService issue has happened if UNKNOWN is set."""

        STATUS_OK: TakeLeaseResponse._Status.ValueType  # 1
        """TakeLease was successful. The lease field will be populated with the
        new lease for the resource. The client is expected to call the RetainLease
        method immediately after.
        """

        STATUS_INVALID_RESOURCE: TakeLeaseResponse._Status.ValueType  # 2
        """TakeLease failed since the resource is not known to LeaseService.
        The ListLeaseResources method may be used to list all known
        resources.
        """

        STATUS_NOT_AUTHORITATIVE_SERVICE: TakeLeaseResponse._Status.ValueType  # 3
        """The LeaseService is not authoritative - so Acquire should not work."""

    class Status(_Status, metaclass=_StatusEnumTypeWrapper):
        pass

    STATUS_UNKNOWN: TakeLeaseResponse.Status.ValueType  # 0
    """UNKNOWN should never be used. An internal LeaseService issue has happened if UNKNOWN is set."""

    STATUS_OK: TakeLeaseResponse.Status.ValueType  # 1
    """TakeLease was successful. The lease field will be populated with the
    new lease for the resource. The client is expected to call the RetainLease
    method immediately after.
    """

    STATUS_INVALID_RESOURCE: TakeLeaseResponse.Status.ValueType  # 2
    """TakeLease failed since the resource is not known to LeaseService.
    The ListLeaseResources method may be used to list all known
    resources.
    """

    STATUS_NOT_AUTHORITATIVE_SERVICE: TakeLeaseResponse.Status.ValueType  # 3
    """The LeaseService is not authoritative - so Acquire should not work."""


    HEADER_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    LEASE_FIELD_NUMBER: builtins.int
    LEASE_OWNER_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.ResponseHeader:
        """Common response header."""
        pass
    status: global___TakeLeaseResponse.Status.ValueType
    """Return status for the request."""

    @property
    def lease(self) -> global___Lease:
        """The lease for the resource. Only set if status field == STATUS_OK."""
        pass
    @property
    def lease_owner(self) -> global___LeaseOwner:
        """The owner for the lease. Set if status field == STATUS_OK."""
        pass
    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.ResponseHeader] = ...,
        status: global___TakeLeaseResponse.Status.ValueType = ...,
        lease: typing.Optional[global___Lease] = ...,
        lease_owner: typing.Optional[global___LeaseOwner] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header","lease",b"lease","lease_owner",b"lease_owner"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header","lease",b"lease","lease_owner",b"lease_owner","status",b"status"]) -> None: ...
global___TakeLeaseResponse = TakeLeaseResponse

class ReturnLeaseRequest(google.protobuf.message.Message):
    """The ReturnLease request message will be sent to the LeaseService. If the lease
    is currently active for the resource, the LeaseService will invalidate the lease.
    Future calls to AcquireLease by any client will now succeed.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    LEASE_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.RequestHeader:
        """Common request header."""
        pass
    @property
    def lease(self) -> global___Lease:
        """The Lease to return back to the LeaseService."""
        pass
    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.RequestHeader] = ...,
        lease: typing.Optional[global___Lease] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header","lease",b"lease"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header","lease",b"lease"]) -> None: ...
global___ReturnLeaseRequest = ReturnLeaseRequest

class ReturnLeaseResponse(google.protobuf.message.Message):
    """The ReturnLease response message"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Status:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[ReturnLeaseResponse._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNKNOWN: ReturnLeaseResponse._Status.ValueType  # 0
        """UNKNOWN should never be used. An internal LeaseService issue has happened if UNKNOWN is set."""

        STATUS_OK: ReturnLeaseResponse._Status.ValueType  # 1
        """ReturnLease was successful."""

        STATUS_INVALID_RESOURCE: ReturnLeaseResponse._Status.ValueType  # 2
        """ReturnLease failed because the resource covered by the lease
        is not being managed by the LeaseService.
        """

        STATUS_NOT_ACTIVE_LEASE: ReturnLeaseResponse._Status.ValueType  # 3
        """ReturnLease failed because the lease was not the active lease."""

        STATUS_NOT_AUTHORITATIVE_SERVICE: ReturnLeaseResponse._Status.ValueType  # 4
        """The LeaseService is not authoritative - so Acquire should not work."""

    class Status(_Status, metaclass=_StatusEnumTypeWrapper):
        pass

    STATUS_UNKNOWN: ReturnLeaseResponse.Status.ValueType  # 0
    """UNKNOWN should never be used. An internal LeaseService issue has happened if UNKNOWN is set."""

    STATUS_OK: ReturnLeaseResponse.Status.ValueType  # 1
    """ReturnLease was successful."""

    STATUS_INVALID_RESOURCE: ReturnLeaseResponse.Status.ValueType  # 2
    """ReturnLease failed because the resource covered by the lease
    is not being managed by the LeaseService.
    """

    STATUS_NOT_ACTIVE_LEASE: ReturnLeaseResponse.Status.ValueType  # 3
    """ReturnLease failed because the lease was not the active lease."""

    STATUS_NOT_AUTHORITATIVE_SERVICE: ReturnLeaseResponse.Status.ValueType  # 4
    """The LeaseService is not authoritative - so Acquire should not work."""


    HEADER_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.ResponseHeader:
        """Common response header."""
        pass
    status: global___ReturnLeaseResponse.Status.ValueType
    """Return status for the request."""

    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.ResponseHeader] = ...,
        status: global___ReturnLeaseResponse.Status.ValueType = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header","status",b"status"]) -> None: ...
global___ReturnLeaseResponse = ReturnLeaseResponse

class ListLeasesRequest(google.protobuf.message.Message):
    """The ListLease request message asks for information about any known lease resources."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    INCLUDE_FULL_LEASE_INFO_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.RequestHeader:
        """Common request header."""
        pass
    include_full_lease_info: builtins.bool
    """Include the full data of leases in use, if available.
    Defaults to false to receive basic information.
    """

    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.RequestHeader] = ...,
        include_full_lease_info: builtins.bool = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header","include_full_lease_info",b"include_full_lease_info"]) -> None: ...
global___ListLeasesRequest = ListLeasesRequest

class LeaseResource(google.protobuf.message.Message):
    """Describes all information about a sepcific lease: including the resource it covers, the
    active lease, and which application is the owner of a lease.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RESOURCE_FIELD_NUMBER: builtins.int
    LEASE_FIELD_NUMBER: builtins.int
    LEASE_OWNER_FIELD_NUMBER: builtins.int
    resource: typing.Text
    """The resource name."""

    @property
    def lease(self) -> global___Lease:
        """The active lease, if any."""
        pass
    @property
    def lease_owner(self) -> global___LeaseOwner:
        """The Lease Owner, if there is a Lease."""
        pass
    def __init__(self,
        *,
        resource: typing.Text = ...,
        lease: typing.Optional[global___Lease] = ...,
        lease_owner: typing.Optional[global___LeaseOwner] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["lease",b"lease","lease_owner",b"lease_owner"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["lease",b"lease","lease_owner",b"lease_owner","resource",b"resource"]) -> None: ...
global___LeaseResource = LeaseResource

class ListLeasesResponse(google.protobuf.message.Message):
    """The ListLease response message returns all known lease resources from the LeaseService."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    RESOURCES_FIELD_NUMBER: builtins.int
    RESOURCE_TREE_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.ResponseHeader:
        """Common response header."""
        pass
    @property
    def resources(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___LeaseResource]:
        """The resources managed by the LeaseService."""
        pass
    @property
    def resource_tree(self) -> global___ResourceTree:
        """Provide the hierarchical lease structure.
        A resource can encapsulate multiple sub-resources.
        For example, the "body" lease may include control of the legs, arm, and gripper.
        """
        pass
    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.ResponseHeader] = ...,
        resources: typing.Optional[typing.Iterable[global___LeaseResource]] = ...,
        resource_tree: typing.Optional[global___ResourceTree] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header","resource_tree",b"resource_tree"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header","resource_tree",b"resource_tree","resources",b"resources"]) -> None: ...
global___ListLeasesResponse = ListLeasesResponse

class RetainLeaseRequest(google.protobuf.message.Message):
    """The RetainLease request will inform the LeaseService that the application contains to hold
    ownership of this lease. Lease holders are expected to be reachable and alive. If enough time
    has passed since the last RetainLeaseRequest, the LeaseService will revoke the lease.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    LEASE_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.RequestHeader:
        """Common request header."""
        pass
    @property
    def lease(self) -> global___Lease:
        """The Lease to retain ownership over. May also be a "super" lease of the lease to retain
        ownership over.
        """
        pass
    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.RequestHeader] = ...,
        lease: typing.Optional[global___Lease] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header","lease",b"lease"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header","lease",b"lease"]) -> None: ...
global___RetainLeaseRequest = RetainLeaseRequest

class RetainLeaseResponse(google.protobuf.message.Message):
    """The RetainLease response message sends the result of the attempted RetainLease request, which
    contains whether or not the lease is still owned by the application sending the request.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    LEASE_USE_RESULT_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> bosdyn.api.header_pb2.ResponseHeader:
        """Common response header."""
        pass
    @property
    def lease_use_result(self) -> global___LeaseUseResult:
        """Result of using the lease."""
        pass
    def __init__(self,
        *,
        header: typing.Optional[bosdyn.api.header_pb2.ResponseHeader] = ...,
        lease_use_result: typing.Optional[global___LeaseUseResult] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header","lease_use_result",b"lease_use_result"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header","lease_use_result",b"lease_use_result"]) -> None: ...
global___RetainLeaseResponse = RetainLeaseResponse
