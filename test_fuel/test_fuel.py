import pytest
from fuel import convert, gauge

def test_valid_fraction_conversion():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("5/10") == 50

def test_fraction_with_zero_denominator():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_fraction_with_non_integer_numerator_or_denominator():
    with pytest.raises(ValueError):
        convert("a/b")
    with pytest.raises(ValueError):
        convert("1/b")
    with pytest.raises(ValueError):
        convert("a/2")

def test_fraction_with_numerator_greater_than_denominator():
    with pytest.raises(ValueError):
        convert("3/2")

def test_gauge_boundaries():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"

if __name__ == "__main__":
    pytest.main()
