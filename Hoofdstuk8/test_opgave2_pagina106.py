import opgave2_pagina106
import pytest

def test1(capsys):
    out = opgave2_pagina106.getFractie(7.35)
    assert pytest.approx(out, 0.000001) == .35

def test2(capsys):
    out = opgave2_pagina106.getFractie(347.3543)
    assert pytest.approx(out, 0.000001) == .3543

def test3(capsys):
    out = opgave2_pagina106.getFractie(-7.325)
    assert pytest.approx(out, 0.000001) == .325

def test4(capsys):
    out = opgave2_pagina106.getFractie(123.45678)
    assert pytest.approx(out, 0.000001) == .45678
