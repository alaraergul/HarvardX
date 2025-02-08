from um import count
import pytest

def test_single_um():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1

def test_multiple_ums():
    assert count("Um, thanks, um...") == 2
    assert count("um um um") == 3
    assert count("um? Um. uM!") == 3

def test_no_um():
    assert count("yummy") == 0
    assert count("umbrella") == 0
    assert count("hello world") == 0

def test_um_edge_cases():
    assert count("um.") == 1
    assert count("um, um") == 2
    assert count("YUM!") == 0
