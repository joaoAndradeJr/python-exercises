import pytest

from exercise_1 import fizzBuzz


def test_raizes_exception_when_fizzBuzz_with_no_parameter():
    with pytest.raises(TypeError):
        fizzBuzz()


def test_returned_list_fizzBuzz():
    assert fizzBuzz(3) is [1, 2, 'Fizz']
