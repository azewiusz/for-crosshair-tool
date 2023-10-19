from main import example_logic_with_enum_with_repr


def test_example_logic_with_enum_with_repr():
    assert example_logic_with_enum_with_repr(None) == None


def test_example_logic_with_enum_with_repr_2():
    assert example_logic_with_enum_with_repr(CustomEnumWithRepr.ENUM_VALUE1) == CustomEnumWithRepr.ENUM_VALUE1
