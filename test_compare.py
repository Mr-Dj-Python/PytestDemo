import pytest


def test_greater():
    num = 100
    assert num > 100


def test_greater_equal():
    num = 100
    assert num >= 100


def test_less():
    num = 100
    assert num < 200


@pytest.mark.great
def test_greater():
   num = 100
   assert num > 100


@pytest.mark.great
def test_greater_equal():
   num = 100
   assert num >= 100


@pytest.mark.others
def test_less():
   num = 100
   assert num < 200
