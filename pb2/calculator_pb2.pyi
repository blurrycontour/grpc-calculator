from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CalcInput(_message.Message):
    __slots__ = ("a", "b")
    A_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    a: float
    b: float
    def __init__(self, a: _Optional[float] = ..., b: _Optional[float] = ...) -> None: ...

class CalcOutput(_message.Message):
    __slots__ = ("out",)
    OUT_FIELD_NUMBER: _ClassVar[int]
    out: float
    def __init__(self, out: _Optional[float] = ...) -> None: ...
