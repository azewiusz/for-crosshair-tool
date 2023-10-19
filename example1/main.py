from __future__ import annotations

import dataclasses
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class CustomEnumZero(Enum):
    ENUM_VALUE1 = 1
    ENUM_VALUE2 = 2
    ENUM_VALUE3 = 3


class CustomEnumOne(Enum):
    ENUM_VALUE1 = 1
    ENUM_VALUE2 = 2
    ENUM_VALUE3 = 3


class CustomEnumWithRepr(Enum):
    ENUM_VALUE1 = 1
    ENUM_VALUE2 = 2
    ENUM_VALUE3 = 3

    def __repr__(self):
        return str(self)


def example_logic_with_enum_with_dataclass(myenum: Optional[CustomEnumZero]):
    if myenum == CustomEnumZero.ENUM_VALUE1:
        return myenum


def example_logic_with_enum_without_custom_repr(myenum: Optional[CustomEnumOne]):
    if myenum == CustomEnumOne.ENUM_VALUE1:
        return myenum


def example_logic_with_enum_with_repr(myenum: Optional[CustomEnumWithRepr]):
    if myenum == CustomEnumWithRepr.ENUM_VALUE1:
        return myenum
