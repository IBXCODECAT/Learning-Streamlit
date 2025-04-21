import pytest
from utility.sqrt import square_number

def test_square_number():
    assert square_number(2) == 4
    assert square_number(-3) == 9
    assert square_number(0) == 0