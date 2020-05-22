import opgave8_4
import pytest


def test1(capsys):
    aantal, opl1, opl2 = opgave8_4.wortelformule(1, 4 ,4)
    assert aantal == 1
    assert pytest.approx(opl1, 0.000000001) == -2
    assert pytest.approx(opl2, 0.000000001) == 0

def test2(capsys):
    aantal, opl1, opl2 = opgave8_4.wortelformule(0, 4 ,3)
    assert aantal == 1
    assert pytest.approx(opl1, 0.000000001) == -0.75
    assert pytest.approx(opl2, 0.000000001) == 0

def test3(capsys):
    aantal, opl1, opl2 = opgave8_4.wortelformule(0, 0 ,4)
    assert aantal == 0
    assert pytest.approx(opl1, 0.000000001) == 0
    assert pytest.approx(opl2, 0.000000001) == 0

def test4(capsys):
    aantal, opl1, opl2 = opgave8_4.wortelformule(1, 0 ,4)
    assert aantal == 0
    assert pytest.approx(opl1, 0.000000001) == 0
    assert pytest.approx(opl2, 0.000000001) == 0

def test5(capsys):
    aantal, opl1, opl2 = opgave8_4.wortelformule(3, 4 ,-7)
    assert aantal == 2
    assert pytest.approx(opl1, 0.000000001) == 1.0
    assert pytest.approx(opl2, 0.000000001) == -2.3333333333333335