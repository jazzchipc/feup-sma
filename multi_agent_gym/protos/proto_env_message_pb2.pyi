# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
    Union as typing___Union,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


class ActionInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def sub_env_info(self) -> SubEnvInfo: ...

    @property
    def action(self) -> NDArray: ...

    def __init__(self,
        *,
        sub_env_info : typing___Optional[SubEnvInfo] = None,
        action : typing___Optional[NDArray] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ActionInfo: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ActionInfo: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"action",u"sub_env_info"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"action",u"sub_env_info"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"action",b"action",u"sub_env_info",b"sub_env_info"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"action",b"action",u"sub_env_info",b"sub_env_info"]) -> None: ...

class Observation(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    reward = ... # type: builtin___float
    done = ... # type: builtin___bool
    info = ... # type: typing___Text

    @property
    def observation(self) -> NDArray: ...

    def __init__(self,
        *,
        observation : typing___Optional[NDArray] = None,
        reward : typing___Optional[builtin___float] = None,
        done : typing___Optional[builtin___bool] = None,
        info : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Observation: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Observation: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"observation"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"done",u"info",u"observation",u"reward"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"observation",b"observation"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"done",b"done",u"info",b"info",u"observation",b"observation",u"reward",b"reward"]) -> None: ...

class InitialObservation(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def observation(self) -> NDArray: ...

    def __init__(self,
        *,
        observation : typing___Optional[NDArray] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> InitialObservation: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> InitialObservation: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"observation"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"observation"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"observation",b"observation"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"observation",b"observation"]) -> None: ...

class NDArray(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ndarray = ... # type: builtin___bytes

    def __init__(self,
        *,
        ndarray : typing___Optional[builtin___bytes] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> NDArray: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> NDArray: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"ndarray"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"ndarray",b"ndarray"]) -> None: ...

class SubEnvInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    sub_env_id = ... # type: typing___Text

    def __init__(self,
        *,
        sub_env_id : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> SubEnvInfo: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> SubEnvInfo: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"sub_env_id"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"sub_env_id",b"sub_env_id"]) -> None: ...
