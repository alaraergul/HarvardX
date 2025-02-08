import pytest
from plates import is_valid

def test_valid_plate_with_no_digits():
    assert is_valid("ABC") == True

def test_valid_plate_with_digits():
    assert is_valid("AB123") == True

def test_valid_plate_with_leading_zeros():
    assert is_valid("AB01") == False

def test_invalid_plate_too_short():
    assert is_valid("A") == False

def test_invalid_plate_too_long():
    assert is_valid("ABCDEFGHI") == False

def test_invalid_plate_non_alpha_numeric():
    assert is_valid("AB!@#") == False

def test_invalid_plate_first_two_non_alpha():
    assert is_valid("1A2B") == False

def test_invalid_plate_digits_after_letters():
    assert is_valid("AB12C") == False

def test_valid_plate_exactly_six_characters():
    assert is_valid("ABC123") == True

def test_valid_plate_two_letters_followed_by_digits():
    assert is_valid("AB12") == True

def test_invalid_plate_no_initial_letters():
    assert is_valid("12AB") == False

def test_invalid_plate_with_special_characters():
    assert is_valid("AB#C") == False

if __name__ == "__main__":
    pytest.main()
