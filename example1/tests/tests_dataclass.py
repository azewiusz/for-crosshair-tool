from main import example_logic_with_enum_with_dataclass


def test_example_logic_with_enum_with_dataclass():
    assert example_logic_with_enum_with_dataclass(None) == None


def test_example_logic_with_enum_with_dataclass_2():
    assert example_logic_with_enum_with_dataclass(CustomEnumZero()) == CustomEnumZero()
