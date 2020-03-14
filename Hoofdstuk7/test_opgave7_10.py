import opgave7_10

def test1(capsys):
    getInteger_numbers = [1]
    opgave7_10.getInteger = lambda n: getInteger_numbers.pop(0)
    input_values = [1]
    def mock_input(s):
        return input_values.pop(0)
    opgave7_10.input = mock_input
    opgave7_10.main()
    out, err = capsys.readouterr()
    assert out == 'Het getal is niet priem!\n'
    assert err == ''

def test2(capsys):
    getInteger_numbers = [2]
    opgave7_10.getInteger = lambda n: getInteger_numbers.pop(0)
    input_values = [2]
    def mock_input(s):
        return input_values.pop(0)
    opgave7_10.input = mock_input
    opgave7_10.main()
    out, err = capsys.readouterr()
    assert out == 'Het getal is priem!\n'
    assert err == ''

def test3(capsys):
    getInteger_numbers = [3]
    opgave7_10.getInteger = lambda n: getInteger_numbers.pop(0)
    input_values = [3]
    def mock_input(s):
        return input_values.pop(0)
    opgave7_10.input = mock_input
    opgave7_10.main()
    out, err = capsys.readouterr()
    assert out == 'Het getal is priem!\n'
    assert err == ''

def test4(capsys):
    getInteger_numbers = [77]
    opgave7_10.getInteger = lambda n: getInteger_numbers.pop(0)
    input_values = [77]
    def mock_input(s):
        return input_values.pop(0)
    opgave7_10.input = mock_input
    opgave7_10.main()
    out, err = capsys.readouterr()
    assert out == 'Het getal is niet priem!\n'
    assert err == ''

def test5(capsys):
    getInteger_numbers = [41]
    opgave7_10.getInteger = lambda n: getInteger_numbers.pop(0)
    input_values = [41]
    def mock_input(s):
        return input_values.pop(0)
    opgave7_10.input = mock_input
    opgave7_10.main()
    out, err = capsys.readouterr()
    assert out == 'Het getal is priem!\n'
    assert err == ''

def test6(capsys):
    getInteger_numbers = [123457]
    opgave7_10.getInteger = lambda n: getInteger_numbers.pop(0)
    input_values = [123457]
    def mock_input(s):
        return input_values.pop(0)
    opgave7_10.input = mock_input
    opgave7_10.main()
    out, err = capsys.readouterr()
    assert out == 'Het getal is priem!\n'
    assert err == ''