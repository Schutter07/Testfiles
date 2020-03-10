import opgave1_pagina71

def test1(capsys):
    getInteger_numbers = [3, 4, 5, 6, 7]
    opgave1_pagina71.getInteger = lambda n: getInteger_numbers.pop(0)
    getFloat_numbers = [3, 4, 5, 6, 7]
    opgave1_pagina71.getFloat = lambda n: getFloat_numbers.pop(0)
    input_values = [3, 4, 5, 6, 7]
    def mock_input(s):
        return input_values.pop(0)
    opgave1_pagina71.input = mock_input
    opgave1_pagina71.main()
    out, err = capsys.readouterr()
    assert out == 'Totaal is 25\nGemiddelde is 5.0\n'
    assert err == ''

def test2(capsys):
    getInteger_numbers = [4, 6, 8, 3, 2]
    opgave1_pagina71.getInteger = lambda n: getInteger_numbers.pop(0)
    getFloat_numbers = [4, 6, 8, 3, 2]
    opgave1_pagina71.getFloat = lambda n: getFloat_numbers.pop(0)
    input_values = [4, 6, 8, 3, 2]
    def mock_input(s):
        return input_values.pop(0)
    opgave1_pagina71.input = mock_input
    opgave1_pagina71.main()
    out, err = capsys.readouterr()
    assert out == 'Totaal is 23\nGemiddelde is 4.6\n'
    assert err == ''

def test3(capsys):
    getInteger_numbers = [-2, 3, -4, 5, -6]
    opgave1_pagina71.getInteger = lambda n: getInteger_numbers.pop(0)
    getFloat_numbers = [-2, 3, -4, 5, -6]
    opgave1_pagina71.getFloat = lambda n: getFloat_numbers.pop(0)
    input_values = [-2, 3, -4, 5, -6]
    def mock_input(s):
        return input_values.pop(0)
    opgave1_pagina71.input = mock_input
    opgave1_pagina71.main()
    out, err = capsys.readouterr()
    assert out == 'Totaal is -4\nGemiddelde is -0.8\n'
    assert err == ''