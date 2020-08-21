import opgave11_3

def test1(capsys):
    opgave11_3.print_inttuple(( 1, 2, ( 3, 4 ), 5, ( ( 6, 7, 8, ( 9, 10 ), 11 ), 12, 13 ), ( ( 14, 15, 16 ), ( 17, 18, 19, 20 ) ) ))
    out, err = capsys.readouterr()
    assert out == "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 "
    assert err == ''

def test2(capsys):
    opgave11_3.print_inttuple((2, 4, 6, (8, 10, (12, 14), 16, (18, 20))))
    out, err = capsys.readouterr()
    assert out == "2 4 6 8 10 12 14 16 18 20 "
    assert err == ''