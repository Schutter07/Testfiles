import opgave9_1


def test1(capsys):
    out = opgave9_1.fib(1)
    assert out == 1

def test2(capsys):
    out = opgave9_1.fib(2)
    assert out == 1

def test3(capsys):
    out = opgave9_1.fib(3)
    assert out == 2

def test4(capsys):
    out = opgave9_1.fib(4)
    assert out == 3

def test5(capsys):
    out = opgave9_1.fib(5)
    assert out == 5

def test6(capsys):
    out = opgave9_1.fib(9)
    assert out == 34

def test7(capsys):
    out = opgave9_1.fib(30)
    assert out == 832040

