import opgave2_pagina75

def test1(capsys):
    opgave2_pagina75.main()
    out, err = capsys.readouterr()
    assert out == '21\n18\n15\n12\n9\n6\n3\n'
    assert err == ''