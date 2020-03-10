import opgave6_4

def test1(capsys):
    getInteger_numbers = [0, 0, 3]
    opgave6_4.getInteger = lambda n: getInteger_numbers.pop(0)
    getFloat_numbers = [0, 0, 3]
    opgave6_4.getFloat = lambda n: getFloat_numbers.pop(0)
    input_values = [0, 0, 3]
    def mock_input(s):
        return input_values.pop(0)
    opgave6_4.input = mock_input
    opgave6_4.main()
    out, err = capsys.readouterr()
    assert out == 'Er zijn geen oplossingen.\n'
    assert err == ''

def test2(capsys):
    getInteger_numbers = [1, 2, 30]
    opgave6_4.getInteger = lambda n: getInteger_numbers.pop(0)
    getFloat_numbers = [1, 2, 30]
    opgave6_4.getFloat = lambda n: getFloat_numbers.pop(0)
    input_values = [1, 2, 30]
    def mock_input(s):
        return input_values.pop(0)
    opgave6_4.input = mock_input
    opgave6_4.main()
    out, err = capsys.readouterr()
    assert out == 'Er zijn geen oplossingen.\n'
    assert err == ''

def test3(capsys):
    getInteger_numbers = [0, 3, 3]
    opgave6_4.getInteger = lambda n: getInteger_numbers.pop(0)
    getFloat_numbers = [0, 3, 3]
    opgave6_4.getFloat = lambda n: getFloat_numbers.pop(0)
    input_values = [0, 3, 3]
    def mock_input(s):
        return input_values.pop(0)
    opgave6_4.input = mock_input
    opgave6_4.main()
    out, err = capsys.readouterr()
    assert out == 'Er is 1 oplossing, namelijk x = -1.0\n'
    assert err == ''

def test4(capsys):
    getInteger_numbers = [1, 1, -6]
    opgave6_4.getInteger = lambda n: getInteger_numbers.pop(0)
    getFloat_numbers = [1, 1, -6]
    opgave6_4.getFloat = lambda n: getFloat_numbers.pop(0)
    input_values = [1, 1, -6]
    def mock_input(s):
        return input_values.pop(0)
    opgave6_4.input = mock_input
    opgave6_4.main()
    out, err = capsys.readouterr()
    assert out == 'Er zijn 2 oplossingen, namelijk x = 2.0 en x = -3.0\n'
    assert err == ''

def test5(capsys):
    getInteger_numbers = [2, 2, -12]
    opgave6_4.getInteger = lambda n: getInteger_numbers.pop(0)
    getFloat_numbers = [2, 2, -12]
    opgave6_4.getFloat = lambda n: getFloat_numbers.pop(0)
    input_values = [2, 2, -12]
    def mock_input(s):
        return input_values.pop(0)
    opgave6_4.input = mock_input
    opgave6_4.main()
    out, err = capsys.readouterr()
    assert out == 'Er zijn 2 oplossingen, namelijk x = 2.0 en x = -3.0\n'
    assert err == ''

def test6(capsys):
    getInteger_numbers = [4, 32, 64]
    opgave6_4.getInteger = lambda n: getInteger_numbers.pop(0)
    getFloat_numbers = [4, 32, 64]
    opgave6_4.getFloat = lambda n: getFloat_numbers.pop(0)
    input_values = [4, 32, 64]
    def mock_input(s):
        return input_values.pop(0)
    opgave6_4.input = mock_input
    opgave6_4.main()
    out, err = capsys.readouterr()
    assert out == 'Er is 1 oplossing, namelijk x = -4.0\n'
    assert err == ''