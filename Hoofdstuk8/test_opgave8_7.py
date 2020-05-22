import opgave8_7


def test1(capsys):
    out = opgave8_7.oppervlakte_van_driehoek(4.5, 1)
    assert out == 2.25

def test2(capsys):
    out = opgave8_7.oppervlakte_van_driehoek(32, 2)
    assert out == 32