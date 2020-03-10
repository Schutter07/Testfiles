import opgave2_1

def test1(capsys):
    input_values = []
    def mock_input(s):
        return input_values.pop(0)
    opgave2_1.input = mock_input
    opgave2_1.main()
    out, err = capsys.readouterr()
    assert out == 'Hello, world!\n'
    assert err == ''
