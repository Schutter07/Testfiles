import opgave8_6
import pytest


def test1(capsys):
    out = opgave8_6.binom(1,1)
    assert out == pytest.approx(1, 0.0000001)

def test2(capsys):
    out = opgave8_6.binom(6,3)
    assert out == pytest.approx(20, 0.0000001)

def test3(capsys):
    out = opgave8_6.binom(9,4)
    assert out == pytest.approx(126, 0.0000001)

def test4(capsys):
    out = opgave8_6.binom(-1,1)
    assert out == pytest.approx(0, 0.0000001)

def test5(capsys):
    out = opgave8_6.binom(1,-10)
    assert out == pytest.approx(0, 0.0000001)

def test6(capsys):
    out = opgave8_6.binom(5,7)
    assert out == pytest.approx(0, 0.0000001)