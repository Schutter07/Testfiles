import opgave3_1

def test1(capsys):
    input_values = []
    def mock_input(s):
        return input_values.pop(0)
    opgave3_1.input = mock_input
    opgave3_1.main()
    out, err = capsys.readouterr()
    assert out == '945.4499999999999\n'
    assert err == ''
