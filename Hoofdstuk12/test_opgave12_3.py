import opgave12_3

def test1(capsys):
    input_values = ["Aron", "Chelsea", "Britt", "Evert", "David", "?", ""]
    def mock_input():
        return input_values.pop(0)

    opgave12_3.input = mock_input
    opgave12_3.main()
    out, err = capsys.readouterr()
    assert out == 'Aron\n'
    assert err == ''

def test2(capsys):
    input_values = ["Aron", "Chelsea", "?", "Britt", "?", "Evert", "David", "?", ""]
    def mock_input():
        return input_values.pop(0)

    opgave12_3.input = mock_input
    opgave12_3.main()
    out, err = capsys.readouterr()
    assert out == 'Aron\nChelsea\nBritt\n'
    assert err == ''

def test3(capsys):
    input_values = ["Aron", "Chelsea", "?", "?", "?", ""]
    def mock_input():
        return input_values.pop(0)

    opgave12_3.input = mock_input
    opgave12_3.main()
    out, err = capsys.readouterr()
    assert out == 'Aron\nChelsea\nFIFO lijst is leeg\n'
    assert err == ''

def test4(capsys):
    input_values = ["Aron", "Chelsea", "?", "?", "?", "?", "Britt", "?", ""]
    def mock_input():
        return input_values.pop(0)

    opgave12_3.input = mock_input
    opgave12_3.main()
    out, err = capsys.readouterr()
    assert out == 'Aron\nChelsea\nFIFO lijst is leeg\nFIFO lijst is leeg\nBritt\n'
    assert err == ''