import opgave7_15

def test1(capsys):
    opgave7_15.main()
    out, err = capsys.readouterr()
    assert out == '15621\n'
    assert err == ''