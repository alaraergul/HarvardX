import pytest

# Import the shorten function from the twttr module
from twttr import shorten

def test_shorten_basic():
    assert shorten("hello") == "hll"
    assert shorten("world") == "wrld"

def test_shorten_uppercase():
    assert shorten("HELLO") == "HLL"
    assert shorten("WORLD") == "WRLD"

def test_shorten_mixed_case():
    assert shorten("HeLLo WoRLD") == "HLL WRLD"

def test_shorten_no_vowels():
    assert shorten("bcd") == "bcd"
    assert shorten("XYZ") == "XYZ"

def test_shorten_all_vowels():
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""

def test_shorten_empty_string():
    assert shorten("") == ""

def test_shorten_single_character():
    assert shorten("a") == ""
    assert shorten("b") == "b"

if __name__ == "__main__":
    pytest.main()
