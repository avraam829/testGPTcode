import os
import sys
import pytest

# Ensure root path for importing calculator
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from calculator import Calculator

@pytest.fixture
def calc() -> Calculator:
    return Calculator()

def test_add(calc: Calculator) -> None:
    assert calc.add(1, 2) == 3

def test_subtract(calc: Calculator) -> None:
    assert calc.subtract(5, 3) == 2

def test_multiply(calc: Calculator) -> None:
    assert calc.multiply(2, 4) == 8

def test_divide(calc: Calculator) -> None:
    assert calc.divide(8, 2) == 4

def test_power(calc: Calculator) -> None:
    assert calc.power(2, 3) == 8

def test_mod(calc: Calculator) -> None:
    assert calc.mod(8, 3) == 2

def test_divide_by_zero(calc: Calculator) -> None:
    with pytest.raises(ValueError):
        calc.divide(5, 0)

def test_mod_by_zero(calc: Calculator) -> None:
    with pytest.raises(ValueError):
        calc.mod(5, 0)
