import opgave1_pagina161

def test1(capsys):
    input_values = ["Aron", "Chelsea", "Britt", "Evert", "David", ""]
    def mock_input(s):
        return input_values.pop(0)

    opgave1_pagina161.input = mock_input
    opgave1_pagina161.vriendenlijst()
    out, err = capsys.readouterr()
    assert out == 'Aron\nBritt\nChelsea\nDavid\nEvert\n'
    assert err == ''

def test2(capsys):
    input_values = ["Mark", "Kevin", "Evert", "David", ""]
    def mock_input(s):
        return input_values.pop(0)

    opgave1_pagina161.input = mock_input
    opgave1_pagina161.vriendenlijst()
    out, err = capsys.readouterr()
    assert out == 'David\nEvert\nKevin\nMark\n'
    assert err == ''