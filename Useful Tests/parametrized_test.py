from utils import str_to_bool
import pytest


# def test_yes_is_true():
#     result = str_to_bool('yes')
#     assert result is True
#
#
# def test_y_is_true():
#     result = str_to_bool('y')
#     assert result is True


@pytest.mark.parametrize('value', ['yes', 'y', ''])
def test_is_true(value):
    result = str_to_bool(value)
    assert result is True


@pytest.mark.parametrize('value', ['N', 'no'])
def test_is_false(value):
    result = str_to_bool(value)
    assert result is False

