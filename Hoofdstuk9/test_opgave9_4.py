import opgave9_4


def test1(capsys):
    out = opgave9_4.ggd(1, 1)
    assert out == 1

def test2(capsys):
    out = opgave9_4.ggd(5, 35)
    assert out == 5

def test3(capsys):
    out = opgave9_4.ggd(35, 7)
    assert out == 7

def test4(capsys):
    out = opgave9_4.ggd(2*3*5*7, 2*5*11)
    assert out == 10

def test5(capsys):
    out = opgave9_4.ggd(3*5*13, 13*17)
    assert out == 13


