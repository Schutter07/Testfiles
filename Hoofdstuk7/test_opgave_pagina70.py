import opgave_pagina70

def test(capsys):
    opgave_pagina70.main()
    out, err = capsys.readouterr()
    assert out == '1\n3\n5\n7\n9\n'
    assert err == ''