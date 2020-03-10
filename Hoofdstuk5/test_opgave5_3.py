import opgave5_3

def test1(capsys):
    getFloat_numbers = [3.0, 3.0, 5.0]
    opgave5_3.getFloat = lambda n: getFloat_numbers.pop(0)
    input_values = [3.0, 3.0, 5.0]
    def mock_input(s):
        return input_values.pop(0)
    opgave5_3.input = mock_input
    opgave5_3.main()
    out, err = capsys.readouterr()
    assert out == 'Grootste: 5.0\nKleinste: 3.0\nGemiddelde: 3.67\n'
    assert err == ''

def test2(capsys):
    getFloat_numbers = [-3.4, 3.3, 5.6]
    opgave5_3.getFloat = lambda n: getFloat_numbers.pop(0)
    input_values = [-3.4, 3.3, 5.6]
    def mock_input(s):
        return input_values.pop(0)
    opgave5_3.input = mock_input
    opgave5_3.main()
    out, err = capsys.readouterr()
    assert out == 'Grootste: 5.6\nKleinste: -3.4\nGemiddelde: 1.83\n'
    assert err == ''

def test3(capsys):
    getFloat_numbers = [-34.2, -3.2, -51.45]
    opgave5_3.getFloat = lambda n: getFloat_numbers.pop(0)
    input_values = [3.0, 3.0, 5.0]
    def mock_input(s):
        return input_values.pop(0)
    opgave5_3.input = mock_input
    opgave5_3.main()
    out, err = capsys.readouterr()
    assert out == 'Grootste: -3.2\nKleinste: -51.45\nGemiddelde: -29.62\n'
    assert err == ''