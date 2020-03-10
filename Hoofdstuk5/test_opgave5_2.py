import opgave5_2

def test1(capsys):
    getFloat_numbers = [3.0, 4.0]
    opgave5_2.getFloat = lambda n: getFloat_numbers.pop(0)
    input_values = [3.0, 4.0]
    def mock_input(s):
        return input_values.pop(0)
    opgave5_2.input = mock_input
    opgave5_2.main()
    out, err = capsys.readouterr()
    assert out == 'Een rechthoekige driehoek met als rechthoekzijden 3.0 en 4.0 heeft als schuine zijde 5.0\n'
    assert err == ''

def test2(capsys):
    getFloat_numbers = [4.2, 7.5]
    opgave5_2.getFloat = lambda n: getFloat_numbers.pop(0)
    input_values = [4.2, 7.5]
    def mock_input(s):
        return input_values.pop(0)
    opgave5_2.main()
    out, err = capsys.readouterr()
    assert out == 'Een rechthoekige driehoek met als rechthoekzijden 4.2 en 7.5 heeft als schuine zijde 8.595929269136642\n'
    assert err == ''
