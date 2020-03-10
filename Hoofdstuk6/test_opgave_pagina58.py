import opgave_pagina58

def test1(capsys):
    getInteger_numbers = [3]
    opgave_pagina58.getInteger = lambda n: getInteger_numbers.pop(0)
    input_values = [3]
    def mock_input(s):
        return input_values.pop(0)
    opgave_pagina58.input = mock_input
    opgave_pagina58.main()
    out, err = capsys.readouterr()
    assert out == 'oneven\n'
    assert err == ''

def test2(capsys):
    getInteger_numbers = [88]
    opgave_pagina58.getInteger = lambda n: getInteger_numbers.pop(0)
    input_values = [88]
    def mock_input(s):
        return input_values.pop(0)
    opgave_pagina58.input = mock_input
    opgave_pagina58.main()
    out, err = capsys.readouterr()
    assert out == 'even\n'
    assert err == ''