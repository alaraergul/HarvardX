import pytest
from bank import value

def test_value_hello():
    assert value("hello") == 0

def test_value_hello_with_punctuation():
    assert value("hello!") == 0

def test_value_Hello():
    assert value("Hello") == 0

def test_value_h():
    assert value("h") == 20

def test_value_H():
    assert value("H") == 20

def test_value_HelloThere():
    assert value("Hello there") == 0

def test_value_hi():
    assert value("hi") == 20

def test_value_greetings():
    assert value("greetings") == 100

def test_value_welcome():
    assert value("welcome") == 100

def test_value_empty_string():
    assert value("") == 100
