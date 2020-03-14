import opgave7_6

def test1(capsys):
    getString_words = ["Beer", "Bevende"]
    opgave7_6.getString = lambda n: getInteger_numbers.pop(0)
    input_values = ["Beer", "Bevende"]
    def mock_input(s):
        return input_values.pop(0)
    opgave7_6.input = mock_input
    opgave7_6.main()
    out, err = capsys.readouterr()
    assert out == 'De gemeenschappelijke letters zijn: Be\n'
    assert err == ''

def test2(capsys):
    getString_words = ["zwevende", "vlinder"]
    opgave7_6.getString = lambda n: getInteger_numbers.pop(0)
    input_values = ["zwevende", "vlinder"]
    def mock_input(s):
        return input_values.pop(0)
    opgave7_6.input = mock_input
    opgave7_6.main()
    out, err = capsys.readouterr()
    assert out == 'De gemeenschappelijke letters zijn: evnd\n'
    assert err == ''