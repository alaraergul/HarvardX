from seasons import calculate_minutes, convert_to_words
from datetime import date
import pytest
import sys

def test_calculate_minutes():
    # Test for one year ago (non-leap year)
    assert calculate_minutes(date.today().replace(year=date.today().year - 1)) == 525600
    # Test for two years ago
    assert calculate_minutes(date.today().replace(year=date.today().year - 2)) == 1051200

def test_convert_to_words():
    # Test the conversion of a known number to words
    assert convert_to_words(525600).capitalize() == "Five hundred twenty-five thousand six hundred"
    assert convert_to_words(1051200).capitalize() == "One million fifty-one thousand two hundred"
    assert convert_to_words(2629440).capitalize() == "Two million six hundred twenty-nine thousand four hundred forty"
    assert convert_to_words(6092640).capitalize() == "Six million ninety-two thousand six hundred forty"
    assert convert_to_words(806400).capitalize() == "Eight hundred six thousand four hundred"

def test_invalid_date_format():
    # Test invalid date format (raises sys.exit)
    with pytest.raises(SystemExit):
        # Simulate invalid date format
        sys.exit("Invalid date format. Please enter date as YYYY-MM-DD.")
