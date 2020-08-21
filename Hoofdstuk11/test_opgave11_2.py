import opgave11_2

def test1(capsys):
    out = opgave11_2.vermenigvuldig_complex((2, 0), (5, 0))
    assert out == (10, 0)

def test2(capsys):
    out = opgave11_2.vermenigvuldig_complex((2, 0), (0, 5))
    assert out == (0, 10)

def test3(capsys):
    out = opgave11_2.vermenigvuldig_complex((0, 2), (5, 0))
    assert out == (0, 10)

def test4(capsys):
    out = opgave11_2.vermenigvuldig_complex((2, 3), (5, 4))
    assert out == (-2, 23)