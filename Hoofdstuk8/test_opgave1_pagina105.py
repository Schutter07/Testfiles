import opgave1_pagina105

def test1(capsys):
    opgave1_pagina105.printx()
    out, err = capsys.readouterr()
    assert out == 'x\n'
    assert err == ''

def test2(capsys):
    opgave1_pagina105.meerderex(5)
    out, err = capsys.readouterr()
    assert out == 'x\nx\nx\nx\nx\n'
    assert err == ''