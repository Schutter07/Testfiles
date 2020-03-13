import opgave7_3

def test1(capsys):
    getInteger_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    opgave7_3.getInteger = lambda n: getInteger_numbers.pop(0)
    getFloat_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    opgave7_3.getFloat = lambda n: getFloat_numbers.pop(0)
    input_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    def mock_input(s):
        return input_values.pop(0)
    opgave7_3.input = mock_input
    opgave7_3.main()
    out, err = capsys.readouterr()
    assert out == 'Grootste is 10\nKleinste is 1\nAantal deelbaar door 3 is 3\n'
    assert err == ''

def test2(capsys):
    getInteger_numbers = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
    opgave7_3.getInteger = lambda n: getInteger_numbers.pop(0)
    getFloat_numbers = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
    opgave7_3.getFloat = lambda n: getFloat_numbers.pop(0)
    input_values = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
    def mock_input(s):
        return input_values.pop(0)
    opgave7_3.input = mock_input
    opgave7_3.main()
    out, err = capsys.readouterr()
    assert out == 'Grootste is 10\nKleinste is -9\nAantal deelbaar door 3 is 3\n'
    assert err == ''

def test3(capsys):
    getInteger_numbers = [3, 13, 23, 33, 43, 53, 63, 73, 83, 93]
    opgave7_3.getInteger = lambda n: getInteger_numbers.pop(0)
    getFloat_numbers = [3, 13, 23, 33, 43, 53, 63, 73, 83, 93]
    opgave7_3.getFloat = lambda n: getFloat_numbers.pop(0)
    input_values = [3, 13, 23, 33, 43, 53, 63, 73, 83, 93]
    def mock_input(s):
        return input_values.pop(0)
    opgave7_3.input = mock_input
    opgave7_3.main()
    out, err = capsys.readouterr()
    assert out == 'Grootste is 93\nKleinste is 3\nAantal deelbaar door 3 is 4\n'
    assert err == ''