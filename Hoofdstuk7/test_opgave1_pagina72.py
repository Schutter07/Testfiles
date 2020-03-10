import opgave1_pagina72

def test1(capsys):
    getInteger_numbers = [1, 2, 3, 4, 5, 0]
    opgave1_pagina72.getInteger = lambda n: getInteger_numbers.pop(0)
    getFloat_numbers = [1, 2, 3, 4, 5, 0]
    opgave1_pagina72.getFloat = lambda n: getFloat_numbers.pop(0)
    input_values = [1, 2, 3, 4, 5, 0]
    def mock_input(s):
        return input_values.pop(0)
    opgave1_pagina72.input = mock_input
    opgave1_pagina72.main()
    out, err = capsys.readouterr()
    assert out == 'Totaal is 15\nGemiddelde is 3.0\n'
    assert err == ''

def test2(capsys):
    getInteger_numbers = [0]
    opgave1_pagina72.getInteger = lambda n: getInteger_numbers.pop(0)
    getFloat_numbers = [0]
    opgave1_pagina72.getFloat = lambda n: getFloat_numbers.pop(0)
    input_values = [0]
    def mock_input(s):
        return input_values.pop(0)
    opgave1_pagina72.input = mock_input
    opgave1_pagina72.main()
    out, err = capsys.readouterr()
    assert out == 'Totaal is 0\nGemiddelde is 0\n'
    assert err == ''

def test3(capsys):
    getInteger_numbers = [-3, 4, -13, 2, 0]
    opgave1_pagina72.getInteger = lambda n: getInteger_numbers.pop(0)
    getFloat_numbers = [-3, 4, -13, 2, 0]
    opgave1_pagina72.getFloat = lambda n: getFloat_numbers.pop(0)
    input_values = [-3, 4, -13, 2, 0]
    def mock_input(s):
        return input_values.pop(0)
    opgave1_pagina72.input = mock_input
    opgave1_pagina72.main()
    out, err = capsys.readouterr()
    assert out == 'Totaal is -10\nGemiddelde is -2.5\n'
    assert err == ''