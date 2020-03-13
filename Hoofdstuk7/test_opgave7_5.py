import opgave7_5

def test1(capsys):
    opgave7_5.main()
    out, err = capsys.readouterr()
    assert out == '1\n1\n2\n3\n5\n8\n13\n21\n34\n55\n89\n144\n233\n377\n610\n987\n'
    assert err == ''