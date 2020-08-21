import opgave11_1

def test1(capsys):
    out = opgave11_1.optelling_complex((2, 3), (5, 3))
    assert out == (7, 6)

def test2(capsys):
    out = opgave11_1.optelling_complex((2, -3), (-5, 3))
    assert out == (-3, 0)

def test3(capsys):
    out = opgave11_1.optelling_complex((2.2, 3.3), (5.1, 3.2))
    assert out == (7.3, 6.5)