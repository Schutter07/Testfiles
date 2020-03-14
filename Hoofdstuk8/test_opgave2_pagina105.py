import opgave2_pagina105

def test1(capsys):
    out = opgave2_pagina105.isEven(7)
    assert out == False

def test2(capsys):
    out = opgave2_pagina105.isEven(72)
    assert out == True