import opgave_pagina20

def test1(capsys):
    input_values = []
    def mock_input(s):
        return input_values.pop(0)
    opgave_pagina20.input = mock_input
    opgave_pagina20.main()
    out, err = capsys.readouterr()
    assert out == '604800\n'
    assert err == ''
