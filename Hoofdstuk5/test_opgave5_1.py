import opgave5_1

def test1(capsys):
    input_values = ["Dit is een lange zin."]
    def mock_input(s):
        return input_values.pop(0)
    opgave5_1.input = mock_input
    opgave5_1.main()
    out, err = capsys.readouterr()
    assert out == '21\n'
    assert err == ''

def test2(capsys):
    input_values = [""]
    def mock_input(s):
        return input_values.pop(0)
    opgave5_1.input = mock_input
    opgave5_1.main()
    out, err = capsys.readouterr()
    assert out == '0\n'
    assert err == ''