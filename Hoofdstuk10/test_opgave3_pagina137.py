import opgave3_pagina137


def test1(capsys):
    out = opgave3_pagina137.alleen_letters("ph@t l00t")
    assert out == "ph t l  t"

def test2(capsys):
    out = opgave3_pagina137.alleen_letters("ph@t l00t T3ST ")
    assert out == "ph t l  t T ST "