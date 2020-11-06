import math

import pytest


def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5


def testsquare():
    num = 7
    assert 7 * 7 == 40


def teset_quality():
    assert 10 == 11


@pytest.mark.square
def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5


@pytest.mark.square
def testsquare():
    num = 7
    assert 7 * 7 == 40


@pytest.mark.others
def test_equality():
    assert 10 == 11
