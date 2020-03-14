import opgave7_14

def test1(capsys):
    opgave7_14.main()
    out, err = capsys.readouterr()
    assert out == 'A = 2\nB = 1\nC = 7\nD = 8\n'
    assert err == ''