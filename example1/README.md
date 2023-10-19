# Issue Summary

CrossHair Tool - Python
Usage of cover with pytest generates test cases with enums that are sometimes not compilable or are sort of useless (but
still these can be readable for human)
Consider following enum definitions:

```python
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

```

Result of running cover command on aff of them by analyzing below code

```python

def example_logic_with_enum_with_dataclass(myenum: Optional[CustomEnumZero]):
    if myenum == CustomEnumZero.ENUM_VALUE1:
        return myenum


def example_logic_with_enum_without_custom_repr(myenum: Optional[CustomEnumOne]):
    if myenum == CustomEnumOne.ENUM_VALUE1:
        return myenum


def example_logic_with_enum_with_repr(myenum: Optional[CustomEnumWithRepr]):
    if myenum == CustomEnumWithRepr.ENUM_VALUE1:
        return myenum
```

Gives the following Python source code output (fragments of tests generated):

```python
def test_example_logic_with_enum_with_dataclass_2():
    assert example_logic_with_enum_with_dataclass(CustomEnumZero()) == CustomEnumZero()


def test_example_logic_with_enum_without_custom_repr_2():
    assert example_logic_with_enum_without_custom_repr( < CustomEnumOne.ENUM_VALUE1: 1 >) == < CustomEnumOne.ENUM_VALUE1: 1 >


def test_example_logic_with_enum_with_repr_2():
    assert example_logic_with_enum_with_repr(CustomEnumWithRepr.ENUM_VALUE1) == CustomEnumWithRepr.ENUM_VALUE1

```

As we can see only the third one makes sense to Python interpreter.
The idea is to make this enum process definition with cover option clear for users.
