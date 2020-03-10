import opgave_pagina82

def test1(capsys):
    opgave_pagina82.main()
    out, err = capsys.readouterr()
    assert out == '(1,2)\n(1,3)\n(2,1)\n(2,3)\n(3,1)\n(3,2)\n'
    assert err == ''