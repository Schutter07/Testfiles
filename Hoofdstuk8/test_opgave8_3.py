import opgave8_3
import pytest

def test1(capsys):
    out = opgave8_3.leibniz(1)
    assert pytest.approx(out, 0.000000001) == 4.0

def test2(capsys):
    out = opgave8_3.leibniz(2)
    assert pytest.approx(out, 0.000000001) == 2.666666666666667

def test3(capsys):
    out = opgave8_3.leibniz(3)
    assert pytest.approx(out, 0.000000001) == 3.466666666666667

def test4(capsys):
    out = opgave8_3.leibniz(4)
    assert pytest.approx(out, 0.000000001) == 2.8952380952380956

def test5(capsys):
    out = opgave8_3.leibniz(5)
    assert pytest.approx(out, 0.000000001) == 3.3396825396825403

def test50(capsys):
    out = opgave8_3.leibniz(50)
    assert pytest.approx(out, 0.000000001) == 3.121594652591011