import opgave7_1

def test1(capsys):
    getInteger_numbers = [12]
    opgave7_1.getInteger = lambda n: getInteger_numbers.pop(0)
    getFloat_numbers = [12]
    opgave7_1.getFloat = lambda n: getFloat_numbers.pop(0)
    input_values = [12]
    def mock_input(s):
        return input_values.pop(0)
    opgave7_1.input = mock_input
    opgave7_1.main()
    out, err = capsys.readouterr()
    assert out == '1 * 12 = 12\n2 * 12 = 24\n3 * 12 = 36\n4 * 12 = 48\n5 * 12 = 60\n6 * 12 = 72\n7 * 12 = 84\n8 * 12 = 96\n9 * 12 = 108\n10 * 12 = 120\n'
    assert err == ''

def test2(capsys):
    getInteger_numbers = [10]
    opgave7_1.getInteger = lambda n: getInteger_numbers.pop(0)
    getFloat_numbers = [10]
    opgave7_1.getFloat = lambda n: getFloat_numbers.pop(0)
    input_values = [10]
    def mock_input(s):
        return input_values.pop(0)
    opgave7_1.input = mock_input
    opgave7_1.main()
    out, err = capsys.readouterr()
    assert out == '1 * 10 = 10\n2 * 10 = 20\n3 * 10 = 30\n4 * 10 = 40\n5 * 10 = 50\n6 * 10 = 60\n7 * 10 = 70\n8 * 10 = 80\n9 * 10 = 90\n10 * 10 = 100\n'
    assert err == ''

def test3(capsys):
    getInteger_numbers = [0]
    opgave7_1.getInteger = lambda n: getInteger_numbers.pop(0)
    getFloat_numbers = [0]
    opgave7_1.getFloat = lambda n: getFloat_numbers.pop(0)
    input_values = [0]
    def mock_input(s):
        return input_values.pop(0)
    opgave7_1.input = mock_input
    opgave7_1.main()
    out, err = capsys.readouterr()
    assert out == '1 * 0 = 0\n2 * 0 = 0\n3 * 0 = 0\n4 * 0 = 0\n5 * 0 = 0\n6 * 0 = 0\n7 * 0 = 0\n8 * 0 = 0\n9 * 0 = 0\n10 * 0 = 0\n'
    assert err == ''

def test4(capsys):
    getInteger_numbers = [1]
    opgave7_1.getInteger = lambda n: getInteger_numbers.pop(0)
    getFloat_numbers = [1]
    opgave7_1.getFloat = lambda n: getFloat_numbers.pop(0)
    input_values = [1]
    def mock_input(s):
        return input_values.pop(0)
    opgave7_1.input = mock_input
    opgave7_1.main()
    out, err = capsys.readouterr()
    assert out == '1 * 1 = 1\n2 * 1 = 2\n3 * 1 = 3\n4 * 1 = 4\n5 * 1 = 5\n6 * 1 = 6\n7 * 1 = 7\n8 * 1 = 8\n9 * 1 = 9\n10 * 1 = 10\n'
    assert err == ''