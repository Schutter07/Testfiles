import opgave1_pagina76

def test1(capsys):
    getInteger_numbers = [2, 3, 4, 5, 6]
    opgave1_pagina76.getInteger = lambda n: getInteger_numbers.pop(0)
    getFloat_numbers = [2, 3, 4, 5, 6]
    opgave1_pagina76.getFloat = lambda n: getFloat_numbers.pop(0)
    input_values = [2, 3, 4, 5, 6]
    def mock_input(s):
        return input_values.pop(0)
    opgave1_pagina76.input = mock_input
    opgave1_pagina76.main()
    out, err = capsys.readouterr()
    assert out == 'Totaal is 20\nGemiddelde is 4.0\n'
    assert err == ''

def test2(capsys):
    getInteger_numbers = [-2, 3, -4, 5, -6]
    opgave1_pagina76.getInteger = lambda n: getInteger_numbers.pop(0)
    getFloat_numbers = [-2, 3, -4, 5, -6]
    opgave1_pagina76.getFloat = lambda n: getFloat_numbers.pop(0)
    input_values = [-2, 3, -4, 5, -6]
    def mock_input(s):
        return input_values.pop(0)
    opgave1_pagina76.input = mock_input
    opgave1_pagina76.main()
    out, err = capsys.readouterr()
    assert out == 'Totaal is -4\nGemiddelde is -0.8\n'
    assert err == ''

def test3(capsys):
    getInteger_numbers = [0, 0, 0, 0, 0]
    opgave1_pagina76.getInteger = lambda n: getInteger_numbers.pop(0)
    getFloat_numbers = [0, 0, 0, 0, 0]
    opgave1_pagina76.getFloat = lambda n: getFloat_numbers.pop(0)
    input_values = [0, 0, 0, 0, 0]
    def mock_input(s):
        return input_values.pop(0)
    opgave1_pagina76.input = mock_input
    opgave1_pagina76.main()
    out, err = capsys.readouterr()
    assert out == 'Totaal is 0\nGemiddelde is 0.0\n'
    assert err == ''