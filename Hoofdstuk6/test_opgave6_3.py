import opgave6_3

def test1(capsys):
    input_values = ["De Heilige Handgranaat van Antioch"]
    def mock_input(s):
        return input_values.pop(0)
    opgave6_3.input = mock_input
    opgave6_3.main()
    out, err = capsys.readouterr()
    assert out == 'Er zitten 4 verschillende klinkers in de string.\n'
    assert err == ''

def test2(capsys):
    input_values = ["De eerste tekst met een letter???"]
    def mock_input(s):
        return input_values.pop(0)
    opgave6_3.input = mock_input
    opgave6_3.main()
    out, err = capsys.readouterr()
    assert out == 'Er zit 1 verschillende klinker in de string.\n'
    assert err == ''

def test3(capsys):
    input_values = ["oeieoeoeoeoeo"]
    def mock_input(s):
        return input_values.pop(0)
    opgave6_3.input = mock_input
    opgave6_3.main()
    out, err = capsys.readouterr()
    assert out == 'Er zitten 3 verschillende klinkers in de string.\n'
    assert err == ''
