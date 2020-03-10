import opgave6_1

def test1(capsys):
    getFloat_numbers = [3]
    opgave6_1.getFloat = lambda n: getFloat_numbers.pop(0)
    input_values = [3]
    def mock_input(s):
        return input_values.pop(0)
    opgave6_1.input = mock_input
    opgave6_1.main()
    out, err = capsys.readouterr()
    assert out == 'F\n'
    assert err == ''

def test2(capsys):
    getFloat_numbers = [5]
    opgave6_1.getFloat = lambda n: getFloat_numbers.pop(0)
    input_values = [5]
    def mock_input(s):
        return input_values.pop(0)
    opgave6_1.input = mock_input
    opgave6_1.main()
    out, err = capsys.readouterr()
    assert out == 'F\n'
    assert err == ''

def test3(capsys):
    getFloat_numbers = [5.5]
    opgave6_1.getFloat = lambda n: getFloat_numbers.pop(0)
    input_values = [5.5]
    def mock_input(s):
        return input_values.pop(0)
    opgave6_1.input = mock_input
    opgave6_1.main()
    out, err = capsys.readouterr()
    assert out == 'D\n'
    assert err == ''

def test4(capsys):
    getFloat_numbers = [7]
    opgave6_1.getFloat = lambda n: getFloat_numbers.pop(0)
    input_values = [7]
    def mock_input(s):
        return input_values.pop(0)
    opgave6_1.input = mock_input
    opgave6_1.main()
    out, err = capsys.readouterr()
    assert out == 'C\n'
    assert err == ''

def test5(capsys):
    getFloat_numbers = [7.5]
    opgave6_1.getFloat = lambda n: getFloat_numbers.pop(0)
    input_values = [7.5]
    def mock_input(s):
        return input_values.pop(0)
    opgave6_1.input = mock_input
    opgave6_1.main()
    out, err = capsys.readouterr()
    assert out == 'B\n'
    assert err == ''

def test6(capsys):
    getFloat_numbers = [10]
    opgave6_1.getFloat = lambda n: getFloat_numbers.pop(0)
    input_values = [10]
    def mock_input(s):
        return input_values.pop(0)
    opgave6_1.input = mock_input
    opgave6_1.main()
    out, err = capsys.readouterr()
    assert out == 'A\n'
    assert err == ''