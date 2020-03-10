import opgave_pagina43

def test1(capsys):
    input_values = [3,4]
    def mock_input(s):
        return input_values.pop(0)
    opgave_pagina43.input = mock_input
    opgave_pagina43.main()
    out, err = capsys.readouterr()
    assert out == 'som: 7\nproduct: 12\n'
    assert err == ''

def test2(capsys):
    input_values = [3,-4]
    def mock_input(s):
        return input_values.pop(0)
    opgave_pagina43.input = mock_input
    opgave_pagina43.main()
    out, err = capsys.readouterr()
    assert out == 'som: -1\nproduct: -12\n'
    assert err == ''

def test3(capsys):
    input_values = [0,-4]
    def mock_input(s):
        return input_values.pop(0)
    opgave_pagina43.input = mock_input
    opgave_pagina43.main()
    out, err = capsys.readouterr()
    assert out == 'som: -4\nproduct: 0\n'
    assert err == ''

def test4(capsys):
    input_values = [35,27]
    def mock_input(s):
        return input_values.pop(0)
    opgave_pagina43.input = mock_input
    opgave_pagina43.main()
    out, err = capsys.readouterr()
    assert out == 'som: 62\nproduct: 945\n'
    assert err == ''