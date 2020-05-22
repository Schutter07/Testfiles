import opgave1_pagina106

def test1(capsys):
    out = opgave1_pagina106.isOneven(1)
    assert out == True

def test2(capsys):
    out = opgave1_pagina106.isOneven(37)
    assert out == True

def test3(capsys):
    out = opgave1_pagina106.isOneven(42)
    assert out == False