import opgave3_5

def test1(capsys):
    input_values = []
    def mock_input(s):
        return input_values.pop(0)
    opgave3_5.input = mock_input
    opgave3_5.main()
    out, err = capsys.readouterr()
    assert out == '21\n'
    assert err == ''
